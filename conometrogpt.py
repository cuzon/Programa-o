import tkinter as tk
import time


def start_timer():
    global start_time
    start_time = time.time()
    update_timer()

def update_timer():
    elapsed_time = time.time() - start_time
    timer_label.config(text=format_time(elapsed_time))
    timer_label.after(1000, update_timer)

def format_time(seconds):
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return '{:02d}:{:02d}'.format(minutes, seconds)

# Configuração da janela
window = tk.Tk()
window.title("Cronômetro")
window.geometry("200x150")

# Rótulos o cronômetro

timer_label = tk.Label(window, font=("Arial", 24))
timer_label.pack(pady=10)

# Botões para iniciar e parar o cronômetro
start_button = tk.Button(window, text="Iniciar", command=start_timer)
start_button.pack()


# Iniciar a janela principal
window.mainloop()