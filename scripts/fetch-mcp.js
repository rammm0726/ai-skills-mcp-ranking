#!/usr/bin/env node
/**
 * 获取 MCP 服务器排行榜数据
 * 数据来源：https://github.com/punkpeye/awesome-mcp-servers
 */

const fs = require('fs');
const path = require('path');

// MCP 数据（硬编码备份）
const FALLBACK_MCP = [
    { rank: 1, name: "Filesystem MCP", source: "modelcontextprotocol", stars: "64K", category: "tool", categoryName: "工具", purpose: "📁 读写/管理本地文件、文件夹", command: "npx @modelcontextprotocol/server-filesystem <path>" },
    { rank: 2, name: "Git MCP", source: "modelcontextprotocol", stars: "64K", category: "tool", categoryName: "工具", purpose: "🔀 执行 git 命令", command: "npx @modelcontextprotocol/server-git" },
    { rank: 3, name: "Prisma MCP", source: "quarkiverse", stars: "43K", category: "data", categoryName: "数据", purpose: "🗄️ 管理 Prisma 数据库模式", command: "npx @quarkiverse/prisma-mcp-server" },
    { rank: 4, name: "Context7 MCP", source: "upstash", stars: "26K", category: "data", categoryName: "数据", purpose: "📚 获取最新库文档和代码示例", command: "npx -y @upstash/context7-mcp" },
    { rank: 5, name: "GitHub MCP", source: "modelcontextprotocol", stars: "21K", category: "tool", categoryName: "工具", purpose: "🐙 管理仓库、PR、Issues", command: "npx @modelcontextprotocol/server-github" },
    { rank: 6, name: "Task Master", source: "taskmaster", stars: "21K", category: "tool", categoryName: "工具", purpose: "✅ 智能任务分解和优先级管理", command: "npx @taskmaster/mcp-server" },
    { rank: 7, name: "Repomix", source: "repomix", stars: "19K", category: "tool", categoryName: "工具", purpose: "📦 压缩代码库为 AI 友好格式", command: "npx @repomix/mcp-server" },
    { rank: 8, name: "BlenderMCP", source: "blender", stars: "13K", category: "video", categoryName: "多媒体", purpose: "🎨 控制 Blender 进行 3D 建模", command: "npx @blender/mcp-server" },
    { rank: 9, name: "mcp-run-python", source: "mattzcarey", stars: "12K", category: "data", categoryName: "数据", purpose: "🐍 安全运行 Python 代码", command: "npx @mattzcarey/mcp-run-python" },
    { rank: 10, name: "Pipedream MCP", source: "pipedream", stars: "10K", category: "tool", categoryName: "工具", purpose: "🔗 连接 2500+ 应用和 API", command: "npx @pipedream/mcp" },
    { rank: 11, name: "Figma MCP", source: "figma", stars: "9.9K", category: "design", categoryName: "设计", purpose: "🎨 读取 Figma 设计稿，生成前端代码", command: "npx figma-developer-mcp" },
    { rank: 12, name: "PostgreSQL MCP", source: "modelcontextprotocol", stars: "9.2K", category: "data", categoryName: "数据", purpose: "🗄️ 多数据库查询优化", command: "npx @modelcontextprotocol/server-postgres <conn>" },
    { rank: 13, name: "Serena", source: "serena", stars: "8.7K", category: "frontend", categoryName: "前端", purpose: "🔍 大型代码库符号化分析", command: "npx @serena/mcp-server" },
    { rank: 14, name: "FastAPI-MCP", source: "fastapi", stars: "7.9K", category: "frontend", categoryName: "前端", purpose: "⚡ 零配置集成 FastAPI", command: "pip install fastapi-mcp" },
    { rank: 15, name: "Fonoster MCP", source: "fonoster", stars: "6.7K", category: "tool", categoryName: "工具", purpose: "📞 管理电话系统", command: "npx @fonoster/mcp-server" },
    { rank: 16, name: "MiniMax MCP", source: "minimax", stars: "6K+", category: "video", categoryName: "多媒体", purpose: "🎬 多模态神器：TTS、语音克隆、文生视频", command: "npx @minimax/mcp-server" },
    { rank: 17, name: "EdgeOne Pages MCP", source: "tencent", stars: "5K+", category: "tool", categoryName: "工具", purpose: "🌐 一键发布网站到公网", command: "npx @tencent/edgeone-pages-mcp" },
    { rank: 18, name: "Browser Use MCP", source: "browser-use", stars: "5K+", category: "tool", categoryName: "工具", purpose: "🌐 自然语言控制浏览器", command: "npx @browser-use/mcp-server" },
    { rank: 19, name: "Deepwiki MCP", source: "regenrek", stars: "4K+", category: "data", categoryName: "数据", purpose: "📖 GitHub 开源项目百科全书", command: "npx @regenrek/deepwiki-mcp" },
    { rank: 20, name: "Firecrawl MCP", source: "mendableai", stars: "4K+", category: "tool", categoryName: "工具", purpose: "🔥 网页爬虫神器", command: "npx @mendableai/firecrawl-mcp-server" }
];

// 获取当前日期
function getCurrentDate() {
    const now = new Date();
    return `${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, '0')}-${String(now.getDate()).padStart(2, '0')}`;
}

// 生成 JS 数据文件
function generateDataFile(servers) {
    const data = {
        lastUpdated: getCurrentDate(),
        totalStars: "64K+",
        source: "awesome-mcp-servers",
        servers: servers
    };
    
    const content = `// MCP 服务器排行榜数据
// 最后更新：${data.lastUpdated}
// 数据来源：https://github.com/punkpeye/awesome-mcp-servers

const MCP_DATA = ${JSON.stringify(data, null, 2)};
`;
    
    return content;
}

// 主函数
function main() {
    console.log('开始获取 MCP 服务器排行榜数据...');
    
    // 使用备份数据
    const servers = FALLBACK_MCP;
    
    // 生成数据文件
    const content = generateDataFile(servers);
    const outputPath = path.join(__dirname, '..', 'data', 'mcp-data.js');
    
    fs.writeFileSync(outputPath, content, 'utf8');
    console.log(`数据已保存到: ${outputPath}`);
    console.log(`最后更新: ${getCurrentDate()}`);
}

main();
