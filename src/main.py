import pygame
from conway import Conway


def main():
    c = Conway()
    pygame.init()
    window_size = 600
    delay_ms = 10
    surface = pygame.display.set_mode((window_size, window_size))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.time.wait(delay_ms)
        lines = c.get_str().split(" ")
        line_break = int(len(lines)**0.5)
        size = window_size // line_break + 1
        x = 0
        y = 0
        for i, j in enumerate(lines):
            if i % line_break == 0 and i != 0:
                y += size
                x = 0
            col = (0, 0, 0) if j == "1" else (255, 255, 255)
            pygame.draw.rect(surface, col, pygame.Rect(x, y, size, size))
            x += size
        pygame.display.update()

        c.cycle()
    return


if __name__ == '__main__':
    main()
