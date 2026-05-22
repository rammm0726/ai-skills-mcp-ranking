# AI Agent Skills & MCP Ranking - Code Wiki

## 项目概述

**项目名称：** AI Agent Skills & MCP Ranking

**项目目标：**
- 展示全网最受欢迎的 AI Agent Skills 和 MCP 服务器排行榜
- 提供技术文章和工具测评板块（SEO/GEO 优化）
- 支持搜索功能，方便用户查找内容
- 部署到 GitHub Pages

**技术栈：**
- 前端：纯 HTML/CSS/JS（无框架）
- 构建：自定义 Python 脚本（`scripts/build.py`）
- 部署：GitHub Pages + GitHub Actions

---

## 目录结构

```
ai-skills-mcp-ranking/
├── .github/workflows/       # CI/CD 配置
│   ├── deploy.yml          # 部署到 GitHub Pages
│   └── update-data.yml     # 定时数据更新（周一运行）
├── _articles/              # 文章源文件（Markdown + Frontmatter）
│   ├── claude-desktop-mcp-review.md
│   ├── find-skills-review.md
│   ├── skills-vs-mcp.md
│   └── what-is-mcp-server.md
├── _layouts/               # HTML 模板
│   ├── article.html        # 文章详情页模板
│   └── default.html        # 基础布局模板
├── css/                    # 样式文件
│   ├── article.css         # 文章页样式
│   └── style.css           # 主样式
├── data/                   # 数据文件
│   ├── mcp-data.js         # MCP 服务器数据
│   └── skills-data.js      # Skills 数据
├── js/                     # JavaScript
│   ├── app.js              # 主应用逻辑
│   └── main.js             # 文章/测评数据与渲染
├── scripts/                # 构建脚本
│   └── build.py            # 静态站点生成器
├── .gitignore              # Git 忽略规则
├── index.html              # 主页（Skills/MCP 排行榜 + 文章/测评 Tab）
└── README.md               # 项目说明
```

---

## 主要模块职责

### 1. 页面入口 (index.html)

**职责：** 主页面的单一入口文件，包含所有功能模块

**核心功能：**
- 顶部导航：Skills 排行榜 | MCP 排行榜 | 技术文章 | 工具测评
- Skills 排行榜表格（带搜索框）
- MCP 排行榜表格（带搜索框 + 分类筛选）
- 技术文章列表（带搜索框）
- 工具测评列表（带搜索框）
- 中英文语言切换
- 一键复制安装命令

**关键数据结构：**
```javascript
// Skills 数据结构
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

// MCP 数据结构
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

### 2. 构建脚本 (scripts/build.py)

**职责：** 将 Markdown 文章转换为静态 HTML 文件

**核心函数：**

| 函数名 | 功能 | 输入 | 输出 |
|--------|------|------|------|
| `parse_frontmatter()` | 解析 YAML frontmatter | Markdown 文件内容 | (frontmatter字符串, 正文内容) |
| `parse_yaml()` | 解析 YAML 配置 | frontmatter 文本 | dict 对象 |
| `convert_md()` | Markdown 转 HTML | Markdown 文本 | HTML 文本 |
| `process_liquid()` | 处理 Liquid 模板变量 | 内容 + 变量字典 | 渲染后的 HTML |
| `load_articles()` | 加载所有文章 | 无 | 文章列表 |
| `build_site()` | 构建整个站点 | 无 | 生成 `_site/` 目录 |

**构建流程：**
1. 清理 `_site/` 目录
2. 复制静态资源（css, js, data）
3. 加载 HTML 模板
4. 解析 Markdown 文章
5. 渲染 Liquid 模板
6. 生成静态 HTML 文件
7. 复制 index.html

**使用方式：**
```bash
python scripts/build.py
```

### 3. JavaScript 模块 (js/main.js)

**职责：** 提供国际化、复制功能和返回顶部功能

**核心函数：**

| 函数名 | 功能 | 参数 |
|--------|------|------|
| `setLanguage(lang)` | 设置界面语言 | `lang`: 'zh' 或 'en' |
| `copyCommand(element)` | 复制命令到剪贴板 | DOM 元素 |

**国际化 (I18N) 数据结构：**
```javascript
I18N = {
    zh: {
        title: "AI Agent Skills & MCP 排行榜",
        subtitle: "全网最受受欢迎的 AI Agent 技能包和 MCP 服务器榜单",
        // ... 其他翻译
    },
    en: {
        title: "AI Agent Skills & MCP Server Ranking",
        subtitle: "Most popular AI Agent Skills and MCP Servers",
        // ... 其他翻译
    }
}
```

### 4. 样式文件 (css/style.css)

**职责：** 提供暗色主题的现代 UI 样式

**主要样式模块：**
- CSS 变量定义（颜色、间距）
- 响应式布局（支持移动端）
- Tab 导航样式
- 表格样式（排行榜）
- 搜索框样式
- 分类标签样式
- 返回顶部按钮
- 语言切换器

**CSS 变量：**
```css
:root {
    --primary: #6366f1;         /* 主色调 - 靛蓝 */
    --primary-dark: #4f46e5;    /* 深色主色调 */
    --bg: #0f172a;              /* 背景色 - 深蓝黑 */
    --bg-card: #1e293b;         /* 卡片背景色 */
    --text: #f1f5f9;            /* 主文本色 */
    --text-secondary: #94a3b8;  /* 次要文本色 */
    --accent: #f59e0b;          /* 强调色 - 琥珀色 */
    --skill-color: #06b6d4;      /* Skills 品牌色 - 青色 */
    --mcp-color: #8b5cf6;       /* MCP 品牌色 - 紫色 */
}
```

### 5. 文章模板 (_layouts/article.html)

**职责：** 渲染文章详情页的布局模板

**模板变量：**
```html
{{ page.title }}           <!-- 文章标题 -->
{{ page.subtitle }}        <!-- 文章副标题 -->
{{ page.date }}            <!-- 发布日期 -->
{{ page.category }}        <!-- 分类 -->
{{ page.reading_time }}    <!-- 阅读时长 -->
{{ content }}              <!-- 文章正文 HTML -->
```

### 6. 文章源文件 (_articles/*.md)

**职责：** 存储文章内容的 Markdown 文件

**Frontmatter 格式：**
```yaml
---
title: "文章标题"              # 必填
subtitle: "副标题"             # 必填
description: "SEO 描述"        # 必填，用于搜索引擎优化
date: 2025-05-20               # 必填，格式：YYYY-MM-DD
category: "教程"               # 必填，可选值：教程、对比、测评
tags: ["MCP", "入门指南"]      # 可选，标签数组
reading_time: 8                # 必填，预估阅读分钟数
author: "作者名"               # 可选
lang: zh                       # 必填，可选值：zh、en
layout: article                # 可选，默认：article；测评类使用：review
---
```

---

## 依赖关系

### Python 依赖
- `markdown` - Markdown 解析库

### GitHub Actions 工作流

**deploy.yml：**
- 触发条件：`push` 到 `main` 分支 或 手动触发
- 构建步骤：
  1. Checkout 代码
  2. 安装 Python 3.x
  3. 运行 `scripts/build.py`
  4. 上传 `_site/` 目录
  5. 部署到 GitHub Pages

**update-data.yml：**
- 触发条件：每周一 00:00 UTC
- 功能：自动更新 Skills 和 MCP 数据

---

## 数据来源

| 数据源 | 说明 |
|--------|------|
| [skills.sh](https://skills.sh/) | Skills 排行榜官方数据 |
| [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | MCP 服务器开源列表 |
| [mcp.so](https://mcp.so) | MCP 聚合平台 |
| [skillhub.cn](https://skillhub.cn/) | 技能包聚合平台 |

---

## 关键配置

### GitHub Pages 配置
- **部署方式：** GitHub Actions → GitHub Pages
- **baseurl：** `/ai-skills-mcp-ranking`

---

## 文件清单

| 文件路径 | 说明 | 行数 |
|----------|------|------|
| index.html | 主页面入口 | ~600 |
| scripts/build.py | 静态站点构建脚本 | ~230 |
| js/main.js | 主 JavaScript 功能 | ~100 |
| css/style.css | 主样式文件 | ~500 |
| _layouts/article.html | 文章详情页模板 | ~20 |
| _articles/*.md | 4篇技术文章和测评 |

---

*最后更新：2026-05-22*
