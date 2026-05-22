#!/usr/bin/env python3
"""
Markdown 文章导入脚本
使用方式: python import_md.py /path/to/article.md article|review
"""

import os
import sys
import re
import shutil
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


def generate_frontmatter(title, category='教程', lang='zh', reading_time=5, featured_image=None):
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


def import_article(file_path, target_type='article'):
    """导入文章"""
    file_path = Path(file_path)
    
    if not file_path.exists():
        print(f"错误: 文件不存在 - {file_path}")
        return False
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    existing_frontmatter = None
    frontmatter_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if frontmatter_match:
        existing_frontmatter = parse_obsidian_frontmatter(frontmatter_match.group(1))
        content = content[len(frontmatter_match.group(0)):]
    
    wiki_images = extract_wiki_images(content)
    print(f"\n📄 文件: {file_path.name}")
    print(f"   目标类型: {target_type}")
    print(f"   找到 {len(wiki_images)} 个 wiki 链接图片")
    
    title = existing_frontmatter.get('title', file_path.stem) if existing_frontmatter else file_path.stem
    slug = slugify(title)
    
    vault_path = file_path.parent
    if wiki_images:
        print(f"\n📦 复制图片到 assets/images/{slug}/")
        copy_images_to_assets(wiki_images, slug, vault_path)
        content = convert_wiki_links(content, slug)
    
    category_map = {
        'article': '教程',
        'review': '测评'
    }
    category = category_map.get(target_type, '教程')
    
    featured_image = None
    if wiki_images:
        featured_image = f"assets/images/{slug}/{os.path.basename(wiki_images[0])}"
    
    new_frontmatter = generate_frontmatter(
        title=title,
        category=category,
        lang='zh',
        reading_time=5,
        featured_image=featured_image
    )
    
    final_content = new_frontmatter + content
    
    output_path = ARTICLES_DIR / f"{slug}.md"
    if output_path.exists():
        print(f"   ⚠ 文件已存在，将覆盖: {output_path}")
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(final_content)
    
    print(f"\n✅ 导入成功!")
    print(f"   文章: {output_path}")
    print(f"   Slug: {slug}")
    
    return True


def show_help():
    """显示帮助信息"""
    print("""
Markdown 文章导入工具

用法:
  python import_md.py /path/to/article.md article|review

参数:
  /path/to/article.md   文章的绝对路径
  article|review        目标类型：article（技术文章）或 review（测评文章）

示例:
  python import_md.py ~/Obsidian/my-article.md article
  python import_md.py ~/Obsidian/review.md review

说明:
  - 自动处理 Obsidian wiki 链接图片 ![[image.png]]
  - 图片自动复制到 assets/images/{slug}/ 目录
  - 自动生成符合规范的 frontmatter
""")


def main():
    if len(sys.argv) != 3:
        show_help()
        sys.exit(1)
    
    file_path = sys.argv[1]
    target_type = sys.argv[2]
    
    if target_type not in ['article', 'review']:
        print(f"错误: 目标类型必须是 article 或 review，当前为: {target_type}")
        sys.exit(1)
    
    print("=" * 50)
    print("🔄 Markdown 文章导入工具")
    print("=" * 50)
    
    import_article(file_path, target_type)
    
    print("\n" + "=" * 50)
    print("📌 下一步操作:")
    print("   1. 检查生成的 .md 文件")
    print("   2. 编辑 frontmatter 补充信息")
    print("   3. 运行构建: python scripts/build.py")
    print("   4. 提交并推送到 GitHub")
    print("=" * 50)


if __name__ == '__main__':
    main()
