import logging

import pwnagotchi.ui.fonts as fonts
from pwnagotchi.ui.hw.base import DisplayImpl


class Spotpear154lcd(DisplayImpl):
    def __init__(self, config):
        super(Spotpear154lcd, self).__init__(config, 'spotpear154lcd')

    def layout(self):
        fonts.setup(10, 9, 10, 35, 25, 9)
        self._layout['width'] = 240
        self._layout['height'] = 240
        self._layout['face'] = (0, 40)
        self._layout['name'] = (5, 20)
        self._layout['channel'] = (0, 0)
        self._layout['aps'] = (28, 0)
        self._layout['uptime'] = (175, 0)
        self._layout['line1'] = [0, 14, 240, 14]
        self._layout['line2'] = [0, 108, 240, 108]
        self._layout['friend_face'] = (0, 92)
        self._layout['friend_name'] = (40, 94)
        self._layout['shakes'] = (0, 109)
        self._layout['mode'] = (215, 109)
        self._layout['status'] = {
            'pos': (125, 20),
            'font': fonts.status_font(fonts.Medium),
            'max': 20
        }

        return self._layout

    def initialize(self):
        logging.info("initializing gamepi15 display")
        from pwnagotchi.ui.hw.libs.pimoroni.displayhatmini.ST7789 import ST7789
        self._display = ST7789(0, 0, 22, 24, 27, 240, 240, 0, True, 60 * 1000 * 1000, 0, 0)

    def render(self, canvas):
        self._display.display(canvas)

    def clear(self):
        self._display.clear()
