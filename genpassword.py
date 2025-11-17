import random
import tkinter as tk
from tkinter import ttk

class PasswordGenerator:
    def __init__(self):
        self.canvas_width = 750
        self.canvas_height = 500
        
        self.setup_window()
        self.setup_variables()
        self.create_widgets()
        
    def setup_window(self):
        """Настройка главного окна"""
        self.window = tk.Tk()
        self.window.title("Генератор паролей")
        
        self.canvas = tk.Canvas(
            self.window, 
            width=self.canvas_width, 
            height=self.canvas_height, 
            bg="grey11"
        )
        self.canvas.pack()
        
    def setup_variables(self):
        """Инициализация переменных"""
        self.character_sets = {
            'digits': ("0-9", ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]),
            'lowercase': ("a-z", list("abcdefghijklmnopqrstuvwxyz")),
            'uppercase': ("A-Z", list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")),
            'symbols1': ("$@&?", ["$", "@", "&", "?"]),
            'symbols2': ("+-*/", ["+", "-", "*", "/"]),
            'symbols3': ("%=№!", ["%", "=", "!", "№"]),
            'symbols4': ("_^,.", ["_", "^", ",", "."])
        }
        
        self.checkbox_vars = {}
        for key in self.character_sets:
            self.checkbox_vars[key] = tk.BooleanVar()
    
    def create_widgets(self):
        """Создание всех элементов интерфейса"""
        self.create_title()
        self.create_controls()
        self.create_checkboxes()
        
    def create_title(self):
        """Создание заголовка"""
        title_config = {
            "bg": "grey11", 
            "foreground": "white", 
            "font": ("Arial", 35, "bold")
        }
        
        tk.Label(self.canvas, text="Генератор", **title_config).place(x=270, y=30)
        tk.Label(self.canvas, text="Паролей", **title_config).place(x=287, y=100)
        
        # Фон для элементов управления
        self.canvas.create_rectangle(50, 450, 700, 180, fill="grey95")
    
    def create_controls(self):
        """Создание элементов управления"""
        # Поле для ввода длины пароля
        self.length_entry = tk.Entry(self.canvas, width=3, validate="key")
        self.length_entry['validatecommand'] = (self.length_entry.register(self.validate_length), '%P')
        self.length_entry.place(x=80, y=300)
        
        # Поле для вывода пароля
        self.password_entry = tk.Entry(
            self.canvas,
            width=50,
            justify=tk.RIGHT,
            font=("Arial", 15, "bold")
        )
        self.password_entry.place(x=100, y=250)
        
        # Кнопка генерации
        generate_btn = ttk.Button(
            self.canvas,
            text="Сгенерировать пароль",
            width=50,
            command=self.generate_password
        )
        generate_btn.place(x=200, y=300)
    
    def create_checkboxes(self):
        """Создание чекбоксов для выбора наборов символов"""
        x_positions = [60, 120, 180, 240, 305, 370, 435]
        
        for i, (key, (label, _)) in enumerate(self.character_sets.items()):
            checkbox = tk.Checkbutton(
                self.canvas,
                text=label,
                variable=self.checkbox_vars[key],
                offvalue=False,
                onvalue=True
            )
            checkbox.place(x=x_positions[i], y=350)
    
    def validate_length(self, value):
        """Валидация ввода длины пароля"""
        if value == "":
            return True
        try:
            length = int(value)
            return 1 <= length <= 40
        except ValueError:
            return False
    
    def generate_password(self):
        """Генерация пароля"""
        # Получение длины пароля
        try:
            length = int(self.length_entry.get())
            if length <= 0 or length > 40:
                self.show_error("Длина пароля должна быть от 1 до 40")
                return
        except ValueError:
            self.show_error("Введите корректную длину пароля")
            return


        # Сбор выбранных наборов символов
        all_chars = []
        for key, (_, chars) in self.character_sets.items():
            if self.checkbox_vars[key].get():
                all_chars.extend(chars)
        
        # Проверка, что выбран хотя бы один набор символов
        if not all_chars:
            self.show_error("Выберите хотя бы один набор символов")
            return
        
        # Генерация пароля
        password = ''.join(random.choices(all_chars, k=length))
        
        # Вывод результата
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)
    
    def show_error(self, message):
        """Показать сообщение об ошибке"""
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, message)
    
    def run(self):
        """Запуск приложения"""
        self.window.mainloop()


# Запуск приложения
if __name__ == "__main__":
    app = PasswordGenerator()
    app.run()
