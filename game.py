import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font
from turtle import bgcolor, window_height
from typing import List
import random

from tkinter_page_router.router import Page

PLAYER_1_COLOR = "Blue"
PLAYER_2_COLOR = "Red"

class game():
    def __init__(self, master: tk.Frame, page: Page):
        self.master = master
        page.set_title("Tic-Tac-Toe")

        self.players = [('X', PLAYER_1_COLOR), ('O', PLAYER_2_COLOR)]
        self.user = random.choice(self.players)
        self._def_color = tk.Button(master)['background']

        s = ttk.Style(master)
        s.configure("board_frame.TFrame",highlightbackground="black", highlightthickness=5)
        # Initialize reset button, board frame, and player label
        self.frame = ttk.Frame(master=master, borderwidth=3, relief="groove")
        self.player_label = tk.Label(master=master, text=f"{self.user[0]} Turn", font=('consolas', 40), fg=self.user[1])
        self.reset_button = ttk.Button(master=master, text="restart", command= lambda: self.new_game(False))
        # Scaling config

        # Create board
        self.board = self.create_board()
        self.board_size = len(self.board)*len(self.board)
        self.win_count = self.board_size

        self.player_label.grid(row=2, column=0)
        self.reset_button.grid(row=3, column=0)
        self.frame.grid(row=4, column=0)

        pass

    def create_board(self, num_match: int = 3) -> List[List[tk.Button]]:
        """
        Create a 2D array of lists of buttons with num_match*num_match number of tiles
        :param num_match: The required number of matching tiles to win
        :return res_list: A 2D list of num_match of buttons
        """
        # s = ttk.Style()
        # s.configure('board_button.TButton', font=('consolas', 40))
        res_list=[[0 for i in range(num_match)] for j in range(num_match)]

        for i in range(num_match):
            # initiated board with buttons
            for j in range(num_match):
                res_list[i][j] = tk.Button(master=self.frame, text="", font=('consolas', 40), width=8,
                                            command=lambda row=i, column=j: self.next_turn(row, column))
                res_list[i][j].grid(row=i ,column=j, sticky="NSEW")
        return res_list

    def next_turn(self, row: int, column: int):
        """
        Actions to make during a turn. Frontend functionality and changing current player
        :param row: The current row index
        :param column: The current column index
        """
        # If empty and there's no winner, can click on button
        if self.board[row][column]['text'] == "" and self.check_winner() is False:
            self.board[row][column].config(text=self.user[0], fg=self.user[1])
            # self.board[row][column].config(state=DISABLED)
            self.win_count -= 1

            game_state = self.check_winner()
            # continue game
            if game_state is False:
                self.user = self.players[0 if self.players.index(self.user) else 1]
                self.player_label.config(text=f"{self.user[0]} Turn", fg=self.user[1])
            # If there's a winner change label
            elif game_state is True:
                self.player_label.config(text=f"{self.user[0]} Wins!", fg=self.user[1])
                self.open_winner_wind("WINNER")
            # If tie
            elif game_state == "TIE":
                self.win_count = self.board_size
                self.open_winner_wind("TIE")
                self.player_label.config(text="Tie!", fg="Black")

    def check_winner(self, num_match: int = 3):
        """
        Check if there's a current winner every turn.
        :param num_match: The required number of matching tiles to win
        :return: True, False, "Tie"
        """
        diagonal_vals_LR = [] # Get diagonal value of top left to bottom right
        diagonal_vals_RL = [] # Get diagonal value of top right to bottom left

        for row in range(num_match):
            diagonal_vals_LR.append(self.board[row][row]['text'])
            diagonal_vals_RL.append(self.board[row][num_match-1-row]['text'])
            button_row_vals = [self.board[row][col]['text'] for col in range(num_match)] # get row values
            button_col_vals = [self.board[col][row]['text'] for col in range(num_match)] # get column values
            # If winning in row
            if button_row_vals.count(self.user[0]) == num_match:
                for button in self.board[row]: 
                    button.config(background="#00FF00")
                return True
            # If winning in column
            elif button_col_vals.count(self.user[0]) == num_match:
                for i in range(num_match):
                    self.board[i][row].config(background="#00FF00")
                return True
            # If winning in diagonal left to right
            elif diagonal_vals_LR.count(self.user[0]) == num_match:
                for i in range(num_match):
                    self.board[i][i].config(background="#00FF00")
                return True
            # If winning in diagonal right to left
            elif diagonal_vals_RL.count(self.user[0]) == num_match:
                for i in range(num_match):
                    self.board[i][num_match-1-i].config(background="#00FF00")
                return True
        if self.win_count == 0:
            print("TIE!")
            return "TIE"
        return False

    def new_game(self, exit: bool):
        """Reset game board"""
        self.win_count = self.board_size
        self.user = random.choice(self.players)
        self.player_label.config(text=self.user[0]+" Turn", fg=self.user[1])
        # iterate through board and reset buttons
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                self.board[row][col].config(
                    text="", state=NORMAL, background=self._def_color, fg='black')

        if exit:
            self.winner_wind.destroy()

    def open_winner_wind(self, status: str):
        """
        Open separate window that displays a text of who won
        :param status: if there's a WINNER or a TIE
        """
        self.winner_wind = Toplevel(self.master)
        self.winner_wind.title("Winner!")

        self.winner_wind.wm_protocol("WM_DELETE_WINDOW", func= lambda x=True: self.new_game(x)) # run function when window is closed
        self.winner_wind.wm_transient(self.master)
        
        # center window 
        window_width = 200
        window_height = 200
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        center_width = int(screen_width/2 - window_width/2)
        center_height = int(screen_height/2 - window_height/2)
        self.winner_wind.geometry(f"{window_width}x{window_height}+{center_width}+{center_height}")

        # Set label of tie or winner
        lab_text = ""
        if status == "TIE":
            lab_text = status
        else:
            lab_text = f"{self.user[0]} WINS!"

        winner_label = tk.Label(self.winner_wind, text=lab_text)
        # confirm_but = tk.Button(winner_label, text="Confirm")
        winner_label.pack()
