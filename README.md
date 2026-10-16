# 布布一二蹭脸

布布在左，一二在右，身体相向、双臂抱住、脸贴脸轻轻动的 Codex 双人组合宠物。


**[下载完整 ZIP](https://github.com/hlshen-coder/bubu-yier-cengceng/archive/refs/heads/main.zip)** · [直接看抱抱动图](previews/hover-hug.gif) · [安装步骤](#安装步骤windows) · [常见问题](#常见问题)

只想使用宠物？下载后只需要 `pet/` 文件夹内的 **两个文件**，无需安装 Python、Git，也无需 API Key 或重新生成图片。

## 动画预览

| 抱抱 · 鼠标悬停 | 依偎 · 慢速待机 |
| :---: | :---: |
| ![布布一二侧身抱抱动画](previews/hover-hug.gif) | ![布布一二慢速依偎动画](previews/idle.gif) |
| 身体相向、双臂抱住，脸颊小幅贴压 | 保持拥抱，缓慢贴近与回落 |

当前素材版本为 **v8**，保留侧身拥抱、小爱心和轻柔动作。这里的 GIF 会循环播放；Codex 中悬停动作通常播放三轮后转入待机，不会一直重复。原生悬停仅 5 帧，仍有轻微逐帧感。

GIF 为了显示柔和边缘使用浅色底；实际安装的 WebP 图集是透明背景。需要透明动画预览可打开 [悬停 WebP](previews/hover-hug.webp) / [待机 WebP](previews/idle.webp)。

## 使用条件

- 使用带有 **Settings → Pets** 入口、能读取自定义宠物的 Codex 桌面版本。
- 本项目的格式与交互在 **Windows / Codex `26.1007.9446`** 上核实；其他系统和后续版本的入口、导入方式可能不同。
- 这是宠物素材包，不是独立桌宠程序，也不需要把整个仓库安装成 Codex 插件。

## 安装步骤（Windows）

### 1. 下载并解压

点击上方 **下载完整 ZIP**，也可以在仓库首页点击绿色 **Code → Download ZIP**。下载后右键 ZIP，选择 **全部解压**。

打开解压后的 `bubu-yier-cengceng-main` 文件夹，找到：

```text
bubu-yier-cengceng-main/
└── pet/
    ├── pet.json           ← 宠物配置
    └── spritesheet.webp   ← 完整透明动画图集
```

两个文件都要保留原名。不要把 README 中的 GIF 或 `source/hug-five.png` 当成安装素材。

### 2. 打开宠物目录

按 **Win + R**，粘贴下面的路径并回车：

```text
%USERPROFILE%\.codex
```

在其中创建 `pets` 文件夹，再在 `pets` 内创建 `bubu-yier-duo` 文件夹。已有相应文件夹时直接打开。

这里使用默认 Codex 数据目录。如果你自行更改过 Codex 数据目录，应把后续的 `pets/bubu-yier-duo` 放到实际数据目录下。

### 3. 复制两个文件

把下载包 `pet/` 里的 `pet.json` 和 `spritesheet.webp` 复制进去。最终必须是：

```text
%USERPROFILE%\.codex\pets\bubu-yier-duo\
├── pet.json
└── spritesheet.webp
```

**不要多套一层 `pet` 文件夹。** `bubu-yier-duo/pet/pet.json` 这样的结构无法按本说明读取。

如果目标目录已经有同名文件，先把整个旧 `bubu-yier-duo` 文件夹复制到其他位置备份，再替换这两个文件。已安装旧版的用户还需看下方[更新已有宠物](#更新已有宠物)。

### 4. 在 Codex 中启用

1. 打开 Codex 的 **Settings（设置）→ Pets**。
2. 点击 **Refresh（刷新）**。
3. 找到并选择 **布布一二·贴贴**。这是配置中的显示名，与仓库标题“布布一二蹭脸”不同。
4. 若已选中但没有显示桌面宠物，可输入 `/pet`，或在命令菜单中选择 **Show pet** 打开浮动宠物；这是[官方设置文档](https://learn.chatgpt.com/docs/reference/settings#pets)列出的显示入口。不同版本的按钮位置可能不同。
5. 出现双人宠物后，把鼠标移到宠物身上，观察抱抱动作。

只切回 Codex 窗口不一定刷新素材，复制或更新后请手动点 **Refresh**。如果仍未出现，检查下面的排查表。

### 5. 确认安装成功

- 能看到布布在左、一二在右，两条手臂在前面交叠。
- 鼠标悬停时，脸部轻轻贴近、回落；整体不会腾空跳跃。
- 宠物背景透明，没有整张 GIF 的浅色矩形。

待机完整循环较慢，约 6.6 秒；悬停一轮约 0.84 秒。视线状态可能覆盖待机动画，不需要不停点击宠物。

<details>
<summary>可选：用 PowerShell 复制文件（首次安装）</summary>

在解压后的仓库根目录，也就是能看到 `pet` 文件夹的地方，打开 PowerShell，运行下面的代码。它只复制素材；目标目录已存在时会停止，不覆盖旧宠物。

```powershell
$petSource = Join-Path (Get-Location) 'pet'
$petDestination = Join-Path $env:USERPROFILE '.codex/pets/bubu-yier-duo'

if (!(Test-Path -LiteralPath (Join-Path $petSource 'pet.json')) -or
    !(Test-Path -LiteralPath (Join-Path $petSource 'spritesheet.webp'))) {
    throw '请先在解压后的仓库根目录打开 PowerShell。'
}
if (Test-Path -LiteralPath $petDestination) {
    throw '目标目录已存在，请先备份，并按 README 的更新说明操作。'
}

New-Item -ItemType Directory -Path $petDestination -Force | Out-Null
Copy-Item -LiteralPath (Join-Path $petSource 'pet.json') -Destination $petDestination
Copy-Item -LiteralPath (Join-Path $petSource 'spritesheet.webp') -Destination $petDestination
Write-Host '素材已复制。请在 Codex 的 Settings → Pets 中 Refresh 并选择布布一二·贴贴。'
```

如果使用自定义 Codex 数据目录，先把 `$petDestination` 改成自己的目标路径。使用上面的手动复制方法即可完成相同操作。

</details>

## 更新已有宠物

### 仍从本地目录读取

备份原目录，替换 `pet.json` 和 `spritesheet.webp`，再进入 **Settings → Pets → Refresh**，重新选择该宠物。

### 已经自动迁移到云端，刷新后仍是旧版

Codex 可能把本地自定义宠物迁移到云端。迁移后，**替换本地文件不会更新现有云端副本**；反复 Refresh 也不会把本地新文件上传。

如果你的 Codex 已启用能更新宠物的 **Pets / Work Pets** 能力：

1. 在 Codex 对话中附上或引用本仓库的 `pet/spritesheet.webp` 文件。
2. 发送下面的要求：

   > 请用这个 spritesheet.webp 更新我现有的“布布一二·贴贴”自定义宠物。保留原来的宠物 ID 和当前选择，不要新建重复宠物；上传前验证 v2 图集，更新后下载核对素材。

3. 确认更新成功后，再进入 **Settings → Pets → Refresh**。

这里调用的是宠物工具，不是 Settings 中的上传按钮。如果对话提示没有宠物更新工具，需要先确认相应能力在你的应用中可用；单纯复制本地文件不能绕过云端更新。

## 常见问题

| 情况 | 排查方法 |
| --- | --- |
| 设置里没有 Pets | 先确认当前桌面版本是否提供宠物功能；本项目不能通过复制素材为不支持的版本增加功能。 |
| Refresh 后找不到宠物 | 检查两个文件是否直接位于 `pets/bubu-yier-duo/`；确保 ZIP 已解压、文件不是 `pet.json.txt`，并确认使用的是实际 Codex 数据目录。 |
| 找不到“布布一二蹭脸”这个名字 | 应用内显示名是 **布布一二·贴贴**。 |
| 已选中，却看不到桌面宠物 | 使用 `/pet` 或 **Show pet** 显示浮动宠物；确认没有切到只显示聊天控件的 Mini 模式。 |
| 刷新后仍然跳跃或显示旧图 | 确认选中了正确宠物；已经迁移到云端的旧宠物需要按上面的云端更新流程操作。 |
| 动画播几次就停了 | 悬停动作通常播放三轮后回到待机，这是已核实版本的播放机制。待机还可能被视线状态覆盖。 |
| 始终只有静态图 | 检查系统是否启用了“减少动态效果 / Reduced motion”。[官方 Pets 文档](https://learn.chatgpt.com/docs/pets#reduce-animation)说明该设置会让宠物使用静态帧；需要动画时再按自己的偏好调整。 |
| 看到一整张多格大图 | `spritesheet.webp` 在图片查看器中本来就是图集；需要连同 `pet.json` 放入宠物目录，由 Codex 按格播放。 |
| 预览有浅色背景 | GIF 预览使用浅色底，实际安装文件是透明 WebP；不要把 GIF 复制成宠物图集。 |
| 想恢复旧版 | 对于本地宠物，恢复备份的两个文件并 Refresh；云端宠物需通过宠物更新工具重新上传备份的旧图集。 |

本说明区分了已验证的本机行为和版本限制，不保证所有客户端都提供相同入口。显示与动画设置参考 [OpenAI 官方 Pets 文档](https://learn.chatgpt.com/docs/pets)；本仓库的具体图集约定见下方开发说明。仓库使用 **1536×2288 的桌面 v2 图集**，与该文档列出的 Web 上传尺寸不同；不要直接套用 Web 上传步骤。

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
