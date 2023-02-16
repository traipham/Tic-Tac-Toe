import tkinter as tk
from tkinter import *
from tkinter.ttk import *

import tkinter_page_router.router as router
import game

if __name__ == "__main__":
    root = router.Router()

    # Window setting
    root.title("Tic-Tac-Toe")
    window_width = 1080
    window_height = 720
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_width = int(screen_width/2 - window_width/2)
    center_height = int(screen_height/2 - window_height/2)
    root.geometry(f"{window_width}x{window_height}+{center_width}+{center_height}")

    # Initiate game
    root.append_new_page("Start")
    game.game(root.pages["Start"].game_frame, root.pages["Start"])

    # Run game
    root.mainloop()
