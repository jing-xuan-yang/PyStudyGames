import sys                  # 导入 sys 模块，用于获取系统信息和退出程序
import random               # 导入 random 模块，用于生成随机数（随机选择背景、管道位置等）
import pygame               # 导入 pygame 模块，这是游戏开发的核心库

FPS = 30                    # 帧率：每秒刷新30次画面（Frames Per Second，帧/秒）
SCREEN_WIDTH  = 480         # 游戏窗口的宽度（单位：像素）
SCREEN_HEIGHT = 360         # 游戏窗口的高度（单位：像素）
BLOCK_WIDTH = 30            # 坦克/地图块的宽度（单位：像素）
BLOCK_HEIGHT = 30           # 坦克/地图块的高度（单位：像素）
TOP_BAR_HEIGHT = 30         # 顶部分数栏高度（单位：像素）
BULLET_WIDTH = 10           # 子弹宽度（单位：像素）
BULLET_HEIGHT = 10          # 子弹高度（单位：像素）
BULLET_SPEED = 8            # 子弹速度（单位：像素/帧）
ENEMY_SPAWN_INTERVAL = FPS * 4   # 敌人固定刷新频率（每 4 秒）
ENEMY_FIRE_INTERVAL = FPS * 2    # 敌人射击频率（每 2 秒）
EXPLOSION_FRAME_INTERVAL = 4     # 爆炸动画每隔多少帧切换一次图片

# 地图行列数（由屏幕大小、top bar、block大小共同决定）
MAP_COLS = SCREEN_WIDTH // BLOCK_WIDTH
MAP_ROWS = (SCREEN_HEIGHT - TOP_BAR_HEIGHT) // BLOCK_HEIGHT

# heart 位置（地图最下面一行的中间）
HEART_COL = MAP_COLS // 2
HEART_ROW = MAP_ROWS - 1
HEART_X = HEART_COL * BLOCK_WIDTH
HEART_Y = TOP_BAR_HEIGHT + HEART_ROW * BLOCK_HEIGHT

# P1/P2 初始位置（相对 heart：左2格、右2格）
# 注意：这里用“格子坐标”计算，改地图大小时出生点会自动跟随。
P1_START_COL = HEART_COL - 2
P1_START_ROW = HEART_ROW
P1_START_X = P1_START_COL * BLOCK_WIDTH
P1_START_Y = TOP_BAR_HEIGHT + P1_START_ROW * BLOCK_HEIGHT

P2_START_COL = HEART_COL + 2
P2_START_ROW = HEART_ROW
P2_START_X = P2_START_COL * BLOCK_WIDTH
P2_START_Y = TOP_BAR_HEIGHT + P2_START_ROW * BLOCK_HEIGHT

# 敌人在地图最上方左/中/右三个位置刷新
ENEMY_LEFT_SPAWN_X = BLOCK_WIDTH
ENEMY_MIDDLE_SPAWN_X = (MAP_COLS // 2) * BLOCK_WIDTH
ENEMY_RIGHT_SPAWN_X = (MAP_COLS - 2) * BLOCK_WIDTH
ENEMY_SPAWN_Y = TOP_BAR_HEIGHT
ENEMY_SPAWN_POINTS = [
    (ENEMY_LEFT_SPAWN_X, ENEMY_SPAWN_Y),
    (ENEMY_MIDDLE_SPAWN_X, ENEMY_SPAWN_Y),
    (ENEMY_RIGHT_SPAWN_X, ENEMY_SPAWN_Y),
]

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
font = pygame.font.Font(None, 30)      # None = 系统默认字体，36 = 字号

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
IMAGES['born'] = (
        pygame.image.load('image/born_1.png').convert_alpha(),
        pygame.image.load('image/born_2.png').convert_alpha(),
        pygame.image.load('image/born_3.png').convert_alpha(),
        pygame.image.load('image/born_4.png').convert_alpha(),
        )

SOUNDS['start'] = pygame.mixer.Sound('audio/start.mp3')    # 死亡音效
SOUNDS['die'] = pygame.mixer.Sound('audio/die.wav')
SOUNDS['hit'] = pygame.mixer.Sound('audio/hit.mp3')    # 撞击音效
SOUNDS['fire'] = pygame.mixer.Sound('audio/fire.mp3')    # 撞击音效

# 精灵组（group），用以碰撞检测或者批量控制
all_sprites = pygame.sprite.Group()
all_enemies = pygame.sprite.Group()
all_enemy_bullets = pygame.sprite.Group()
all_p1_bullets = pygame.sprite.Group()
all_p2_bullets = pygame.sprite.Group()
all_walls = pygame.sprite.Group()
all_barriers = pygame.sprite.Group()
all_waters = pygame.sprite.Group()
all_grasses = pygame.sprite.Group()
all_tanks = pygame.sprite.Group()
all_bullets = pygame.sprite.Group()

def load_block_image(image_file):
    image = pygame.image.load("image/" + image_file).convert_alpha()
    image = pygame.transform.scale(image, (BLOCK_WIDTH, BLOCK_HEIGHT))  # 调整图片大小
    return image


# 所有精灵块的创建
def sprite_create(name, images, x, y, update, size=None):
    sprite = pygame.sprite.Sprite()
    sprite.name = name
    sprite.images = images
    # 可选缩放：传入 size=(w, h) 时，统一缩放该精灵的所有动画帧。
    if size is not None:
        resized_images = []
        for image in images:
            resized_images.append(pygame.transform.smoothscale(image, size))
        sprite.images = resized_images
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
    elif name == 'water':
        all_waters.add(sprite)
    elif name == 'grass':
        all_grasses.add(sprite)

    return sprite

# 所有坦克的控制
def tank_move(tank, direction):
    """通用坦克移动函数，direction 为 'up'/'down'/'left'/'right'"""
    # 先保存旧位置。若发生碰撞，再回退到旧位置。
    old_x = tank.rect.x
    old_y = tank.rect.y

    if direction == 'left' and tank.rect.left > 0:
        tank.rect.x -= tank.speed
    elif direction == 'right' and tank.rect.right < SCREEN_WIDTH:
        tank.rect.x += tank.speed
    elif direction == 'up' and tank.rect.top > TOP_BAR_HEIGHT:
        tank.rect.y -= tank.speed
    elif direction == 'down' and tank.rect.bottom < SCREEN_HEIGHT:
        tank.rect.y += tank.speed

    # 与 wall / barrier / water 碰撞则回退位置（达到“不能穿过”的效果）
    hit_wall = pygame.sprite.spritecollideany(tank, all_walls)
    hit_barrier = pygame.sprite.spritecollideany(tank, all_barriers)
    hit_water = pygame.sprite.spritecollideany(tank, all_waters)
    if hit_wall or hit_barrier or hit_water:
        tank.rect.x = old_x
        tank.rect.y = old_y

    tank.direction = direction
    tank.frame = (tank.frame + 1) % len(tank.images)

    # 根据方向旋转图片（原始图片朝右）
    angles = {'right': 0, 'left': 180, 'up': 90, 'down': -90}
    tank.image = pygame.transform.rotate(tank.images[tank.frame], angles[direction])


def add_score_by_name(name, value):
    global p1_score, p2_score
    if name == 'p1':
        p1_score += value
    elif name == 'p2':
        p2_score += value


def respawn_tank(tank):
    if tank.name == 'p1':
        tank.rect.x = P1_START_X
        tank.rect.y = P1_START_Y
    elif tank.name == 'p2':
        tank.rect.x = P2_START_X
        tank.rect.y = P2_START_Y

    tank.direction = 'up'
    tank.frame = 0
    tank.image = tank.images[0]


def explosion_update(explosion, name):
    explosion.frame_tick += 1
    if explosion.frame_tick >= EXPLOSION_FRAME_INTERVAL:
        explosion.frame_tick = 0
        explosion.frame += 1
        if explosion.frame >= len(explosion.images):
            explosion.kill()
        else:
            explosion.image = explosion.images[explosion.frame]


def spawn_tank_explosion(x, y):
    explosion = sprite_create('explosion',
            [load_block_image('explosion_1.png'), load_block_image('explosion_1.png')],
            x, y, explosion_update, size=(BLOCK_WIDTH, BLOCK_HEIGHT)
    )
    explosion.frame_tick = 0

    SOUNDS['die'].play()


def handle_tank_hit(target_tank, bullet):
    global p1_life, p2_life

    # 同阵营命中：无副作用（仅子弹消失）
    if target_tank.team == bullet.team:
        return

    # 播放被击中爆炸动画（两帧）与死亡音效
    spawn_tank_explosion(target_tank.rect.x, target_tank.rect.y)

    # 异阵营命中：消灭目标
    if target_tank.team == 'enemy':
        target_tank.kill()
        add_score_by_name(bullet.name, 10)
    elif target_tank.name == 'p1':
        p1_life -= 1
        if p1_life > 0:
            respawn_tank(target_tank)
        else:
            target_tank.kill()
    elif target_tank.name == 'p2':
        p2_life -= 1
        if p2_life > 0:
            respawn_tank(target_tank)
        else:
            target_tank.kill()


def bullet_update(bullet):
    if not bullet.alive():
        return

    if bullet.direction == 'left':
        bullet.rect.x -= bullet.speed
    elif bullet.direction == 'right':
        bullet.rect.x += bullet.speed
    elif bullet.direction == 'up':
        bullet.rect.y -= bullet.speed
    elif bullet.direction == 'down':
        bullet.rect.y += bullet.speed

    if bullet.rect.right < 0 or bullet.rect.left > SCREEN_WIDTH or bullet.rect.bottom < TOP_BAR_HEIGHT or bullet.rect.top > SCREEN_HEIGHT:
        bullet.kill()
        return


def process_bullet_collisions():
    # ============================================================
    # pygame.sprite.groupcollide 详细说明（本函数核心）
    # ------------------------------------------------------------
    # 函数签名：
    #   pygame.sprite.groupcollide(group1, group2, dokill1, dokill2)
    #
    # 参数含义：
    #   group1 / group2 : 两个要做碰撞检测的精灵组
    #   dokill1         : 若为 True，group1 中发生碰撞的精灵会自动 kill()
    #   dokill2         : 若为 True，group2 中发生碰撞的精灵会自动 kill()
    #
    # 返回值（非常重要）：
    #   返回一个字典 dict：
    #     键   -> group1 里“发生了碰撞”的某个精灵
    #     值   -> 一个列表，里面是它在 group2 中撞到的所有精灵
    #
    #   结构示意：
    #     {
    #       sprite_a: [sprite_x, sprite_y],
    #       sprite_b: [sprite_z],
    #     }
    #
    # 结合下面代码看：
    #   bullet_hits = groupcollide(all_bullets, all_bullets, False, False)
    #   含义是：
    #   - 键：某颗子弹 bullet
    #   - 值：这颗子弹碰到的其他子弹列表 other_bullets
    #
    # 注意：本函数里 dokill 都是 False，表示“先检测，再由我们自己决定业务逻辑”。
    # 这样做的好处：
    #   - 可以自定义加分
    #   - 可以按阵营区分
    #   - 可以先判断再 kill，逻辑更清晰
    # ============================================================

    # 1) 子弹互相抵消（批量检测）
    bullet_hits = pygame.sprite.groupcollide(all_bullets, all_bullets, False, False)
    for bullet, other_bullets in bullet_hits.items():
        if not bullet.alive():
            continue
        for other_bullet in other_bullets:
            if other_bullet == bullet or not other_bullet.alive():
                continue

            add_score_by_name(bullet.name, 1)
            add_score_by_name(other_bullet.name, 1)
            bullet.kill()
            other_bullet.kill()
            break

    # 2) 子弹打墙（批量检测）
    # 返回值结构：
    #   {
    #     某颗子弹bullet: [撞到的墙1, 撞到的墙2, ...],
    #     ...
    #   }
    # 这里我们只处理第一块墙 walls[0]，并让子弹消失。
    bullet_wall_hits = pygame.sprite.groupcollide(all_bullets, all_walls, False, False)
    for bullet, walls in bullet_wall_hits.items():
        if not bullet.alive() or len(walls) == 0:
            continue
        walls[0].kill()
        add_score_by_name(bullet.name, 1)
        bullet.kill()

    # 3) 子弹打坦克（批量检测）
    # 返回值结构：
    #   {
    #     某颗子弹bullet: [撞到的坦克1, 撞到的坦克2, ...],
    #     ...
    #   }
    # 后续再按业务规则过滤：
    #   - 不处理子弹自己的 owner
    #   - 不处理已经死亡的 tank
    #   - 其余交给 handle_tank_hit()（里面有阵营判断和掉血/加分）
    bullet_tank_hits = pygame.sprite.groupcollide(all_bullets, all_tanks, False, False)
    for bullet, tanks in bullet_tank_hits.items():
        if not bullet.alive():
            continue
        for tank in tanks:
            if tank == bullet.owner or not tank.alive():
                continue
            handle_tank_hit(tank, bullet)
            bullet.kill()
            break


def fire_bullet(shooter):
    if shooter.name == 'p1' or shooter.name == 'p2':
        SOUNDS['fire'].play()

    def bullet_sprite_update(sprite, name):
        bullet_update(sprite)

    bullet_x = shooter.rect.centerx - (BULLET_WIDTH // 2)
    bullet_y = shooter.rect.centery - (BULLET_HEIGHT // 2)
    bullet = sprite_create(
        shooter.name,                 # 子弹 name 记录发送者
        [load_block_image('bullet_1.png')],
        bullet_x,
        bullet_y,
        bullet_sprite_update,
        size=(BULLET_WIDTH, BULLET_HEIGHT),
    )

    bullet.owner = shooter
    bullet.team = shooter.team
    bullet.direction = shooter.direction
    bullet.speed = BULLET_SPEED

    all_bullets.add(bullet)

    if shooter.name == 'p1':
        all_p1_bullets.add(bullet)
    elif shooter.name == 'p2':
        all_p2_bullets.add(bullet)
    elif shooter.name.startswith('enemy'):
        all_enemy_bullets.add(bullet)


enemy_counter = 0


def enemy_update(enemy, name):
    enemy.move_tick += 1
    if enemy.move_tick >= enemy.move_interval:
        enemy.move_tick = 0
        enemy.direction = random.choice(['left', 'right', 'up', 'down', 'down', 'down'])

    tank_move(enemy, enemy.direction)

    enemy.fire_tick += 1
    if enemy.fire_tick >= ENEMY_FIRE_INTERVAL:
        enemy.fire_tick = 0
        fire_bullet(enemy)


def spawn_enemy(x, y):
    global enemy_counter
    enemy_counter += 1
    enemy_name = f'enemy_{enemy_counter}'
    enemy = sprite_create(
        enemy_name,
        [load_block_image("enemy_1.png"), load_block_image("enemy_2.png")],
        x,
        y,
        enemy_update,
        size=(BLOCK_WIDTH - 5, BLOCK_HEIGHT - 5),
    )
    enemy.direction = 'down'
    enemy.speed = 2
    enemy.team = 'enemy'
    all_tanks.add(enemy)
    all_enemies.add(enemy)
    enemy.move_tick = 0
    enemy.move_interval = 12
    enemy.fire_tick = 0
    return enemy


def spawn_enemies_at_top():
    for spawn_x, spawn_y in ENEMY_SPAWN_POINTS:
        spawn_enemy(spawn_x, spawn_y)


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

    # heart 本体与其左/上/右三面墙，统一先预留，避免随机地图覆盖。
    # 预留后，这些格子不会参与随机生成。
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
            # 用 1~120 映射概率，便于直观看出比例。
            roll = random.randint(1, 120)

            if roll <= 20:
                continue
            elif roll <= 40:
                sprite_create('barrier', [barrier_image], x, y, map_update)
            elif roll <= 60:
                water = sprite_create('water', water_images, x, y, map_update)
                # 水面动画计时器：不每帧切图，避免闪烁。
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
# P1：方向键控制
p1_key_map = {pygame.K_LEFT: 'left', pygame.K_RIGHT: 'right',
              pygame.K_UP: 'up', pygame.K_DOWN: 'down'}

def p1_update(self, name):
    tank = self
    if len(p1_pressed_keys) > 0:
        tank_move(tank, p1_pressed_keys[-1])  # 响应最后按下的键

p1_score = 0
p1_life = 3
p1 = sprite_create('p1', [load_block_image("p1_1.png"), load_block_image("p1_2.png")], P1_START_X, P1_START_Y, p1_update, size=(BLOCK_WIDTH - 5, BLOCK_HEIGHT - 5))
p1.team = 'player'
all_tanks.add(p1)

print('【启动】创建P2 ...')
p2_pressed_keys = []
# P2：WASD 控制
p2_key_map = {pygame.K_a: 'left', pygame.K_d: 'right',
              pygame.K_w: 'up', pygame.K_s: 'down'}

def p2_update(self, name):
    tank = self
    if len(p2_pressed_keys) > 0:
        tank_move(tank, p2_pressed_keys[-1])  # 响应最后按下的键

p2_score = 0
p2_life = 3
p2 = sprite_create('p2', [load_block_image("p2_1.png"), load_block_image("p2_2.png")], P2_START_X, P2_START_Y, p2_update, size=(BLOCK_WIDTH - 5, BLOCK_HEIGHT - 5))
p2.team = 'player'
all_tanks.add(p2)

# 开始时同时刷新 3 个敌人（左/中/右）
spawn_enemies_at_top()
enemy_spawn_tick = 0

print('【开始游戏】...')

#print(f"display select ...")
#screen.blit(IMAGES['select'], (0, 0))
#screen.blit(IMAGES['wall'], (0, 0))
#pygame.display.update()  # 将绘制的内容刷新到屏幕上（不调用这行画面不会更新）

SOUNDS['start'].play()

running = True
while running:
    enemy_spawn_tick += 1
    if enemy_spawn_tick >= ENEMY_SPAWN_INTERVAL:
        enemy_spawn_tick = 0
        spawn_enemies_at_top()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key in p1_key_map:
            p1_pressed_keys.append(p1_key_map[event.key])
        elif event.type == pygame.KEYDOWN and event.key in p2_key_map:
            p2_pressed_keys.append(p2_key_map[event.key])
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if p1.alive() and p1_life > 0:
                fire_bullet(p1)
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_0 or event.key == pygame.K_KP0):
            if p2.alive() and p2_life > 0:
                fire_bullet(p2)
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
    process_bullet_collisions() # 子弹碰撞统一批量处理（更高效）
    all_sprites.draw(screen) # 将组内每个精灵的 image 绘制到 screen 上对应的 rect 位置。
    # 再画一次 grass：利用“后画的盖在上面”实现草丛遮挡坦克效果。
    all_grasses.draw(screen)

    # 顶部分数栏（灰色背景）
    pygame.draw.rect(screen, GRAY, (0, 0, SCREEN_WIDTH, TOP_BAR_HEIGHT))
    score_text = font.render(f"P1 Score:{p1_score} Life:{p1_life}", True, WHITE)  # 显示分数和生命
    screen.blit(score_text, (10, 0))
    score_text = font.render(f"P2 Score:{p2_score} Life:{p2_life}", True, WHITE)  # 显示分数和生命
    screen.blit(score_text, (220, 0))

    pygame.display.update()  # 将绘制的内容刷新到屏幕上（不调用这行画面不会更新）
    clock.tick(FPS)       # 控制帧率，确保每秒只刷新 FPS 次

pygame.quit()
sys.exit()
