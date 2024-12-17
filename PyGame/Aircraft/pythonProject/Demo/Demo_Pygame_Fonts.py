import sys
from doctest import script_from_examples

import pygame

def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 400))
    pygame.display.set_caption("Show Text")

    print(pygame.font.get_default_font())
    print(pygame.font.get_fonts())

    # 0
    font0 = pygame.font.SysFont(None, 23)
    text0 = font0.render("0.defalut font 0", True, (0, 0, 255))

    # 1
    font1 = pygame.font.SysFont("汉仪中黑简", 48)
    text1_0 = font1.render("1.系统字体", True, (255, 0, 0))
    text1_1 = font1.render("汉仪中黑简", True, (255, 0, 0), (220, 220, 220))

    # 2
    font2 = pygame.font.SysFont("方正毡笔黑简体", 48, True, True)
    text2 = font2.render("2.系统字体方正毡笔黑简体加粗斜体", True, (0, 0, 0))

    # 3
    font3 = pygame.font.Font(None, 32)
    text3 = font3.render("3.default font 1", True, (0, 0, 255))

    # 4
    font4 = pygame.font.Font("comici.ttf", 48)
    font4.set_bold(True)
    font4.set_italic(True)
    font4.set_underline(True)
    text4 = font4.render("4.customed font", True, (0, 128, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((255, 255, 255))

        screen.blit(text0, (200, 20))
        screen.blit(text1_0, (80, 80))
        screen.blit(text1_1, (320, 80))
        screen.blit(text2, (10, 170))
        screen.blit(text3, (200, 260))
        screen.blit(text4, (80, 300))

        pygame.display.flip()


if __name__ == "__main__":
    main()

