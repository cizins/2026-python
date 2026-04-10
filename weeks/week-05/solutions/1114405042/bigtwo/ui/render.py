import pygame

class Renderer:
    COLORS = {
        'background': (45, 45, 45),
        'card_back': (74, 144, 217),
        'spade_club': (255, 255, 255),
        'heart_diamond': (231, 76, 60),
        'player': (46, 204, 113),
        'ai': (149, 165, 166),
        'selected': (241, 196, 15),
        'button': (52, 152, 219)
    }
    CARD_WIDTH = 60
    CARD_HEIGHT = 90

    def draw_card(self, screen, card, x, y, selected=False):
        pass

    def draw_hand(self, screen, hand, x, y, selected_indices):
        pass

    def draw_player(self, screen, player, x, y, is_current):
        pass

    def draw_last_play(self, screen, cards, player_name, x, y):
        pass

    def draw_buttons(self, screen, buttons, x, y):
        pass
