import time

while True:
  # Obtém a hora atual em formato de tupla (hora, minuto, segundo)
  current_time = time.localtime()
  # Formata a hora atual como uma string HH:MM:SS
  current_time_str = time.strftime("%H:%M:%S", current_time)
  # Imprime a hora atual
  print(current_time_str)
  # Espera 1 segundo antes de atualizar novamente
  time.sleep(1)