import pygame as pg
from pygame.constants import K_DOWN

#====================================================WINDOW====================================================
WINDOW_HIGHT = 500  # Высота окна/поля
WINDOW_WIGTH = 500  # Ширина окна/поля
WINDOW_BACKGROUND = (34, 40, 49)  # Цвет заднего фона
WINDOW_PADING = 10  # Отступы от рамки во время спавна еды
WINDOW_SIZE = (WINDOW_WIGTH, WINDOW_HIGHT)
#====================================================SNAKE====================================================
SNAKE_COLOR = (0, 173, 181)   # Цвет змейки в RGB
SNAKE_SIZE = 10 # Размер сегмента змейки
SNAKE_START_SIZE = 2    # Размер змейки при старте игры, не считая головы
#====================================================EAT====================================================
EAT_COLOR = (238, 238, 238) # Цвет еды в RGB
EAT_SIZE = 10   # Размер еды
#====================================================KEY====================================================
K_LEFT = pg.K_a  # Клавиша при нажитии которой змаейка начинает двигаться влево
K_RIGHT = pg.K_d    # Клавиша при нажитии которой змаейка начинает двигаться вправо
K_UP = pg.K_w  # Клавиша при нажитии которой змаейка начинает двигаться вверх
K_DOWN = pg.K_s  # Клавиша при нажитии которой змаейка начинает двигаться вниз
#====================================================GAME====================================================
GAME_NAME = 'Snake'
GAME_START_POS = () # Стартовая позиция змейки, если требуется случайное значение, то оставить пустой кортеж
GAME_START_DIR = 'left' # Стартовое направление змейки, доступны down/up/left/right, если SNAKE_START_SIZE > 0, то right не работает т.к. змейка врезается сама в себя
GAME_FPS = 10    # Кол-во кадров в секкунду
GAME_DELTA_FPS = 1  # На сколько будет увеличиваться FPS при наборе очков 
GAME_POINTS_CHANGE = 1  # При наборе очков кратных этой цифре FPS будет увеличиваться на GAME_DELTA_FPS
GAME_FONT_SIZE = 60 # Размер шрифта в игре
GAME_FONT_COLOR = (57, 62, 70) # Цвет текста в RGB
GAME_EXIT_PAUSE = 2    # Время задержки экрана проигрыша перед выходом в секундах