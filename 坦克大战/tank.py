import sys                  # 导入 sys 模块，用于获取系统信息和退出程序
import random               # 导入 random 模块，用于生成随机数（随机选择背景、管道位置等）
import pygame               # 导入 pygame 模块，这是游戏开发的核心库

FPS = 30                    # 帧率：每秒刷新30次画面（Frames Per Second，帧/秒）
SCREEN_WIDTH  = 480         # 游戏窗口的宽度（单位：像素）
SCREEN_HEIGHT = 360         # 游戏窗口的高度（单位：像素）
BLOCK_WIDTH = 30            # 坦克/地图块的宽度（单位：像素）
BLOCK_HEIGHT = 30           # 坦克/地图块的高度（单位：像素）
TOP_BAR_HEIGHT = 30         # 顶部分数栏高度（单位：像素）

# 地图行列数（由屏幕大小、top bar、block大小共同决定）
MAP_COLS = SCREEN_WIDTH // BLOCK_WIDTH
MAP_ROWS = (SCREEN_HEIGHT - TOP_BAR_HEIGHT) // BLOCK_HEIGHT

# heart 位置（地图最下面一行的中间）
HEART_COL = MAP_COLS // 2
HEART_ROW = MAP_ROWS - 1
HEART_X = HEART_COL * BLOCK_WIDTH
HEART_Y = TOP_BAR_HEIGHT + HEART_ROW * BLOCK_HEIGHT

# P1/P2 初始位置（相对 heart：左2格、右2格）
P1_START_COL = HEART_COL - 2
P1_START_ROW = HEART_ROW
P1_START_X = P1_START_COL * BLOCK_WIDTH
P1_START_Y = TOP_BAR_HEIGHT + P1_START_ROW * BLOCK_HEIGHT

P2_START_COL = HEART_COL + 2
P2_START_ROW = HEART_ROW
P2_START_X = P2_START_COL * BLOCK_WIDTH
P2_START_Y = TOP_BAR_HEIGHT + P2_START_ROW * BLOCK_HEIGHT

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (80, 80, 80)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

print('【启动】开始初始化游戏...')
pygame.init()               # 初始化 Pygame 的所有子模块（显示、声音、字体等）

# 创建游戏窗口. 返回一个 Surface 对象（可以理解为“画布”），后续所有图像都画在这上面
print(f'【初始化】游戏窗口创建完成，大小: {SCREEN_WIDTH}x{SCREEN_HEIGHT}')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 创建字体对象
font = pygame.font.Font(None, 36)      # None = 系统默认字体，36 = 字号

# 创建一个时钟对象，用于控制游戏帧率（刷新速度）
clock = pygame.time.Clock()

# --- 全局字典，用于存储游戏资源 ---
# IMAGES：存储所有图片资源（Surface 对象）
# SOUNDS：存储所有音效资源（Sound 对象）
IMAGES = {}
SOUNDS = {}

print('【启动】开始加载游戏资源...')
IMAGES['win'] = pygame.image.load('image/win.png').convert_alpha()
IMAGES['select'] = pygame.image.load('image/select.png').convert_alpha()
IMAGES['gameover'] = pygame.image.load('image/gameover.png').convert_alpha()
IMAGES['p1'] = (
        pygame.image.load('image/p1_1.png').convert_alpha(),
        pygame.image.load('image/p1_2.png').convert_alpha(),
        )
IMAGES['p2'] = (
        pygame.image.load('image/p2_1.png').convert_alpha(),
        pygame.image.load('image/p2_2.png').convert_alpha(),
        )
IMAGES['enemy'] = (
        pygame.image.load('image/enemy_1.png').convert_alpha(),
        pygame.image.load('image/enemy_2.png').convert_alpha(),
        )
IMAGES['born'] = (
        pygame.image.load('image/born_1.png').convert_alpha(),
        pygame.image.load('image/born_2.png').convert_alpha(),
        pygame.image.load('image/born_3.png').convert_alpha(),
        pygame.image.load('image/born_4.png').convert_alpha(),
        )
IMAGES['explosion'] = (
        pygame.image.load('image/explosion_1.png').convert_alpha(),
        pygame.image.load('image/explosion_2.png').convert_alpha(),
        )
IMAGES['bullet'] = pygame.image.load('image/bullet_1.png').convert_alpha()
IMAGES['wall'] = pygame.image.load('image/wall.png').convert_alpha()
IMAGES['water'] = pygame.image.load('image/water_1.png').convert_alpha()
IMAGES['barrier'] = pygame.image.load('image/barrier.png').convert_alpha()

SOUNDS['start'] = pygame.mixer.Sound('audio/start.mp3')    # 死亡音效
SOUNDS['die'] = pygame.mixer.Sound('audio/die.wav')    # 死亡音效
SOUNDS['hit'] = pygame.mixer.Sound('audio/hit.mp3')    # 撞击音效

# 精灵组（group），用以碰撞检测
all_sprites = pygame.sprite.Group()
all_enemies = pygame.sprite.Group()
all_enemy_bullets = pygame.sprite.Group()
all_p1_bullets = pygame.sprite.Group()
all_p2_bullets = pygame.sprite.Group()
all_walls = pygame.sprite.Group()
all_barriers = pygame.sprite.Group()
all_grasses = pygame.sprite.Group()

def load_block_image(image_file):
    image = pygame.image.load("image/" + image_file).convert_alpha()
    image = pygame.transform.scale(image, (BLOCK_WIDTH, BLOCK_HEIGHT))  # 调整图片大小
    return image

# 所有精灵块的创建
def sprite_create(name, images, x, y, update):
    sprite = pygame.sprite.Sprite()
    sprite.name = name
    sprite.images = images
    sprite.image = sprite.images[0]
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = x
    sprite.rect.y = y
    sprite.speed = 4
    sprite.direction = 'up'      # 默认朝上
    sprite.frame = 0             # 当前动画帧
    def sprite_update():
        update(sprite, name)
    sprite.update = sprite_update
    all_sprites.add(sprite)

    if name == 'wall':
        all_walls.add(sprite)
    elif name == 'barrier':
        all_barriers.add(sprite)
    elif name == 'grass':
        all_grasses.add(sprite)

    return sprite

# 所有坦克的控制
def tank_move(tank, direction):
    """通用坦克移动函数，direction 为 'up'/'down'/'left'/'right'"""
    if direction == 'left' and tank.rect.left > 0:
        tank.rect.x -= tank.speed
    elif direction == 'right' and tank.rect.right < SCREEN_WIDTH:
        tank.rect.x += tank.speed
    elif direction == 'up' and tank.rect.top > TOP_BAR_HEIGHT:
        tank.rect.y -= tank.speed
    elif direction == 'down' and tank.rect.bottom < SCREEN_HEIGHT:
        tank.rect.y += tank.speed

    tank.direction = direction
    tank.frame = (tank.frame + 1) % len(tank.images)

    # 根据方向旋转图片（原始图片朝右）
    angles = {'right': 0, 'left': 180, 'up': 90, 'down': -90}
    tank.image = pygame.transform.rotate(tank.images[tank.frame], angles[direction])


print('【启动】创建Map ...')

# 地图块：统一 update（可拿到类型名）
def map_update(map_block, name):
    # 示例：水块做简单动画，其它地图块不动
    if name == 'water' and len(map_block.images) > 1:
        map_block.animation_tick += 1
        if map_block.animation_tick >= 8:   # 每 8 帧切换一次，避免闪烁
            map_block.animation_tick = 0
            map_block.frame = (map_block.frame + 1) % len(map_block.images)
            map_block.image = map_block.images[map_block.frame]


def build_random_map():
    wall_image = load_block_image('wall.png')
    barrier_image = load_block_image('barrier.png')
    water_images = [load_block_image('water_1.png'), load_block_image('water_2.png')]
    grass_image = load_block_image('grass.png')
    heart_images = [load_block_image('heart_ok.png'), load_block_image('heart_die.png')]

    # heart 本体与其左/上/右三面墙，统一先预留，避免随机地图覆盖
    reserved_cells = {
        (HEART_ROW, HEART_COL),         # heart
        (HEART_ROW, HEART_COL - 1),     # 左 wall
        (HEART_ROW, HEART_COL + 1),     # 右 wall
        (HEART_ROW - 1, HEART_COL),     # 上 wall
    }

    for row in range(MAP_ROWS):
        for col in range(MAP_COLS):
            if (row, col) in reserved_cells:
                continue

            # 地图四周保留一圈为空
            if row == 0 or row == MAP_ROWS - 1 or col == 0 or col == MAP_COLS - 1:
                continue

            x = col * BLOCK_WIDTH
            y = TOP_BAR_HEIGHT + row * BLOCK_HEIGHT

            # 按权重随机：空格20，barrier20，water20，grass20，wall40
            roll = random.randint(1, 120)

            if roll <= 20:
                continue
            elif roll <= 40:
                sprite_create('barrier', [barrier_image], x, y, map_update)
            elif roll <= 60:
                water = sprite_create('water', water_images, x, y, map_update)
                water.animation_tick = 0
            elif roll <= 80:
                sprite_create('grass', [grass_image], x, y, map_update)
            else:
                sprite_create('wall', [wall_image], x, y, map_update)

    # 放置 heart（最下面一行中间）
    heart = sprite_create('heart', heart_images, HEART_X, HEART_Y, map_update)

    # 用 wall 包围 heart 的左/上/右
    sprite_create('wall', [wall_image], HEART_X - BLOCK_WIDTH, HEART_Y, map_update)
    sprite_create('wall', [wall_image], HEART_X + BLOCK_WIDTH, HEART_Y, map_update)
    sprite_create('wall', [wall_image], HEART_X, HEART_Y - BLOCK_HEIGHT, map_update)

    return heart

heart = build_random_map()


print('【启动】创建P1 ...')
# 记录当前按下的方向键，最后一个是最新按下的
p1_pressed_keys = []
p1_key_map = {pygame.K_LEFT: 'left', pygame.K_RIGHT: 'right',
              pygame.K_UP: 'up', pygame.K_DOWN: 'down'}

def p1_update(self, name):
    tank = self
    if len(p1_pressed_keys) > 0:
        tank_move(tank, p1_pressed_keys[-1])  # 响应最后按下的键

p1_score = 1234
p1 = sprite_create('p1', [load_block_image("p1_1.png"), load_block_image("p1_2.png")], P1_START_X, P1_START_Y, p1_update)

print('【启动】创建P2 ...')
p2_pressed_keys = []
p2_key_map = {pygame.K_a: 'left', pygame.K_d: 'right',
              pygame.K_w: 'up', pygame.K_s: 'down'}

def p2_update(self, name):
    tank = self
    if len(p2_pressed_keys) > 0:
        tank_move(tank, p2_pressed_keys[-1])  # 响应最后按下的键

p2_score = 1234
p2 = sprite_create('p2', [load_block_image("p2_1.png"), load_block_image("p2_2.png")], P2_START_X, P2_START_Y, p2_update)

print('【开始游戏】...')

#SOUNDS['start'].play()
#print(f"display select ...")
#screen.blit(IMAGES['select'], (0, 0))
#screen.blit(IMAGES['wall'], (0, 0))
#pygame.display.update()  # 将绘制的内容刷新到屏幕上（不调用这行画面不会更新）

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key in p1_key_map:
            p1_pressed_keys.append(p1_key_map[event.key])
        elif event.type == pygame.KEYDOWN and event.key in p2_key_map:
            p2_pressed_keys.append(p2_key_map[event.key])
        elif event.type == pygame.KEYUP and event.key in p1_key_map:
            direction = p1_key_map[event.key]
            if direction in p1_pressed_keys:
                p1_pressed_keys.remove(direction)
        elif event.type == pygame.KEYUP and event.key in p2_key_map:
            direction = p2_key_map[event.key]
            if direction in p2_pressed_keys:
                p2_pressed_keys.remove(direction)

    # 绘制
    screen.fill(BLACK)  # 清空屏幕
    all_sprites.update() # 调用所有sprites的update函数
    all_sprites.draw(screen) # 将组内每个精灵的 image 绘制到 screen 上对应的 rect 位置。
    all_grasses.draw(screen) # 再画一次草地，保证草在坦克上层

    # 顶部分数栏（灰色背景）
    pygame.draw.rect(screen, GRAY, (0, 0, SCREEN_WIDTH, TOP_BAR_HEIGHT))
    score_text = font.render(f"P1 Score: {p1_score}", True, WHITE)  # 显示分数
    screen.blit(score_text, (10, 0))
    score_text = font.render(f"P2 Score: {p2_score}", True, WHITE)  # 显示分数
    screen.blit(score_text, (220, 0))

    pygame.display.update()  # 将绘制的内容刷新到屏幕上（不调用这行画面不会更新）
    clock.tick(FPS)       # 控制帧率，确保每秒只刷新 FPS 次

pygame.quit()
sys.exit()
