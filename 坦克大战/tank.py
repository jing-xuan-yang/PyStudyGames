import sys                  # 导入 sys 模块，用于获取系统信息和退出程序
import random               # 导入 random 模块，用于生成随机数（随机选择背景、管道位置等）
import pygame               # 导入 pygame 模块，这是游戏开发的核心库

FPS = 30                    # 帧率：每秒刷新30次画面（Frames Per Second，帧/秒）
SCREEN_WIDTH  = 480         # 游戏窗口的宽度（单位：像素）
SCREEN_HEIGHT = 360         # 游戏窗口的高度（单位：像素）
BLOCK_WIDTH = 30            # 坦克/地图块的宽度（单位：像素）
BLOCK_HEIGHT = 30           # 坦克/地图块的高度（单位：像素）

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
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
# --- 加载数字图片（0-9），用于在屏幕上显示分数 ---
# convert_alpha() 将图片转换为支持透明通道的格式，提高绘制效率
IMAGES['numbers'] = (
        pygame.image.load('image/0.png').convert_alpha(),  # 数字 0
        pygame.image.load('image/1.png').convert_alpha(),  # 数字 1
        pygame.image.load('image/2.png').convert_alpha(),  # 数字 2
        pygame.image.load('image/3.png').convert_alpha(),  # 数字 3
        pygame.image.load('image/4.png').convert_alpha(),  # 数字 4
        pygame.image.load('image/5.png').convert_alpha(),  # 数字 5
        pygame.image.load('image/6.png').convert_alpha(),  # 数字 6
        pygame.image.load('image/7.png').convert_alpha(),  # 数字 7
        pygame.image.load('image/8.png').convert_alpha(),  # 数字 8
        pygame.image.load('image/9.png').convert_alpha()   # 数字 9
        )
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

def load_block_image(image_file):
    image = pygame.image.load("image/" + image_file).convert_alpha()
    image = pygame.transform.scale(image, (BLOCK_WIDTH, BLOCK_HEIGHT))  # 调整图片大小
    return image

# 所有精灵块的创建
def sprite_create(images, x, y, update):
    sprite = pygame.sprite.Sprite()
    sprite.images = images
    sprite.image = sprite.images[0]
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = x
    sprite.rect.y = y
    sprite.speed = 1
    sprite.direction = 'up'      # 默认朝上
    sprite.frame = 0             # 当前动画帧
    def sprite_update():
        update(sprite)
    sprite.update = sprite_update
    all_sprites.add(sprite)
    return sprite

# 所有坦克的控制
def tank_move(tank, direction):
    """通用坦克移动函数，direction 为 'up'/'down'/'left'/'right'"""
    if direction == 'left' and tank.rect.left > 0:
        tank.rect.x -= tank.speed
    elif direction == 'right' and tank.rect.right < SCREEN_WIDTH:
        tank.rect.x += tank.speed
    elif direction == 'up' and tank.rect.top > 0:
        tank.rect.y -= tank.speed
    elif direction == 'down' and tank.rect.bottom < SCREEN_HEIGHT:
        tank.rect.y += tank.speed

    tank.direction = direction
    tank.frame = (tank.frame + 1) % len(tank.images)

    # 根据方向旋转图片（原始图片朝右）
    angles = {'right': 0, 'left': 180, 'up': 90, 'down': -90}
    tank.image = pygame.transform.rotate(tank.images[tank.frame], angles[direction])


print('【启动】创建Map ...')


print('【启动】创建P1 ...')
# 记录当前按下的方向键，最后一个是最新按下的
p1_pressed_keys = []
p1_key_map = {pygame.K_LEFT: 'left', pygame.K_RIGHT: 'right',
              pygame.K_UP: 'up', pygame.K_DOWN: 'down'}

def p1_update(self):
    tank = self
    if len(p1_pressed_keys) > 0:
        tank_move(tank, p1_pressed_keys[-1])  # 响应最后按下的键

p1_score = 1234
p1 = sprite_create([load_block_image("p1_1.png"), load_block_image("p1_2.png")], 100, 100, p1_update)

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
        elif event.type == pygame.KEYUP and event.key in p1_key_map:
            direction = p1_key_map[event.key]
            if direction in p1_pressed_keys:
                p1_pressed_keys.remove(direction)

    # 绘制
    screen.fill(BLACK)  # 清空屏幕
    all_sprites.update() # 调用所有sprites的update函数
    all_sprites.draw(screen) # 将组内每个精灵的 image 绘制到 screen 上对应的 rect 位置。

    score_text = font.render(f"P1 Score: {p1_score}", True, WHITE)  # 显示分数
    screen.blit(score_text, (10, 10))

    pygame.display.update()  # 将绘制的内容刷新到屏幕上（不调用这行画面不会更新）
    clock.tick(FPS)       # 控制帧率，确保每秒只刷新 FPS 次

pygame.quit()
sys.exit()
