import pygame as pg
import setings as st
import random
from snake import Snake as sn
from time import sleep


def spawn_eat():
    x = random.randint(st.WINDOW_PADING, (st.WINDOW_WIGTH - st.WINDOW_PADING))
    y = random.randint(st.WINDOW_PADING, (st.WINDOW_HIGHT - st.WINDOW_PADING))
    return pg.Rect(x, y, st.EAT_SIZE, st.EAT_SIZE)


def game_over(snake, screen):
    screen.fill(st.WINDOW_BACKGROUND)
    font = pg.font.Font(None, int(st.GAME_FONT_SIZE*1.5))
    text = font.render("Game over", True, st.GAME_FONT_COLOR)
    screen.blit(text, (st.WINDOW_WIGTH//6, st.WINDOW_HIGHT//6))
    with open('score.txt', 'r') as f:
        score = int(f.read())
    if score < len(snake.body) - snake.start_len:
        with open('score.txt', 'w') as f:
            f.write(str(len(snake.body) - snake.start_len))
    font = pg.font.Font(None, st.GAME_FONT_SIZE)
    text = font.render(f"You scored {str(len(snake.body) - snake.start_len)}", True, st.GAME_FONT_COLOR)
    screen.blit(text, (st.WINDOW_WIGTH//6, (st.WINDOW_HIGHT//6)*2))
    font = pg.font.Font(None, st.GAME_FONT_SIZE)
    text = font.render(f'Your record: {score}', True, st.GAME_FONT_COLOR)
    screen.blit(text, (st.WINDOW_WIGTH//6, (st.WINDOW_HIGHT//6)*3))
    pg.display.update()
    sleep(st.GAME_EXIT_PAUSE)
    pg.quit()
    quit()
    


def main():
#====================================================Иницилизация====================================================
# Иницилизация pygame
    pg.init()
    screen = pg.display.set_mode(st.WINDOW_SIZE)
    pg.display.set_caption(st.GAME_NAME)
    clock = pg.time.Clock()
# Иницилизация змейки
    if st.GAME_START_POS:
        x, y = st.GAME_START_POS
    else:
        x = random.randint(st.WINDOW_PADING, st.WINDOW_WIGTH - st.WINDOW_PADING)
        y = random.randint(st.WINDOW_PADING, st.WINDOW_HIGHT - st.WINDOW_PADING)
    snake = sn(x, y, st.SNAKE_START_SIZE)
    if st.GAME_START_DIR and st.GAME_START_DIR in {'left', 'right', 'up', 'down'}:
        dir = st.GAME_START_DIR
    else: 
        dir = 'left'
    eat = spawn_eat()
# Иницилизация шривтов
    pg.font.init()
    font = pg.font.Font(None, st.GAME_FONT_SIZE)
    text = font.render(str(len(snake.body) - snake.start_len), True, st.GAME_FONT_COLOR)
    textpos = (10, 10)
# Иницилизация FPS
    FPS = st.GAME_FPS
#====================================================================================================================

    while True:
        snake.step(dir)


        for i in pg.event.get():
            if i.type == pg.QUIT:
                pg.quit()
                pg.quit()
                return
            elif i.type == pg.KEYDOWN:
                if i.key == st.K_LEFT:
                    if dir == 'right':
                        pass
                    else:
                        dir = 'left'
                elif i.key == st.K_RIGHT:
                    if dir == 'left':
                        pass
                    else:
                        dir = 'right'
                elif i.key == st.K_UP:
                    if dir == 'down':
                        pass
                    else:
                        dir = 'up'
                elif i.key == st.K_DOWN:
                    if dir == 'up':
                        pass
                    else:
                        dir = 'down'

        pg.draw.rect(screen, st.EAT_COLOR, eat)        

        if snake.body[0].colliderect(eat):
            snake.eat()
            text = font.render(str(len(snake.body) - snake.start_len), True, st.GAME_FONT_COLOR)
            eat = spawn_eat()
            # Проверка на увиличение FPS
            if (len(snake.body) - snake.start_len) % st.GAME_POINTS_CHANGE == 0:
                FPS += st.GAME_DELTA_FPS

        for i in snake.body[2:]:
            center_x = i.x + (st.SNAKE_SIZE / 2)
            center_y = i.y + (st.SNAKE_SIZE / 2)
            if snake.body[0].collidepoint(center_x, center_y):
                game_over(snake, screen)

        x = snake.body[0].x
        y = snake.body[0].y

        if x >= st.WINDOW_WIGTH:
            game_over(snake, screen)
        elif x <= 0:
            game_over(snake, screen)
        elif y <= 0:
            game_over(snake, screen)
        elif y >= st.WINDOW_HIGHT:
            game_over(snake, screen)


        for i in snake.body:
            pg.draw.rect(screen, st.SNAKE_COLOR, i)
        
        
        screen.blit(text, textpos)
        pg.display.update()
        screen.fill(st.WINDOW_BACKGROUND) 

        clock.tick(FPS)


if __name__ == '__main__':
    main()