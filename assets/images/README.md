# 图片资源目录

此目录用于存放文章中的图片资源。

## 目录结构

```
assets/
└── images/
    └── {article-slug}/      # 每篇文章的图片放在独立的子目录
        ├── image1.png
        └── image2.jpg
```

## 使用说明

1. **自动管理**：通过 `scripts/import_obsidian.py` 导入文章时，图片会自动复制到对应目录

2. **手动添加**：如果需要手动添加图片，请创建以文章 slug 命名的子目录

3. **推荐格式**：
   - 使用 WebP 格式（现代浏览器支持，更小体积）
   - PNG 用于需要透明背景的图片
   - JPG 用于照片类图片

4. **图片引用**：在 Markdown 中使用相对路径引用：
   ```markdown
   ![图片描述](../assets/images/article-slug/image.png)
   ```
