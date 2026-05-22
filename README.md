# AI Agent Skills & MCP Ranking

全网最受欢迎的 AI Agent 技能包和 MCP 服务器榜单。

## 访问地址

**GitHub Pages:** https://rrramxy.github.io/ai-skills-mcp-ranking/

## 功能特性

- **Skills 排行榜** - 展示最受欢迎的 AI Agent 技能包
- **MCP 服务器排行榜** - 展示最受欢迎的 MCP 服务器
- **实时搜索** - 支持按名称、功能搜索
- **分类筛选** - 按前端、Azure、工具、设计等分类筛选
- **一键复制** - 点击安装命令即可复制
- **中英文切换** - 支持 CN/EN 界面
- **自动更新** - 每周一自动更新数据

## 数据来源

- [skills.sh](https://skills.sh/) - Skills 排行榜
- [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) - MCP 服务器列表
- [mcp.so](https://mcp.so) - MCP 聚合平台
- [skillhub.cn](https://skillhub.cn/) - 技能包聚合平台

## 本地开发

```bash
# 克隆仓库
git clone https://github.com/rrramxy/ai-skills-mcp-ranking.git
cd ai-skills-mcp-ranking

# 构建静态文件
python scripts/build.py

# 启动本地服务器
npx serve .
# 或
python -m http.server 8080
```

## 项目结构

```
ai-skills-mcp-ranking/
├── .github/workflows/    # GitHub Actions
├── _articles/           # Markdown 文章源文件
├── _layouts/           # HTML 模板
├── css/                # 样式文件
├── data/               # 数据文件
├── js/                 # JavaScript
├── scripts/            # 构建脚本
└── index.html          # 主页面
```

## 技术栈

- 前端：纯 HTML/CSS/JS（无框架）
- 构建：Python 3.x + Markdown
- 部署：GitHub Pages + GitHub Actions

## License

MIT License

---

## 新增文章指南

### 方法一：使用 Obsidian 导入脚本（推荐）

如果你在 Obsidian 中创作文章，可以一键导入：

```bash
# 1. 导入单个文章（需要指定你的 Obsidian Vault 路径用于查找图片）
./scripts/quick-import.sh ~/Obsidian/my-article.md ~/Obsidian

# 或使用 Python 直接运行
python scripts/import_obsidian.py /path/to/article.md --vault /path/to/Obsidian

# 2. 预览模式（不写入文件）
python scripts/import_obsidian.py /path/to/article.md --dry-run

# 3. 扫描整个 Vault
python scripts/import_obsidian.py /path/to/Vault --scan
```

脚本会自动处理：
- Wiki 链接图片 `![[image.png]]` → 复制到 `assets/images/{slug}/`
- 生成符合规范的 frontmatter
- 转换图片路径为相对路径

### 方法二：手动添加

1. 在 `_articles/` 目录创建 `.md` 文件
2. 按照以下格式编写 frontmatter：

```markdown
---
title: "文章标题"
subtitle: "副标题"
description: "SEO 描述（必填）"
date: 2026-05-22
category: "教程"        # 可选值：教程、对比、测评
tags: ["标签1", "标签2"]
reading_time: 5         # 阅读时长（分钟）
author: "作者名"
lang: zh                # 可选值：zh、en
featured_image: "assets/images/article-slug/image.png"  # 特色图片
---

文章正文...
```

3. 在文章中使用图片：

```markdown
![图片描述](../assets/images/article-slug/image.png)
```

### 文章分类说明

| 分类 | 说明 | 目录 |
|------|------|------|
| 教程 | 技术教程、入门指南 | `_articles/` |
| 对比 | 产品对比、分析文章 | `_articles/` |
| 测评 | 工具测评、使用体验 | `_articles/` |

### 发布流程

```bash
# 1. 运行构建脚本
python scripts/build.py

# 2. 本地预览
python -m http.server 8080
# 然后访问 http://localhost:8080

# 3. 提交并推送
git add .
git commit -m "feat: 新增文章 - 文章标题"
git push

# 4. GitHub Actions 自动部署到 GitHub Pages
```
