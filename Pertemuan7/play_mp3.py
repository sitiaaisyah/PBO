import tkinter as tk
from playsound import playsound

def play_sound():
    # Replace the file path with the path to your MP3 file
    mp3_file_path = "music.mp3"
    playsound(mp3_file_path, True)

# Create the main window
root = tk.Tk()
root.title("Sound Player App")

# Create a button that will play the sound when clicked
play_button = tk.Button(root, text="Play Sound", command=play_sound)
play_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()