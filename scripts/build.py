#!/usr/bin/env python3
"""
Static site builder for GitHub Actions
Processes Jekyll-style templates and outputs static HTML
"""

import os
import re
import shutil
from pathlib import Path
from datetime import datetime

SITE_DIR = Path(".")
OUTPUT_DIR = SITE_DIR / "_site"

def parse_frontmatter(content):
    """Extract YAML frontmatter from markdown/HTML files"""
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            return parts[1].strip(), parts[2].strip()
    return "", content

def parse_yaml(yaml_text):
    """Simple YAML parser for frontmatter"""
    data = {}
    for line in yaml_text.split('\n'):
        line = line.strip()
        if ':' in line and not line.startswith('#'):
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            data[key] = value
    return data

def process_template(template_content, variables, site_config):
    """Process Jekyll Liquid-style templates"""
    result = template_content
    
    # Handle special '/' variable for relative_url
    result = result.replace("{{ '/' | relative_url }}", '/')
    result = result.replace("{{ '/' }}", '/')
    
    # Handle page.xxx variables
    page_vars = {}
    for key, value in variables.items():
        if key not in ('content',):
            page_vars['page.' + key] = value
    
    # Replace page.xxx with filters
    for var_name, var_value in page_vars.items():
        result = result.replace('{{ ' + var_name + ' }}', str(var_value))
        result = result.replace('{{' + var_name + '}}', str(var_value))
        # Handle escape filter
        if isinstance(var_value, str):
            escaped = var_value.replace('"', '&quot;').replace("'", '&#39;')
            result = result.replace('{{ ' + var_name + ' | escape }}', escaped)
    
    # Handle site.xxx variables
    for key, value in site_config.items():
        result = result.replace('{{ site.' + key + ' }}', str(value))
        result = result.replace('{{site.' + key + '}}', str(value))
    
    # Handle {{ content }}
    if 'content' in variables:
        result = result.replace('{{ content }}', variables['content'])
        result = result.replace('{{content}}', variables['content'])
    
    return result

def convert_markdown_to_html(markdown_content):
    """Simple markdown to HTML converter"""
    html = markdown_content
    
    # Headers
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    
    # Bold and italic
    html = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', html)
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)
    
    # Code blocks
    html = re.sub(r'```(\w*)\n(.*?)```', r'<pre><code class="\1">\2</code></pre>', html, flags=re.DOTALL)
    html = re.sub(r'`(.+?)`', r'<code>\1</code>', html)
    
    # Links
    html = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', html)
    
    # Paragraphs
    lines = html.split('\n')
    in_paragraph = False
    result_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped and not stripped.startswith('<'):
            if not in_paragraph:
                result_lines.append('<p>' + stripped)
                in_paragraph = True
            else:
                result_lines.append(stripped)
        else:
            if in_paragraph:
                result_lines[-1] += '</p>'
                in_paragraph = False
            result_lines.append(line)
    if in_paragraph:
        result_lines[-1] += '</p>'
    html = '\n'.join(result_lines)
    
    return html

def load_articles():
    """Load all articles from _articles directory"""
    articles = []
    articles_dir = SITE_DIR / "_articles"
    if not articles_dir.exists():
        return articles
    
    for md_file in articles_dir.glob("*.md"):
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        frontmatter, body = parse_frontmatter(content)
        metadata = parse_yaml(frontmatter)
        
        articles.append({
            'title': metadata.get('title', md_file.stem),
            'subtitle': metadata.get('subtitle', ''),
            'category': metadata.get('category', 'article'),
            'categoryEn': metadata.get('categoryEn', 'Article'),
            'date': metadata.get('date', ''),
            'readingTime': metadata.get('readingTime', 5),
            'url': 'articles/' + md_file.stem + '/',
            'content': body,
            'layout': metadata.get('layout', 'article')
        })
    
    articles.sort(key=lambda x: x.get('date', ''), reverse=True)
    return articles

def build_site():
    """Build the static site"""
    print("Building site...")
    
    # Clean output directory
    if OUTPUT_DIR.exists():
        try:
            shutil.rmtree(OUTPUT_DIR)
        except PermissionError:
            for item in OUTPUT_DIR.iterdir():
                if item.is_dir():
                    try:
                        shutil.rmtree(item)
                    except:
                        pass
                else:
                    try:
                        item.unlink()
                    except:
                        pass
    OUTPUT_DIR.mkdir(exist_ok=True)
    
    # Site configuration
    site_config = {
        'title': 'AI Agent Skills & MCP Ranking',
        'description': '全网最受欢迎的 AI Agent 技能包和 MCP 服务器排行榜',
        'url': 'https://rammm0726.github.io',
        'baseurl': '/ai-skills-mcp-ranking',
        'articles': load_articles()
    }
    
    # Copy static assets
    for folder in ['css', 'js', 'data']:
        src = SITE_DIR / folder
        if src.exists():
            dst = OUTPUT_DIR / folder
            if dst.exists():
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
    
    # Load default layout
    default_layout_path = SITE_DIR / "_layouts" / "default.html"
    if default_layout_path.exists():
        with open(default_layout_path, 'r', encoding='utf-8') as f:
            default_layout = f.read()
    else:
        default_layout = '{{ content }}'
    
    # Load article layout
    article_layout_path = SITE_DIR / "_layouts" / "article.html"
    if article_layout_path.exists():
        with open(article_layout_path, 'r', encoding='utf-8') as f:
            article_layout = f.read()
    else:
        article_layout = default_layout
    
    # Process articles
    for article in site_config['articles']:
        # Determine output path based on layout
        layout = article.get('layout', 'article')
        if layout == 'review':
            output_dir = OUTPUT_DIR / "reviews" / article['url'].split('/')[-2]
        else:
            output_dir = OUTPUT_DIR / "articles" / article['url'].split('/')[-2]
        
        output_dir.mkdir(parents=True, exist_ok=True)
        output_file = output_dir / "index.html"
        
        # Convert markdown content
        html_content = convert_markdown_to_html(article['content'])
        
        # Use article layout
        page_vars = article.copy()
        page_vars['content'] = html_content
        
        # Process article layout
        html = process_template(article_layout, page_vars, site_config)
        
        # Then process with default layout
        final_vars = page_vars.copy()
        final_vars['content'] = html
        final_html = process_template(default_layout, final_vars, site_config)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(final_html)
        
        print(f"  Generated: {article['url']}")
    
    # Copy index.html
    index_src = SITE_DIR / "index.html"
    if index_src.exists():
        shutil.copy(index_src, OUTPUT_DIR / "index.html")
        print("  Copied: /index.html")
    
    print(f"\nSite built successfully in: {OUTPUT_DIR}")

if __name__ == "__main__":
    build_site()
