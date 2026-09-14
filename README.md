# 随星录 · 世界观设定精简版

从 [完整版 SOW](https://github.com/Meauzeek/SOW) 独立整理的轻量仓库，面向世界观记录、文字编辑和网页版 AI 阅读。使用全新的 Git 历史，不包含完整版历史中的图片、字体和高程大文件。

- **123 个国家与地区、437 座城市**，保留名称、语言、人口、GDP、现实原型、主权归属与设定备注。
- 保留现有架空疆域的轻量交互地图；没有城市照片、国旗国徽图片、DEM、高程、地形、海侵计算、夜景贴图或原图扫描件。
- 无构建步骤、无服务端、无外部字体请求。网页支持搜索、文字资料编辑、城市增删、浏览器保存及 JSON 导入导出。
- 工作文件总量远低于 **100 MB**。运行 `python scripts/validate.py` 可复核。

## 阅读或交给 AI

1. [设定说明](docs/AI_CONTEXT.md)：资料来源、单位及已确认的关键设定。
2. [国家索引](docs/COUNTRY_INDEX.md)：每个国家及其城市的 Markdown 章节。
3. `data/countries.json`、`data/cities.json`：完整文字字段，适合检索和修改。
4. `data/boundaries.geojson`：只在需要理解地图边界时使用。仅做文字讨论不必上传这个文件。

GitHub 的 **Code → Download ZIP** 可下载整个精简仓库。若网页版 AI 不接收仓库链接，可上传 ZIP，或只上传 `docs/` 与两个资料 JSON 文件。不同 AI 的上传限制不同。

## 打开网页

在线地址：<https://meauzeek.github.io/SOW-worldbuilding-lite/>

本地预览：在仓库目录运行 `python -m http.server 4175 --bind 127.0.0.1`，然后访问 <http://127.0.0.1:4175/>。直接双击 HTML 可能因浏览器限制无法读取 JSON。

网页修改保存在当前浏览器，**不会自动写回 GitHub**。点击“下载设定 JSON”备份；再次导入可恢复。该导出格式为本精简版专用，完整版 JSON 不能直接导入。

## 维护数据

`data/` 是当前发布设定；`docs/countries/` 是由其生成的可读副本。修改 JSON 后运行：

```sh
python scripts/generate_docs.py
python scripts/validate.py
```

人口单位为**人**，`gdpHundredMillionUSD` 单位为**亿美元**；已从完整版的内部“十亿美元”数值乘以 10 转换。原有数据中的创作估算标识保留，不能把这些数值当成现实统计或已全部确认的小说设定。

基准：完整版提交 5c9db8bd8958d5bf4a1801fdd36db27b3408f314，整理日期 2026-09-14。精简版与完整版独立维护，不会自动覆盖或同步对方。

作者世界观资料的权利归原作者所有。第三方地图来源及 D3 许可见 [来源与许可](docs/SOURCES.md)。
