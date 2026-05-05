tempo_voltas = []

print("--- Registro de Tempos: Stock Car ---")

for i in range(5):
    tempo = float(input(f"Digite o tempo da volta {i+1} (em segundos): "))
    tempo_voltas.append(tempo)

print(tempo_voltas[75])