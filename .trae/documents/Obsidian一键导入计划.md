# Obsidian 文章一键导入网站计划

## 背景

用户已经在 Obsidian 中准备好了文章，希望能够一键将文章（含图片）导入到网站中。

## 目标

1. 创建 Obsidian 导入脚本，自动处理：
   - 解析 `![[image.png]]` 格式的 wiki 链接图片
   - 复制图片到正确目录
   - 转换图片路径为相对路径
   - 生成符合规范的 frontmatter

2. 更新 README.md 文档，说明使用流程

3. 提供简单的命令行操作方式

---

## 实施步骤

### 步骤 1：创建 Obsidian 导入脚本

**文件：** `/workspace/scripts/import_obsidian.py`

**功能：**
- 接收用户 Obsidian Vault 中的 Markdown 文件路径
- 解析 wiki 链接格式的图片 `![[image.png]]`
- 自动复制图片到 `assets/images/{slug}/` 目录
- 生成符合网站规范的 frontmatter
- 转换图片链接为相对路径 `assets/images/{slug}/image.png`

**核心逻辑：**
```python
# 1. 读取 Obsidian Markdown 文件
# 2. 解析 frontmatter (如果存在)
# 3. 提取 ![[image.png]] 格式的图片引用
# 4. 创建文章专用图片目录 assets/images/{slug}/
# 5. 复制图片到目标目录
# 6. 替换 wiki 链接为相对路径
# 7. 生成符合规范的 frontmatter (如果缺失)
# 8. 输出到 _articles/ 目录
```

### 步骤 2：创建快速启动脚本

**文件：** `/workspace/scripts/quick-import.sh`

**功能：**
- 提供简化的命令行接口
- 支持拖拽文件导入
- 自动运行构建脚本

### 步骤 3：更新 README.md

**内容：**
- 添加"新增文章"章节
- 说明 Obsidian 导入流程
- 提供快速命令示例

---

## 详细实现

### 1. import_obsidian.py 脚本结构

```python
#!/usr/bin/env python3
import os
import sys
import re
import shutil
import argparse
from datetime import datetime

def extract_wiki_images(content):
    """提取 ![[image.png]] 格式的图片引用"""
    pattern = r'!\[\[([^\]]+)\]\]'
    return re.findall(pattern, content)

def copy_images_to_assets(image_paths, slug, assets_dir):
    """复制图片到 assets/images/{slug}/ 目录"""
    copied = []
    for img in image_paths:
        # 从 Obsidian Vault 路径复制
        src = img  # 或使用用户提供的 Vault 路径
        dst = os.path.join(assets_dir, slug, os.path.basename(img))
        # 复制文件
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
        copied.append(os.path.basename(img))
    return copied

def convert_wiki_links(content, slug):
    """转换 ![[image.png]] 为相对路径格式"""
    def replacer(match):
        img_name = match.group(1)
        return f'![{img_name}](../assets/images/{slug}/{img_name})'
    return re.sub(r'!\[\[([^\]]+)\]\]', replacer, content)

def generate_frontmatter(title, category='教程', lang='zh'):
    """生成符合规范的 frontmatter"""
    return f'''---
title: "{title}"
subtitle: ""
description: ""
date: {datetime.now().strftime('%Y-%m-%d')}
category: "{category}"
tags: []
reading_time: 5
author: ""
lang: {lang}
---
'''

def main():
    # 解析命令行参数
    # 处理文件导入
    # 执行转换
    pass
```

### 2. 使用流程（用户操作）

```bash
# 方式一：直接指定 Obsidian 文件路径
python scripts/import_obsidian.py "/path/to/your/article.md"

# 方式二：指定 Obsidian Vault 目录，自动扫描
python scripts/import_obsidian.py --vault "/path/to/Obsidian Vault"

# 方式三：交互式选择文件
python scripts/import_obsidian.py --interactive
```

### 3. 输出示例

**输入（Obsidian 格式）：**
```markdown
---
uid: 20250522-1234
title: 我的新文章
---

这是文章内容。

![示意图](../.obsidian/images/abc123.png)

更多内容。
```

**输出（网站格式）：**
```markdown
---
title: "我的新文章"
subtitle: ""
description: ""
date: 2026-05-22
category: "教程"
tags: []
reading_time: 5
author: ""
lang: zh
featured_image: "assets/images/wo-de-xin-wen-zhang/abc123.png"
---

这是文章内容。

![示意图](../assets/images/wo-de-xin-wen-zhang/abc123.png)

更多内容。
```

---

## 验证检查点

| 检查项 | 验证方式 |
|--------|----------|
| 图片文件被正确复制 | 检查 `assets/images/{slug}/` 目录 |
| wiki 链接被正确转换 | 检查生成的 Markdown 文件 |
| frontmatter 格式正确 | 使用 build.py 构建成功 |
| 网站显示正常 | 访问页面检查图片显示 |

---

## 风险与注意事项

1. **图片路径冲突**：同名图片可能覆盖
   - 解决方案：使用 UUID 或时间戳命名

2. **Obsidian Vault 结构差异**：用户的 Vault 结构可能不同
   - 解决方案：支持自定义 Vault 路径和图片路径

3. **中文文件名**：需要处理 URL 编码
   - 解决方案：转换为 slug 格式

---

## 预期成果

1. 用户只需一行命令即可导入文章
2. 图片自动处理，无需手动操作
3. 生成的文章符合网站规范
4. README 文档完整说明操作流程
