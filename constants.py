import time

EVENT_NONE             = 0x00
EVENT_SINGLE_PRESS     = 0x01
EVENT_DOUBLE_PRESS     = 0x02
EVENT_LONG_PRESS       = 0x04
EVENT_EXTRA_LONG_PRESS = 0x08
EVENT_KEY_DOWN         = 0x10
EVENT_KEY_UP           = 0x20

KEYBOARD_DELAY = 0.2
ANIMATION_FRAME = 0.15
ANIMATION_WAIT = 0.25

COLOUR_WHITE  = (0xFF, 0xFF, 0xFF)
COLOUR_RED    = (0xFF, 0x00, 0x00)
COLOUR_ORANGE = (0xFF, 0xA5, 0x00)
COLOUR_YELLOW = (0xFF, 0xFF, 0x00)
COLOUR_GREEN  = (0x00, 0xFF, 0x00)
COLOUR_BLUE   = (0x00, 0x00, 0xFF)
COLOUR_INDIGO = (0x4B, 0x00, 0x82)
COLOUR_VIOLET = (0x8F, 0x00, 0xFF)
COLOUR_CLEAR  = (0x08, 0x08, 0x08)
COLOUR_OFF    = (0x00, 0x00, 0x00)

COLOUR_WHITE_MID   = (0x80, 0x80, 0x80)
COLOUR_DARK_RED    = (0x80, 0x00, 0x00)
COLOUR_DARK_ORANGE = (0x80, 0x52, 0x00)
COLOUR_DARK_YELLOW = (0x80, 0x80, 0x00)
COLOUR_DARK_GREEN  = (0x00, 0x80, 0x00)
COLOUR_DARK_BLUE   = (0x00, 0x00, 0x80)
COLOUR_DARK_INDIGO = (0x25, 0x00, 0x41)
COLOUR_DARK_VIOLET = (0x74, 0x00, 0x80)

DOUBLE_GAP = 250
LONG_HOLD = 1000
EXTRA_LONG_HOLD = 3000

BUTTON_COUNT = 16

def noOp():
    pass

def timeInMillis():
    return int(time.monotonic() * 1000)

def darkVersion(colour):
    if colour == COLOUR_RED:
        return COLOUR_DARK_RED
    if colour == COLOUR_ORANGE:
        return COLOUR_DARK_ORANGE
    if colour == COLOUR_YELLOW:
        return COLOUR_DARK_YELLOW
    if colour == COLOUR_GREEN:
        return COLOUR_DARK_GREEN
    if colour == COLOUR_BLUE:
        return COLOUR_DARK_BLUE
    if colour == COLOUR_INDIGO:
        return COLOUR_DARK_INDIGO
    if colour == COLOUR_VIOLET:
        return COLOUR_DARK_VIOLET
    if colour == COLOUR_WHITE:
        return COLOUR_WHITE_MID
