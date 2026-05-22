// Skills 排行榜数据
// 最后更新：2026-05-20
// 数据来源：https://skills.sh/

const SKILLS_DATA = {
  lastUpdated: "2026-05-20",
  totalInstalls: "1.6M+",
  source: "skills.sh",
  skills: [
    { rank: 1, name: "find-skills", source: "vercel-labs", installs: "1.6M", category: "tool", categoryName: "工具", purpose: "🔍 智能搜索和安装 Skills，从 85,000+ 技能库中搜索最合适的方案", command: "npx skills add vercel-labs/skills@find-skills" },
    { rank: 2, name: "frontend-design", source: "anthropics", installs: "433.7K", category: "design", categoryName: "设计", purpose: "🎨 生产级前端界面设计，反"AI 味"宣言——拒绝同质化设计", command: "npx skills add anthropics/skills@frontend-design" },
    { rank: 3, name: "vercel-react-best-practices", source: "vercel-labs", installs: "412.1K", category: "frontend", categoryName: "前端", purpose: "⚡ React/Next.js 性能优化指南，64 条规则覆盖 8 大类别", command: "npx skills add vercel-labs/agent-skills@vercel-react-best-practices" },
    { rank: 4, name: "microsoft-foundry", source: "microsoft", installs: "331.5K", category: "azure", categoryName: "Azure", purpose: "🏗️ Microsoft Foundry 企业开发平台集成", command: "npx skills add microsoft/azure-skills@microsoft-foundry" },
    { rank: 5, name: "web-design-guidelines", source: "vercel-labs", installs: "331.0K", category: "design", categoryName: "设计", purpose: "✅ Web 界面设计规范审查，file:line 格式精确问题定位", command: "npx skills add vercel-labs/agent-skills@web-design-guidelines" },
    { rank: 6, name: "azure-ai", source: "microsoft", installs: "330.0K", category: "azure", categoryName: "Azure", purpose: "🤖 Azure AI 服务集成，AI Search/Speech/OpenAI", command: "npx skills add microsoft/azure-skills@azure-ai" },
    { rank: 7, name: "azure-messaging", source: "microsoft", installs: "318.7K", category: "azure", categoryName: "Azure", purpose: "📨 Azure 消息服务，Service Bus/Event Grid/Hubs", command: "npx skills add microsoft/azure-skills@azure-messaging" },
    { rank: 8, name: "azure-hosted-copilot-sdk", source: "microsoft", installs: "302.2K", category: "azure", categoryName: "Azure", purpose: "🤖 Azure 托管 Copilot SDK，快速构建 AI 助手", command: "npx skills add microsoft/azure-skills@azure-hosted-copilot-sdk" },
    { rank: 9, name: "remotion-best-practices", source: "remotion-dev", installs: "319.3K", category: "video", categoryName: "多媒体", purpose: "🎬 React 视频程序化创作，30+ 规则覆盖动画/3D/图表", command: "npx skills add remotion-dev/skills@remotion-best-practices" },
    { rank: 10, name: "agent-browser", source: "vercel-labs", installs: "288.8K", category: "tool", categoryName: "工具", purpose: "🌐 持久化浏览器自动化，支持 Headless/真实 Chrome", command: "npx skills add vercel-labs/agent-browser@agent-browser" },
    { rank: 11, name: "azure-compute", source: "microsoft", installs: "273.0K", category: "azure", categoryName: "Azure", purpose: "💻 Azure 计算服务，VM/Functions/Container Instances", command: "npx skills add microsoft/azure-skills@azure-compute" },
    { rank: 12, name: "azure-cloud-migrate", source: "microsoft", installs: "263.3K", category: "azure", categoryName: "Azure", purpose: "☁️ Azure 云迁移工具，评估、规划、执行迁移", command: "npx skills add microsoft/azure-skills@azure-cloud-migrate" },
    { rank: 13, name: "skill-creator", source: "anthropics", installs: "219.3K", category: "tool", categoryName: "工具", purpose: "🔧 Skills 开发与迭代工具，包含完整开发流程", command: "npx skills add anthropics/skills@skill-creator" },
    { rank: 14, name: "azure-cost-optimization", source: "microsoft", installs: "205.8K", category: "azure", categoryName: "Azure", purpose: "💰 Azure 成本优化，云支出分析与降本策略", command: "npx skills add microsoft/azure-skills@azure-cost-optimization" },
    { rank: 15, name: "azure-quotas", source: "microsoft", installs: "200.3K", category: "azure", categoryName: "Azure", purpose: "📊 Azure 配额管理，查询和申请资源配额提升", command: "npx skills add microsoft/azure-skills@azure-quotas" },
    { rank: 16, name: "azure-upgrade", source: "microsoft", installs: "192.9K", category: "azure", categoryName: "Azure", purpose: "⬆️ Azure 服务升级管理，规划版本升级路径", command: "npx skills add microsoft/azure-skills@azure-upgrade" },
    { rank: 17, name: "vercel-composition-patterns", source: "vercel-labs", installs: "180.1K", category: "frontend", categoryName: "前端", purpose: "🧩 React 组件组合模式，解决 boolean prop 问题", command: "npx skills add vercel-labs/agent-skills@vercel-composition-patterns" },
    { rank: 18, name: "supabase-postgres-best-practices", source: "supabase", installs: "177.2K", category: "data", categoryName: "数据", purpose: "🗄️ Supabase/PostgreSQL 最佳实践，RLS/索引优化", command: "npx skills add supabase/agent-skills@supabase-postgres-best-practices" },
    { rank: 19, name: "ui-ux-pro-max", source: "nextlevelbuilder", installs: "173.3K", category: "design", categoryName: "设计", purpose: "🖼️ UI/UX 设计全栈能力，50+ 风格/161 套配色", command: "npx skills add nextlevelbuilder/ui-ux-pro-max-skill@ui-ux-pro-max" },
    { rank: 20, name: "grill-me", source: "mattpocock", installs: "173.3K", category: "tool", categoryName: "工具", purpose: "🔥 代码评审与质疑，深度追问发现潜在问题", command: "npx skills add mattpocock/skills@grill-me" }
  ]
};
