# AI Agent Skills & MCP Ranking

全网最受欢迎的 AI Agent 技能包和 MCP 服务器排行榜  
The most popular AI Agent Skills & MCP Server Ranking in China.

[Online Demo 在线预览](https://rammm0726.github.io/ai-skills-mcp-ranking/)

---

## 项目简介 / Project Overview

- 展示全网最受欢迎的 AI Agent Skills 及 MCP 服务器排行榜
- 提供技术文章、工具测评、SEO 优化内容
- 实时搜索与分类筛选（支持中英文界面切换）
- 一键复制安装指令，自动数据更新
- 完全静态站点，部署于 GitHub Pages

---

## 特性 Features

- **Skills 排行榜**：热门 AI Agent Skills 人气排行
- **MCP 服务器榜单**：优质 MCP Server 推荐与数据
- **技术文章 & 工具测评**：详解、对比与入门指南
- **支持搜索/分类筛选/一键复制**：提升用户体验
- **中英双语切换/暗黑主题/响应式布局**
- **自动数据更新**：每周一 GitHub Actions 定时更新

---

## 目录结构 Directory Structure

```
ai-skills-mcp-ranking/
├── .github/workflows/   # CI/CD工作流 (deploy.yml、update-data.yml)
├── _articles/           # 技术文档、评测原稿 (Markdown)
├── _reviews/            # 工具评测文章 (Markdown)
├── _layouts/            # HTML模板 (default/article)
├── assets/images/       # 文章图片存储目录
├── css/                 # 样式文件，支持暗色主题与响应式
├── data/                # skills/mcp 排行榜数据 (JavaScript)
├── js/                  # JS业务逻辑与渲染
├── scripts/             # Python构建脚本 (build.py)
├── index.html           # 主页面 (Skills/MCP + 文章Tab)
└── README.md
```

---

## 数据结构 Data Structure

**Skills 示例**
```js
SKILLS_DATA = {
    lastUpdated: "2026-05-20",
    totalInstalls: "1.6M+",
    source: "skills.sh",
    skills: [
        {
            rank: 1,
            name: "find-skills",
            source: "vercel-labs",
            installs: "1.6M",
            category: "tool",
            categoryName: { zh: "工具", en: "Tools" },
            purpose: { zh: "智能搜索和安装 Skills", en: "Smart search and install Skills" },
            command: "npx skills add vercel-labs/skills@find-skills"
        }
    ]
}
```
**MCP 示例**
```js
MCP_DATA = {
    lastUpdated: "2026-05-20",
    totalStars: "64K+",
    source: "awesome-mcp-servers",
    servers: [
        {
            rank: 1,
            name: "Filesystem MCP",
            source: "modelcontextprotocol",
            stars: "64K",
            category: "tool",
            categoryName: { zh: "工具", en: "Tools" },
            purpose: { zh: "文件系统管理", en: "File system management" },
            command: "npx @modelcontextprotocol/server-filesystem <path>"
        }
    ]
}
```

---

## 本地开发与构建

**依赖环境**
- Python 3.x (`markdown`库)
- Node.js/现代浏览器

**快速开始**
```bash
# 克隆仓库
git clone https://github.com/rammm0726/ai-skills-mcp-ranking.git
cd ai-skills-mcp-ranking

# 构建静态文件
python scripts/build.py

# 本地预览
npx serve .
# 或
python -m http.server 8080
```
---

## 自动化与部署

- 基于 GitHub Actions 自动构建与数据刷新
  - `.github/workflows/deploy.yml`：推送即部署至 GitHub Pages
  - `.github/workflows/update-data.yml`：每周一自动拉取最新排行榜
- 产物发布到 [Pages 站点](https://rammm0726.github.io/ai-skills-mcp-ranking/)  

---

## 技术栈 Tech Stack

- 前端：HTML、CSS（暗色主题/响应式）、原生 JavaScript
- 构建：Python（静态 Markdown 转 HTML）
- 部署：GitHub Pages + Actions

---

## 数据来源 Data Sources

| 源站         | 说明                                    |
| ------------ | --------------------------------------- |
| [skills.sh](https://skills.sh/)                  | Skills 排行榜官方数据 |
| [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | 开源MCP服务器列表 |
| [mcp.so](https://mcp.so)                        | MCP 聚合平台        |
| [skillhub.cn](https://skillhub.cn/)             | 技能包聚合/搜索      |

---

## 新增文章 & 图片处理

### 方式1：从 Obsidian 导入（推荐）

如果您在 Obsidian 中撰写文章，支持自动导入和图片处理：

```bash
python scripts/import_obsidian.py /path/to/your/article.md article
# 或
python scripts/import_obsidian.py /path/to/review.md review
```

脚本会自动：
- 解析 Obsidian 的 wiki 链接（![[image.png]]）
- 查找并复制图片到正确的目录
- 转换 Markdown 引用格式
- 生成标准的 Frontmatter

### 方式2：使用创建脚本

快速创建新文章框架：

```bash
python scripts/create_article.py article "文章标题"
python scripts/create_article.py review "评测文章标题"
```

### 方式3：手动创建

参考模板 [docs/ARTICLE_TEMPLATE.md](docs/ARTICLE_TEMPLATE.md) 手动创建。

---

## 文章与 Frontmatter 规范

技术文章采用 Yaml Frontmatter，支持分类、标签与多语言：

```yaml
---
title: "文章标题"
subtitle: "副标题"
description: "SEO 描述"
date: 2026-05-20
category: "教程"
tags: ["MCP", "入门指南"]
reading_time: 8
author: "作者名"
lang: zh
layout: article
featured_image: "assets/images/articles/article-slug/featured.png"
---
```

### 图片使用规范

- 文章图片放置于：`assets/images/articles/[文章slug]/` 或 `assets/images/reviews/[文章slug]/`
- Markdown 引用：`![图片描述](assets/images/[类型]/[slug]/image.png)`
- 图片格式建议：PNG / WebP
- 特色图片推荐尺寸：1200x630

---

## License

MIT License

> 最后更新：2026-05-22
