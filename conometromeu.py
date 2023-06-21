import tkinter as tk
import time

def update_clock():
    current_time = time.strftime('%H:%M:%S') # o comando strftime do módulo time serve para obter a hora atual formatada no formato de horas, minutos e segundos (%H:%M:%S)
    clock_label.config(text=current_time) # "clock_label" é o valor da variável "current_time", fazendo com q atualize o rótulo com a hora atual
    clock_label.after(1000, update_clock) # bota um temporizador para chamar o comando "update_clock" novamente após 1000 milissegundos (ou seja, 1 segundo", criando um loop infinito onde a função update_clock é chamada repetidamente a cada segundo, atualizando assim o relógio exibido.

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

# Rótulos para o relogio e o cronômetro
clock_label = tk.Label(window, font=("Arial", 24))
clock_label.pack(pady=10) # criam um rótulo com a fonte Arial de tamanho 24 e o exibem na janela principal com um espaço vertical de 10 pixels abaixo dele

timer_label = tk.Label(window, font=("Arial", 24))
timer_label.pack(pady=10)

# Botões para iniciar e parar o cronômetro
start_button = tk.Button(window, text="Iniciar", command=start_timer)
start_button.pack()

update_clock() # atualizar o relogio inicialmente

# Iniciar a janela principal
window.mainloop()