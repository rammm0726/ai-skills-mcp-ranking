# AI Agent Skills & MCP Ranking

**访问地址:** https://rammm0726.github.io/ai-skills-mcp-ranking/

---

## Project Overview

展示全网最受欢迎的 AI Agent Skills 及 MCP 服务器排行榜

**功能特性：**
- Skills 排行榜 - 展示最受欢迎的 AI Agent 技能包
- MCP 服务器排行榜 - 展示最受欢迎的 MCP 服务器
- 实时搜索与分类筛选（支持中英文界面切换）
- 一键复制安装指令，自动数据更新
- 完全静态站点，部署于 GitHub Pages

**数据来源：**
- [skills.sh](https://skills.sh/) - Skills 排行榜
- [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) - MCP 服务器列表
- [mcp.so](https://mcp.so) - MCP 聚合平台
- [skillhub.cn](https://skillhub.cn/) - 技能包聚合平台

---

## 新增文章指南

### 使用导入脚本

```bash
# 技术文章
python scripts/import_md.py /path/to/article.md article

# 测评文章
python scripts/import_md.py /path/to/article.md review
```

**脚本自动处理：**
- Wiki 链接图片 `![[image.png]]` → 复制到 `assets/images/{slug}/`
- 转换图片路径为相对路径
- 生成符合规范的 frontmatter

### 手动添加

1. 在 `_articles/` 目录创建 `.md` 文件
2. 按照以下格式编写：

```markdown
---
title: "文章标题"
subtitle: "副标题"
description: "SEO 描述"
date: 2026-05-22
category: "教程"
tags: []
reading_time: 5
author: ""
lang: zh
---

文章正文...

![图片描述](../assets/images/article-slug/image.png)
```

---

## 发布流程

```bash
# 1. 克隆仓库
git clone https://github.com/rammm0726/ai-skills-mcp-ranking.git
cd ai-skills-mcp-ranking

# 2. 导入文章
python scripts/import_md.py ~/Obsidian/my-article.md article

# 3. 编辑 .md 文件，补充 frontmatter 信息

# 4. 构建静态文件
python scripts/build.py

# 5. 本地预览
python -m http.server 8080

# 6. 提交并推送
git add .
git commit -m "feat: 新增文章 - 文章标题"
git push
```

GitHub Actions 自动部署到 GitHub Pages

---

## 项目结构

```
ai-skills-mcp-ranking/
├── _articles/           # Markdown 文章源文件
├── _layouts/           # HTML 模板
├── assets/images/      # 文章图片资源
├── css/                # 样式文件
├── data/               # 数据文件
├── js/                 # JavaScript
├── scripts/            # 构建脚本
│   ├── build.py        # 静态站点生成器
│   └── import_md.py    # 文章导入脚本
└── index.html          # 主页面
```

**技术栈：**
- 前端：纯 HTML/CSS/JS（无框架）
- 构建：Python 3.x + Markdown
- 部署：GitHub Pages + GitHub Actions

---

## License

MIT License
