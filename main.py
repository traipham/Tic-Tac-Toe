import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import asyncio
import tkinter_page_router.router as router
import game

def main():
    root = router.Router()

    # Window setting
    root.title("Tic-Tac-Toe")
    window_width = 640 
    window_height = 480
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_width = int(screen_width/2 - window_width/2)
    center_height = int(screen_height/2 - window_height/2)
    root.geometry(f"{window_width}x{window_height}+{center_width}+{center_height}")

    # Initiate game
    root.append_new_page("Start")
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.columnconfigure(1, weight=1)
    tic_tac_toe_game = game.game(root.pages["Start"].game_frame, root.pages["Start"], root)
    # Run game
    root.mainloop()

if __name__ == "__main__":
    main()
