#!/usr/bin/env python3
"""
Import an article from Obsidian vault, automatically handling images.
Usage: python scripts/import_obsidian.py /path/to/article.md [article|review]
"""

import sys
import re
import shutil
from pathlib import Path
from datetime import datetime


def slugify(text):
    """Convert text to slug format"""
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')


def parse_frontmatter(content):
    """Parse YAML frontmatter"""
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            return parts[1].strip(), parts[2].strip()
    return '', content


def parse_yaml(text):
    """Simple YAML parser"""
    data = {}
    for line in text.split('\n'):
        line = line.strip()
        if ':' in line and not line.startswith('#'):
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            data[key] = value
    return data


def main():
    if len(sys.argv) < 3:
        print("Usage: python scripts/import_obsidian.py /path/to/article.md [article|review]")
        return

    source_file = Path(sys.argv[1])
    article_type = sys.argv[2].lower()

    if not source_file.exists():
        print(f"Error: File not found: {source_file}")
        return

    if article_type not in ['article', 'review']:
        print("Type must be 'article' or 'review'")
        return

    # Read source content
    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Parse frontmatter
    fm, body = parse_frontmatter(content)
    meta = parse_yaml(fm)

    # Get title from frontmatter or filename
    title = meta.get('title', source_file.stem)
    slug = slugify(title)

    # Setup destination paths
    base_dir = Path(".")
    if article_type == 'article':
        content_dir = base_dir / "_articles"
        images_dir = base_dir / "assets" / "images" / "articles"
    else:
        content_dir = base_dir / "_reviews"
        images_dir = base_dir / "assets" / "images" / "reviews"

    dest_file = content_dir / f"{slug}.md"
    dest_images_dir = images_dir / slug

    # Create directories
    content_dir.mkdir(parents=True, exist_ok=True)
    dest_images_dir.mkdir(parents=True, exist_ok=True)

    # Process images
    # Pattern 1: Obsidian wiki links ![[image.png]]
    wiki_pattern = r'!\[\[([^\]]+\.(?:png|jpg|jpeg|gif|webp|svg))\]\]'
    # Pattern 2: Standard markdown !...(...)
    md_pattern = r'!\[([^\]]*)\]\(([^\)]+\.(?:png|jpg|jpeg|gif|webp|svg))\)'

    image_count = 0

    # Function to find image file in vault
    def find_image_file(img_name):
        # Try same directory first
        same_dir = source_file.parent / img_name
        if same_dir.exists():
            return same_dir

        # Try common attachments directories
        for dir_name in ['attachments', 'images', 'assets', 'media']:
            attachments_dir = source_file.parent / dir_name
            if attachments_dir.exists():
                img_path = attachments_dir / img_name
                if img_path.exists():
                    return img_path

        # Walk up the tree
        for parent in source_file.parents:
            img_path = parent / img_name
            if img_path.exists():
                return img_path
            for dir_name in ['attachments', 'images', 'assets', 'media']:
                img_path = parent / dir_name / img_name
                if img_path.exists():
                    return img_path
        return None

    # Process Obsidian wiki links
    def replace_wiki(match):
        nonlocal image_count
        img_name = match.group(1)
        img_src = find_image_file(img_name)
        if img_src:
            # Copy to destination
            img_dest = dest_images_dir / img_name
            shutil.copy2(img_src, img_dest)
            image_count += 1
            # New relative path
            new_path = f"assets/images/{article_type}s/{slug}/{img_name}"
            return f'![{img_name}]({new_path})'
        else:
            print(f"Warning: Image not found: {img_name}")
            return match.group(0)

    body = re.sub(wiki_pattern, replace_wiki, body)

    # Process standard markdown links
    def replace_md(match):
        nonlocal image_count
        alt_text = match.group(1)
        img_path_str = match.group(2)
        img_path = Path(img_path_str)
        if img_path.is_absolute():
            img_src = img_path
        else:
            img_src = (source_file.parent / img_path).resolve()
        if img_src.exists():
            img_dest = dest_images_dir / img_src.name
            shutil.copy2(img_src, img_dest)
            image_count += 1
            new_path = f"assets/images/{article_type}s/{slug}/{img_src.name}"
            return f'![{alt_text}]({new_path})'
        else:
            print(f"Warning: Image not found: {img_path}")
            return match.group(0)

    body = re.sub(md_pattern, replace_md, body)

    # Generate frontmatter
    date_str = meta.get('date', datetime.now().strftime("%Y-%m-%d"))
    new_fm = f'''---
title: "{title}"
subtitle: "{meta.get('subtitle', '')}"
description: "{meta.get('description', '')}"
date: {date_str}
category: "{meta.get('category', article_type)}"
tags: {meta.get('tags', '[]')}
reading_time: {meta.get('reading_time', '5')}
author: "{meta.get('author', '')}"
lang: zh
layout: {article_type}
featured_image: ""
---
'''

    # Write output file
    with open(dest_file, 'w', encoding='utf-8') as f:
        f.write(new_fm + body)

    print(f"✓ Article imported: {dest_file}")
    print(f"✓ {image_count} images copied to: {dest_images_dir}")
    print(f"\nNext steps:")
    print(f"1. Review and edit: {dest_file}")
    print(f"2. Set a featured_image in the frontmatter if needed")
    print(f"3. Build the site: python scripts/build.py")


if __name__ == "__main__":
    main()
