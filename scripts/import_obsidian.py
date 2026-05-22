#!/usr/bin/env python3
"""
Obsidian 文章导入脚本
自动将 Obsidian 格式的文章（含 wiki 链接图片）导入到网站中
"""

import os
import sys
import re
import shutil
import argparse
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.resolve()
ARTICLES_DIR = PROJECT_ROOT / "_articles"
ASSETS_DIR = PROJECT_ROOT / "assets" / "images"


def slugify(text):
    """将文本转换为 URL 友好的 slug"""
    import unicodedata
    text = unicodedata.normalize('NFKD', text)
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-').lower()


def extract_wiki_images(content):
    """提取 ![[image.png]] 格式的图片引用"""
    pattern = r'!\[\[([^\]]+)\]\]'
    return re.findall(pattern, content)


def find_image_in_vault(image_name, vault_path, search_paths=None):
    """在 Obsidian Vault 中查找图片"""
    if search_paths is None:
        search_paths = [
            vault_path,
            vault_path / ".obsidian",
            vault_path / ".obsidian" / "images",
            vault_path / "images",
            vault_path / "assets",
            vault_path / "assets" / "images",
        ]
    
    for search_dir in search_paths:
        if not search_dir.exists():
            continue
        for root, dirs, files in os.walk(search_dir):
            if image_name in files:
                return Path(root) / image_name
    return None


def copy_images_to_assets(image_paths, slug, vault_path=None):
    """复制图片到 assets/images/{slug}/ 目录"""
    if not image_paths:
        return []
    
    target_dir = ASSETS_DIR / slug
    os.makedirs(target_dir, exist_ok=True)
    
    copied = []
    for img_path in image_paths:
        img_name = os.path.basename(img_path)
        if not img_name:
            continue
        
        src = Path(img_path)
        if not src.exists() and vault_path:
            src = find_image_in_vault(img_name, Path(vault_path))
        
        if src and src.exists():
            dst = target_dir / img_name
            shutil.copy2(src, dst)
            copied.append(img_name)
            print(f"  ✓ 复制图片: {img_name} -> {slug}/")
        else:
            print(f"  ✗ 未找到图片: {img_path}")
    
    return copied


def convert_wiki_links(content, slug):
    """转换 ![[image.png]] 为相对路径格式"""
    def replacer(match):
        img_name = os.path.basename(match.group(1))
        return f'![{img_name}](../assets/images/{slug}/{img_name})'
    return re.sub(r'!\[\[([^\]]+)\]\]', replacer, content)


def parse_existing_frontmatter(content):
    """解析现有的 frontmatter"""
    pattern = r'^---\s*\n(.*?)\n---\s*\n'
    match = re.match(pattern, content, re.DOTALL)
    if match:
        return match.group(1), match.group(0)
    return None, None


def generate_frontmatter(title, category='教程', lang='zh', reading_time=5, featured_image=None, **kwargs):
    """生成符合规范的 frontmatter"""
    fm = f'''---
title: "{title}"
subtitle: ""
description: ""
date: {datetime.now().strftime('%Y-%m-%d')}
category: "{category}"
tags: []
reading_time: {reading_time}
author: ""
lang: {lang}
'''
    if featured_image:
        fm += f'featured_image: "{featured_image}"\n'
    fm += '---\n'
    return fm


def parse_obsidian_frontmatter(frontmatter_text):
    """解析 Obsidian 格式的 frontmatter"""
    data = {}
    
    for line in frontmatter_text.split('\n'):
        line = line.strip()
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip().strip('"\'')
            
            key_mapping = {
                'title': 'title',
                'uid': None,
                'tags': 'tags',
                'created': 'date',
                'modified': None,
            }
            
            mapped_key = key_mapping.get(key, key)
            if mapped_key:
                data[mapped_key] = value
    
    return data


def import_article(file_path, vault_path=None, category='教程', lang='zh', dry_run=False):
    """导入单个文章文件"""
    file_path = Path(file_path)
    
    if not file_path.exists():
        print(f"错误: 文件不存在 - {file_path}")
        return False
    
    with open(file_path, 'r', encoding='utf-8') as f:
        original_content = f.read()
    
    content = original_content
    existing_frontmatter = None
    original_frontmatter_raw = None
    
    frontmatter_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if frontmatter_match:
        existing_frontmatter = parse_obsidian_frontmatter(frontmatter_match.group(1))
        original_frontmatter_raw = frontmatter_match.group(0)
        content = content[len(original_frontmatter_raw):]
    
    wiki_images = extract_wiki_images(content)
    print(f"\n📄 文件: {file_path.name}")
    print(f"   找到 {len(wiki_images)} 个 wiki 链接图片")
    
    title = existing_frontmatter.get('title', file_path.stem) if existing_frontmatter else file_path.stem
    slug = slugify(title)
    
    if wiki_images:
        print(f"\n📦 复制图片到 assets/images/{slug}/")
        copy_images_to_assets(wiki_images, slug, vault_path)
        content = convert_wiki_links(content, slug)
    
    featured_image = None
    if wiki_images:
        featured_image = f"assets/images/{slug}/{os.path.basename(wiki_images[0])}"
    
    new_frontmatter = generate_frontmatter(
        title=title,
        category=category,
        lang=lang,
        reading_time=5,
        featured_image=featured_image
    )
    
    final_content = new_frontmatter + content
    
    if not dry_run:
        output_path = ARTICLES_DIR / f"{slug}.md"
        if output_path.exists():
            print(f"   ⚠ 文件已存在，将覆盖: {output_path}")
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(final_content)
        
        print(f"\n✅ 导入成功!")
        print(f"   文章: {output_path}")
        print(f"   Slug: {slug}")
        print(f"   别名: {output_path.name}")
    else:
        print(f"\n🔍 预览模式 - 未写入文件")
        print(f"   将创建: {ARTICLES_DIR / f'{slug}.md'}")
        print(f"   标题: {title}")
        print(f"   图片: {len(wiki_images)} 个")
    
    return True


def scan_vault_for_articles(vault_path, category='教程'):
    """扫描 Vault 目录查找所有 Markdown 文件"""
    vault_path = Path(vault_path)
    articles = []
    
    for root, dirs, files in os.walk(vault_path):
        root_path = Path(root)
        
        if '.obsidian' in [d.name for d in root_path.iterdir() if d.is_dir()]:
            continue
        
        for file in files:
            if file.endswith('.md'):
                file_path = root_path / file
                articles.append((file_path, category))
    
    return articles


def main():
    parser = argparse.ArgumentParser(
        description='将 Obsidian 文章导入到网站',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
示例:
  # 导入单个文件
  python import_obsidian.py /path/to/article.md
  
  # 指定 Obsidian Vault 路径（用于查找图片）
  python import_obsidian.py /path/to/article.md --vault /path/to/Obsidian
  
  # 扫描整个 Vault
  python import_obsidian.py /path/to/Vault --scan
  
  # 预览模式（不写入文件）
  python import_obsidian.py /path/to/article.md --dry-run
        '''
    )
    
    parser.add_argument('path', nargs='?', help='文章文件路径或 Vault 目录')
    parser.add_argument('--vault', '-v', help='Obsidian Vault 根目录路径')
    parser.add_argument('--scan', '-s', action='store_true', help='扫描 Vault 中的所有文章')
    parser.add_argument('--category', '-c', default='教程', 
                       choices=['教程', '对比', '测评', '其他'],
                       help='文章分类 (默认: 教程)')
    parser.add_argument('--lang', '-l', default='zh',
                       choices=['zh', 'en'],
                       help='文章语言 (默认: zh)')
    parser.add_argument('--dry-run', '-n', action='store_true', help='预览模式，不写入文件')
    
    args = parser.parse_args()
    
    if not args.path:
        parser.print_help()
        print("\n❌ 错误: 请提供文章文件路径或 Vault 目录")
        return 1
    
    path = Path(args.path)
    
    if not path.exists():
        print(f"❌ 错误: 路径不存在 - {path}")
        return 1
    
    print("=" * 50)
    print("🔄 Obsidian 文章导入工具")
    print("=" * 50)
    
    if path.is_file():
        import_article(path, args.vault, args.category, args.lang, args.dry_run)
    elif path.is_dir():
        if args.scan:
            print(f"\n📂 扫描目录: {path}")
            articles = scan_vault_for_articles(path, args.category)
            print(f"   找到 {len(articles)} 个 Markdown 文件\n")
            
            for i, (article_path, cat) in enumerate(articles, 1):
                print(f"[{i}/{len(articles)}]")
                import_article(article_path, args.vault, cat, args.lang, args.dry_run)
        else:
            print(f"❌ 错误: 目录路径请使用 --scan 参数进行扫描")
            print(f"   python import_obsidian.py {path} --scan")
            return 1
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
