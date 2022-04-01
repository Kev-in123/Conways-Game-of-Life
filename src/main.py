import pygame
from conway import Conway

c = Conway()

def main():
    pygame.init()
    surface = pygame.display.set_mode((600, 600))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        with open("level.txt", "w") as f:
            f.write(c.get_str())
        pygame.time.wait(100)
        with open("level.txt", "r") as f:
            lines = "".join(f.readlines()).split(" ")
            x = 0
            y = 0
            for i in range(400):
                if i % 20 == 0 and i != 0:
                    y += 30
                    x = 0
                col = (0, 0, 0) if lines[i] == "1" else (255, 255, 255)
                pygame.draw.rect(surface, col, pygame.Rect(x, y, 30, 30))
                x += 30     
            pygame.display.update()
        c.cycle()
    return   

if __name__ == '__main__':
    main()
