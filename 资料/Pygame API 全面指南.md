# Pygame API 全面指南

> 本文档归类并详细介绍 Pygame 的所有核心 API，包含参数说明、适用游戏场景和可运行示例代码。

---

## 目录

- [1. pygame — 顶层模块](#1-pygame--顶层模块)
- [2. pygame.display — 显示窗口管理](#2-pygamedisplay--显示窗口管理)
- [3. pygame.surface — Surface 表面对象](#3-pygamesurface--surface-表面对象)
- [4. pygame.event — 事件处理](#4-pygameevent--事件处理)
- [5. pygame.key — 键盘输入](#5-pygamekey--键盘输入)
- [6. pygame.mouse — 鼠标输入](#6-pygamemouse--鼠标输入)
- [7. pygame.draw — 图形绘制](#7-pygamedraw--图形绘制)
- [8. pygame.image — 图像加载与保存](#8-pygameimage--图像加载与保存)
- [9. pygame.transform — 图像变换](#9-pygametransform--图像变换)
- [10. pygame.font — 字体与文本渲染](#10-pygamefont--字体与文本渲染)
- [11. pygame.mixer — 音频混合器](#11-pygamemixer--音频混合器)
- [12. pygame.mixer.music — 背景音乐](#12-pygamemixermusic--背景音乐)
- [13. pygame.time — 时间控制](#13-pygametime--时间控制)
- [14. pygame.Rect — 矩形对象](#14-pygamerect--矩形对象)
- [15. pygame.sprite — 精灵系统](#15-pygamesprite--精灵系统)
- [16. pygame.math — 数学工具](#16-pygamemath--数学工具)
- [17. pygame.Color — 颜色对象](#17-pygamecolor--颜色对象)
- [18. pygame.cursors — 光标](#18-pygamecursors--光标)
- [19. pygame.joystick — 手柄/摇杆](#19-pygamejoystick--手柄摇杆)
- [20. pygame.mask — 像素遮罩(精确碰撞)](#20-pygamemask--像素遮罩精确碰撞)
- [21. pygame.pixelarray — 像素数组](#21-pygamepixelarray--像素数组)
- [22. pygame.sndarray — 声音数组](#22-pygamesndarray--声音数组)
- [23. pygame.surfarray — Surface 数组](#23-pygamesurfarray--surface-数组)
- [24. pygame.freetype — 高级字体渲染](#24-pygamefreetype--高级字体渲染)
- [25. pygame.gfxdraw — 抗锯齿绘图](#25-pygamegfxdraw--抗锯齿绘图)
- [26. pygame.scrap — 剪贴板](#26-pygamescrap--剪贴板)

---

## 1. pygame — 顶层模块

顶层模块负责 Pygame 库的初始化和全局状态管理。

### `pygame.init()`

初始化所有已导入的 Pygame 模块。

| 参数 | 说明 |
|------|------|
| 无 | — |
| **返回值** | `(numpass, numfail)` 元组，成功和失败的模块数 |

**适用场景：** 所有 Pygame 程序的起点，必须在使用任何 Pygame 功能前调用。

```python
import pygame

result = pygame.init()
print(f"初始化成功: {result[0]}, 失败: {result[1]}")
pygame.quit()
```

### `pygame.quit()`

反初始化所有 Pygame 模块。

| 参数 | 说明 |
|------|------|
| 无 | — |
| **返回值** | None |

**适用场景：** 程序退出前清理资源。

### `pygame.get_init()`

检查 Pygame 是否已经初始化。

| 参数 | 说明 |
|------|------|
| 无 | — |
| **返回值** | `bool` |

### `pygame.error`

Pygame 的标准异常类型。

### `pygame.get_error()` / `pygame.set_error()`

获取/设置当前的 SDL 错误信息。

### `pygame.get_sdl_version()`

返回 SDL 库版本号。

```python
import pygame
pygame.init()
print("SDL 版本:", pygame.get_sdl_version())
pygame.quit()
```

### `pygame.version`

Pygame 版本信息模块。

```python
import pygame
print("Pygame 版本:", pygame.version.ver)
print("SDL 版本:", pygame.version.SDL)
```

---

## 2. pygame.display — 显示窗口管理

管理游戏窗口和屏幕显示。

### `pygame.display.set_mode()`

创建游戏窗口。

```python
surface = pygame.display.set_mode(size, flags=0, depth=0, display=0, vsync=0)
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `size` | `(width, height)` | 窗口分辨率 |
| `flags` | `int` | 显示标志（可组合）|
| `depth` | `int` | 颜色位深（通常自动） |
| `display` | `int` | 使用哪个显示器 |
| `vsync` | `int` | 1 启用垂直同步 |

**常用 flags：**
| 标志 | 说明 |
|------|------|
| `pygame.FULLSCREEN` | 全屏 |
| `pygame.RESIZABLE` | 可调整大小 |
| `pygame.NOFRAME` | 无边框窗口 |
| `pygame.SCALED` | 自动缩放 |
| `pygame.DOUBLEBUF` | 双缓冲（推荐配合硬件加速）|
| `pygame.HWSURFACE` | 硬件加速 |
| `pygame.OPENGL` | OpenGL 渲染 |

**适用场景：** 所有游戏必备 — 创建游戏可视窗口。

```python
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("我的游戏窗口")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((30, 30, 30))
    pygame.display.flip()

pygame.quit()
sys.exit()
```

### `pygame.display.flip()`

将整个显示 Surface 更新到屏幕上（双缓冲翻转）。

| 参数 | 说明 |
|------|------|
| 无 | — |
| **返回值** | None |

**适用场景：** 每帧渲染后刷新屏幕。

### `pygame.display.update()`

更新屏幕的部分区域。

```python
pygame.display.update(rect_list=None)
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `rect_list` | `Rect` 或 `list[Rect]` | 需要更新的矩形区域，`None` 更新全部 |

**适用场景：** 只有局部画面变化时，比 `flip()` 更高效。

### `pygame.display.set_caption()`

设置窗口标题。

```python
pygame.display.set_caption(title, icontitle=None)
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `title` | `str` | 窗口标题文字 |
| `icontitle` | `str` | 最小化时显示的标题 |

### `pygame.display.get_caption()`

获取当前窗口标题，返回 `(title, icontitle)` 元组。

### `pygame.display.set_icon()`

设置窗口图标。

```python
pygame.display.set_icon(surface)
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `surface` | `Surface` | 32x32 像素的图标 Surface |

**注意：** 必须在 `set_mode()` **之前**调用。

### `pygame.display.get_surface()`

获取当前显示的 Surface 对象。

### `pygame.display.get_driver()`

获取当前的视频驱动名称。

### `pygame.display.Info()`

返回一个 `VideoInfo` 对象，包含显示器信息。

```python
import pygame
pygame.init()
info = pygame.display.Info()
print(f"屏幕分辨率: {info.current_w} x {info.current_h}")
pygame.quit()
```

### `pygame.display.get_wm_info()`

获取窗口管理器的系统信息。

### `pygame.display.toggle_fullscreen()`

切换全屏/窗口模式。

### `pygame.display.iconify()`

最小化窗口。

### `pygame.display.get_active()`

窗口是否在前台活跃。

---

## 3. pygame.surface — Surface 表面对象

Surface 是 Pygame 中最核心的图像对象，所有图像操作都基于 Surface。

### `pygame.Surface()`

创建一个新 Surface。

```python
surface = pygame.Surface(size, flags=0, depth=0, masks=None)
# 或
surface = pygame.Surface(size, flags=0, surface=None)
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `size` | `(width, height)` | Surface 尺寸 |
| `flags` | `int` | `pygame.SRCALPHA` 启用透明通道 |

**适用场景：** 创建离屏绘制面、子画面、UI 元素等。

```python
import pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))

# 创建一个带透明通道的表面
overlay = pygame.Surface((200, 150), pygame.SRCALPHA)
overlay.fill((255, 0, 0, 128))  # 半透明红色

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    screen.blit(overlay, (100, 75))
    pygame.display.flip()

pygame.quit()
```

### `Surface.blit()`

将一个 Surface 绘制到另一个 Surface 上。

```python
rect = dest_surface.blit(source, dest, area=None, special_flags=0)
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `source` | `Surface` | 要绘制的源 Surface |
| `dest` | `(x, y)` 或 `Rect` | 目标位置 |
| `area` | `Rect` | 源 Surface 的裁剪区域 |
| `special_flags` | `int` | 混合模式 |
| **返回值** | `Rect` | 实际绘制的矩形区域 |

**常用 special_flags：**
| 标志 | 说明 |
|------|------|
| `BLEND_ADD` | 加法混合 |
| `BLEND_SUB` | 减法混合 |
| `BLEND_MULT` | 乘法混合 |
| `BLEND_RGBA_ADD` | RGBA 加法 |
| `BLEND_ALPHA_SDL2` | SDL2 Alpha 混合 |

**适用场景：** 游戏中所有图像绘制（角色、背景、UI等）。

### `Surface.blits()`

批量绘制多个 Surface（性能更优）。

```python
rects = surface.blits(blit_sequence, doreturn=True)
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `blit_sequence` | `list[(source, dest)]` | 要绘制的序列 |
| `doreturn` | `bool` | 是否返回 Rect 列表 |

### `Surface.fill()`

用颜色填充 Surface。

```python
rect = surface.fill(color, rect=None, special_flags=0)
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `color` | `Color` | 填充颜色 |
| `rect` | `Rect` | 填充区域，None 为全部 |
| `special_flags` | `int` | 混合模式 |

### `Surface.convert()` / `Surface.convert_alpha()`

转换 Surface 像素格式以加速 blit 操作。

```python
new_surface = surface.convert()        # 匹配显示格式
new_surface = surface.convert_alpha()  # 匹配显示格式并保留 Alpha
```

**适用场景：** 加载图片后务必调用，可显著提升渲染性能。

### `Surface.set_colorkey()`

设置透明色（该颜色将不被绘制）。

```python
surface.set_colorkey(color, flags=0)
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `color` | `Color` 或 `None` | 透明色，None 取消 |
| `flags` | `int` | `pygame.RLEACCEL` 加速 |

**适用场景：** 不带 Alpha 通道的精灵图去背景色。

```python
import pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))

# 创建一个带白色背景的精灵表面
sprite = pygame.Surface((50, 50))
sprite.fill((255, 255, 255))  # 白色背景
pygame.draw.circle(sprite, (255, 0, 0), (25, 25), 20)  # 红色圆

# 设置白色为透明色
sprite.set_colorkey((255, 255, 255))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 100, 200))
    screen.blit(sprite, (175, 125))
    pygame.display.flip()

pygame.quit()
```

### `Surface.get_colorkey()`

获取当前透明色。

### `Surface.set_alpha()`

设置整个 Surface 的透明度。

```python
surface.set_alpha(value, flags=0)
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `value` | `int` (0-255) 或 `None` | 透明度，0 全透明，255 不透明 |

### `Surface.get_alpha()`

获取 Surface 透明度。

### `Surface.copy()`

复制 Surface。

### `Surface.get_size()` / `Surface.get_width()` / `Surface.get_height()`

获取 Surface 的尺寸。

### `Surface.get_rect()`

获取 Surface 的矩形区域。

```python
rect = surface.get_rect(**kwargs)
```

`kwargs` 可以设置 Rect 的属性，如 `center=(200,150)`, `topleft=(0,0)`。

**适用场景：** 获取精灵/图像的定位矩形。

### `Surface.get_at()` / `Surface.set_at()`

获取/设置单个像素的颜色。

```python
color = surface.get_at((x, y))
surface.set_at((x, y), color)
```

### `Surface.subsurface()`

创建一个共享像素数据的子 Surface。

```python
sub = surface.subsurface(rect)
```

**适用场景：** 从精灵表(spritesheet)中提取单帧。

### `Surface.get_clip()` / `Surface.set_clip()`

获取/设置 Surface 的裁剪区域，限制绘制范围。

### `Surface.get_parent()`

获取父 Surface（如果是 subsurface）。

### `Surface.lock()` / `Surface.unlock()`

锁定/解锁 Surface 以便直接像素访问。

### `Surface.mustlock()`

是否需要锁定。

### `Surface.get_locked()`

是否已锁定。

### `Surface.get_locks()`

获取所有锁。

### `Surface.get_bitsize()` / `Surface.get_bytesize()`

获取每像素位数/字节数。

### `Surface.get_masks()` / `Surface.get_shifts()` / `Surface.get_losses()`

获取像素格式的掩码、偏移和精度损失。

### `Surface.get_flags()`

获取 Surface 标志。

### `Surface.get_pitch()`

获取每行的字节数。

### `Surface.get_buffer()` / `Surface.get_view()`

获取 Surface 的缓冲区对象或内存视图。

---

## 4. pygame.event — 事件处理

事件系统是 Pygame 交互的核心，处理键盘、鼠标、窗口等所有输入。

### `pygame.event.get()`

获取事件队列中的所有事件。

```python
events = pygame.event.get(eventtype=None, pump=True, exclude=None)
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `eventtype` | `int` 或 `list` | 只获取指定类型事件 |
| `pump` | `bool` | 是否自动泵入事件 |
| `exclude` | `int` 或 `list` | 排除指定类型事件 |
| **返回值** | `list[Event]` | 事件列表 |

**适用场景：** 主循环中获取用户输入。

### `pygame.event.poll()`

获取单个事件，队列空时返回 `NOEVENT`。

### `pygame.event.wait()`

等待下一个事件（阻塞）。

| 参数 | 类型 | 说明 |
|------|------|------|
| `timeout` | `int` | 超时时间（毫秒），0 无限等待 |

**适用场景：** 静态游戏/工具，如象棋，不需要持续刷新。

### `pygame.event.peek()`

检查队列中是否有指定类型的事件（不移除）。

### `pygame.event.clear()`

清空事件队列。

### `pygame.event.pump()`

让 Pygame 内部处理事件队列。如果不调用 `get()` 或 `poll()`，则需要定期调用此函数。

### `pygame.event.set_blocked()` / `pygame.event.set_allowed()`

阻止/允许特定类型的事件进入队列。

```python
pygame.event.set_blocked(pygame.MOUSEMOTION)  # 屏蔽鼠标移动事件
```

### `pygame.event.get_blocked()`

检查某事件类型是否被阻止。

### `pygame.event.set_grab()` / `pygame.event.get_grab()`

设置/获取输入锁定（鼠标限制在窗口内）。

### `pygame.event.post()`

向事件队列提交自定义事件。

```python
pygame.event.post(event)
```

### `pygame.event.custom_type()`

生成一个自定义事件类型 ID。

### `pygame.event.Event()`

创建事件对象。

```python
event = pygame.event.Event(type, **attributes)
```

**常用事件类型及属性：**

| 类型 | 属性 | 说明 |
|------|------|------|
| `QUIT` | — | 关闭窗口 |
| `KEYDOWN` | `key`, `mod`, `unicode`, `scancode` | 按键按下 |
| `KEYUP` | `key`, `mod`, `scancode` | 按键释放 |
| `MOUSEMOTION` | `pos`, `rel`, `buttons` | 鼠标移动 |
| `MOUSEBUTTONDOWN` | `pos`, `button` | 鼠标按下 |
| `MOUSEBUTTONUP` | `pos`, `button` | 鼠标释放 |
| `MOUSEWHEEL` | `x`, `y`, `flipped` | 滚轮 |
| `VIDEORESIZE` | `size`, `w`, `h` | 窗口大小改变 |
| `USEREVENT` | 自定义 | 自定义事件 |

**完整事件处理示例：**

```python
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("事件处理示例")

# 自定义事件
SPAWN_ENEMY = pygame.event.custom_type()
pygame.time.set_timer(SPAWN_ENEMY, 2000)  # 每 2 秒触发

font = pygame.font.SysFont(None, 30)
messages = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            messages.append(f"按键: {pygame.key.name(event.key)}")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            messages.append(f"鼠标点击: {event.pos}")
        elif event.type == SPAWN_ENEMY:
            messages.append("自定义事件: 生成敌人!")

    # 只保留最近5条消息
    messages = messages[-5:]

    screen.fill((20, 20, 40))
    for i, msg in enumerate(messages):
        text = font.render(msg, True, (200, 200, 200))
        screen.blit(text, (10, 10 + i * 30))
    pygame.display.flip()

pygame.quit()
sys.exit()
```

---

## 5. pygame.key — 键盘输入

### `pygame.key.get_pressed()`

获取所有键的当前按下状态。

```python
keys = pygame.key.get_pressed()
```

| 参数 | 说明 |
|------|------|
| 无 | — |
| **返回值** | `ScancodeWrapper`，可按键常量索引 |

**适用场景：** 角色持续移动（如 WASD 方向控制）。

```python
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

x, y = 200, 150
speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x -= speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x += speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y -= speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y += speed

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 200, 100), (x - 15, y - 15, 30, 30))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
```

### `pygame.key.get_mods()`

获取当前修饰键状态（Shift、Ctrl、Alt 等）。

```python
mods = pygame.key.get_mods()
if mods & pygame.KMOD_SHIFT:
    print("Shift 被按住")
if mods & pygame.KMOD_CTRL:
    print("Ctrl 被按住")
```

### `pygame.key.set_mods()`

模拟设置修饰键状态。

### `pygame.key.set_repeat()`

设置按住键时的重复触发。

```python
pygame.key.set_repeat(delay, interval)
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `delay` | `int` | 首次重复延迟（毫秒）|
| `interval` | `int` | 之后的重复间隔（毫秒）|

**适用场景：** 文本输入框中按住按键连续输入字符。

### `pygame.key.get_repeat()`

获取当前重复设置。

### `pygame.key.name()`

获取键名字符串。

```python
name = pygame.key.name(pygame.K_SPACE)  # "space"
```

### `pygame.key.key_code()`

从键名获取键码。

```python
code = pygame.key.key_code("space")  # 32
```

### `pygame.key.start_text_input()` / `pygame.key.stop_text_input()`

开始/停止文本输入模式（用于 IME 输入法）。

### `pygame.key.get_focused()`

窗口是否拥有键盘焦点。

**常用键码常量：**

| 常量 | 按键 | 常量 | 按键 |
|------|------|------|------|
| `K_UP` | 上箭头 | `K_DOWN` | 下箭头 |
| `K_LEFT` | 左箭头 | `K_RIGHT` | 右箭头 |
| `K_SPACE` | 空格 | `K_RETURN` | 回车 |
| `K_ESCAPE` | Esc | `K_TAB` | Tab |
| `K_a` ~ `K_z` | 字母键 | `K_0` ~ `K_9` | 数字键 |
| `K_F1` ~ `K_F12` | 功能键 | `K_LSHIFT` | 左Shift |
| `K_LCTRL` | 左Ctrl | `K_LALT` | 左Alt |

---

## 6. pygame.mouse — 鼠标输入

### `pygame.mouse.get_pos()`

获取鼠标当前位置。

```python
x, y = pygame.mouse.get_pos()
```

### `pygame.mouse.get_pressed()`

获取鼠标按钮状态。

```python
buttons = pygame.mouse.get_pressed(num_buttons=3)
# buttons[0] 左键, buttons[1] 中键, buttons[2] 右键
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `num_buttons` | `int` | 3 或 5（支持额外按钮）|

### `pygame.mouse.get_rel()`

获取鼠标自上次调用后的相对移动量。

### `pygame.mouse.set_pos()`

设置鼠标位置。

```python
pygame.mouse.set_pos((x, y))
```

### `pygame.mouse.set_visible()`

显示/隐藏鼠标光标。

```python
pygame.mouse.set_visible(True)  # 或 False
```

### `pygame.mouse.get_visible()`

光标是否可见。

### `pygame.mouse.set_cursor()` / `pygame.mouse.get_cursor()`

设置/获取鼠标光标样式。

```python
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
```

**系统光标常量：**
`SYSTEM_CURSOR_ARROW`, `SYSTEM_CURSOR_IBEAM`, `SYSTEM_CURSOR_WAIT`, `SYSTEM_CURSOR_CROSSHAIR`, `SYSTEM_CURSOR_HAND`...

### `pygame.mouse.get_focused()`

鼠标是否在窗口内。

**鼠标交互示例：**

```python
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("鼠标交互示例")
clock = pygame.time.Clock()

circles = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 左键
                circles.append((event.pos, (255, 100, 50)))
            elif event.button == 3:  # 右键
                circles.append((event.pos, (50, 100, 255)))

    screen.fill((30, 30, 30))
    for pos, color in circles:
        pygame.draw.circle(screen, color, pos, 20)

    # 跟随鼠标的光标指示
    mx, my = pygame.mouse.get_pos()
    pygame.draw.circle(screen, (200, 200, 200), (mx, my), 5)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
```

---

## 7. pygame.draw — 图形绘制

所有绘图函数都返回绘制区域的 `Rect`。

### `pygame.draw.rect()`

绘制矩形。

```python
rect = pygame.draw.rect(surface, color, rect, width=0, border_radius=0,
                         border_top_left_radius=-1, border_top_right_radius=-1,
                         border_bottom_left_radius=-1, border_bottom_right_radius=-1)
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `surface` | `Surface` | 目标表面 |
| `color` | `Color` | 颜色 |
| `rect` | `Rect` | 矩形位置和大小 |
| `width` | `int` | 边框宽度，0 为填充 |
| `border_radius` | `int` | 圆角半径 |

### `pygame.draw.circle()`

绘制圆形。

```python
rect = pygame.draw.circle(surface, color, center, radius, width=0,
                           draw_top_right=None, draw_top_left=None,
                           draw_bottom_left=None, draw_bottom_right=None)
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `center` | `(x, y)` | 圆心位置 |
| `radius` | `int/float` | 半径 |
| `width` | `int` | 边框宽度，0 为填充 |
| `draw_*` | `bool` | 只画某个象限 |

### `pygame.draw.ellipse()`

绘制椭圆。

```python
rect = pygame.draw.ellipse(surface, color, rect, width=0)
```

### `pygame.draw.line()`

绘制直线。

```python
rect = pygame.draw.line(surface, color, start_pos, end_pos, width=1)
```

### `pygame.draw.lines()`

绘制多条连线。

```python
rect = pygame.draw.lines(surface, color, closed, points, width=1)
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `closed` | `bool` | 是否闭合（首尾相连）|
| `points` | `list[(x,y)]` | 顶点列表 |

### `pygame.draw.aaline()` / `pygame.draw.aalines()`

绘制抗锯齿线条。

```python
rect = pygame.draw.aaline(surface, color, start_pos, end_pos, blend=1)
rect = pygame.draw.aalines(surface, color, closed, points, blend=1)
```

### `pygame.draw.polygon()`

绘制多边形。

```python
rect = pygame.draw.polygon(surface, color, points, width=0)
```

### `pygame.draw.arc()`

绘制弧形。

```python
rect = pygame.draw.arc(surface, color, rect, start_angle, stop_angle, width=1)
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `start_angle` | `float` | 起始角度（弧度）|
| `stop_angle` | `float` | 结束角度（弧度）|

**绘图综合示例：**

```python
import pygame
import sys
import math

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("pygame.draw 综合示例")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((240, 240, 240))

    # 填充矩形（圆角）
    pygame.draw.rect(screen, (70, 130, 180), (20, 20, 120, 80), border_radius=10)
    # 边框矩形
    pygame.draw.rect(screen, (220, 80, 80), (160, 20, 120, 80), width=3)
    # 填充圆
    pygame.draw.circle(screen, (100, 180, 100), (360, 60), 40)
    # 边框圆
    pygame.draw.circle(screen, (180, 100, 180), (460, 60), 40, width=3)
    # 椭圆
    pygame.draw.ellipse(screen, (200, 150, 50), (20, 130, 160, 60))
    # 直线
    pygame.draw.line(screen, (0, 0, 0), (20, 220), (280, 220), width=2)
    # 抗锯齿线
    pygame.draw.aaline(screen, (255, 0, 0), (20, 250), (280, 280))
    # 多边形（三角形）
    pygame.draw.polygon(screen, (255, 200, 0), [(350, 150), (300, 250), (400, 250)])
    # 弧形
    pygame.draw.arc(screen, (0, 0, 200), (420, 130, 150, 150), 0, math.pi, width=3)
    # 多段线
    points = [(20, 330), (80, 300), (140, 350), (200, 310), (260, 370)]
    pygame.draw.lines(screen, (100, 50, 50), False, points, width=2)

    pygame.display.flip()

pygame.quit()
sys.exit()
```

---

## 8. pygame.image — 图像加载与保存

### `pygame.image.load()`

从文件加载图像。

```python
surface = pygame.image.load(filename)
surface = pygame.image.load(fileobj, namehint="")
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `filename` | `str` | 文件路径 |
| `fileobj` | `file-like` | 文件对象 |
| `namehint` | `str` | 帮助判断格式后缀 |

**支持格式：** BMP, GIF, JPEG, PNG, TGA, TIFF, WEBP, SVG 等。

**适用场景：** 加载角色图片、背景图、UI 素材。

```python
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 300))

# 加载并优化图片格式
# image = pygame.image.load("player.png").convert_alpha()

# 演示：用绘图替代图片
player = pygame.Surface((40, 40), pygame.SRCALPHA)
pygame.draw.circle(player, (0, 150, 255), (20, 20), 18)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((50, 50, 50))
    screen.blit(player, (180, 130))
    pygame.display.flip()

pygame.quit()
sys.exit()
```

### `pygame.image.save()`

将 Surface 保存为图片文件。

```python
pygame.image.save(surface, filename)
pygame.image.save(surface, fileobj, namehint="")
```

**支持格式：** BMP, TGA, PNG, JPEG。

**适用场景：** 截图功能。

```python
# 截图保存
# pygame.image.save(screen, "screenshot.png")
```

### `pygame.image.tostring()` / `pygame.image.fromstring()`

Surface 与字节串之间转换。

```python
string = pygame.image.tostring(surface, format, flipped=False)
surface = pygame.image.fromstring(string, size, format, flipped=False)
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `format` | `str` | `"RGBA"`, `"RGB"`, `"ARGB"` 等 |
| `flipped` | `bool` | 是否垂直翻转 |

**适用场景：** 与 NumPy、OpenGL 等互操作。

### `pygame.image.frombuffer()`

从缓冲区创建 Surface（不复制数据）。

### `pygame.image.get_sdl_image_version()`

获取 SDL_image 库版本。

### `pygame.image.get_extended()`

是否支持扩展图片格式（PNG, JPEG 等）。

---

## 9. pygame.transform — 图像变换

### `pygame.transform.scale()`

缩放 Surface。

```python
new_surface = pygame.transform.scale(surface, size, dest_surface=None)
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `surface` | `Surface` | 原始 Surface |
| `size` | `(width, height)` | 目标尺寸 |
| `dest_surface` | `Surface` | 可选的目标 Surface |

### `pygame.transform.scale_by()`

按倍数缩放（Pygame 2.1.3+）。

```python
new_surface = pygame.transform.scale_by(surface, factor, dest_surface=None)
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `factor` | `float` 或 `(fx, fy)` | 缩放倍数 |

### `pygame.transform.scale2x()`

快速 2 倍放大（AdvanceMAME Scale2X 算法）。

### `pygame.transform.smoothscale()`

平滑缩放（抗锯齿）。

```python
new_surface = pygame.transform.smoothscale(surface, size, dest_surface=None)
```

### `pygame.transform.smoothscale_by()`

按倍数平滑缩放。

### `pygame.transform.rotate()`

旋转 Surface。

```python
new_surface = pygame.transform.rotate(surface, angle)
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `angle` | `float` | 旋转角度（度），逆时针为正 |

**注意：** 旋转会增大 Surface 尺寸，需要重新获取 rect。

### `pygame.transform.rotozoom()`

同时旋转和缩放。

```python
new_surface = pygame.transform.rotozoom(surface, angle, scale)
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `angle` | `float` | 旋转角度 |
| `scale` | `float` | 缩放倍数 |

**适用场景：** 旋转的子弹、旋转的道具。

```python
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

# 创建一个箭头形状
arrow = pygame.Surface((60, 20), pygame.SRCALPHA)
pygame.draw.polygon(arrow, (255, 200, 0),
                    [(0, 5), (40, 5), (40, 0), (60, 10), (40, 20), (40, 15), (0, 15)])

angle = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    angle += 2
    rotated = pygame.transform.rotozoom(arrow, angle, 1.0)
    rect = rotated.get_rect(center=(200, 150))

    screen.fill((30, 30, 50))
    screen.blit(rotated, rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
```

### `pygame.transform.flip()`

水平/垂直翻转。

```python
new_surface = pygame.transform.flip(surface, flip_x, flip_y)
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `flip_x` | `bool` | 水平翻转 |
| `flip_y` | `bool` | 垂直翻转 |

**适用场景：** 角色转向（左右翻转精灵图）。

### `pygame.transform.chop()`

剪裁掉 Surface 中的矩形区域。

### `pygame.transform.laplacian()`

边缘检测。

### `pygame.transform.average_surfaces()`

多个 Surface 取平均值。

### `pygame.transform.average_color()`

计算 Surface 的平均颜色。

### `pygame.transform.grayscale()`

转灰度图。

```python
gray_surface = pygame.transform.grayscale(surface, dest_surface=None)
```

### `pygame.transform.threshold()`

颜色阈值检测。

```python
count = pygame.transform.threshold(
    dest_surface, surface, search_color, threshold=(0,0,0,0),
    set_color=(0,0,0,0), set_behavior=1, search_surf=None, inverse_set=False)
```

**适用场景：** 颜色替换、绿幕效果。

---

## 10. pygame.font — 字体与文本渲染

### `pygame.font.init()` / `pygame.font.quit()`

初始化/反初始化字体模块（通常 `pygame.init()` 已包含）。

### `pygame.font.get_init()`

字体模块是否已初始化。

### `pygame.font.get_default_font()`

获取默认字体文件名。

### `pygame.font.get_fonts()`

获取系统中所有可用字体名称列表。

### `pygame.font.match_font()`

查找匹配的字体文件路径。

```python
path = pygame.font.match_font(name, bold=False, italic=False)
```

### `pygame.font.SysFont()`

从系统字体创建 Font 对象。

```python
font = pygame.font.SysFont(name, size, bold=False, italic=False)
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `name` | `str` 或 `None` | 字体名，None 使用默认 |
| `size` | `int` | 字号 |

### `pygame.font.Font()`

从字体文件创建 Font 对象。

```python
font = pygame.font.Font(filename, size)
font = pygame.font.Font(None, size)   # 使用默认字体
```

### Font 对象方法

#### `Font.render()`

渲染文本为 Surface。

```python
surface = font.render(text, antialias, color, background=None)
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `text` | `str` | 要渲染的文本 |
| `antialias` | `bool` | 是否抗锯齿 |
| `color` | `Color` | 文字颜色 |
| `background` | `Color` | 背景颜色（可选）|

**注意：** `Font.render()` 一次只能渲染一行文本。

#### `Font.size()`

获取文本渲染后的尺寸 `(width, height)`，不实际渲染。

#### `Font.set_bold()` / `Font.get_bold()`

设置/获取粗体。

#### `Font.set_italic()` / `Font.get_italic()`

设置/获取斜体。

#### `Font.set_underline()` / `Font.get_underline()`

设置/获取下划线。

#### `Font.set_strikethrough()` / `Font.get_strikethrough()`

设置/获取删除线。

#### `Font.get_height()` / `Font.get_linesize()` / `Font.get_ascent()` / `Font.get_descent()`

获取字体的高度信息。

**文本渲染完整示例：**

```python
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((500, 350))
pygame.display.set_caption("字体渲染示例")

# 不同字体和样式
font_big = pygame.font.SysFont(None, 48)
font_normal = pygame.font.SysFont(None, 32)
font_small = pygame.font.SysFont(None, 24)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((20, 20, 40))

    # 标题
    title = font_big.render("Pygame Font Demo", True, (255, 255, 100))
    screen.blit(title, (50, 20))

    # 普通文本
    text1 = font_normal.render("Normal Text", True, (200, 200, 200))
    screen.blit(text1, (50, 90))

    # 带背景色
    text2 = font_normal.render("With Background", True, (255, 255, 255), (100, 50, 50))
    screen.blit(text2, (50, 140))

    # 粗体 & 斜体
    font_normal.set_bold(True)
    text3 = font_normal.render("Bold Text", True, (100, 200, 100))
    screen.blit(text3, (50, 190))
    font_normal.set_bold(False)

    font_normal.set_italic(True)
    text4 = font_normal.render("Italic Text", True, (100, 100, 255))
    screen.blit(text4, (50, 240))
    font_normal.set_italic(False)

    # 显示尺寸信息
    info = font_small.render(f"Font height: {font_normal.get_height()}px", True, (150, 150, 150))
    screen.blit(info, (50, 300))

    pygame.display.flip()

pygame.quit()
sys.exit()
```

---

## 11. pygame.mixer — 音频混合器

管理声音效果的加载和播放。

### `pygame.mixer.init()`

初始化混合器。

```python
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512,
                  devicename=None, allowedchanges=AUDIO_ALLOW_FREQUENCY_CHANGE |
                  AUDIO_ALLOW_CHANNELS_CHANGE)
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `frequency` | `int` | 采样率（Hz）|
| `size` | `int` | 样本大小（位），负数表示有符号 |
| `channels` | `int` | 1 单声道，2 立体声 |
| `buffer` | `int` | 缓冲区大小 |

### `pygame.mixer.quit()` / `pygame.mixer.get_init()`

关闭/检查混合器。

### `pygame.mixer.get_num_channels()` / `pygame.mixer.set_num_channels()`

获取/设置可用的混音通道数。

### `pygame.mixer.set_reserved()`

保留指定数量的通道。

### `pygame.mixer.find_channel()`

找一个空闲通道。

```python
channel = pygame.mixer.find_channel(force=False)
```

### `pygame.mixer.get_busy()`

是否有通道在播放。

### `pygame.mixer.fadeout()`

淡出所有通道。

### `pygame.mixer.pause()` / `pygame.mixer.unpause()` / `pygame.mixer.stop()`

暂停/恢复/停止所有通道。

### `pygame.mixer.Sound()`

创建声音对象。

```python
sound = pygame.mixer.Sound(filename)
sound = pygame.mixer.Sound(file=filename)
sound = pygame.mixer.Sound(buffer=bytes_data)
sound = pygame.mixer.Sound(array=numpy_array)
```

**支持格式：** WAV, OGG, FLAC, MP3（Pygame 2.0+ 部分支持）。

### Sound 对象方法

| 方法 | 说明 |
|------|------|
| `sound.play(loops=0, maxtime=0, fade_ms=0)` | 播放，loops=-1 循环 |
| `sound.stop()` | 停止播放 |
| `sound.fadeout(time)` | 淡出 |
| `sound.set_volume(value)` | 设置音量 0.0~1.0 |
| `sound.get_volume()` | 获取音量 |
| `sound.get_length()` | 获取时长（秒）|
| `sound.get_num_channels()` | 正在播放的通道数 |
| `sound.get_raw()` | 获取原始音频数据 |

### Channel 对象

```python
channel = pygame.mixer.Channel(id)
```

| 方法 | 说明 |
|------|------|
| `channel.play(sound, loops=0, maxtime=0, fade_ms=0)` | 在此通道播放 |
| `channel.stop()` | 停止 |
| `channel.pause()` / `channel.unpause()` | 暂停/恢复 |
| `channel.fadeout(time)` | 淡出 |
| `channel.set_volume(left, right=None)` | 设置音量（支持立体声平衡）|
| `channel.get_volume()` | 获取音量 |
| `channel.get_busy()` | 是否在播放 |
| `channel.get_sound()` | 获取当前 Sound |
| `channel.queue(sound)` | 排队下一个音效 |
| `channel.get_queue()` | 获取排队的音效 |
| `channel.set_endevent(type=None)` | 播放完发送事件 |
| `channel.get_endevent()` | 获取结束事件类型 |

**音效播放示例：**

```python
import pygame
import sys
import math
import struct

pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=1)
screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("音效示例")
font = pygame.font.SysFont(None, 28)

# 用代码生成一个正弦波声音（无需外部文件）
sample_rate = 44100
duration = 0.3  # 秒
frequency = 440  # Hz (A4音)
n_samples = int(sample_rate * duration)

buf = bytearray()
for i in range(n_samples):
    t = i / sample_rate
    # 带衰减的正弦波
    value = int(32767 * math.sin(2 * math.pi * frequency * t) * (1 - t / duration))
    buf.extend(struct.pack('<h', value))

beep = pygame.mixer.Sound(buffer=bytes(buf))
beep.set_volume(0.5)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                beep.play()

    screen.fill((30, 30, 50))
    text = font.render("Press SPACE to play beep", True, (200, 200, 200))
    screen.blit(text, (50, 85))
    pygame.display.flip()

pygame.quit()
sys.exit()
```

---

## 12. pygame.mixer.music — 背景音乐

专门管理背景音乐（流式加载，适合大文件）。

### `pygame.mixer.music.load()`

加载背景音乐文件。

```python
pygame.mixer.music.load(filename)
pygame.mixer.music.load(fileobj, namehint="")
```

**支持格式：** MP3, OGG, WAV, FLAC, MOD, MIDI 等。

### `pygame.mixer.music.play()`

播放音乐。

```python
pygame.mixer.music.play(loops=0, start=0.0, fade_ms=0)
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `loops` | `int` | 循环次数，-1 无限循环 |
| `start` | `float` | 起始位置（秒）|
| `fade_ms` | `int` | 淡入时间（毫秒）|

### 其他方法

| 方法 | 说明 |
|------|------|
| `music.stop()` | 停止 |
| `music.pause()` | 暂停 |
| `music.unpause()` | 恢复 |
| `music.rewind()` | 回到开始 |
| `music.fadeout(time)` | 淡出 |
| `music.set_volume(value)` | 音量 0.0~1.0 |
| `music.get_volume()` | 获取音量 |
| `music.get_busy()` | 是否在播放 |
| `music.get_pos()` | 播放位置（毫秒）|
| `music.set_pos(pos)` | 设置位置 |
| `music.queue(filename)` | 排队下一首 |
| `music.set_endevent(type)` | 播放完触发事件 |
| `music.get_endevent()` | 获取结束事件类型 |
| `music.unload()` | 卸载音乐释放内存 |

**适用场景：** 游戏背景音乐播放。

```python
# 背景音乐使用模式
# pygame.mixer.music.load("bgm.mp3")
# pygame.mixer.music.set_volume(0.5)
# pygame.mixer.music.play(-1)  # 无限循环
```

---

## 13. pygame.time — 时间控制

### `pygame.time.get_ticks()`

获取自 `pygame.init()` 以来经过的毫秒数。

```python
ms = pygame.time.get_ticks()
```

**适用场景：** 计时器、冷却时间、动画计时。

### `pygame.time.wait()`

暂停程序指定毫秒数（使用 CPU 休眠）。

```python
actual_ms = pygame.time.wait(milliseconds)
```

### `pygame.time.delay()`

暂停程序指定毫秒数（更精确，使用 CPU 忙等待）。

```python
actual_ms = pygame.time.delay(milliseconds)
```

### `pygame.time.set_timer()`

设置定时事件。

```python
pygame.time.set_timer(event, millis, loops=0)
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `event` | `int` 或 `Event` | 事件类型 |
| `millis` | `int` | 毫秒间隔，0 取消 |
| `loops` | `int` | 触发次数，0 无限 |

**适用场景：** 定期生成敌人、定时掉落道具。

### `pygame.time.Clock()`

创建时钟对象（帧率控制核心）。

### Clock 对象方法

#### `Clock.tick()`

控制帧率。

```python
dt = clock.tick(framerate=0)
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `framerate` | `int` | 目标帧率（FPS），0 不限制 |
| **返回值** | `int` | 自上次调用经过的毫秒数 |

#### `Clock.tick_busy_loop()`

更精确的帧率控制（CPU 占用更高）。

#### `Clock.get_time()`

上两次 `tick()` 之间的毫秒数。

#### `Clock.get_rawtime()`

未含 `tick()` 延迟的真实毫秒数。

#### `Clock.get_fps()`

获取当前平均帧率。

**帧率控制与计时示例：**

```python
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("时间控制示例")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 28)

# 冷却计时器示例
COOLDOWN = 1000  # 1秒冷却
last_shot = 0
shot_count = 0

running = True
while running:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                now = pygame.time.get_ticks()
                if now - last_shot >= COOLDOWN:
                    last_shot = now
                    shot_count += 1

    screen.fill((20, 30, 50))
    now = pygame.time.get_ticks()
    cd_remaining = max(0, COOLDOWN - (now - last_shot))

    texts = [
        f"FPS: {clock.get_fps():.1f}",
        f"Delta: {dt}ms",
        f"Time: {now // 1000}s",
        f"Press SPACE (CD: {cd_remaining}ms)",
        f"Shots: {shot_count}",
    ]
    for i, t in enumerate(texts):
        surf = font.render(t, True, (200, 200, 200))
        screen.blit(surf, (20, 20 + i * 35))

    pygame.display.flip()

pygame.quit()
sys.exit()
```

---

## 14. pygame.Rect — 矩形对象

`Rect` 是 Pygame 中最常用的数据类型之一，用于表示位置和大小，提供丰富的碰撞检测和对齐方法。

### 创建方式

```python
rect = pygame.Rect(left, top, width, height)
rect = pygame.Rect((left, top), (width, height))
rect = pygame.Rect(object)  # 从有 rect 属性的对象创建
```

### 属性（可读写）

| 属性 | 类型 | 说明 |
|------|------|------|
| `x`, `y` | `int` | 左上角坐标 |
| `top`, `left`, `bottom`, `right` | `int` | 各边位置 |
| `topleft`, `bottomleft`, `topright`, `bottomright` | `(int, int)` | 四角坐标 |
| `midtop`, `midleft`, `midbottom`, `midright` | `(int, int)` | 四边中点 |
| `center`, `centerx`, `centery` | `(int, int)` / `int` | 中心点 |
| `size` | `(int, int)` | (width, height) |
| `width`, `height` | `int` | 宽高 |
| `w`, `h` | `int` | 宽高缩写 |

### 方法

#### 位移

```python
new_rect = rect.move(x, y)     # 返回新 Rect
rect.move_ip(x, y)             # 就地移动
```

#### 缩放

```python
new_rect = rect.inflate(x, y)  # 返回新 Rect（中心不变）
rect.inflate_ip(x, y)          # 就地缩放
```

#### 缩放到指定大小

```python
new_rect = rect.scale_by(sx, sy)   # 按倍数缩放
rect.scale_by_ip(sx, sy)
```

#### 裁剪与合并

```python
new_rect = rect.clamp(other_rect)     # 限制 rect 在 other 内
rect.clamp_ip(other_rect)
clip_rect = rect.clip(other_rect)     # 裁剪到交集区域
union_rect = rect.union(other_rect)   # 合并两个矩形
union_rect = rect.unionall(rect_list) # 合并多个矩形
rect.union_ip(other_rect)
rect.unionall_ip(rect_list)
```

#### 适应

```python
new_rect = rect.fit(other_rect)  # 保持纵横比适应到目标内
```

#### 归一化

```python
rect.normalize()  # 确保 width/height 为正数
```

#### 碰撞检测（核心方法）

```python
bool = rect.contains(other_rect)              # other 是否完全在 rect 内？
bool = rect.collidepoint(x, y)                # 点是否在 rect 内？
bool = rect.colliderect(other_rect)           # 两矩形是否重叠？
index = rect.collidelist(rect_list)           # 返回第一个碰撞的索引，-1无碰撞
indices = rect.collidelistall(rect_list)      # 返回所有碰撞的索引列表
dict = rect.collidedict(rect_dict)            # 字典碰撞
list = rect.collidedictall(rect_dict)         # 字典全碰撞
bool = rect.collideobjects(obj_list, key=None)# 对象碰撞
indices = rect.collideobjectsall(obj_list, key=None)
```

**碰撞检测示例：**

```python
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Rect 碰撞检测示例")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

# 玩家
player = pygame.Rect(50, 50, 40, 40)
speed = 4

# 障碍物
obstacles = [
    pygame.Rect(150, 100, 60, 60),
    pygame.Rect(300, 200, 80, 40),
    pygame.Rect(100, 280, 50, 80),
    pygame.Rect(350, 50, 70, 70),
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    dx = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * speed
    dy = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * speed
    player.move_ip(dx, dy)

    # 限制在屏幕内
    player.clamp_ip(screen.get_rect())

    # 碰撞检测
    collision_index = player.collidelist(obstacles)

    screen.fill((30, 30, 50))

    # 绘制障碍物
    for i, obs in enumerate(obstacles):
        color = (255, 80, 80) if i == collision_index else (100, 100, 100)
        pygame.draw.rect(screen, color, obs)

    # 绘制玩家
    player_color = (255, 255, 0) if collision_index != -1 else (0, 200, 100)
    pygame.draw.rect(screen, player_color, player)

    # 鼠标碰撞测试
    mx, my = pygame.mouse.get_pos()
    hover_text = "Mouse: "
    if player.collidepoint(mx, my):
        hover_text += "On Player"
    else:
        hover_text += f"({mx}, {my})"

    text = font.render(hover_text, True, (200, 200, 200))
    screen.blit(text, (10, 375))

    status = "COLLISION!" if collision_index != -1 else "Safe"
    status_surf = font.render(status, True, (255, 100, 100) if collision_index != -1 else (100, 255, 100))
    screen.blit(status_surf, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
```

---

## 15. pygame.sprite — 精灵系统

精灵系统是 Pygame 提供的高层游戏对象管理框架。

### `pygame.sprite.Sprite`

所有游戏精灵的基类。

```python
class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((32, 32))  # 必须
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()       # 必须

    def update(self, *args, **kwargs):
        # 每帧更新逻辑
        pass
```

**必须属性：**
- `self.image` — 要绘制的 Surface
- `self.rect` — 位置和大小

**方法：**

| 方法 | 说明 |
|------|------|
| `sprite.update(*args, **kwargs)` | 更新逻辑（需重写）|
| `sprite.add(*groups)` | 加入精灵组 |
| `sprite.remove(*groups)` | 从组中移除 |
| `sprite.kill()` | 从所有组中移除 |
| `sprite.alive()` | 是否还在某个组中 |
| `sprite.groups()` | 所属的组列表 |

### `pygame.sprite.Group`

精灵组，批量管理精灵。

```python
group = pygame.sprite.Group(*sprites)
```

**方法：**

| 方法 | 说明 |
|------|------|
| `group.sprites()` | 返回精灵列表 |
| `group.add(*sprites)` | 添加精灵 |
| `group.remove(*sprites)` | 移除精灵 |
| `group.has(*sprites)` | 是否包含精灵 |
| `group.update(*args, **kwargs)` | 调用所有精灵的 update |
| `group.draw(surface)` | 绘制所有精灵 |
| `group.clear(surface, background)` | 清除精灵覆盖区域 |
| `group.empty()` | 移除所有精灵 |
| `group.copy()` | 复制组 |
| `len(group)` | 精灵数量 |
| 迭代 | `for sprite in group:` |

### 特殊精灵组

#### `pygame.sprite.GroupSingle`

只保留一个精灵的组（新增替换旧的）。

```python
group = pygame.sprite.GroupSingle(sprite=None)
group.sprite  # 获取当前精灵
```

**适用场景：** 管理唯一的玩家角色。

#### `pygame.sprite.RenderUpdates`

跟踪脏区域的组，`draw()` 返回变化区域列表。

#### `pygame.sprite.OrderedUpdates`

按添加顺序绘制的组。

#### `pygame.sprite.LayeredUpdates`

支持图层的组。

```python
group = pygame.sprite.LayeredUpdates(*sprites, **kwargs)
```

| 方法 | 说明 |
|------|------|
| `group.change_layer(sprite, layer)` | 改变精灵层 |
| `group.get_layer_of_sprite(sprite)` | 获取精灵所在层 |
| `group.get_top_layer()` | 获取最高层 |
| `group.get_bottom_layer()` | 获取最低层 |
| `group.get_sprites_at(pos)` | 获取指定位置的精灵 |
| `group.get_sprites_from_layer(layer)` | 获取指定层的精灵 |
| `group.move_to_front(sprite)` | 移到最前 |
| `group.move_to_back(sprite)` | 移到最后 |
| `group.switch_layer(layer1, layer2)` | 交换两层 |

#### `pygame.sprite.LayeredDirty`

支持脏矩形更新的分层组，性能最优。

### 碰撞检测函数

#### `pygame.sprite.spritecollide()`

精灵与精灵组的碰撞。

```python
hit_list = pygame.sprite.spritecollide(sprite, group, dokill, collided=None)
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `sprite` | `Sprite` | 检测目标 |
| `group` | `Group` | 检测组 |
| `dokill` | `bool` | 碰撞后是否从组中移除 |
| `collided` | `callable` | 自定义碰撞函数 |

#### `pygame.sprite.groupcollide()`

两个组之间的碰撞。

```python
collision_dict = pygame.sprite.groupcollide(group1, group2, dokill1, dokill2, collided=None)
```

**返回值：** `dict[Sprite, list[Sprite]]`

#### `pygame.sprite.spritecollideany()`

快速检查精灵是否与组中任何精灵碰撞。

```python
result = pygame.sprite.spritecollideany(sprite, group, collided=None)
```

**内置碰撞回调函数：**

| 函数 | 说明 |
|------|------|
| `pygame.sprite.collide_rect` | 矩形碰撞（默认）|
| `pygame.sprite.collide_rect_ratio(ratio)` | 缩放矩形碰撞 |
| `pygame.sprite.collide_circle` | 圆形碰撞 |
| `pygame.sprite.collide_circle_ratio(ratio)` | 缩放圆形碰撞 |
| `pygame.sprite.collide_mask` | 像素级碰撞 |

**精灵系统完整示例：**

```python
import pygame
import sys
import random

pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("精灵系统示例")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 28)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, (0, 255, 100),
                            [(15, 0), (0, 30), (30, 30)])
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 50))
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        self.rect.clamp_ip(screen.get_rect())


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((4, 10))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect(center=(x, y))

    def update(self, *args):
        self.rect.y -= 8
        if self.rect.bottom < 0:
            self.kill()


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((25, 25))
        self.image.fill((255, 50, 50))
        self.rect = self.image.get_rect(
            center=(random.randint(20, WIDTH - 20), -20))
        self.speed = random.uniform(1, 3)

    def update(self, *args):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.kill()


# 创建精灵和精灵组
player = Player()
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()
all_sprites.add(player)

# 定时生成敌人
SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_EVENT, 800)

score = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                b = Bullet(player.rect.centerx, player.rect.top)
                all_sprites.add(b)
                bullets.add(b)
        elif event.type == SPAWN_EVENT:
            e = Enemy()
            all_sprites.add(e)
            enemies.add(e)

    keys = pygame.key.get_pressed()
    player.update(keys)
    bullets.update()
    enemies.update()

    # 碰撞检测：子弹 vs 敌人
    hits = pygame.sprite.groupcollide(bullets, enemies, True, True)
    score += len(hits)

    # 碰撞检测：玩家 vs 敌人
    if pygame.sprite.spritecollideany(player, enemies):
        score = max(0, score - 1)

    screen.fill((10, 10, 30))
    all_sprites.draw(screen)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
```

---

## 16. pygame.math — 数学工具

### `pygame.math.Vector2`

2D 向量，游戏开发中最常用的数学工具。

```python
v = pygame.math.Vector2(x=0, y=0)
v = pygame.math.Vector2((x, y))
v = pygame.math.Vector2(other_vector)
```

**属性：**
- `v.x`, `v.y` — 分量
- `v.xy` — 以元组返回

**运算符：**
```python
v1 + v2    # 向量加法
v1 - v2    # 向量减法
v * scalar # 标量乘法
v / scalar # 标量除法
v1 @ v2    # 点积（Python 3.5+）
-v         # 取反
v[0], v[1] # 索引访问
```

**方法：**

| 方法 | 说明 |
|------|------|
| `v.length()` | 向量长度（模）|
| `v.length_squared()` | 长度的平方（避免开方）|
| `v.normalize()` | 返回单位向量 |
| `v.normalize_ip()` | 就地归一化 |
| `v.is_normalized()` | 是否已归一化 |
| `v.scale_to_length(length)` | 缩放到指定长度 |
| `v.dot(other)` | 点积 |
| `v.cross(other)` | 叉积（返回标量）|
| `v.reflect(normal)` | 反射向量 |
| `v.reflect_ip(normal)` | 就地反射 |
| `v.angle_to(other)` | 到另一向量的角度 |
| `v.rotate(angle)` | 旋转（度）|
| `v.rotate_ip(angle)` | 就地旋转 |
| `v.rotate_rad(angle)` | 旋转（弧度）|
| `v.distance_to(other)` | 到另一点的距离 |
| `v.distance_squared_to(other)` | 距离平方 |
| `v.lerp(other, t)` | 线性插值 |
| `v.slerp(other, t)` | 球面线性插值 |
| `v.elementwise()` | 逐元素运算 |
| `v.project(other)` | 投影 |
| `v.move_towards(target, max_distance)` | 向目标移动 |
| `v.clamp_magnitude(max)` | 限制最大长度 |
| `v.clamp_magnitude_ip(min, max)` | 限制长度范围 |
| `v.update(x, y)` | 更新值 |
| `v.copy()` | 复制 |
| `Vector2.from_polar((r, phi))` | 从极坐标创建 |
| `v.as_polar()` | 转换为极坐标 |

### `pygame.math.Vector3`

3D 向量，方法与 Vector2 类似，额外支持 z 分量和 3D 相关操作。

### `pygame.math.clamp()`

将值限制在范围内。

```python
result = pygame.math.clamp(value, min, max)
```

### `pygame.math.lerp()`

线性插值。

```python
result = pygame.math.lerp(a, b, t)  # t in [0,1]
```

**Vector2 综合示例（追踪与避障）：**

```python
import pygame
import sys
import math

pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Vector2 示例 - 追踪")
clock = pygame.time.Clock()

player_pos = pygame.math.Vector2(WIDTH // 2, HEIGHT // 2)
enemy_pos = pygame.math.Vector2(100, 100)
enemy_speed = 2.0

running = True
while running:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 玩家跟随鼠标
    mouse = pygame.math.Vector2(pygame.mouse.get_pos())
    player_pos = player_pos.lerp(mouse, 0.1)

    # 敌人追踪玩家
    direction = player_pos - enemy_pos
    distance = direction.length()
    if distance > 5:
        direction.normalize_ip()
        enemy_pos += direction * enemy_speed

    screen.fill((20, 20, 40))

    # 绘制玩家
    pygame.draw.circle(screen, (0, 200, 100), (int(player_pos.x), int(player_pos.y)), 15)

    # 绘制敌人
    pygame.draw.circle(screen, (200, 50, 50), (int(enemy_pos.x), int(enemy_pos.y)), 12)

    # 绘制方向线
    if distance > 5:
        end = enemy_pos + direction * 30
        pygame.draw.line(screen, (255, 100, 100),
                         (int(enemy_pos.x), int(enemy_pos.y)),
                         (int(end.x), int(end.y)), 2)

    # 距离信息
    font = pygame.font.SysFont(None, 24)
    dist_text = font.render(f"Distance: {distance:.1f}", True, (200, 200, 200))
    angle = enemy_pos.angle_to(player_pos - enemy_pos)
    angle_text = font.render(f"Angle: {angle:.1f}°", True, (200, 200, 200))
    screen.blit(dist_text, (10, 10))
    screen.blit(angle_text, (10, 35))

    pygame.display.flip()

pygame.quit()
sys.exit()
```

---

## 17. pygame.Color — 颜色对象

### 创建方式

```python
color = pygame.Color(r, g, b, a=255)
color = pygame.Color(color_name)        # 如 "red", "dodgerblue"
color = pygame.Color("#RRGGBB")         # 十六进制
color = pygame.Color("#RRGGBBAA")       # 带 Alpha
color = pygame.Color(int_value)         # 整数映射
```

### 属性

| 属性 | 说明 |
|------|------|
| `color.r`, `color.g`, `color.b`, `color.a` | RGBA 分量 (0-255) |
| `color.cmy` | CMY 颜色空间 |
| `color.hsva` | HSVA 颜色空间 |
| `color.hsla` | HSLA 颜色空间 |
| `color.i1i2i3` | I1I2I3 颜色空间 |

### 方法

| 方法 | 说明 |
|------|------|
| `color.normalize()` | 返回归一化 (0.0~1.0) 的 RGBA |
| `color.correct_gamma(gamma)` | Gamma 校正 |
| `color.set_length(len)` | 设置长度（3 或 4）|
| `color.lerp(other, t)` | 颜色线性插值 |
| `color.premul_alpha()` | 预乘 Alpha |
| `color.update(r, g, b, a)` | 更新值 |
| `color.grayscale()` | 灰度色 |

**Pygame 内置颜色名称（部分）：**
`"red"`, `"green"`, `"blue"`, `"white"`, `"black"`, `"yellow"`, `"cyan"`, `"magenta"`, `"orange"`, `"purple"`, `"gold"`, `"gray"`, `"pink"`, `"navy"`, `"coral"`, `"dodgerblue"`, `"forestgreen"` 等数百种。

```python
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Color 示例")
font = pygame.font.SysFont(None, 22)

colors = [
    pygame.Color("red"),
    pygame.Color("dodgerblue"),
    pygame.Color("#FF8C00"),
    pygame.Color(100, 200, 100),
    pygame.Color("purple"),
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))
    for i, c in enumerate(colors):
        # 绘制色块
        pygame.draw.rect(screen, c, (20, 20 + i * 55, 50, 40))
        # 绘制过渡色（与白色 lerp）
        for j in range(10):
            lerped = c.lerp(pygame.Color("white"), j / 10)
            pygame.draw.rect(screen, lerped, (90 + j * 30, 20 + i * 55, 28, 40))
        # 标注 RGBA
        info = font.render(f"R:{c.r} G:{c.g} B:{c.b}", True, (200, 200, 200))
        screen.blit(info, (400, 30 + i * 55))

    pygame.display.flip()

pygame.quit()
sys.exit()
```

---

## 18. pygame.cursors — 光标

提供系统光标常量和自定义光标工具。

### 系统光标

```python
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)       # 箭头
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)       # 文本光标
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_WAIT)        # 等待
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)   # 十字
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)        # 手型
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_NO)          # 禁止
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZEALL)     # 四向箭头
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZENS)      # 上下箭头
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZEWE)      # 左右箭头
```

### `pygame.cursors.compile()`

从字符串编译光标数据。

```python
data, mask = pygame.cursors.compile(strings, black='X', white='.', xor='o')
```

### `pygame.Cursor()`

创建光标对象。

```python
# 位图光标
cursor = pygame.Cursor(size, hotspot, data, mask)
# 颜色光标
cursor = pygame.Cursor(hotspot, surface)
# 系统光标
cursor = pygame.Cursor(constant)
```

---

## 19. pygame.joystick — 手柄/摇杆

### 初始化

```python
pygame.joystick.init()
count = pygame.joystick.get_count()
```

### Joystick 对象

```python
joystick = pygame.joystick.Joystick(id)
joystick.init()
```

| 方法 | 说明 |
|------|------|
| `joystick.get_name()` | 手柄名称 |
| `joystick.get_guid()` | 唯一标识 |
| `joystick.get_numaxes()` | 轴数量 |
| `joystick.get_axis(axis_number)` | 轴值 (-1.0~1.0) |
| `joystick.get_numbuttons()` | 按钮数量 |
| `joystick.get_button(button)` | 按钮状态 |
| `joystick.get_numhats()` | 方向键数量 |
| `joystick.get_hat(hat_number)` | 方向键值 (x, y) |
| `joystick.rumble(low, high, duration)` | 手柄震动 |
| `joystick.stop_rumble()` | 停止震动 |

**适用场景：** 手柄/摇杆控制的游戏。

**相关事件：**
`JOYAXISMOTION`, `JOYBUTTONDOWN`, `JOYBUTTONUP`, `JOYHATMOTION`, `JOYDEVICEADDED`, `JOYDEVICEREMOVED`

```python
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("手柄检测")
font = pygame.font.SysFont(None, 28)

joysticks = {}

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.JOYDEVICEADDED:
            joy = pygame.joystick.Joystick(event.device_index)
            joysticks[joy.get_instance_id()] = joy
            print(f"手柄连接: {joy.get_name()}")
        elif event.type == pygame.JOYDEVICEREMOVED:
            del joysticks[event.instance_id]

    screen.fill((30, 30, 30))
    count = pygame.joystick.get_count()
    text = font.render(f"Connected joysticks: {count}", True, (200, 200, 200))
    screen.blit(text, (20, 20))

    y = 60
    for jid, joy in joysticks.items():
        name = font.render(f"  {joy.get_name()}", True, (100, 200, 100))
        screen.blit(name, (20, y))
        y += 35

    if not joysticks:
        hint = font.render("No joystick detected", True, (150, 150, 150))
        screen.blit(hint, (20, 60))

    pygame.display.flip()

pygame.quit()
sys.exit()
```

---

## 20. pygame.mask — 像素遮罩（精确碰撞）

基于像素的碰撞检测，比矩形碰撞更精确。

### `pygame.mask.from_surface()`

从 Surface 创建 Mask。

```python
mask = pygame.mask.from_surface(surface, threshold=127)
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `surface` | `Surface` | 源 Surface（需有 Alpha 通道）|
| `threshold` | `int` | Alpha 阈值，大于此值的像素设为 1 |

### `pygame.mask.from_threshold()`

从颜色阈值创建 Mask。

### `pygame.mask.Mask()`

手动创建 Mask。

```python
mask = pygame.mask.Mask(size, fill=False)
```

### Mask 方法

| 方法 | 说明 |
|------|------|
| `mask.get_size()` | 获取尺寸 |
| `mask.get_at(pos)` | 获取像素值（0 或 1）|
| `mask.set_at(pos, value)` | 设置像素 |
| `mask.overlap(other, offset)` | 返回第一个重叠点 |
| `mask.overlap_area(other, offset)` | 重叠面积 |
| `mask.overlap_mask(other, offset)` | 重叠的 Mask |
| `mask.fill()` / `mask.clear()` | 全填充/全清除 |
| `mask.invert()` | 反转 |
| `mask.count()` | 已设置的像素数 |
| `mask.centroid()` | 重心位置 |
| `mask.angle()` | 旋转角度 |
| `mask.outline(every=1)` | 轮廓点列表 |
| `mask.convolve(other)` | 卷积 |
| `mask.connected_component()` | 最大连通分量 |
| `mask.connected_components()` | 所有连通分量列表 |
| `mask.get_bounding_rects()` | 边界矩形列表 |
| `mask.to_surface()` | 转换为 Surface |
| `mask.draw(other, offset)` | 绘制另一个 Mask |
| `mask.erase(other, offset)` | 擦除 |
| `mask.scale(size)` | 缩放 |

**像素碰撞示例：**

```python
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Mask 像素碰撞")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

# 创建不规则形状
circle_surf = pygame.Surface((60, 60), pygame.SRCALPHA)
pygame.draw.circle(circle_surf, (0, 200, 100, 255), (30, 30), 28)
circle_mask = pygame.mask.from_surface(circle_surf)
circle_pos = [170, 120]

star_surf = pygame.Surface((60, 60), pygame.SRCALPHA)
import math
points = []
for i in range(5):
    angle = math.radians(i * 72 - 90)
    points.append((30 + 28 * math.cos(angle), 30 + 28 * math.sin(angle)))
    angle2 = math.radians(i * 72 - 90 + 36)
    points.append((30 + 12 * math.cos(angle2), 30 + 12 * math.sin(angle2)))
pygame.draw.polygon(star_surf, (255, 200, 0, 255), points)
star_mask = pygame.mask.from_surface(star_surf)
star_pos = [50, 50]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 星星跟随鼠标
    mx, my = pygame.mouse.get_pos()
    star_pos = [mx - 30, my - 30]

    # Mask 碰撞
    offset = (circle_pos[0] - star_pos[0], circle_pos[1] - star_pos[1])
    overlap = star_mask.overlap(circle_mask, offset)

    screen.fill((30, 30, 50))
    color = (255, 50, 50) if overlap else (0, 200, 100)
    # 重新着色圆
    circle_surf.fill((0, 0, 0, 0))
    pygame.draw.circle(circle_surf, (*color, 255), (30, 30), 28)

    screen.blit(circle_surf, circle_pos)
    screen.blit(star_surf, star_pos)

    status = "PIXEL COLLISION!" if overlap else "No collision"
    text = font.render(status, True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
```

---

## 21. pygame.pixelarray — 像素数组

直接访问和修改 Surface 的像素数据。

### `pygame.PixelArray()`

```python
pxarray = pygame.PixelArray(surface)
```

**操作：**

```python
# 读取像素
color = pxarray[x, y]

# 设置像素
pxarray[x, y] = (255, 0, 0)

# 切片操作（整行/列/区域）
pxarray[10:20, :] = (0, 255, 0)    # 第10-19列设为绿色

# 使用完毕必须关闭
pxarray.close()
# 或使用 with 语句
```

### 方法

| 方法 | 说明 |
|------|------|
| `pxarray.surface` | 关联的 Surface |
| `pxarray.itemsize` | 每像素字节数 |
| `pxarray.shape` | 数组形状 |
| `pxarray.strides` | 步长 |
| `pxarray.ndim` | 维度数 |
| `pxarray.make_surface()` | 从数组创建新 Surface |
| `pxarray.replace(old_color, new_color, distance=0, weights=(0.299,0.587,0.114))` | 颜色替换 |
| `pxarray.extract(color, distance=0, weights=...)` | 提取匹配颜色 |
| `pxarray.compare(other, distance=0, weights=...)` | 比较两个数组 |
| `pxarray.transpose()` | 转置 |
| `pxarray.close()` | 释放锁定 |

```python
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("PixelArray 示例")

surface = pygame.Surface((300, 300))
pxarray = pygame.PixelArray(surface)

# 绘制渐变
for x in range(300):
    for y in range(300):
        r = int(x / 300 * 255)
        g = int(y / 300 * 255)
        b = 128
        pxarray[x, y] = (r, g, b)

pxarray.close()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(surface, (0, 0))
    pygame.display.flip()

pygame.quit()
sys.exit()
```

---

## 22. pygame.sndarray — 声音数组

将 Sound 对象与 NumPy 数组互相转换。

### 函数

```python
import pygame.sndarray

array = pygame.sndarray.array(sound)        # Sound → NumPy 数组（拷贝）
array = pygame.sndarray.samples(sound)      # Sound → NumPy 数组（引用）
sound = pygame.sndarray.make_sound(array)   # NumPy 数组 → Sound
```

**适用场景：** 音频处理、音效合成、可视化。

> **注意：** 需要安装 NumPy。

---

## 23. pygame.surfarray — Surface 数组

将 Surface 像素与 NumPy 数组互相转换。

### 函数

```python
import pygame.surfarray

# 获取像素数据（NumPy 数组）
array3d = pygame.surfarray.array3d(surface)      # RGB (拷贝)
array2d = pygame.surfarray.array2d(surface)      # 映射颜色值 (拷贝)
alpha = pygame.surfarray.array_alpha(surface)    # Alpha (拷贝)

ref3d = pygame.surfarray.pixels3d(surface)       # RGB (引用，修改直接生效)
ref2d = pygame.surfarray.pixels2d(surface)       # 映射值 (引用)
refal = pygame.surfarray.pixels_alpha(surface)   # Alpha (引用)

# 从数组创建 Surface
surface = pygame.surfarray.make_surface(array3d)

# 直接写入
pygame.surfarray.blit_array(surface, array)
```

**适用场景：** 图像处理、像素效果、与 NumPy/OpenCV 集成。

```python
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("surfarray 示例")

# 用 surfarray 创建渐变（需要 NumPy）
try:
    import numpy as np
    arr = np.zeros((400, 300, 3), dtype=np.uint8)
    for x in range(400):
        arr[x, :, 0] = int(x / 400 * 255)  # R
    for y in range(300):
        arr[:, y, 2] = int(y / 300 * 255)  # B
    arr[:, :, 1] = 80  # G
    gradient = pygame.surfarray.make_surface(arr)
except ImportError:
    gradient = pygame.Surface((400, 300))
    gradient.fill((100, 80, 150))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(gradient, (0, 0))
    pygame.display.flip()

pygame.quit()
sys.exit()
```

---

## 24. pygame.freetype — 高级字体渲染

比 `pygame.font` 更强大的字体模块，基于 FreeType 库。

### `pygame.freetype.Font()`

```python
font = pygame.freetype.Font(file, size=0)
font = pygame.freetype.SysFont(name, size, bold=False, italic=False)
```

### Font 方法

| 方法 | 说明 |
|------|------|
| `font.render(text, fgcolor, bgcolor=None, style=STYLE_DEFAULT, rotation=0, size=0)` | 返回 `(surface, rect)` |
| `font.render_to(surf, dest, text, fgcolor, bgcolor=None, style=..., rotation=..., size=...)` | 直接渲染到 Surface |
| `font.get_rect(text, style=..., rotation=..., size=...)` | 获取文本矩形 |
| `font.get_metrics(text, size=0)` | 获取字符度量 |
| `font.get_sized_height(size=0)` | 指定大小的行高 |
| `font.get_sized_ascender(size=0)` | 上升部分高度 |
| `font.get_sized_descender(size=0)` | 下降部分高度 |
| `font.get_sized_glyph_height(size=0)` | 字形高度 |

### 属性

| 属性 | 说明 |
|------|------|
| `font.size` | 默认字号 |
| `font.style` | 样式标志 |
| `font.name` | 字体名 |
| `font.path` | 文件路径 |
| `font.strong` | 粗体 |
| `font.oblique` | 斜体 |
| `font.wide` | 宽体 |
| `font.underline` | 下划线 |
| `font.ucs4` | UCS-4 模式 |
| `font.antialiased` | 抗锯齿 |
| `font.kerning` | 字间距 |
| `font.vertical` | 竖排 |
| `font.rotation` | 旋转角度 |
| `font.fgcolor` | 前景色 |
| `font.bgcolor` | 背景色 |
| `font.origin` | 使用基线原点 |
| `font.pad` | 填充 |

**优势：** 支持旋转文本、更好的 Unicode 支持、可一次渲染不同样式和大小。

```python
import pygame
import pygame.freetype
import sys

pygame.init()
screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("freetype 示例")

font = pygame.freetype.SysFont(None, 32)

running = True
angle = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((20, 20, 40))

    # 普通渲染
    font.render_to(screen, (20, 30), "FreeType Normal", (255, 255, 200), size=28)

    # 粗体
    font.render_to(screen, (20, 70), "FreeType Strong", (200, 255, 200), size=28,
                   style=pygame.freetype.STYLE_STRONG)

    # 旋转文本
    angle = (angle + 1) % 360
    surf, rect = font.render("Rotating!", (255, 200, 100), size=24, rotation=angle)
    rect.center = (350, 200)
    screen.blit(surf, rect)

    # 不同大小
    for i, sz in enumerate([16, 20, 24, 28, 32]):
        font.render_to(screen, (20, 120 + i * 35), f"Size {sz}", (180, 180, 255), size=sz)

    pygame.display.flip()

pygame.quit()
sys.exit()
```

---

## 25. pygame.gfxdraw — 抗锯齿绘图

提供更精细的绘图函数，支持抗锯齿。

> **注意：** 这是实验性模块，API 可能变化。

### 函数

| 函数 | 说明 |
|------|------|
| `gfxdraw.pixel(surface, x, y, color)` | 画素 |
| `gfxdraw.hline(surface, x1, x2, y, color)` | 水平线 |
| `gfxdraw.vline(surface, x, y1, y2, color)` | 垂直线 |
| `gfxdraw.line(surface, x1, y1, x2, y2, color)` | 直线 |
| `gfxdraw.rectangle(surface, rect, color)` | 矩形框 |
| `gfxdraw.box(surface, rect, color)` | 填充矩形 |
| `gfxdraw.circle(surface, x, y, r, color)` | 圆框 |
| `gfxdraw.aacircle(surface, x, y, r, color)` | 抗锯齿圆框 |
| `gfxdraw.filled_circle(surface, x, y, r, color)` | 填充圆 |
| `gfxdraw.ellipse(surface, x, y, rx, ry, color)` | 椭圆框 |
| `gfxdraw.aaellipse(surface, x, y, rx, ry, color)` | 抗锯齿椭圆 |
| `gfxdraw.filled_ellipse(surface, x, y, rx, ry, color)` | 填充椭圆 |
| `gfxdraw.arc(surface, x, y, r, start, end, color)` | 弧 |
| `gfxdraw.pie(surface, x, y, r, start, end, color)` | 扇形 |
| `gfxdraw.trigon(surface, x1, y1, x2, y2, x3, y3, color)` | 三角形框 |
| `gfxdraw.aatrigon(...)` | 抗锯齿三角形 |
| `gfxdraw.filled_trigon(...)` | 填充三角形 |
| `gfxdraw.polygon(surface, points, color)` | 多边形框 |
| `gfxdraw.aapolygon(surface, points, color)` | 抗锯齿多边形 |
| `gfxdraw.filled_polygon(surface, points, color)` | 填充多边形 |
| `gfxdraw.textured_polygon(surface, points, texture, tx, ty)` | 纹理多边形 |
| `gfxdraw.bezier(surface, points, steps, color)` | 贝塞尔曲线 |

**抗锯齿绘图最佳实践：** 先绘制 filled，再绘制 aa 轮廓。

```python
import pygame
import pygame.gfxdraw
import sys

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("gfxdraw 抗锯齿示例")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((240, 240, 240))

    # 抗锯齿圆（先填充再画轮廓）
    pygame.gfxdraw.filled_circle(screen, 100, 100, 50, (70, 130, 180))
    pygame.gfxdraw.aacircle(screen, 100, 100, 50, (70, 130, 180))

    # 抗锯齿三角形
    pygame.gfxdraw.filled_trigon(screen, 250, 50, 200, 150, 300, 150, (200, 100, 100))
    pygame.gfxdraw.aatrigon(screen, 250, 50, 200, 150, 300, 150, (200, 100, 100))

    # 贝塞尔曲线
    points = [(20, 250), (100, 180), (200, 280), (380, 200)]
    pygame.gfxdraw.bezier(screen, points, 20, (50, 150, 50))

    # 抗锯齿椭圆
    pygame.gfxdraw.filled_ellipse(screen, 320, 100, 60, 35, (180, 100, 180))
    pygame.gfxdraw.aaellipse(screen, 320, 100, 60, 35, (180, 100, 180))

    pygame.display.flip()

pygame.quit()
sys.exit()
```

---

## 26. pygame.scrap — 剪贴板

系统剪贴板访问。

### 函数

```python
pygame.scrap.init()                        # 初始化
pygame.scrap.get_init()                    # 是否已初始化
pygame.scrap.get(type)                     # 获取剪贴板数据
pygame.scrap.get_types()                   # 可用的数据类型列表
pygame.scrap.put(type, data)               # 写入剪贴板
pygame.scrap.contains(type)                # 是否包含指定类型
pygame.scrap.lost()                        # 是否失去剪贴板所有权
pygame.scrap.set_mode(mode)                # 设置模式 (SCRAP_CLIPBOARD/SCRAP_SELECTION)
```

**适用场景：** 文本编辑器功能、复制粘贴。

```python
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("剪贴板示例")
font = pygame.font.SysFont(None, 24)

pygame.scrap.init()

# 写入剪贴板
pygame.scrap.put(pygame.SCRAP_TEXT, b"Hello from Pygame!")

# 读取
clip = pygame.scrap.get(pygame.SCRAP_TEXT)
text = clip.decode("utf-8", errors="ignore") if clip else "Empty"

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_v and pygame.key.get_mods() & pygame.KMOD_CTRL:
                clip = pygame.scrap.get(pygame.SCRAP_TEXT)
                text = clip.decode("utf-8", errors="ignore") if clip else "Empty"

    screen.fill((30, 30, 50))
    label = font.render("Clipboard:", True, (150, 150, 150))
    content = font.render(text[:50], True, (200, 200, 200))
    screen.blit(label, (20, 40))
    screen.blit(content, (20, 80))
    hint = font.render("Ctrl+V to refresh", True, (100, 100, 100))
    screen.blit(hint, (20, 150))
    pygame.display.flip()

pygame.quit()
sys.exit()
```

---

## 附录 A：Pygame 程序基本模板

```python
import pygame
import sys

# 初始化
pygame.init()

# 常量
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 创建窗口
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Title")
clock = pygame.time.Clock()

# 游戏主循环
running = True
while running:
    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # 更新逻辑
    # ...

    # 渲染
    screen.fill(BLACK)
    # ... 绘制游戏元素 ...
    pygame.display.flip()

    # 帧率控制
    clock.tick(FPS)

# 退出
pygame.quit()
sys.exit()
```

---

## 附录 B：Pygame 模块一览表

| 模块 | 说明 | 常用度 |
|------|------|--------|
| `pygame` | 顶层初始化 | ★★★★★ |
| `pygame.display` | 窗口管理 | ★★★★★ |
| `pygame.event` | 事件处理 | ★★★★★ |
| `pygame.key` | 键盘输入 | ★★★★★ |
| `pygame.mouse` | 鼠标输入 | ★★★★★ |
| `pygame.draw` | 图形绘制 | ★★★★★ |
| `pygame.image` | 图片加载保存 | ★★★★★ |
| `pygame.font` | 字体文本 | ★★★★★ |
| `pygame.time` | 时间帧率 | ★★★★★ |
| `pygame.Rect` | 矩形对象 | ★★★★★ |
| `pygame.Surface` | 表面对象 | ★★★★★ |
| `pygame.sprite` | 精灵系统 | ★★★★☆ |
| `pygame.mixer` | 音效 | ★★★★☆ |
| `pygame.mixer.music` | 背景音乐 | ★★★★☆ |
| `pygame.transform` | 图像变换 | ★★★★☆ |
| `pygame.math` | 数学向量 | ★★★★☆ |
| `pygame.Color` | 颜色对象 | ★★★☆☆ |
| `pygame.mask` | 像素碰撞 | ★★★☆☆ |
| `pygame.freetype` | 高级字体 | ★★★☆☆ |
| `pygame.gfxdraw` | 抗锯齿绘图 | ★★☆☆☆ |
| `pygame.cursors` | 光标 | ★★☆☆☆ |
| `pygame.joystick` | 手柄 | ★★☆☆☆ |
| `pygame.pixelarray` | 像素数组 | ★★☆☆☆ |
| `pygame.surfarray` | Surface数组 | ★★☆☆☆ |
| `pygame.sndarray` | 声音数组 | ★☆☆☆☆ |
| `pygame.scrap` | 剪贴板 | ★☆☆☆☆ |

---

## 附录 C：常用技巧速查

### 帧率无关的移动

```python
clock = pygame.time.Clock()
while running:
    dt = clock.tick(60) / 1000.0  # 秒
    player.x += speed * dt
```

### 简易动画（帧动画）

```python
class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, frames, fps=10):
        super().__init__()
        self.frames = frames
        self.index = 0
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.animation_speed = 1000 / fps
        self.last_update = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_speed:
            self.last_update = now
            self.index = (self.index + 1) % len(self.frames)
            self.image = self.frames[self.index]
```

### 简易按钮

```python
class Button:
    def __init__(self, x, y, w, h, text, font):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.font = font
        self.color = (70, 130, 180)
        self.hover_color = (100, 160, 210)
        self.is_hovered = False

    def draw(self, surface):
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(surface, color, self.rect, border_radius=5)
        text_surf = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False
```

### 简易粒子效果

```python
import random

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-4, -1)
        self.life = random.randint(20, 40)
        self.color = (255, random.randint(100, 200), 0)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.1  # 重力
        self.life -= 1

    def draw(self, surface):
        if self.life > 0:
            alpha = int(255 * self.life / 40)
            size = max(1, self.life // 10)
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), size)

# 使用
particles = []
# 在需要时添加
particles.extend([Particle(200, 300) for _ in range(20)])
# 在主循环中更新和绘制
for p in particles[:]:
    p.update()
    p.draw(screen)
    if p.life <= 0:
        particles.remove(p)
```

### 简易场景管理

```python
class Scene:
    def handle_event(self, event):
        pass
    def update(self):
        pass
    def draw(self, screen):
        pass

class MenuScene(Scene):
    def draw(self, screen):
        screen.fill((20, 20, 60))

class GameScene(Scene):
    def draw(self, screen):
        screen.fill((20, 60, 20))

class SceneManager:
    def __init__(self):
        self.scenes = {}
        self.current = None

    def add(self, name, scene):
        self.scenes[name] = scene

    def switch(self, name):
        self.current = self.scenes[name]

# 使用
manager = SceneManager()
manager.add("menu", MenuScene())
manager.add("game", GameScene())
manager.switch("menu")
```

---

> **参考资料：** [Pygame 官方文档](https://www.pygame.org/docs/)
>
> 本文档基于 Pygame 2.x 版本整理，部分 API 可能因版本差异略有不同。
