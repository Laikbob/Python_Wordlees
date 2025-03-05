import tkinter as tk
import random

# Загружаем слова из файла
with open("words.txt", "r", encoding="utf-8") as f:
    words = [line.strip().upper() for line in f.readlines()]

# Выбираем случайное слово
TARGET_WORD = random.choice(words)
WORD_LENGTH = len(TARGET_WORD)
MAX_ATTEMPTS = 6
attempts = 0

def check_word():
    global attempts
    if attempts >= MAX_ATTEMPTS:
        return
    
    guess = "".join(entries[attempts][i].get().upper() for i in range(WORD_LENGTH))
    
    if len(guess) != WORD_LENGTH or "" in guess:
        return  # Проверяем, чтобы все клетки были заполнены
    
    feedback = ["gray"] * WORD_LENGTH  # Серый по умолчанию
    for i in range(WORD_LENGTH):
        if guess[i] == TARGET_WORD[i]:
            feedback[i] = "green"
        elif guess[i] in TARGET_WORD:
            feedback[i] = "yellow"
    
    for i in range(WORD_LENGTH):
        entries[attempts][i].config(bg=feedback[i], fg="white", state="disabled")
    
    attempts += 1
    if guess == TARGET_WORD or attempts >= MAX_ATTEMPTS:
        result_label.config(text=f"Правильное слово: {TARGET_WORD}", fg="red")
        submit_button.config(state=tk.DISABLED)

def reset_game():
    global TARGET_WORD, attempts
    TARGET_WORD = random.choice(words)
    attempts = 0
    result_label.config(text="")
    submit_button.config(state=tk.NORMAL)
    for row in entries:
        for entry in row:
            entry.delete(0, tk.END)
            entry.config(bg="white", fg="black", state="normal")
    entries[0][0].focus_set()

def limit_entry_length(event, row, col):
    entry = event.widget
    if len(entry.get()) > 1:
        entry.delete(1, tk.END)  # Удаляем лишние символы
    
    if entry.get():
        if col < WORD_LENGTH - 1:
            entries[row][col + 1].focus_set()
        elif col == WORD_LENGTH - 1:
            check_word()
            if attempts < MAX_ATTEMPTS:
                entries[attempts][0].focus_set()

root = tk.Tk()
root.title("Wordle")
root.geometry("400x400")

entries = []
for r in range(MAX_ATTEMPTS):
    row_entries = []
    for c in range(WORD_LENGTH):
        entry = tk.Entry(root, font=("Arial", 18), width=2, justify='center')
        entry.grid(row=r, column=c, padx=5, pady=2)
        entry.bind("<KeyRelease>", lambda e, row=r, col=c: limit_entry_length(e, row, col))
        row_entries.append(entry)
    entries.append(row_entries)

submit_button = tk.Button(root, text="Сбросить", font=("Arial", 14), command=reset_game)
submit_button.grid(row=MAX_ATTEMPTS, columnspan=WORD_LENGTH, pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.grid(row=MAX_ATTEMPTS + 1, columnspan=WORD_LENGTH)

entries[0][0].focus_set()

root.mainloop()
