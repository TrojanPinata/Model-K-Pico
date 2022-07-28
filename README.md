# Model K Pico
This is the repository for a custom 75% keyboard designed to be a fusion of the [Cannonkeys Satisfaction75](https://cannonkeys.com/products/gb-satisfaction-75-keyboard-round-2), [CFTKB Mysterium](https://github.com/coseyfannitutti/mysterium), and [Envious Data Delirium](https://github.com/Envious-Data/Env-KB). I've designed around the ATmega32A and similar AVR controllers, and I really wanted to try working with the RP2040 as it comes fully prepackaged and works with [KMK](https://github.com/KMKfw/kmk_firmware) or  [QMK](https://github.com/qmk/qmk_firmware/tree/develop) (with the develop branch *kinda*). The original things that led me to do this were my desire to have the 75% form factor, exposed PCB, rotary encoder for audio, and I2C OLED display all in the same package. My goal was to combine all of these things together while still keeping it reasonable for a layman to make themself. 

I think it has come out pretty decent minus some cracks in the switchplate (because 1.5mm acrylic is really thin) and a misplaced screw hole. I couldnt find M2 screws short notice either so I ended up drilling out the holes to be larger (which was a mistake and I would not do again). I think it looks good, it sounds good, and most of all it works. The only thing I need is some pads to keep  it from slipping :).

If you plan on making this yourself I will try and make a guide in the future, but that might take a bit. I recommend [Ponoko](https://www.ponoko.com/) for the acrylic and [JLCPCB](https://jlcpcb.com/) for the PCB manufacturing. Everything else can be found in the BOM from either your local hardware store, [Keeb.io](https://keeb.io/) or [Divinikey](https://divinikey.com/). I chose to use some cheap keycaps and Gateron KS-9 2.0 Red switches and I like how everything feels. Anyway, if you have any questions start a issue or something B).

![final build](DOCS/IMAGES/moneyshot.JPG)

![top down](DOCS/IMAGES/topdown.JPG)

![rear](DOCS/IMAGES/rearreflection.JPG)

![pcb but 3d](https://i.imgur.com/Os8a2fJ.png)

![pcb 3d back](https://i.imgur.com/0yjpz0L.png)

![pcb in kicad](https://i.imgur.com/imwtyWo.png)
