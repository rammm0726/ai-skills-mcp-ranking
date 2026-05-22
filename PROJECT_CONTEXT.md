# AI Skills & MCP Ranking 项目上下文

> 整理时间：2026-05-21
> 整理目的：供 SOLO 继续后续任务

---

## 1. 项目概述

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

## 2. 项目结构

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

## 3. 核心功能实现

### 3.1 页面结构

**主页（index.html）：**
- 顶部导航：Skills 排行榜 | MCP 排行榜 | 技术文章 | 工具测评
- Skills 排行榜表格（带搜索框）
- MCP 排行榜表格（带搜索框）
- 技术文章列表（带搜索框）
- 工具测评列表（带搜索框）

**文章详情页：**
- 由 `scripts/build.py` 从 `_articles/*.md` 生成
- 输出到 `_site/articles/{slug}/index.html`
- 使用 `_layouts/article.html` 模板

### 3.2 搜索功能

```javascript
// 技术文章搜索
var ARTICLES_DATA = [...];  // 文章数据数组
function renderArticles(data) { ... }  // 渲染函数
// 搜索过滤：标题、副标题、分类

// 工具测评搜索
var REVIEWS_DATA = [...];   // 测评数据数组
function renderReviews(data) { ... }
```

### 3.3 构建系统

**构建脚本：** `scripts/build.py`

**功能：**
- 解析 Markdown Frontmatter
- 转换 Markdown → HTML（支持表格、列表、代码块、内联格式）
- 处理 Liquid 模板变量（`{{ page.title }}`、`{{ content }}` 等）
- 生成静态 HTML 文件到 `_site/`

**构建命令：**
```bash
python scripts/build.py
```

---

## 4. 已完成的工作

### 4.1 功能实现 ✅

| 功能 | 状态 | 说明 |
|------|------|------|
| Skills 排行榜 | ✅ | 完整表格 + 搜索 |
| MCP 排行榜 | ✅ | 完整表格 + 搜索 |
| 技术文章板块 | ✅ | 4篇文章 + 搜索框 |
| 工具测评板块 | ✅ | 2篇测评 + 搜索框 |
| 文章详情页 | ✅ | Markdown → HTML 渲染 |
| 表格渲染 | ✅ | 支持加粗、代码等内联格式 |
| 搜索过滤 | ✅ | 实时搜索，按标题/副标题/分类过滤 |
| 多语言切换 | ✅ | CN/EN 切换 |

### 4.2 代码清理 ✅

**已删除文件（15个）：**
- `_site/` 整个目录（13个文件）- 构建产物，已加入 .gitignore
- `articles.html` - 未使用的 Jekyll 残留
- `_config.yml` - build.py 未读取的配置

**已安装技能：**
- `jeffallan/claude-skills@code-reviewer` (2.9K installs)

---

## 5. 待办事项 / 后续任务

### 5.1 已知问题

1. **文章页面导航问题**
   - 点击文章详情页后，导航栏的 Tab 切换需要优化
   - 当前从文章页点击 Skills/MCP 标签应正确跳转回首页

2. **GitHub Pages 部署**
   - 需要验证部署后路径是否正确（baseurl: `/ai-skills-mcp-ranking`）
   - 检查 CSS/JS 资源加载是否正常

3. **数据更新工作流**
   - `.github/workflows/update-data.yml` 只更新数据，没有重新构建 `_site`
   - 需要添加构建步骤或修改部署方式

### 5.2 建议优化

1. **SEO 优化**
   - 添加 meta description、keywords
   - 添加 Open Graph 标签
   - 添加 sitemap.xml

2. **性能优化**
   - 图片懒加载
   - 数据分页（如果数据量增大）

3. **内容扩展**
   - 添加更多技术文章
   - 添加更多工具测评
   - 添加文章标签/分类筛选

### 5.3 技术债务

1. **构建脚本改进**
   - 当前 `build.py` 硬编码了 site_config
   - 可考虑从配置文件读取

2. **模板系统**
   - 当前使用简单的字符串替换处理 Liquid 模板
   - 复杂逻辑（如 for 循环）已移除简化

---

## 6. 关键配置

### 6.1 GitHub Pages 配置

**部署方式：** GitHub Actions → GitHub Pages

**baseurl：** `/ai-skills-mcp-ranking`

**访问地址：** `https://rammm0726.github.io/ai-skills-mcp-ranking/`

### 6.2 构建配置

```python
# scripts/build.py 中的硬编码配置
site_config = {
    'title': 'AI Agent Skills & MCP Ranking',
    'description': '全网最受欢迎的 AI Agent 技能包和 MCP 服务器排行榜',
    'url': 'https://rammm0726.github.io',
    'baseurl': '/ai-skills-mcp-ranking',
    'articles': load_articles()
}
```

### 6.3 .gitignore

```
# 构建产物
_site/

# Python 缓存
__pycache__/
*.pyc

# 依赖
node_modules/

# 其他...
```

---

## 7. 本地开发

**启动本地服务器：**
```bash
cd ai-skills-mcp-ranking
python scripts/build.py  # 构建
python -m http.server 8080  # 启动服务器
cd _site && python -m http.server 8080  # 或直接服务构建产物
```

**访问：** http://localhost:8080

---

## 8. 部署流程

1. 本地修改代码
2. 运行 `python scripts/build.py` 测试构建
3. 本地浏览器验证（localhost:8080）
4. `git add -A && git commit -m "..."`
5. `git push origin main`
6. GitHub Actions 自动部署到 GitHub Pages

---

## 9. 重要文件内容

### 9.1 index.html 关键结构

```html
<!-- 导航栏 -->
<nav class="main-nav">
  <div class="tabs" id="nav-tabs">
    <button class="tab" data-tab="skills">Skills 排行榜</button>
    <button class="tab" data-tab="mcp">MCP 排行榜</button>
    <button class="tab" data-tab="articles">技术文章</button>
    <button class="tab" data-tab="reviews">工具测评</button>
  </div>
</nav>

<!-- 内容区域 -->
<div id="skills-section">...</div>
<div id="mcp-section">...</div>
<div id="articles-section">...</div>
<div id="reviews-section">...</div>
```

### 9.2 文章 Frontmatter 格式

```yaml
---
title: "文章标题"
subtitle: "副标题"
category: "教程"
date: "2025-05-20"
reading_time: 8
---

文章内容...
```

---

## 10. 联系方式与资源

- **GitHub 仓库：** https://github.com/rammm0726/ai-skills-mcp-ranking
- **Skills 官网：** https://skills.sh/
- **MCP 资源：** https://github.com/punkpeye/awesome-mcp-servers

---

*文档结束*
