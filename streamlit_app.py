# Streamlitライブラリをインポート
import streamlit as st

import streamlit as st
import pygame
import random

# ゲームのパラメータ
WIDTH, HEIGHT = 600, 400
PADDLE_WIDTH, PADDLE_HEIGHT = 80, 20
BALL_RADIUS = 10
PADDLE_SPEED = 5
BALL_SPEED = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 初期化
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Air Hockey")
clock = pygame.time.Clock()

# パドルのクラス
class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, PADDLE_WIDTH, PADDLE_HEIGHT))

# ボールのクラス
class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = BALL_SPEED * random.choice([-1, 1])
        self.dy = BALL_SPEED * random.choice([-1, 1])

    def draw(self):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), BALL_RADIUS)

    def update(self):
        self.x += self.dx
        self.y += self.dy

# ゲームのメイン関数
def main():
    paddle = Paddle(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 2 * PADDLE_HEIGHT)
    ball = Ball(WIDTH // 2, HEIGHT // 2)

    while True:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.x -= PADDLE_SPEED
        if keys[pygame.K_RIGHT]:
            paddle.x += PADDLE_SPEED

        paddle.draw()
        ball.draw()
        ball.update()

        if ball.x - BALL_RADIUS <= 0 or ball.x + BALL_RADIUS >= WIDTH:
            ball.dx *= -1
        if ball.y - BALL_RADIUS <= 0 or ball.y + BALL_RADIUS >= HEIGHT:
            ball.dy *= -1
        if ball.y + BALL_RADIUS >= HEIGHT - PADDLE_HEIGHT and \
           paddle.x < ball.x < paddle.x + PADDLE_WIDTH:
            ball.dy *= -1

        pygame.display.flip()
        clock.tick(60)

# Streamlitアプリケーションの作成
def run():
    st.title("エアホッケーゲーム")
    st.write("キーボードの左右矢印キーでパドルを操作してください。")

    main()

if __name__ == "__main__":
    run()
