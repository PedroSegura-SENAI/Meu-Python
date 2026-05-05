def calcular_dano(ataque_base, multiplicador, foi_critico):
    if foi_critico == True:
        dano_total = ataque_base * multiplicador
        return f" ACERTO CRÍTICO! Você causou {dano_total} de dano"
    
    else:
        return f"Acerto normal. Você causou {ataque_base} de dano"
    

ataque_1 = calcular_dano(50, 2.5, False)
ataque_2 = calcular_dano(50, 2.5, True)

print(ataque_1)
print(ataque_2)