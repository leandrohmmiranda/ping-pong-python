# python pong.py para iniciar
import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Pong")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Configurações da bola e das barras
BALL_SIZE = 20
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SPEED = 4.5
PADDLE_SPEED = 15

# Inicialização da posição e velocidade
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_vel = [BALL_SPEED, BALL_SPEED]
paddle1_pos, paddle2_pos = HEIGHT // 2, HEIGHT // 2

# Pontuação
score1, score2 = 0, 0

# Função principal do jogo
def main():
    global ball_pos, ball_vel, paddle1_pos, paddle2_pos, score1, score2
    
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddle1_pos -= PADDLE_SPEED
        if keys[pygame.K_s]:
            paddle1_pos += PADDLE_SPEED
        if keys[pygame.K_UP]:
            paddle2_pos -= PADDLE_SPEED
        if keys[pygame.K_DOWN]:
            paddle2_pos += PADDLE_SPEED

        # Movimento da bola
        ball_pos[0] += ball_vel[0]
        ball_pos[1] += ball_vel[1]

        # Colisões com as bordas superiores e inferiores
        if ball_pos[1] <= 0 or ball_pos[1] >= HEIGHT - BALL_SIZE:
            ball_vel[1] = -ball_vel[1]

        # Colisões com as barras
        if (ball_pos[0] <= PADDLE_WIDTH and paddle1_pos < ball_pos[1] < paddle1_pos + PADDLE_HEIGHT) or \
           (ball_pos[0] >= WIDTH - PADDLE_WIDTH - BALL_SIZE and paddle2_pos < ball_pos[1] < paddle2_pos + PADDLE_HEIGHT):
            ball_vel[0] = -ball_vel[0]

        # Pontuação
        if ball_pos[0] <= 0:
            score2 += 1
            ball_pos = [WIDTH // 2, HEIGHT // 2]
        if ball_pos[0] >= WIDTH - BALL_SIZE:
            score1 += 1
            ball_pos = [WIDTH // 2, HEIGHT // 2]

        # Desenho dos elementos na tela
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, (0, paddle1_pos, PADDLE_WIDTH, PADDLE_HEIGHT))
        pygame.draw.rect(screen, WHITE, (WIDTH - PADDLE_WIDTH, paddle2_pos, PADDLE_WIDTH, PADDLE_HEIGHT))
        pygame.draw.ellipse(screen, WHITE, (ball_pos[0], ball_pos[1], BALL_SIZE, BALL_SIZE))
        
        font = pygame.font.Font(None, 74)
        text = font.render(str(score1), 1, WHITE)
        screen.blit(text, (250, 10))
        text = font.render(str(score2), 1, WHITE)
        screen.blit(text, (510, 10))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
