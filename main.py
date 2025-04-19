import pygame
from states.game import Game
from states.start_menu import StartMenu

def main():
    pygame.init()
    screen = pygame.display.set_mode((720, 720))
    clock = pygame.time.Clock()

    states = {}
    context = {
        "match": None,
        "screen": screen,
        "font": pygame.font.Font(None, 36),
        "small_font": pygame.font.Font(None, 15),
        "options": {
            "show_yaw": True
        }
    }
    current_state = None

    def switch_state(state_name):
        nonlocal current_state
        if state_name == "game":
            # Initialize Game state here
            try:
                match = context["match"]
            except KeyError:
                raise ValueError("Match object is required to initialize Game state.")
            
            current_state = Game(switch_state, context)
            states[state_name] = current_state

        current_state = states[state_name]

    # Initialize states
    states["start_menu"] = StartMenu(switch_state, context)
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