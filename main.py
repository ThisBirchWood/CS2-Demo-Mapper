import pygame
from states.game import Game
from states.start_menu import StartMenu


def main():
    pygame.init()
    screen = pygame.display.set_mode((720, 720))
    clock = pygame.time.Clock()

    states = {}
    current_state = None

    def switch_state(state_name, data=None):
        nonlocal current_state
        if state_name == "game":
            match = data.get("match")
            current_state = Game(switch_state, screen, match)
            states[state_name] = current_state

        current_state = states[state_name]

    # Initialize states
    states["start_menu"] = StartMenu(switch_state, screen)
    switch_state("start_menu")

    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        current_state.handle_events(events)
        current_state.update()
        current_state.draw()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()