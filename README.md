# AI Agent Skills & MCP 排行榜

全网最受欢迎的 AI Agent 技能包和 MCP 服务器榜单。

## 🌐 访问地址

GitHub Pages: https://rrramxy.github.io/ai-skills-mcp-ranking/

## ✨ 功能特性

- 📦 **Skills 排行榜**：展示全网最受欢迎的 AI Agent 技能包
- 🔌 **MCP 服务器排行榜**：展示最受欢迎的 MCP 服务器
- 🔍 **实时搜索**：支持按名称、功能搜索
- 🏷️ **分类筛选**：按前端、Azure、工具、设计等分类筛选
- 📋 **一键复制**：点击安装命令即可复制
- 🔄 **自动更新**：每周一自动更新数据

## 📊 数据来源

- [skills.sh](https://skills.sh/) - Skills 排行榜
- [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) - MCP 服务器列表
- [mcp.so](https://mcp.so) - MCP 聚合平台

## 🛠️ 本地开发

```bash
# 克隆仓库
git clone https://github.com/rrramxy/ai-skills-mcp-ranking.git

# 进入目录
cd ai-skills-mcp-ranking

# 本地预览（使用任意静态服务器）
npx serve .
# 或
python -m http.server 8080
```

## 📁 项目结构

```
ai-skills-mcp-ranking/
├── .github/workflows/    # GitHub Actions
├── data/                 # 数据文件
├── css/                  # 样式文件
├── js/                   # JavaScript
├── scripts/              # 数据获取脚本
└── index.html            # 主页面
```

## 📅 更新频率

- **自动更新**：每周一 00:00 UTC（北京时间周一 08:00）
- **手动更新**：可通过 GitHub Actions 手动触发

## 📄 License

MIT License
