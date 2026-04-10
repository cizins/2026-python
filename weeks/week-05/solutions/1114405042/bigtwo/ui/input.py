class InputHandler:
    def __init__(self, renderer):
        self.renderer = renderer
        self.selected_indices = []
        self.buttons = {}

    def handle_event(self, event, game) -> bool:
        return False

    def handle_click(self, pos, game) -> bool:
        return False

    def handle_key(self, key, game) -> bool:
        return False

    def try_play(self, game) -> bool:
        return False
