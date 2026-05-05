def processar_boletim(nota1, nota2, nota3):
    media = (nota1 + nota2+ nota3) / 3

    if media >= 6.0:
        situacao = "APROVADO"
    else:
        situacao = "REPROVADO"

    return media, situacao

status_aluno, media_aluno = processar_boletim(7.5, 5.0, 8.0)

print(f"Resultado Final: Média {status_aluno:.1f} -> Status: {media_aluno}")
