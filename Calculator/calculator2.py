import tkinter as tk

# Настройки цвета и шрифта
BG_COLOR = "#202124"           # Тёмный фон
DISPLAY_COLOR = "#303134"      # Поле ввода
BTN_COLOR = "#3c4043"          # Кнопки
BTN_HOVER = "#5f6368"
BTN_TEXT = "#ffffff"
FONT_DISPLAY = ("Segoe UI", 32)
FONT_BUTTON = ("Segoe UI", 20)

# Главное окно
root = tk.Tk()
root.title("Pro Calculator")
root.geometry("360x580")
root.configure(bg=BG_COLOR)
root.resizable(False, False)

# Поле вывода
display = tk.Entry(root, font=FONT_DISPLAY, bg=DISPLAY_COLOR,
                   fg=BTN_TEXT, bd=0, justify="right", insertbackground=BTN_TEXT)
display.pack(fill="both", padx=10, pady=20, ipady=20)

# Обработка нажатий
def on_click(symbol):
    if symbol == "=":
        try:
            result = str(eval(display.get()))
            display.delete(0, tk.END)
            display.insert(tk.END, result)
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Ошибка")
    elif symbol == "C":
        display.delete(0, tk.END)
    elif symbol == "+/-":
        try:
            val = eval(display.get())
            display.delete(0, tk.END)
            display.insert(tk.END, str(-val))
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Ошибка")
    else:
        display.insert(tk.END, symbol)

# Создание кнопки
def create_button(parent, text, wide=False):
    btn = tk.Button(
        parent, text=text, font=FONT_BUTTON,
        bg=BTN_COLOR, fg=BTN_TEXT, activebackground=BTN_HOVER,
        bd=0, command=lambda: on_click(text)
    )
    if wide:
        btn.pack(side="left", expand=True, fill="both", padx=5, pady=5, ipadx=50)
    else:
        btn.pack(side="left", expand=True, fill="both", padx=5, pady=5)
    return btn

# Сетка кнопок
buttons = [
    ["C", "+/-", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "="]
]

# Отрисовка кнопок
for row in buttons:
    frame = tk.Frame(root, bg=BG_COLOR)
    frame.pack(expand=True, fill="both", padx=10)
    for i, char in enumerate(row):
        if char == "0":
            create_button(frame, char, wide=True)
        else:
            create_button(frame, char)

# Запуск
root.mainloop()
