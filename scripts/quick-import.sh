#!/bin/bash
#
# Obsidian 文章快速导入脚本
# 
# 用法:
#   ./quick-import.sh <文章文件路径> [Vault路径]
#   ./quick-import.sh --help
#
# 示例:
#   ./quick-import.sh ~/Obsidian/my-article.md
#   ./quick-import.sh ~/Obsidian/my-article.md ~/Obsidian
#   ./quick-import.sh --dry-run ~/Obsidian/my-article.md
#

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
IMPORT_SCRIPT="$SCRIPT_DIR/import_obsidian.py"

show_help() {
    cat << EOF
Obsidian 文章快速导入工具

用法:
    $0 <文章路径> [Vault路径]

参数:
    文章路径    Obsidian 中的 Markdown 文件路径
    Vault路径  (可选) Obsidian Vault 根目录，用于查找图片

示例:
    # 导入单个文章
    $0 ~/Obsidian/my-article.md

    # 指定 Vault 路径
    $0 ~/Obsidian/my-article.md ~/Obsidian

    # 预览模式（不写入）
    $0 --dry-run ~/Obsidian/my-article.md

    # 扫描整个 Vault
    $0 --scan ~/Obsidian/Vault

    # 指定文章分类
    $0 ~/Obsidian/my-article.md -c 测评

EOF
}

if [ "$1" == "--help" ] || [ "$1" == "-h" ]; then
    show_help
    exit 0
fi

if [ ! -f "$IMPORT_SCRIPT" ]; then
    echo "错误: 找不到导入脚本 $IMPORT_SCRIPT"
    exit 1
fi

cd "$SCRIPT_DIR/.."

python3 "$IMPORT_SCRIPT" "$@"

echo ""
echo "========================================"
echo "📌 下一步操作:"
echo "   1. 检查生成的 .md 文件"
echo "   2. 编辑 frontmatter 补充信息"
echo "   3. 运行构建: python scripts/build.py"
echo "   4. 提交并推送到 GitHub"
echo "========================================"
