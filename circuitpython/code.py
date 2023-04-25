from adafruit_circuitplayground import cp
from sensorlightdisplay import SensorLightDisplay
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

sensorlightdisplay_instance = SensorLightDisplay(0.1)
kbd = Keyboard(usb_hid.devices)
acceleration_peak = 9.81
black = [0,0,0]
while True:
    x,y,z = cp.acceleration
    if cp.switch:
        if x < 0:
            flipped_x = x*-1
        else:
            flipped_x = x
        if flipped_x <= acceleration_peak:
            sensorlightdisplay_instance.advanced_control_feedback(x)
            if x > 3:
                kbd.press(Keycode.RIGHT_ARROW)
                kbd.release(Keycode.LEFT_ARROW)
            elif x < -3:
                kbd.press(Keycode.LEFT_ARROW)
                kbd.release(Keycode.RIGHT_ARROW)
            else:
                kbd.release(Keycode.LEFT_ARROW)
                kbd.release(Keycode.RIGHT_ARROW)
        if cp.button_a or cp.button_b:
            kbd.send(Keycode.SPACE)
    else:
        kbd.release(Keycode.LEFT_ARROW)
        kbd.release(Keycode.RIGHT_ARROW)
        cp.pixels.fill(black)
        cp.pixels.show()
