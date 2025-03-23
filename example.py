import pygame
import pygame_gifs

display = pygame.display.set_mode((600, 600))
gf = pygame_gifs.GifRecorder("output2.gif", 600, 600, threads=8)
gf.start_recording()

clock = pygame.time.Clock()

x = 0
while True:
    display.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            gf.stop_recording()
            raise SystemExit

    x += 1
    pygame.draw.rect(display, "red", (x, 40, 32, 32))

    gf.upload_frame(display)

    pygame.display.set_caption(f"{clock.get_fps()}")
    pygame.display.update()
    clock.tick(60)