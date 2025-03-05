import tkinter as tk
import random
from unittest import result

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
    guess = "".join(entry.get().upper() for entry in entry_fields)
    
    if len(guess) != WORD_LENGTH:
        return  # Проверяем, чтобы длина была правильная
    
    # Проверяем буквы
    feedback = ["gray"] * WORD_LENGTH  # Серый по умолчанию
    for i in range(WORD_LENGTH):
        if guess[i] == TARGET_WORD[i]:
            feedback[i] = "green"
        elif guess[i] in TARGET_WORD:
            feedback[i] = "yellow"
    
    for i in range(WORD_LENGTH):
        entry_fields[i].config(bg=feedback[i], fg="white")
    
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
    for entry in entry_fields:
        entry.delete(0, tk.END)
        entry.config(bg="white", fg="black")


root = tk.Tk()
root.title("Wordle")
root.geometry("400x350")


entry_fields = []
for i in range(WORD_LENGTH):
    entry = tk.Entry(root, font=("Arial", 18), width=2, justify='center')
    entry.grid(row=0, column=i, padx=5, pady=10)
    entry_fields.append(entry)

submit_button=tk.Button(root,text="Проверить", font=("Arial",14)command=check_word)
submit_button.grid(row=1, columnspan=WORD_LENGTH, pady=10)

result_button=tk.Button(root,text="Ресультат", font=("Arial",14)command=check_word)
result_button.grid(row=2, columnspan=WORD_LENGTH, pady=10)

result_label=tk.Button(root,text="",font=("Arial",14)command=check_word)
result_label.grid(row=3, columnspan=WORD_LENGTH)

root.mainloop()