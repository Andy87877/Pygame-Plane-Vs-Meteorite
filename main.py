import pygame

FPS = 60 # 一秒執行幾次
WHITE = (255,255,255) # 白色
WIDTH = 500 # 寬度
HEIGHT = 600 # 高度

# 遊戲初始化 and 創建視窗
pygame.init() #全部初始化
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # 畫面寬度和高度
clock = pygame.time.Clock() # 可以用時間操控

running = True # 執行遊戲迴圈

# 遊戲迴圈
while running:
    clock.tick(FPS) # 一秒執行幾次
    # 取得輸入
    for event in pygame.event.get(): # 回傳發生的所有事件(列表)
        if event.type == pygame.QUIT: # 按右上角的XX
            running = False # 跳出遊戲迴圈

    # 更新遊戲

    # 畫面顯示
    screen.fill(WHITE) # 填滿顏色 (R,G,B)
    pygame.display.update() #畫面更新

pygame.quit() # 把遊戲視窗關掉
