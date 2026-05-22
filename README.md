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
