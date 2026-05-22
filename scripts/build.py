#!/usr/bin/env python3
"""
Static site builder - processes Markdown articles with Liquid templates
"""

import os
import re
import shutil
from pathlib import Path
from datetime import datetime

SITE_DIR = Path(".")
OUTPUT_DIR = SITE_DIR / "_site"
BASEURL = '/ai-skills-mcp-ranking'

def parse_frontmatter(content):
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            return parts[1].strip(), parts[2].strip()
    return "", content

def parse_yaml(text):
    data = {}
    for line in text.split('\n'):
        line = line.strip()
        if ':' in line and not line.startswith('#'):
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            data[key] = value
    return data

def convert_md(html):
    """Convert markdown to HTML (line-by-line for correct table/list handling)"""
    lines = html.split('\n')
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        s = line.strip()
        if not s:
            result.append(''); i += 1; continue
        # Code block
        if s.startswith('```'):
            lang = s[3:].strip()
            code = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('```'):
                code.append(lines[i]); i += 1
            result.append(f'<pre><code class="{lang}">{chr(10).join(code)}</code></pre>')
            i += 1; continue
        # Table
        if s.startswith('|') and i + 1 < len(lines) and re.match(r'^\|[\s\-:|]+\|$', lines[i+1].strip()):
            headers = [c.strip() for c in s.split('|')[1:-1]]
            i += 2  # skip header + separator
            rows = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                cells = [c.strip() for c in lines[i].strip().split('|')[1:-1]]
                if cells: rows.append(cells)
                i += 1
            def fmt(cell):
                cell = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', cell)
                cell = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', cell)
                cell = re.sub(r'\*(.+?)\*', r'<em>\1</em>', cell)
                cell = re.sub(r'`(.+?)`', r'<code>\1</code>', cell)
                return cell
            t = '<table class="md-table"><thead><tr>'
            for h in headers: t += f'<th>{fmt(h)}</th>'
            t += '</tr></thead><tbody>'
            for row in rows:
                t += '<tr>'
                for c in row: t += f'<td>{fmt(c)}</td>'
                t += '</tr>'
            t += '</tbody></table>'
            result.append(t); continue
        # Headers
        if s.startswith('#### '): result.append(f'<h4>{s[5:]}</h4>'); i += 1; continue
        if s.startswith('### '): result.append(f'<h3>{s[4:]}</h3>'); i += 1; continue
        if s.startswith('## '): result.append(f'<h2>{s[3:]}</h2>'); i += 1; continue
        if s.startswith('# '): result.append(f'<h1>{s[2:]}</h1>'); i += 1; continue
        # HR
        if re.match(r'^-{3,}$', s): result.append('<hr>'); i += 1; continue
        # Blockquote
        if s.startswith('> '): result.append(f'<blockquote>{s[2:]}</blockquote>'); i += 1; continue
        # Unordered list
        if s.startswith('- '):
            items = []
            while i < len(lines) and lines[i].strip().startswith('- '):
                items.append(lines[i].strip()[2:]); i += 1
            result.append('<ul>')
            for it in items: result.append(f'<li>{it}</li>')
            result.append('</ul>'); continue
        # Ordered list
        if re.match(r'^\d+\. ', s):
            items = []
            while i < len(lines) and re.match(r'^\d+\. ', lines[i].strip()):
                items.append(re.sub(r'^\d+\. ', '', lines[i].strip())); i += 1
            result.append('<ol>')
            for it in items: result.append(f'<li>{it}</li>')
            result.append('</ol>'); continue
        # Inline formatting
        f = s
        f = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', f)
        f = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', f)
        f = re.sub(r'\*(.+?)\*', r'<em>\1</em>', f)
        f = re.sub(r'`(.+?)`', r'<code>\1</code>', f)
        f = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', f)
        if f and not f.startswith('<'):
            result.append(f'<p>{f}</p>')
        else:
            result.append(f)
        i += 1
    return '\n'.join(result)

def process_liquid(content, variables):
    """Process Liquid template variables"""
    result = content
    baseurl = variables.get('baseurl', BASEURL)

    # {{ '/xxx' | relative_url }}
    result = re.sub(r'\{\{\s*[\'"](.+?)[\'"]\s*\|\s*relative_url\s*\}\}', lambda m: baseurl + m.group(1), result)
    # {{ xxx | default: yyy }}
    def default_filter(m):
        key = m.group(1).replace('page.', '').replace('site.', '')
        val = variables.get(key, '')
        return str(val) if val else m.group(2).strip().strip("'\"")
    result = re.sub(r'\{\{\s*([^|}]+?)\s*\|\s*default:\s*([^}]+?)\s*\}\}', default_filter, result)
    # {{ xxx | escape }}
    result = re.sub(r'\{\{\s*([^|}]+?)\s*\|\s*escape\s*\}\}', lambda m: str(variables.get(m.group(1).replace('page.','').replace('site.',''), '')).replace('<','&lt;').replace('>','&gt;'), result)
    # Remove remaining {% %} tags
    result = re.sub(r'\{%[^%]*%\}', '', result)
    # Replace {{ page.xxx }} and {{ site.xxx }}
    for key, value in variables.items():
        if value is None: value = ''
        result = result.replace('{{ page.' + key + ' }}', str(value))
        result = result.replace('{{ site.' + key + ' }}', str(value))
        result = result.replace('{{ ' + key + ' }}', str(value))
    # Remove any remaining {{ }}
    result = re.sub(r'\{\{.*?\}\}', '', result)
    return result

def load_articles():
    articles = []
    articles_dir = SITE_DIR / "_articles"
    if not articles_dir.exists():
        return articles
    for md_file in articles_dir.glob("*.md"):
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        fm, body = parse_frontmatter(content)
        meta = parse_yaml(fm)
        layout = meta.get('layout', 'article')
        slug = md_file.stem
        if layout == 'review':
            url = 'reviews/' + slug + '/'
        else:
            url = 'articles/' + slug + '/'
        articles.append({
            'title': meta.get('title', slug),
            'subtitle': meta.get('subtitle', ''),
            'description': meta.get('description', ''),
            'category': meta.get('category', 'article'),
            'date': meta.get('date', ''),
            'reading_time': meta.get('reading_time', '5'),
            'url': url,
            'content': body,
            'layout': layout
        })
    articles.sort(key=lambda x: x.get('date', ''), reverse=True)
    return articles

def build_site():
    print("Building site...")
    if OUTPUT_DIR.exists():
        try: shutil.rmtree(OUTPUT_DIR)
        except:
            for item in OUTPUT_DIR.iterdir():
                try: (shutil.rmtree(item) if item.is_dir() else item.unlink())
                except: pass
    OUTPUT_DIR.mkdir(exist_ok=True)

    articles = load_articles()
    site_config = {
        'title': 'AI Agent Skills & MCP Ranking',
        'description': '全网最受欢迎的 AI Agent 技能包和 MCP 服务器排行榜',
        'url': 'https://rammm0726.github.io',
        'baseurl': BASEURL,
    }

    # Copy static assets
    for folder in ['css', 'js', 'data']:
        src = SITE_DIR / folder
        if src.exists():
            dst = OUTPUT_DIR / folder
            if dst.exists(): shutil.rmtree(dst)
            shutil.copytree(src, dst)

    # Load layouts
    default_layout = (SITE_DIR / "_layouts" / "default.html").read_text('utf-8') if (SITE_DIR / "_layouts" / "default.html").exists() else '{{ content }}'
    article_layout = (SITE_DIR / "_layouts" / "article.html").read_text('utf-8') if (SITE_DIR / "_layouts" / "article.html").exists() else '{{ content }}'

    # Process articles
    for article in articles:
        out_dir = OUTPUT_DIR / article['url'].rstrip('/')
        out_dir.mkdir(parents=True, exist_ok=True)
        out_file = out_dir / "index.html"

        html_body = convert_md(article['content'])
        page_vars = {k: v for k, v in article.items() if k != 'content'}
        page_vars['content'] = html_body

        # article layout → default layout
        step1 = process_liquid(article_layout, {**site_config, **page_vars})
        step2_vars = {**page_vars, 'content': step1}
        final = process_liquid(default_layout, {**site_config, **step2_vars})

        out_file.write_text(final, 'utf-8')
        print(f"  Generated: {article['url']}")

    # Copy index.html
    index_src = SITE_DIR / "index.html"
    if index_src.exists():
        shutil.copy(index_src, OUTPUT_DIR / "index.html")
        print("  Copied: /index.html")

    print(f"\nDone! Output: {OUTPUT_DIR}")

if __name__ == "__main__":
    build_site()
