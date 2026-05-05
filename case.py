comando = 3

match comando:
    case 1:
        print("Iniciando novo jogo!")
    case 2:
        print("Carregando jogo")
    case 3:
        print("Abrindo configurações")
    case _:
        print("Comando Inválido! Tente  novamente.")