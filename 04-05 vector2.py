tempo_voltas = []

print("--- Registro de Tempos: Stock Car ---")

for i in range(5):
    tempo = float(input(f"Digite o tempo da volta {i+1} (em segundos): "))
    tempo_voltas.append(tempo)

melhor_tempo = min(tempo_voltas)

posicao_melhor = tempo_voltas.index(melhor_tempo) + 1

media_tempo = sum(tempo_voltas) / len(tempo_voltas)

print("\n --- Resultados --- ")
print(f"O melhor tempo foi de {melhor_tempo:.2f} segundos")
print(f"A sua melhor posição foi {posicao_melhor}")
print(f"A media das voltas foi {media_tempo:.2f} segundos")