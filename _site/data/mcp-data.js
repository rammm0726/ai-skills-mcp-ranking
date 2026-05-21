// MCP 服务器排行榜数据
// 最后更新：2026-05-20
// 数据来源：https://github.com/punkpeye/awesome-mcp-servers

const MCP_DATA = {
  lastUpdated: "2026-05-20",
  totalStars: "64K+",
  source: "awesome-mcp-servers",
  servers: [
    { rank: 1, name: "Filesystem MCP", source: "modelcontextprotocol", stars: "64K", category: "tool", categoryName: "工具", purpose: "📁 读写/管理本地文件、文件夹，代码分析、文档生成必备", command: "npx @modelcontextprotocol/server-filesystem <path>" },
    { rank: 2, name: "Git MCP", source: "modelcontextprotocol", stars: "64K", category: "tool", categoryName: "工具", purpose: "🔀 执行 git 命令，commit/push/pull/branch/merge", command: "npx @modelcontextprotocol/server-git" },
    { rank: 3, name: "Prisma MCP", source: "quarkiverse", stars: "43K", category: "data", categoryName: "数据", purpose: "🗄️ 管理 Prisma 数据库模式，schema 迁移、查询优化", command: "npx @quarkiverse/prisma-mcp-server" },
    { rank: 4, name: "Context7 MCP", source: "upstash", stars: "26K", category: "data", categoryName: "数据", purpose: "📚 获取最新库文档和代码示例，解决 AI 知识过时问题", command: "npx -y @upstash/context7-mcp" },
    { rank: 5, name: "GitHub MCP", source: "modelcontextprotocol", stars: "21K", category: "tool", categoryName: "工具", purpose: "🐙 管理仓库、PR、Issues、Actions，开源项目管理必备", command: "npx @modelcontextprotocol/server-github" },
    { rank: 6, name: "Task Master", source: "taskmaster", stars: "21K", category: "tool", categoryName: "工具", purpose: "✅ 智能任务分解和优先级管理，依赖追踪、进度可视化", command: "npx @taskmaster/mcp-server" },
    { rank: 7, name: "Repomix", source: "repomix", stars: "19K", category: "tool", categoryName: "工具", purpose: "📦 压缩代码库为 AI 友好格式，大型代码审查必备", command: "npx @repomix/mcp-server" },
    { rank: 8, name: "BlenderMCP", source: "blender", stars: "13K", category: "video", categoryName: "多媒体", purpose: "🎨 控制 Blender 进行 3D 建模、渲染、动画", command: "npx @blender/mcp-server" },
    { rank: 9, name: "mcp-run-python", source: "mattzcarey", stars: "12K", category: "data", categoryName: "数据", purpose: "🐍 安全运行 Python 代码，沙箱执行、算法验证", command: "npx @mattzcarey/mcp-run-python" },
    { rank: 10, name: "Pipedream MCP", source: "pipedream", stars: "10K", category: "tool", categoryName: "工具", purpose: "🔗 连接 2500+ 应用和 API，业务流程自动化", command: "npx @pipedream/mcp" },
    { rank: 11, name: "Figma MCP", source: "figma", stars: "9.9K", category: "design", categoryName: "设计", purpose: "🎨 读取 Figma 设计稿，生成前端代码，设计转代码神器", command: "npx figma-developer-mcp" },
    { rank: 12, name: "PostgreSQL MCP", source: "modelcontextprotocol", stars: "9.2K", category: "data", categoryName: "数据", purpose: "🗄️ 多数据库查询优化，PostgreSQL/MySQL/SQLite/MongoDB", command: "npx @modelcontextprotocol/server-postgres <conn>" },
    { rank: 13, name: "Serena", source: "serena", stars: "8.7K", category: "frontend", categoryName: "前端", purpose: "🔍 大型代码库符号化分析，跨文件引用、依赖追踪", command: "npx @serena/mcp-server" },
    { rank: 14, name: "FastAPI-MCP", source: "fastapi", stars: "7.9K", category: "frontend", categoryName: "前端", purpose: "⚡ 零配置集成 FastAPI，自动生成 OpenAPI 文档", command: "pip install fastapi-mcp" },
    { rank: 15, name: "Fonoster MCP", source: "fonoster", stars: "6.7K", category: "tool", categoryName: "工具", purpose: "📞 管理电话系统，VoIP、呼叫路由、语音信箱", command: "npx @fonoster/mcp-server" },
    { rank: 16, name: "MiniMax MCP", source: "minimax", stars: "6K+", category: "video", categoryName: "多媒体", purpose: "🎬 多模态神器：TTS、语音克隆、文生视频、图生视频", command: "npx @minimax/mcp-server" },
    { rank: 17, name: "EdgeOne Pages MCP", source: "tencent", stars: "5K+", category: "tool", categoryName: "工具", purpose: "🌐 腾讯出品，一键发布 AI 生成的网站到公网", command: "npx @tencent/edgeone-pages-mcp" },
    { rank: 18, name: "Browser Use MCP", source: "browser-use", stars: "5K+", category: "tool", categoryName: "工具", purpose: "🌐 自然语言控制浏览器，网页抓取、自动化测试", command: "npx @browser-use/mcp-server" },
    { rank: 19, name: "Deepwiki MCP", source: "regenrek", stars: "4K+", category: "data", categoryName: "数据", purpose: "📖 GitHub 开源项目百科全书，索引 3 万+ 仓库", command: "npx @regenrek/deepwiki-mcp" },
    { rank: 20, name: "Firecrawl MCP", source: "mendableai", stars: "4K+", category: "tool", categoryName: "工具", purpose: "🔥 网页爬虫神器，支持静态/动态网页、子页面抓取", command: "npx @mendableai/firecrawl-mcp-server" }
  ]
};
