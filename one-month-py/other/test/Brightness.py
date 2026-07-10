"""
Управление яркостью ноутбука с анимированным OSD в правом верхнем углу.
  Alt + P — увеличить на 5%
  Alt + N — уменьшить на 5%
  Ctrl+Shift+Q — выход
"""

import tkinter as tk
import keyboard
import screen_brightness_control as sbc

# ---------- Настройки ----------
MARGIN = 20                # отступ от края экрана
FADE_IN_STEP = 0.08        # шаг увеличения прозрачности
FADE_IN_INTERVAL = 15      # мс между шагами fade-in
FADE_OUT_STEP = 0.08       # шаг уменьшения прозрачности
FADE_OUT_INTERVAL = 15     # мс между шагами fade-out
DISPLAY_TIME = 1200        # сколько мс показывать окно перед скрытием

# ---------- Глобальные переменные ----------
root = None
osd_window = None
osd_label = None
hide_timer = None
fade_after_id = None
is_fading_out = False


def schedule_show_osd(brightness: float):
    """Поставить показ OSD в очередь главного потока."""
    if root:
        root.after(0, show_osd, brightness)


def show_osd(brightness: float):
    """Показать или обновить OSD. Вызывается только в главном потоке."""
    global osd_window, osd_label, hide_timer, fade_after_id, is_fading_out

    # Если уже выезжаем (fade-out) – отменяем скрытие и возвращаем окно
    if is_fading_out and osd_window and osd_window.winfo_exists():
        # Останавливаем fade-out
        if fade_after_id:
            root.after_cancel(fade_after_id)
            fade_after_id = None
        # Возвращаем видимость до целевой прозрачности
        osd_window.attributes('-alpha', 0.85)
        is_fading_out = False

    # Если окно уже существует – просто обновляем текст и сбрасываем таймер автоскрытия
    if osd_window is not None and osd_window.winfo_exists():
        osd_label.config(text=f"Яркость: {int(brightness)}%")
        if hide_timer is not None:
            root.after_cancel(hide_timer)
        hide_timer = root.after(DISPLAY_TIME, start_fade_out)
        return

    # Создаём новое окно OSD
    osd_window = tk.Toplevel()
    osd_window.overrideredirect(True)
    osd_window.attributes('-topmost', True)
    osd_window.attributes('-alpha', 0.0)  # начинаем полностью прозрачным
    osd_window.configure(bg='black')

    osd_label = tk.Label(
        osd_window,
        text=f"Яркость: {int(brightness)}%",
        font=("Segoe UI", 20, "bold"),
        fg="white",
        bg="black",
        padx=15,
        pady=8,
    )
    osd_label.pack()

    # Определяем размеры и позиционируем в правом верхнем углу
    osd_window.update_idletasks()
    w = osd_window.winfo_width()
    h = osd_window.winfo_height()
    sw = osd_window.winfo_screenwidth()
    x = sw - w - MARGIN
    y = MARGIN
    osd_window.geometry(f"+{x}+{y}")

    # Запускаем fade-in анимацию
    fade_in(0.0)

    # Планируем автоматическое скрытие
    hide_timer = root.after(DISPLAY_TIME, start_fade_out)


def fade_in(current_alpha: float):
    """Рекурсивно увеличиваем прозрачность до 0.85."""
    if not osd_window or not osd_window.winfo_exists():
        return
    new_alpha = min(current_alpha + FADE_IN_STEP, 0.85)
    osd_window.attributes('-alpha', new_alpha)
    if new_alpha < 0.85:
        # Продолжаем анимацию
        global fade_after_id
        fade_after_id = root.after(FADE_IN_INTERVAL, fade_in, new_alpha)
    else:
        fade_after_id = None


def start_fade_out():
    """Запускает плавное исчезновение окна."""
    global is_fading_out, hide_timer
    if is_fading_out:
        return
    if not osd_window or not osd_window.winfo_exists():
        return
    is_fading_out = True
    if hide_timer:
        root.after_cancel(hide_timer)
        hide_timer = None
    fade_out(0.85)


def fade_out(current_alpha: float):
    """Рекурсивно уменьшаем прозрачность до 0, затем уничтожаем окно."""
    global osd_window, osd_label, fade_after_id, is_fading_out
    if not osd_window or not osd_window.winfo_exists():
        is_fading_out = False
        return
    new_alpha = max(current_alpha - FADE_OUT_STEP, 0.0)
    osd_window.attributes('-alpha', new_alpha)
    if new_alpha > 0.0:
        fade_after_id = root.after(FADE_OUT_INTERVAL, fade_out, new_alpha)
    else:
        # Анимация завершена, убираем окно
        osd_window.destroy()
        osd_window = None
        osd_label = None
        fade_after_id = None
        is_fading_out = False


# ---------- Управление яркостью ----------
def change_brightness(delta: int):
    """Изменить яркость на delta % ( +5 или -5 )."""
    try:
        current = sbc.get_brightness(display=0)
        if isinstance(current, list):
            current = current[0]
        new_value = max(0, min(100, current + delta))
        sbc.set_brightness(new_value, display=0)
        schedule_show_osd(float(new_value))
    except Exception as e:
        print(f"Ошибка управления яркостью: {e}")
        schedule_show_osd(current if 'current' in locals() else 0.0)


def on_increase():
    change_brightness(5)


def on_decrease():
    change_brightness(-5)


# ---------- Главный блок ----------
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    root.title("Brightness Control")

    # Регистрируем горячие клавиши
    keyboard.add_hotkey("alt+p", on_increase)
    keyboard.add_hotkey("alt+n", on_decrease)
    keyboard.add_hotkey("ctrl+shift+q", lambda: root.quit())

    print("Скрипт запущен. Alt+P / Alt+N — яркость, Ctrl+Shift+Q — выход.")
    root.mainloop()
    print("Скрипт остановлен.")