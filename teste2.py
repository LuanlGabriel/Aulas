import time

# Função para exibir texto com efeito de digitação
def type_effect(text, speed=0.05):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(speed)
    print()

# Função para simular o começo do jogo com uma escolha de narrativa
def start_game():
    type_effect("Detroit: Become Human - Início\n")
    time.sleep(1)

    type_effect("Você é Connor, um androide policial, em uma missão para resolver uma situação tensa...\n")
    time.sleep(2)

    type_effect("Você chega a um prédio e encontra um androide em uma situação crítica. O androide parece estar em pânico.\n")
    type_effect("O androide está segurando uma criança como refém.\n")
    time.sleep(2)

    type_effect("O que você faz?\n")
    time.sleep(1)

    # Apresenta opções ao jogador
    print("1. Tentar convencer o androide a se entregar.")
    print("2. Usar força para neutralizar o androide.")

    # Leitura da escolha do jogador
    choice = input("Escolha uma opção (1 ou 2): ").strip()

    if choice == "1":
        type_effect("\nVocê tenta convencer o androide a se entregar, falando sobre a liberdade que ele pode conquistar.")
        type_effect("O androide hesita... mas ele acaba cedendo e entrega a criança.\n")
        type_effect("Você conseguiu evitar um confronto violento, mas será que isso foi o melhor a longo prazo?\n")
        # Continuação da narrativa baseada na escolha
        continuation()
        
    elif choice == "2":
        type_effect("\nVocê decide usar a força e neutralizar o androide.")
        type_effect("O androide tenta resistir, mas você consegue desativá-lo com precisão.")
        type_effect("A criança está a salvo, mas o androide foi destruído. O que isso significa para você, um androide que sempre seguiu ordens?\n")
        # Continuação da narrativa baseada na escolha
        continuation()

    else:
        type_effect("Escolha inválida. Tente novamente.")
        start_game()  # Reinicia o jogo se a escolha for inválida

# Função para continuar a narrativa
def continuation():
    time.sleep(2)
    type_effect("\nA missão foi cumprida, mas você começa a refletir sobre o que aconteceu.")
    type_effect("Como um androide, você sempre segue ordens, mas e se, um dia, você começasse a questioná-las?\n")
    time.sleep(3)

    # Escolha final de reflexão
    type_effect("\nVocê começa a se perguntar: 'O que significa ser humano?'")
    type_effect("Será que a sua programação é tudo o que você é?\n")
    time.sleep(2)
    
    # Fim do trecho
    type_effect("\nA história de Connor está apenas começando...")

# Iniciar o jogo
if __name__ == "__main__":
    start_game()
