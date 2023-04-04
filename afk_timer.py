import os
import sys
import tkinter as tk

import pygame

# total time in seconds of a full cycle of the timer
timer_duration = 240
# time in seconds left until a new cycle is started
remaining_time = 240


def play_sound():
    sound_label = sounds_var.get()
    sound_file = sound_file_label_mapping[sound_label]
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


def update_timer_duration():
    global timer_duration, remaining_time
    try:
        new_duration = int(timer_duration_var.get())
        # set total duration
        timer_duration = new_duration
        # reset timer
        remaining_time = timer_duration
    except ValueError:
        pass


def update_remaining_time():
    global remaining_time
    remaining_time -= 1
    time_label.config(text=f"Please move in: {remaining_time} s")
    if remaining_time == 0:
        play_sound()
        # reset timer
        remaining_time = timer_duration
    root.after(1000, update_remaining_time)


def get_file_path(filename: str) -> str:
    if getattr(sys, 'frozen', False):
        # Executable mode
        return os.path.join(sys._MEIPASS, filename)
    # Script mode
    return filename


# Build the main window
root = tk.Tk()
root.title("BG AFK Timer")
root.geometry("250x200")
root.iconbitmap(get_file_path('app_icon.ico'))

# Build timer duration input
timer_duration_var = tk.StringVar(root, value="240")
timer_duration_entry = tk.Entry(root, textvariable=timer_duration_var)
timer_duration_entry.pack(pady=10)

# Build "Update Timer" button
update_timer_button = tk.Button(root, text="Update Timer", command=update_timer_duration)
update_timer_button.pack(pady=10)

# init the timer with default value of 240s
update_timer_duration()

# Initialize pygame mixer
pygame.mixer.init()

# Build the label to display remaining time
time_label = tk.Label(root, text=f"Please move in: {remaining_time} s")
time_label.pack(pady=10)

# Build the dropdown menu for sound selection
sound_file_label_mapping = {
    'Sound 1': get_file_path('sound1.mp3'),
    'Sound 2': get_file_path('sound2.mp3'),
    'Sound 3': get_file_path('sound3.mp3'),
    'Sound 4': get_file_path('sound4.mp3'),
}
sounds_var = tk.StringVar(root)
# default sound
sounds_var.set('Sound 1')
sound_option_menu = tk.OptionMenu(root, sounds_var, *sound_file_label_mapping.keys())
sound_option_menu.pack(pady=10)

# Start updating the remaining time and playing the sound
root.after(1000, update_remaining_time)

# Run the main loop
root.mainloop()
