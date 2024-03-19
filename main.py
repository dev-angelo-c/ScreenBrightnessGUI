import tkinter as tk
import ctypes

class BrightnessAdjuster:
    def __init__(self, master):
        self.master = master
        master.title("Screen Brightness Control")

        self.label = tk.Label(master, text="Adjust Screen Brightness")
        self.label.pack()

        self.scale = tk.Scale(master, from_=0, to=100, orient=tk.HORIZONTAL, command=self.update_brightness)
        self.scale.set(100)  # Set initial brightness to maximum
        self.scale.pack()

    def update_brightness(self, brightness):
        try:
            brightness = int(brightness)
            self.set_brightness(brightness)
        except ValueError:
            pass  # Ignore non-integer input

    def set_brightness(self, brightness):
        # Clamp brightness value between 0 and 100
        brightness = max(0, min(brightness, 100))

        # Load the dxva2.dll library
        dxva2 = ctypes.windll.LoadLibrary("dxva2.dll")

        # Call the SetMonitorBrightness function
        result = dxva2.SetMonitorBrightness(0, brightness)
        if result == 0:
            print("Brightness adjusted successfully.")
        else:
            print("Failed to adjust brightness.")

root = tk.Tk()
brightness_adjuster = BrightnessAdjuster(root)
root.mainloop()
