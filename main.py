import random
import tkinter as tk
from tkinter import ttk


def play_game(root: tk.Tk, word_list: list[str], check_guess=None) -> None:
    target_word = random.choice(word_list)
    max_attempts = 6
    attempts = 0

    main_frame = tk.Frame(root, background='#075275', padx=20, pady=20)
    main_frame.grid(row=0, column=0, sticky='nsew')

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    instructions = tk.Label(main_frame, text="Welcome to Wordle! Guess the 5-letter word.", font=("Arial", 14), background='#075275', foreground='#ffffff')
    instructions.grid(row=0, column=0, columnspan=5, pady=10)

    labels = []
    for row in range(max_attempts):
        row_labels = []
        for col in range(5):
            label = ttk.Label(main_frame, width=2, anchor='center', font=("Arial", 16), relief="solid")
            label.grid(row=row + 1, column=col, padx=5, pady=5)
            row_labels.append(label)
        labels.append(row_labels)

    feedback_label = tk.Label(main_frame, text="", font=("Arial", 12), background='#075275', foreground='#ffffff')
    feedback_label.grid(row=max_attempts + 1, column=0, columnspan=5, pady=10)

    guess_entry = ttk.Entry(main_frame, font=("Arial", 16))
    guess_entry.grid(row=max_attempts + 2, column=0, columnspan=3, padx=5, pady=10)

    root.bind("<Return>", lambda event: check_guess())


    def check_guess():
        nonlocal attempts

        guess = guess_entry.get().strip().lower()
        if len(guess) != 5:
            feedback_label.config(text="Please enter a valid 5-letter word.")
            return

        for col, char in enumerate(guess):
            labels[attempts][col].config(text=char)
            if char == target_word[col]:
                labels[attempts][col].config(background="green")
            elif char in target_word:
                labels[attempts][col].config(background="yellow")
            else:
                labels[attempts][col].config(background="gray")

        attempts += 1

        if guess == target_word:
            feedback_label.config(text="Congratulations! You guessed the word!", foreground="green")
            guess_button.config(state="disabled")
            return
        elif attempts == max_attempts:
            feedback_label.config(text=f"Game over! The word was '{target_word}'.", foreground="red")
            guess_button.config(state="disabled")
            return

        guess_entry.delete(0, tk.END)
        feedback_label.config(text=f"Attempts remaining: {max_attempts - attempts}")

    guess_button = ttk.Button(main_frame, text="Submit Guess", command=check_guess)
    guess_button.grid(row=max_attempts + 2, column=3, padx=5, pady=10)

    def restart_game():
        nonlocal attempts, target_word
        attempts = 0
        target_word = random.choice(word_list)
        feedback_label.config(text="Game restarted! Guess the word.", foreground="black")
        guess_button.config(state="normal")

        for label in labels:
            for entry in label:
                entry.config(text="")
                entry.config(background="white")

        guess_entry.delete(0, tk.END)

    restart_button = ttk.Button(main_frame, text="Restart Game", command=restart_game)
    restart_button.grid(row=max_attempts + 2, column=4, padx=5, pady=10)

    feedback_label.config(text=f"Attempts remaining: {max_attempts}")


def main() -> None:
    word_list = [
        "apple", "grape", "mango", "peach", "lemon", "berry", "charm", "brave", "dance",
        "flame", "smile", "trust", "cloud", "daisy", "light", "shore", "stone", "world"
    ]

    root = tk.Tk()
    root.title("Wordle Game")
    root.geometry("500x450")
    root.configure(background='#000000')

    play_game(root, word_list)

    root.mainloop()


if __name__ == '__main__':
    main()
