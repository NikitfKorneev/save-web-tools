import random
import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip

class PasswordGenerator:
    def __init__(self):
        self.canvas_width = 900
        self.canvas_height = 700
        
        self.setup_window()
        self.setup_variables()
        self.create_widgets()
        
    def setup_window(self):
        """Настройка главного окна"""
        self.window = tk.Tk()
        self.window.title("Генератор паролей - Создавайте надежные пароли")
        self.window.resizable(False, False)
        
        # Центрирование окна
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width - self.canvas_width) // 2
        y = (screen_height - self.canvas_height) // 2
        self.window.geometry(f"{self.canvas_width}x{self.canvas_height}+{x}+{y}")
        
        self.canvas = tk.Canvas(
            self.window, 
            width=self.canvas_width, 
            height=self.canvas_height, 
            bg="#f0f8ff"
        )
        self.canvas.pack()
        
    def setup_variables(self):
        """Инициализация переменных"""
        self.character_sets = {
            'digits': ("Цифры 0-9", "0123456789", "🔢"),
            'lowercase': ("Буквы a-z", "abcdefghijklmnopqrstuvwxyz", "📝"),
            'uppercase': ("Буквы A-Z", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "🔠"),
            'symbols1': ("Символы $@&?", "$@&?", "⚡"),
            'symbols2': ("Символы +-*/", "+-*/", "➕"),
            'symbols3': ("Символы %=№!", "%=!№", "⚠️"),
            'symbols4': ("Символы _^,.", "_^,.", "🔧")
        }
        
        self.checkbox_vars = {}
        for key in self.character_sets:
            self.checkbox_vars[key] = tk.BooleanVar(value=True)
        
        self.length_var = tk.StringVar(value="16")
        self.password_strength = tk.StringVar(value="Оцените сложность")
        self.generated_password = tk.StringVar(value="Ваш пароль появится здесь")
        
    def create_widgets(self):
        """Создание всех элементов интерфейса"""
        self.create_header()
        self.create_length_section()
        self.create_character_section()
        self.create_password_display()
        self.create_strength_indicator()  # Перемещено выше create_actions_section
        self.create_actions_section()
        
    def create_header(self):
        """Создание шапки приложения"""
        # Главный заголовок
        title_frame = tk.Frame(self.canvas, bg="#2c3e50", height=120)
        title_frame.place(x=0, y=0, width=self.canvas_width)
        
        tk.Label(
            title_frame, 
            text="🔐 Генератор Паролей", 
            bg="#2c3e50", 
            fg="white", 
            font=("Arial", 28, "bold")
        ).pack(pady=20)
        
        tk.Label(
            title_frame, 
            text="Создавайте безопасные и надежные пароли за секунды", 
            bg="#2c3e50", 
            fg="#ecf0f1", 
            font=("Arial", 12)
        ).pack()
        
    def create_length_section(self):
        """Секция настройки длины пароля"""
        section_frame = tk.Frame(self.canvas, bg="white", relief="ridge", bd=1)
        section_frame.place(x=50, y=150, width=800, height=100)
        
        tk.Label(
            section_frame,
            text="📏 Длина пароля:",
            bg="white",
            fg="#2c3e50",
            font=("Arial", 14, "bold")
        ).place(x=20, y=15)
        
        # Отображение текущей длины
        self.length_display = tk.Label(
            section_frame,
            textvariable=self.length_var,
            bg="#3498db",
            fg="white",
            font=("Arial", 16, "bold"),
            width=3,
            relief="raised"
        )
        self.length_display.place(x=700, y=15)
        
        # Слайдер для длины пароля
        self.length_scale = ttk.Scale(
            section_frame,
            from_=8,
            to=32,
            orient="horizontal",
            length=600,
            command=self.on_scale_change
        )
        self.length_scale.set(16)
        self.length_scale.place(x=100, y=50)
        
        # Подписи минимальной и максимальной длины
        tk.Label(section_frame, text="8", bg="white", fg="#7f8c8d").place(x=100, y=70)
        tk.Label(section_frame, text="32", bg="white", fg="#7f8c8d").place(x=680, y=70)
        
    def create_character_section(self):
        """Секция выбора типов символов"""
        section_frame = tk.Frame(self.canvas, bg="white", relief="ridge", bd=1)
        section_frame.place(x=50, y=270, width=800, height=150)
        
        tk.Label(
            section_frame,
            text="🎛️ Выберите типы символов:",
            bg="white",
            fg="#2c3e50",
            font=("Arial", 14, "bold")
        ).place(x=20, y=15)
        
        # Создание чекбоксов в две строки
        positions_row1 = [(50, 50), (250, 50), (450, 50), (650, 50)]
        positions_row2 = [(150, 100), (350, 100), (550, 100)]
        
        keys = list(self.character_sets.keys())
        
        for i, key in enumerate(keys[:4]):
            x, y = positions_row1[i]
            self.create_fancy_checkbox(section_frame, key, x, y)
            
        for i, key in enumerate(keys[4:]):
            x, y = positions_row2[i]
            self.create_fancy_checkbox(section_frame, key, x, y)
            
    def create_fancy_checkbox(self, parent, key, x, y):
        """Создание стилизованного чекбокса"""
        label, chars, emoji = self.character_sets[key]
        
        # Кастомный чекбокс с эмодзи
        def toggle_checkbox():
            current = self.checkbox_vars[key].get()
            self.checkbox_vars[key].set(not current)
            self.update_checkbox_display(key)
            self.update_strength()
        
        # Фрейм для чекбокса
        checkbox_frame = tk.Frame(parent, bg="white")
        checkbox_frame.place(x=x, y=y)
        
        # Индикатор состояния
        self.checkbox_indicator = tk.Label(
            checkbox_frame,
            text="✓" if self.checkbox_vars[key].get() else "☐",
            bg="white",
            fg="#27ae60" if self.checkbox_vars[key].get() else "#95a5a6",
            font=("Arial", 16),
            cursor="hand2"
        )
        self.checkbox_indicator.pack(side=tk.LEFT)
        self.checkbox_indicator.bind("<Button-1>", lambda e: toggle_checkbox())
        
        # Текст с эмодзи
        checkbox_label = tk.Label(
            checkbox_frame,
            text=f"{emoji} {label}",
            bg="white",
            fg="#2c3e50",
            font=("Arial", 11),
            cursor="hand2"
        )
        checkbox_label.pack(side=tk.LEFT, padx=5)
        checkbox_label.bind("<Button-1>", lambda e: toggle_checkbox())
        
        # Сохраняем ссылку на индикатор для обновления
        if not hasattr(self, 'checkbox_indicators'):
            self.checkbox_indicators = {}
        self.checkbox_indicators[key] = self.checkbox_indicator
        
    def update_checkbox_display(self, key):
        """Обновление отображения конкретного чекбокса"""
        if hasattr(self, 'checkbox_indicators') and key in self.checkbox_indicators:
            indicator = self.checkbox_indicators[key]
            if self.checkbox_vars[key].get():
                indicator.config(text="✓", fg="#27ae60")
            else:
                indicator.config(text="☐", fg="#95a5a6")
        
    def create_password_display(self):
        """Секция отображения сгенерированного пароля"""
        section_frame = tk.Frame(self.canvas, bg="#ecf0f1", relief="ridge", bd=1)
        section_frame.place(x=50, y=440, width=800, height=80)
        
        tk.Label(
            section_frame,
            text="🎯 Ваш пароль:",
            bg="#ecf0f1",
            fg="#2c3e50",
            font=("Arial", 12, "bold")
        ).place(x=20, y=10)
        
        # Поле для отображения пароля
        self.password_display = tk.Entry(
            section_frame,
            textvariable=self.generated_password,
            font=("Consolas", 16, "bold"),
            justify="center",
            state="readonly",
            relief="solid",
            bd=2,
            bg="#2c3e50",
            fg="#ecf0f1",
            readonlybackground="#2c3e50"
        )
        self.password_display.place(x=20, y=40, width=760, height=35)
        
    def create_strength_indicator(self):
        """Индикатор сложности пароля"""
        section_frame = tk.Frame(self.canvas, bg="white", relief="ridge", bd=1)
        section_frame.place(x=50, y=540, width=800, height=80)
        
        tk.Label(
            section_frame,
            text="📊 Сложность пароля:",
            bg="white",
            fg="#2c3e50",
            font=("Arial", 11, "bold")
        ).place(x=20, y=10)
        
        self.strength_label = tk.Label(
            section_frame,
            textvariable=self.password_strength,
            bg="white",
            font=("Arial", 11, "bold"),
            width=15
        )
        self.strength_label.place(x=180, y=10)
        
        # Индикатор прогресса - теперь создается до использования
        self.strength_progress = ttk.Progressbar(
            section_frame,
            orient="horizontal",
            length=400,
            mode="determinate"
        )
        self.strength_progress.place(x=320, y=15)
        
        # Инициализируем начальное значение
        self.update_strength()
        
    def create_actions_section(self):
        """Секция кнопок действий"""
        section_frame = tk.Frame(self.canvas, bg="white", relief="ridge", bd=1)
        section_frame.place(x=50, y=640, width=800, height=50)
        
        # Кнопка генерации
        generate_btn = tk.Button(
            section_frame,
            text="🔄 Сгенерировать пароль",
            command=self.generate_password,
            bg="#27ae60",
            fg="white",
            font=("Arial", 12, "bold"),
            width=20,
            height=1,
            cursor="hand2",
            relief="raised",
            bd=3
        )
        generate_btn.place(x=50, y=10)
        
        # Кнопка копирования
        copy_btn = tk.Button(
            section_frame,
            text="📋 Копировать",
            command=self.copy_to_clipboard,
            bg="#3498db",
            fg="white",
            font=("Arial", 12, "bold"),
            width=15,
            height=1,
            cursor="hand2",
            relief="raised",
            bd=3
        )
        copy_btn.place(x=300, y=10)
        
        # Кнопка очистки
        clear_btn = tk.Button(
            section_frame,
            text="🗑️ Очистить",
            command=self.clear_password,
            bg="#e74c3c",
            fg="white",
            font=("Arial", 12, "bold"),
            width=15,
            height=1,
            cursor="hand2",
            relief="raised",
            bd=3
        )
        clear_btn.place(x=500, y=10)
        
    def on_scale_change(self, value):
        """Обработчик изменения слайдера"""
        length = int(float(value))
        self.length_var.set(str(length))
        self.update_strength()
        
    def validate_length(self, value):
        """Валидация ввода длины пароля"""
        if value == "":
            return True
        try:
            length = int(value)
            if 8 <= length <= 32:
                self.length_scale.set(length)
                self.update_strength()
                return True
            return False
        except ValueError:
            return False
    
    def generate_password(self):
        """Генерация пароля"""
        try:
            length = int(self.length_var.get())
            if length < 8 or length > 32:
                messagebox.showerror("Ошибка", "Длина пароля должна быть от 8 до 32 символов")
                return
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректную длину пароля")
            return

        # Сбор выбранных наборов символов
        all_chars = ""
        enabled_sets = []
        for key, (_, chars, _) in self.character_sets.items():
            if self.checkbox_vars[key].get():
                all_chars += chars
                enabled_sets.append(chars)
        
        if not all_chars:
            messagebox.showerror("Ошибка", "Выберите хотя бы один тип символов")
            return
        
        # Гарантируем, что пароль содержит хотя бы по одному символу из каждого выбранного набора
        password_chars = []
        for chars in enabled_sets:
            password_chars.append(random.choice(chars))
        
        # Добираем остальные символы
        remaining_length = length - len(password_chars)
        if remaining_length > 0:
            password_chars.extend(random.choices(all_chars, k=remaining_length))
        
        # Перемешиваем символы
        random.shuffle(password_chars)
        password = ''.join(password_chars)
        
        # Вывод результата
        self.generated_password.set(password)
        self.update_strength()
        
        # Показываем подсказку о успешной генерации
        self.show_tooltip("Пароль успешно сгенерирован!")
    
    def show_tooltip(self, message):
        """Показать всплывающую подсказку"""
        tooltip = tk.Toplevel(self.window)
        tooltip.wm_overrideredirect(True)
        tooltip.wm_geometry("+%d+%d" % (self.window.winfo_rootx()+400, self.window.winfo_rooty()+300))
        
        label = tk.Label(tooltip, text=message, background="#ffffe0", relief="solid", borderwidth=1)
        label.pack()
        
        # Автоматическое закрытие подсказки
        self.window.after(2000, tooltip.destroy)
    
    def update_strength(self):
        """Обновление индикатора сложности пароля"""
        try:
            length = int(self.length_var.get())
        except:
            length = 0
            
        # Подсчитываем количество выбранных наборов символов
        char_sets_count = sum(1 for var in self.checkbox_vars.values() if var.get())
        
        # Вычисляем сложность на основе длины и разнообразия символов
        strength_score = length * 2 + char_sets_count * 10
        
        if strength_score < 40:
            strength = "Очень слабый"
            progress = 20
            color = "#e74c3c"
        elif strength_score < 60:
            strength = "Слабый"
            progress = 40
            color = "#e67e22"
        elif strength_score < 80:
            strength = "Средний"
            progress = 60
            color = "#f1c40f"
        elif strength_score < 100:
            strength = "Хороший"
            progress = 80
            color = "#2ecc71"
        else:
            strength = "Отличный"
            progress = 100
            color = "#27ae60"
            
        self.password_strength.set(strength)
        if hasattr(self, 'strength_progress'):
            self.strength_progress['value'] = progress
        if hasattr(self, 'strength_label'):
            self.strength_label.config(fg=color)
    
    def copy_to_clipboard(self):
        """Копирование пароля в буфер обмена"""
        password = self.generated_password.get()
        if password and password != "Ваш пароль появится здесь":
            pyperclip.copy(password)
            self.show_tooltip("Пароль скопирован в буфер обмена! ✅")
        else:
            messagebox.showwarning("Внимание", "Сначала сгенерируйте пароль")
    
    def clear_password(self):
        """Очистка поля пароля"""
        self.generated_password.set("Ваш пароль появится здесь")
        self.password_strength.set("Оцените сложность")
        if hasattr(self, 'strength_progress'):
            self.strength_progress['value'] = 0
        if hasattr(self, 'strength_label'):
            self.strength_label.config(fg="#7f8c8d")
    
    def run(self):
        """Запуск приложения"""
        # Настройка стилей
        style = ttk.Style()
        style.theme_use('clam')
        
        # Кастомные стили для прогресс-бара
        style.configure("TProgressbar", thickness=20)
        
        self.window.mainloop()


# Запуск приложения
if __name__ == "__main__":
    try:
        app = PasswordGenerator()
        app.run()
    except ImportError:
        print("Для работы приложения требуется библиотека pyperclip")
        print("Установите её: pip install pyperclip")