import board

from kb import KMKKeyboard
from kmk.keys import KC
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.peg_oled_display import Oled,OledDisplayMode,OledReactionType,OledData

keyboard = KMKKeyboard()

keyboard.modules.append(Layers())
layers = Layers()
media_keys = MediaKeys()
encoder_handler = EncoderHandler()
encoder_handler.pins = ((keyboard.enc_pin0, keyboard.enc_pin1, None, False))

keyboard.modules = [layers, encoder_handler]

#keyboard.tap_time = 150

# OLED stuff - only one block should be uncommented at a time
#uncomment for text
oled_ext = Oled(
    OledData(
        corner_one={0:OledReactionType.STATIC,1:["Model K"]},
        corner_two={0:OledReactionType.LAYER,1:["Layer 1","Layer 2"]},
        corner_three={0:OledReactionType.STATIC,1:["V0.2"]},
        corner_four={0:OledReactionType.LAYER,1:["BASE","ALT"]}
        ),
        toDisplay=OledDisplayMode.TXT,flip=False)

#uncomment for image 
#oled_ext = Oled(OledData(image={0:OledReactionType.LAYER,1:["base.bmp","alt.bmp"]}),toDisplay=OledDisplayMode.IMG,flip=False)

keyboard.extensions.append(oled_ext)

nokey = KC.NO

keyboard.keymap = [
    [
    #Layer 0
        KC.ESC, nokey, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.MUTE,
        KC.GRAVE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINUS, KC.EQUAL, KC.BSPC, KC.DEL,
        KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.BSLS, KC.INS,
        KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, nokey, KC.ENT, KC.HOME,
        KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, nokey, KC.RSHIFT, KC.UP, KC.END,
        KC.LCTL, KC.LGUI, KC.LALT, nokey, nokey, nokey, KC.SPC, nokey, nokey, KC.RALT, KC.MO(1), KC.RCTRL, KC.LEFT, KC.DOWN, KC.RIGHT,
    ],
    [
    #Layer 1
        KC.TRNS, nokey, KC.F13, KC.F14, KC.F15, KC.F16, KC.F17, KC.F18, KC.F19, KC.F20, KC.F21, KC.F22, KC.F23, KC.F24, KC.MUTE,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.VOLU,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.VOLD,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, nokey, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,  nokey, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, nokey, nokey, nokey, KC.TRNS, nokey, nokey, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
    ],
]

encoder_handler.map = [
    ((KC.VOLD, KC.VOLU, KC.TRNS)),  # Layer 0
    ((KC.TRNS, KC.TRNS, KC.TRNS)),  # Layer 1
]

if __name__ == '__main__':
    keyboard.go()

