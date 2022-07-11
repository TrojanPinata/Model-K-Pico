import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

class KMKKeyboard(_KMKKeyboard):
   col_pins = (
      board.GP2, 
      board.GP3, 
      board.GP4, 
      board.GP5, 
      board.GP6, 
      board.GP7, 
      board.GP8, 
      board.GP9, 
      board.GP10, 
      board.GP11, 
      board.GP12, 
      board.GP13, 
      board.GP14, 
      board.GP15, 
      board.GP16,
   )

   row_pins = (
      board.GP20, 
      board.GP21, 
      board.GP22, 
      board.GP26, 
      board.GP27, 
      board.GP28,
   )
   
   diode_orientation = DiodeOrientation.COL2ROW
   SCL = board.GP1
   SDA = board.GP0

   enc_pin0 = board.GP17
   enc_pin1 = board.GP19
