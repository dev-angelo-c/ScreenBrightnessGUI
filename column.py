import tkinter as tk

def increase_brightness():
    # Add code to increase brightness
    pass

def decrease_brightness():
    # Add code to decrease brightness
    pass

def increase_volume():
    # Add code to increase volume
    pass

def decrease_volume():
    # Add code to decrease volume
    pass

def mute():
    # Add code to mute
    pass

root = tk.Tk()
root.title("Control Panel")

# Create a frame with yellow background
frame = tk.Frame(root, width=60, height=200, bg="yellow")
frame.pack()

# Create buttons
btn_brightness_increase = tk.Button(frame, text="B+", command=increase_brightness)
btn_brightness_increase.pack(fill=tk.X)

btn_brightness_decrease = tk.Button(frame, text="B-", command=decrease_brightness)
btn_brightness_decrease.pack(fill=tk.X)

btn_volume_increase = tk.Button(frame, text="V+", command=increase_volume)
btn_volume_increase.pack(fill=tk.X)

btn_volume_decrease = tk.Button(frame, text="V-", command=decrease_volume)
btn_volume_decrease.pack(fill=tk.X)

btn_mute = tk.Button(frame, text="Mute", command=mute)
btn_mute.pack(fill=tk.X)

root.mainloop()