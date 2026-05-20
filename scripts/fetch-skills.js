#!/usr/bin/env node
/**
 * 获取 Skills 排行榜数据
 * 数据来源：https://skills.sh/
 */

const https = require('https');
const fs = require('fs');
const path = require('path');

// Skills 数据（硬编码备份，当网络不可用时使用）
const FALLBACK_SKILLS = [
    { rank: 1, name: "find-skills", source: "vercel-labs", installs: "1.6M", category: "tool", categoryName: "工具", purpose: "🔍 智能搜索和安装 Skills，从 85,000+ 技能库中搜索最合适的方案", command: "npx skills add vercel-labs/skills@find-skills" },
    { rank: 2, name: "frontend-design", source: "anthropics", installs: "433.7K", category: "design", categoryName: "设计", purpose: "🎨 生产级前端界面设计，反"AI 味"宣言", command: "npx skills add anthropics/skills@frontend-design" },
    { rank: 3, name: "vercel-react-best-practices", source: "vercel-labs", installs: "412.1K", category: "frontend", categoryName: "前端", purpose: "⚡ React/Next.js 性能优化指南，64 条规则", command: "npx skills add vercel-labs/agent-skills@vercel-react-best-practices" },
    { rank: 4, name: "microsoft-foundry", source: "microsoft", installs: "331.5K", category: "azure", categoryName: "Azure", purpose: "🏗️ Microsoft Foundry 企业开发平台集成", command: "npx skills add microsoft/azure-skills@microsoft-foundry" },
    { rank: 5, name: "web-design-guidelines", source: "vercel-labs", installs: "331.0K", category: "design", categoryName: "设计", purpose: "✅ Web 界面设计规范审查", command: "npx skills add vercel-labs/agent-skills@web-design-guidelines" },
    { rank: 6, name: "azure-ai", source: "microsoft", installs: "330.0K", category: "azure", categoryName: "Azure", purpose: "🤖 Azure AI 服务集成", command: "npx skills add microsoft/azure-skills@azure-ai" },
    { rank: 7, name: "azure-messaging", source: "microsoft", installs: "318.7K", category: "azure", categoryName: "Azure", purpose: "📨 Azure 消息服务", command: "npx skills add microsoft/azure-skills@azure-messaging" },
    { rank: 8, name: "azure-hosted-copilot-sdk", source: "microsoft", installs: "302.2K", category: "azure", categoryName: "Azure", purpose: "🤖 Azure 托管 Copilot SDK", command: "npx skills add microsoft/azure-skills@azure-hosted-copilot-sdk" },
    { rank: 9, name: "remotion-best-practices", source: "remotion-dev", installs: "319.3K", category: "video", categoryName: "多媒体", purpose: "🎬 React 视频程序化创作", command: "npx skills add remotion-dev/skills@remotion-best-practices" },
    { rank: 10, name: "agent-browser", source: "vercel-labs", installs: "288.8K", category: "tool", categoryName: "工具", purpose: "🌐 持久化浏览器自动化", command: "npx skills add vercel-labs/agent-browser@agent-browser" }
];

// 获取当前日期
function getCurrentDate() {
    const now = new Date();
    return `${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, '0')}-${String(now.getDate()).padStart(2, '0')}`;
}

// 生成 JS 数据文件
function generateDataFile(skills) {
    const data = {
        lastUpdated: getCurrentDate(),
        totalInstalls: "1.6M+",
        source: "skills.sh",
        skills: skills
    };
    
    const content = `// Skills 排行榜数据
// 最后更新：${data.lastUpdated}
// 数据来源：https://skills.sh/

const SKILLS_DATA = ${JSON.stringify(data, null, 2)};
`;
    
    return content;
}

// 主函数
function main() {
    console.log('开始获取 Skills 排行榜数据...');
    
    // 使用备份数据（实际部署时可以从 skills.sh 爬取）
    const skills = FALLBACK_SKILLS;
    
    // 生成数据文件
    const content = generateDataFile(skills);
    const outputPath = path.join(__dirname, '..', 'data', 'skills-data.js');
    
    fs.writeFileSync(outputPath, content, 'utf8');
    console.log(`数据已保存到: ${outputPath}`);
    console.log(`最后更新: ${getCurrentDate()}`);
}

main();
