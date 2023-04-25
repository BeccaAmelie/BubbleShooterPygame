from adafruit_circuitplayground import cp
import time

class SensorLightDisplay:
    __pixels_off_state = [0, 0, 0]
    __acceleration_peak = 9.81
    __neopixels_amount = len(cp.pixels)

    def __init__(self, brightness):
        cp.pixels.brightness = brightness
        cp.pixels.auto_write = False

    def advanced_control_feedback(self, acceleration_x):
        if acceleration_x <= SensorLightDisplay.__acceleration_peak and SensorLightDisplay.__acceleration_peak >= -SensorLightDisplay.__acceleration_peak:
            if acceleration_x > 3 or acceleration_x<-3:
                factor= 255/SensorLightDisplay.__acceleration_peak
                flipped_acceleration = acceleration_x
                if acceleration_x <0:
                    flipped_acceleration *=-1
            if acceleration_x > 3:
                purple = [flipped_acceleration*factor, 0, 255-(flipped_acceleration*factor)]
                first_neopixel_location = int(SensorLightDisplay.__neopixels_amount//4)
                mapping_value = int(acceleration_x * SensorLightDisplay.__neopixels_amount//4 / SensorLightDisplay.__acceleration_peak)
                print(mapping_value)
                last_neopixel_location_a = first_neopixel_location + mapping_value
                last_neopixel_location_b = first_neopixel_location - mapping_value
                for pixel in range(first_neopixel_location, SensorLightDisplay.__neopixels_amount//2):
                    if pixel <= last_neopixel_location_a and pixel >=last_neopixel_location_b:
                        cp.pixels[((SensorLightDisplay.__neopixels_amount//2)-1)-pixel] = purple
                        cp.pixels[pixel] = purple
                        cp.pixels.show()
                    else:
                        cp.pixels[((SensorLightDisplay.__neopixels_amount//2)-1)-pixel] = SensorLightDisplay.__pixels_off_state
                        cp.pixels[pixel] = SensorLightDisplay.__pixels_off_state
                        cp.pixels.show()
            elif acceleration_x< -3:
                purple = [255-(flipped_acceleration*factor), 0, flipped_acceleration*factor]
                first_neopixel_location = int(SensorLightDisplay.__neopixels_amount*(3/4))
                mapping_value = int(acceleration_x * SensorLightDisplay.__neopixels_amount//4 / SensorLightDisplay.__acceleration_peak)*-1
                print(mapping_value)
                last_neopixel_location_a = first_neopixel_location + mapping_value
                last_neopixel_location_b = first_neopixel_location - mapping_value
                for pixel in range(first_neopixel_location, SensorLightDisplay.__neopixels_amount):
                    if pixel <= last_neopixel_location_a and pixel >=last_neopixel_location_b:
                        cp.pixels[pixel] = purple
                        cp.pixels[first_neopixel_location*2-pixel] = purple
                        cp.pixels.show()
                    else:
                        cp.pixels[pixel] = SensorLightDisplay.__pixels_off_state
                        cp.pixels[first_neopixel_location*2-pixel] = SensorLightDisplay.__pixels_off_state
                        cp.pixels.show()

            else:
                cp.pixels.fill(SensorLightDisplay.__pixels_off_state)
                cp.pixels.show()





