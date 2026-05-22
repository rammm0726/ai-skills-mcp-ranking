#!/usr/bin/env python3
"""
Create a new article with automatic directory structure.
Usage: python scripts/create_article.py [article|review "Article Title"
"""

import sys
from pathlib import Path
from datetime import datetime
import re


def slugify(text):
    """Convert text to slug format"""
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')


def main():
    if len(sys.argv) < 3:
        print("Usage: python scripts/create_article.py [article|review] \"Article Title\"")
        return

    article_type = sys.argv[1].lower()
    title = sys.argv[2]

    if article_type not in ['article', 'review']:
        print("Type must be 'article' or 'review'")
        return

    # Setup paths
    base_dir = Path(".")
    if article_type == 'article':
        content_dir = base_dir / "_articles"
        images_dir = base_dir / "assets" / "images" / "articles"
    else:
        content_dir = base_dir / "_reviews"
        images_dir = base_dir / "assets" / "images" / "reviews"

    slug = slugify(title)
    article_file = content_dir / f"{slug}.md"
    article_images_dir = images_dir / slug

    # Create directories if they don't exist
    content_dir.mkdir(parents=True, exist_ok=True)
    article_images_dir.mkdir(parents=True, exist_ok=True)

    # Date
    date_str = datetime.now().strftime("%Y-%m-%d")

    # Template content
    template = f'''---
title: "{title}"
subtitle: ""
description: ""
date: {date_str}
category: "{article_type}"
tags: []
reading_time: 5
author: ""
lang: zh
layout: {article_type}
featured_image: ""
---

## 标题

文章正文...

'''

    # Write file
    with open(article_file, 'w', encoding='utf-8') as f:
        f.write(template)

    print(f"✓ Created: {article_file}")
    print(f"✓ Created: {article_images_dir}")
    print(f"\n✓ Images can be placed in: {article_images_dir}")
    print(f"\nNext step: Edit {article_file} to add content and images!")


if __name__ == "__main__":
    main()
