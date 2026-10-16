# 布布一二蹭脸

布布在左，一二在右，身体相向、双臂抱住、脸贴脸轻轻动的 Codex 双人组合宠物。

<p><img src="previews/hover-hug.gif" width="192" height="208" alt="布布一二抱抱动画"> <img src="previews/idle.gif" width="192" height="208" alt="布布一二慢速依偎动画"></p>

左侧为悬停动作，右侧为慢速待机。当前版本为 v8：保留侧身拥抱、小爱心和小幅贴压动作，不是整组跳跃。

## 在 Codex 中使用

下载仓库，将 `pet/` 中的两个文件复制到自己的 Codex 宠物目录：

```text
~/.codex/pets/bubu-yier-duo/
├── pet.json
└── spritesheet.webp
```

Windows 对应 `%USERPROFILE%\.codex\pets\bubu-yier-duo\`。若已存在同名宠物，请先备份原目录。然后进入 **Settings → Pets → Refresh**，选择 **布布一二·贴贴**。鼠标悬停可触发抱抱动作。

若该本地宠物已经自动迁移到云端，替换本地文件不会更新现有云端副本；需在 Codex 中让 Pets 插件用新图集更新自己的现有自定义宠物。可以把 `pet/spritesheet.webp` 交给 Codex，并要求“更新我现有的布布一二宠物，保留原来的宠物 ID”。这不是 Settings 中的上传按钮。仓库不含任何账号的云端宠物 ID 或凭据。

以上格式与交互在 Codex `26.1007.9446` 上核实，后续版本可能变化。原生悬停使用 5 帧，一轮 840 ms，通常播放三轮后回到待机；待机完整循环为 6.6 秒，视线状态可能覆盖待机动画。动作是轻柔贴压，仍有有限帧数带来的逐帧感。

## 文件

| 路径 | 用途 |
| --- | --- |
| `pet/` | 可直接复制安装的最终 v2 图集和配置 |
| `previews/` | GIF、透明 animated WebP 和逐帧联系表 |
| `source/hug-five.png` | 内置 image_gen 生成的五帧原始图 |
| `source/frames/` | 从最终图集提取的五张透明帧，192×208 |
| `source/prompt.txt` | 本次生成使用的提示词 |
| `tools/build.py` | 使用编辑后的帧重建图集与预览，并验证结构 |
| `docs/DEVELOPMENT.md` | 图集布局、动作约束、验证与已知限制 |
| `checksums.json` | 发布素材的 SHA-256 校验值 |

无需 Python 即可使用 `pet/`。仅在修改、构建素材时需要 Python 和 Pillow：

```sh
python -m pip install -r requirements.txt
python tools/build.py
```

构建输出到 `dist/`，不会修改已安装宠物。代码不会调用图像生成 API，也不会自动上传云端。

## 制作与来源

素材通过 OpenAI 内置 image_gen，根据用户提供的布布一二形象及拥抱姿态参考生成，再进行透明帧提取、共享缩放、图集装配和验证。早期制作参考了 [MakerCore/hatch-pet](https://github.com/MakerCore/hatch-pet) 的图集工作流；本仓库未包含该工具或 Codex 私有运行代码。

本项目为非官方同人宠物制作记录。布布、一二等角色及原参考作品的权利归原权利人；本仓库不授予这些角色或参考作品的商用许可。
