// AI Agent Skills & MCP 排行榜主逻辑

// DOM 元素
const skillsSection = document.getElementById('skills-section');
const mcpSection = document.getElementById('mcp-section');
const skillsBody = document.getElementById('skills-body');
const mcpBody = document.getElementById('mcp-body');
const skillsSearch = document.getElementById('skills-search');
const mcpSearch = document.getElementById('mcp-search');
const skillsNoResults = document.getElementById('skills-no-results');
const mcpNoResults = document.getElementById('mcp-no-results');
const lastUpdatedEl = document.getElementById('last-updated');
const footerUpdatedEl = document.getElementById('footer-updated');

// 当前筛选状态
let currentMcpFilter = 'all';

// 初始化
document.addEventListener('DOMContentLoaded', () => {
    // 显示最后更新时间
    if (SKILLS_DATA && SKILLS_DATA.lastUpdated) {
        if (lastUpdatedEl) lastUpdatedEl.textContent = SKILLS_DATA.lastUpdated;
        if (footerUpdatedEl) footerUpdatedEl.textContent = SKILLS_DATA.lastUpdated;
    }
    
    // 渲染数据
    renderSkills(SKILLS_DATA.skills);
    renderMcp(MCP_DATA.servers);
    
    // 绑定事件
    bindEvents();
});

// 绑定事件
function bindEvents() {
    // Tab 切换
    document.querySelectorAll('.tab').forEach(tab => {
        tab.addEventListener('click', () => {
            document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
            tab.classList.add('active');
            
            const tabName = tab.dataset.tab;
            skillsSection.classList.toggle('hidden', tabName !== 'skills');
            mcpSection.classList.toggle('hidden', tabName !== 'mcp');
        });
    });
    
    // Skills 搜索
    skillsSearch.addEventListener('input', (e) => {
        const query = e.target.value.toLowerCase();
        const filtered = SKILLS_DATA.skills.filter(item => 
            item.name.toLowerCase().includes(query) ||
            item.purpose.toLowerCase().includes(query) ||
            item.source.toLowerCase().includes(query)
        );
        renderSkills(filtered);
    });
    
    // MCP 搜索
    mcpSearch.addEventListener('input', (e) => {
        const query = e.target.value.toLowerCase();
        filterMcp(query);
    });
    
    // MCP 分类筛选
    document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            currentMcpFilter = btn.dataset.filter;
            filterMcp(mcpSearch.value.toLowerCase());
        });
    });
}

// 渲染 Skills 表格
function renderSkills(data) {
    if (data.length === 0) {
        skillsBody.innerHTML = '';
        skillsNoResults.classList.remove('hidden');
        return;
    }
    
    skillsNoResults.classList.add('hidden');
    skillsBody.innerHTML = data.map(item => `
        <tr>
            <td><span class="rank ${item.rank <= 3 ? 'rank-' + item.rank : ''}">${item.rank}</span></td>
            <td>
                <div class="name">${item.name}</div>
                <div class="source">${item.source}</div>
            </td>
            <td><span class="installs">${item.installs}</span></td>
            <td><span class="category-badge cat-${item.category}">${item.categoryName}</span></td>
            <td class="purpose">${item.purpose}</td>
            <td>
                <div class="command-container">
                    <span class="command" onclick="copyCommand(this)">${item.command}</span>
                    <button class="copy-btn" onclick="copyCommand(this.previousElementSibling)">复制</button>
                </div>
            </td>
        </tr>
    `).join('');
}

// 渲染 MCP 表格
function renderMcp(data) {
    if (data.length === 0) {
        mcpBody.innerHTML = '';
        mcpNoResults.classList.remove('hidden');
        return;
    }
    
    mcpNoResults.classList.add('hidden');
    mcpBody.innerHTML = data.map(item => `
        <tr>
            <td><span class="rank ${item.rank <= 3 ? 'rank-' + item.rank : ''}">${item.rank}</span></td>
            <td>
                <div class="name">${item.name}</div>
                <div class="source">${item.source}</div>
            </td>
            <td><span class="installs">${item.stars}</span></td>
            <td><span class="category-badge cat-${item.category}">${item.categoryName}</span></td>
            <td class="purpose">${item.purpose}</td>
            <td>
                <div class="command-container">
                    <span class="command" onclick="copyCommand(this)">${item.command}</span>
                    <button class="copy-btn" onclick="copyCommand(this.previousElementSibling)">复制</button>
                </div>
            </td>
        </tr>
    `).join('');
}

// MCP 筛选
function filterMcp(query) {
    let filtered = MCP_DATA.servers.filter(item => 
        item.name.toLowerCase().includes(query) ||
        item.purpose.toLowerCase().includes(query) ||
        item.source.toLowerCase().includes(query)
    );
    
    if (currentMcpFilter !== 'all') {
        filtered = filtered.filter(item => item.category === currentMcpFilter);
    }
    
    renderMcp(filtered);
}

// 复制命令
function copyCommand(element) {
    const text = element.textContent;
    navigator.clipboard.writeText(text).then(() => {
        const btn = element.nextElementSibling;
        if (btn && btn.classList.contains('copy-btn')) {
            btn.textContent = '已复制!';
            btn.classList.add('copied');
            setTimeout(() => {
                btn.textContent = '复制';
                btn.classList.remove('copied');
            }, 2000);
        }
    }).catch(err => {
        console.error('复制失败:', err);
        // 降级方案
        const textarea = document.createElement('textarea');
        textarea.value = text;
        document.body.appendChild(textarea);
        textarea.select();
        document.execCommand('copy');
        document.body.removeChild(textarea);
        
        const btn = element.nextElementSibling;
        if (btn && btn.classList.contains('copy-btn')) {
            btn.textContent = '已复制!';
            btn.classList.add('copied');
            setTimeout(() => {
                btn.textContent = '复制';
                btn.classList.remove('copied');
            }, 2000);
        }
    });
}
