import pygame as PG
from player.player import player

version = "0.0.1"

def main():
    PG.init()
    screen = PG.display.set_mode((800, 600))
    PG.display.set_caption("PTDS - Version " + version)
    clock = PG.time.Clock()
    running = True

    player = player()
    player_surf = PG.Surface((50, 50))
    player_surf.fill((255, 0, 0))
    player_pos = [375, 275]  # center of screen

    def update():
        player.controls()
        player.heal()

    while running:
        for event in PG.event.get():
            if event.type == PG.QUIT:
                running = False
        screen.fill((0, 0, 0))
        screen.blit(player_surf, player_pos)  # actually draw the player
        PG.display.flip()
        clock.tick(60)
    PG.quit()

if __name__ == "__main__":
    main()