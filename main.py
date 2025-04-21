import pygame
from states.game import Game
from states.start_menu import StartMenu
from states.settings_menu import SettingsMenu
from utils.stack import Stack

def main():
    pygame.init()
    screen = pygame.display.set_mode((720, 720))
    clock = pygame.time.Clock()
    pygame.display.set_caption("CS2 Demo Viewer")

    states = {}
    context = {
        "match": None,
        "screen": screen,
        "previous_states": Stack(), 
        "font": pygame.font.Font(None, 36),
        "small_font": pygame.font.Font(None, 15),
        "options": {
            "show_yaw": True,
            "show_health": True,
            "show_names": True
        }
    }

    current_state = None
    current_state_name = None

    def switch_state(state_name):
        nonlocal current_state
        nonlocal current_state_name

        if state_name == "game":
            # Initialize Game state here
            try:
                context["match"]
            except KeyError:
                raise ValueError("Match object is required to initialize Game state.")
            
            current_state = Game(switch_state, context)
            states[state_name] = current_state

        context["previous_states"].push(current_state_name)

        current_state = states[state_name]
        current_state_name = state_name

    # Initialize states
    states["start_menu"] = StartMenu(switch_state, context)
    states["settings_menu"] = SettingsMenu(switch_state, context)
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