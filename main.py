
"""
Jogo de Adivinhação de Números
Um programa interativo onde o jogador tenta adivinhar um número gerado aleatoriamente pelo computador.
"""

import random
import time
import os

def limpar_tela():
    """Limpa a tela do terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_banner():
    """Exibe o banner do jogo"""
    print("=" * 50)
    print("🎯 JOGO DE ADIVINHAÇÃO DE NÚMEROS 🎯")
    print("=" * 50)
    print("🎲 O computador escolheu um número entre 1 e 100")
    print("💡 Você deve tentar adivinhar qual é!")
    print("=" * 50)

def obter_dificuldade():
    """Permite ao usuário escolher a dificuldade"""
    print("\n📊 Escolha a dificuldade:")
    print("1️⃣  Fácil (1-50, 10 tentativas)")
    print("2️⃣  Médio (1-100, 7 tentativas)")
    print("3️⃣  Difícil (1-200, 5 tentativas)")
    
    while True:
        try:
            escolha = input("\n🎮 Digite sua escolha (1-3): ").strip()
            if escolha in ['1', '2', '3']:
                return escolha
            else:
                print("❌ Por favor, escolha 1, 2 ou 3.")
        except KeyboardInterrupt:
            print("\n\n👋 Jogo interrompido. Até logo!")
            exit()

def configurar_jogo(dificuldade):
    """Configura o jogo baseado na dificuldade escolhida"""
    if dificuldade == '1':
        return 1, 50, 10, "FÁCIL"
    elif dificuldade == '2':
        return 1, 100, 7, "MÉDIO"
    else:
        return 1, 200, 5, "DIFÍCIL"

def dar_dica(numero_secreto, tentativa_atual, max_tentativas):
    """Fornece dicas baseadas na tentativa atual"""
    diferenca = abs(numero_secreto - tentativa_atual)
    
    if tentativa_atual < numero_secreto:
        if diferenca <= 10:
            return "🔥 Quente! Tente um número maior."
        elif diferenca <= 25:
            return "🌤️  Morno! Tente um número maior."
        else:
            return "❄️  Frio! Tente um número bem maior."
    else:
        if diferenca <= 10:
            return "🔥 Quente! Tente um número menor."
        elif diferenca <= 25:
            return "🌤️  Morno! Tente um número menor."
        else:
            return "❄️  Frio! Tente um número bem menor."

def jogar_rodada():
    """Executa uma rodada completa do jogo"""
    limpar_tela()
    exibir_banner()
    
    # Escolher dificuldade
    dificuldade = obter_dificuldade()
    min_num, max_num, max_tentativas, nome_dificuldade = configurar_jogo(dificuldade)
    
    # Gerar número secreto
    numero_secreto = random.randint(min_num, max_num)
    
    print(f"\n🎯 Dificuldade: {nome_dificuldade}")
    print(f"🔢 Número entre {min_num} e {max_num}")
    print(f"🎲 Tentativas disponíveis: {max_tentativas}")
    print("=" * 50)
    
    tentativas = 0
    numeros_tentados = []
    
    while tentativas < max_tentativas:
        tentativas += 1
        tentativas_restantes = max_tentativas - tentativas
        
        print(f"\n🎯 Tentativa {tentativas}/{max_tentativas}")
        if tentativas_restantes > 0:
            print(f"⏰ Tentativas restantes: {tentativas_restantes}")
        
        # Mostrar números já tentados
        if numeros_tentados:
            print(f"📝 Números tentados: {', '.join(map(str, numeros_tentados))}")
        
        # Obter palpite do usuário
        while True:
            try:
                palpite = input(f"\n💭 Digite seu palpite ({min_num}-{max_num}): ").strip()
                
                if palpite.lower() in ['sair', 'quit', 'exit']:
                    print("\n👋 Obrigado por jogar! Até logo!")
                    return False
                
                palpite = int(palpite)
                
                if min_num <= palpite <= max_num:
                    break
                else:
                    print(f"❌ Por favor, digite um número entre {min_num} e {max_num}.")
            except ValueError:
                print("❌ Por favor, digite um número válido.")
            except KeyboardInterrupt:
                print("\n\n👋 Jogo interrompido. Até logo!")
                exit()
        
        numeros_tentados.append(palpite)
        
        # Verificar se acertou
        if palpite == numero_secreto:
            print("\n" + "🎉" * 20)
            print("🎉 PARABÉNS! VOCÊ ACERTOU! 🎉")
            print("🎉" * 20)
            print(f"🎯 O número era: {numero_secreto}")
            print(f"🏆 Você acertou em {tentativas} tentativa(s)!")
            
            if tentativas == 1:
                print("🌟 INCRÍVEL! Primeira tentativa!")
            elif tentativas <= 3:
                print("👏 Excelente! Muito bem!")
            elif tentativas <= 5:
                print("👍 Bom trabalho!")
            else:
                print("💪 Você conseguiu!")
            
            return True
        
        # Dar dica se errou
        print(f"\n❌ Não é {palpite}!")
        dica = dar_dica(numero_secreto, palpite, tentativas)
        print(f"💡 {dica}")
        
        if tentativas_restantes > 0:
            print(f"⏰ Tentativas restantes: {tentativas_restantes}")
        
        # Pausa para suspense
        time.sleep(1)
    
    # Se chegou aqui, perdeu
    print("\n" + "💀" * 20)
    print("💀 GAME OVER! Você esgotou todas as tentativas! 💀")
    print("💀" * 20)
    print(f"🎯 O número era: {numero_secreto}")
    print("😔 Melhor sorte na próxima vez!")
    
    return False

def main():
    """Função principal do jogo"""
    print("🚀 Iniciando o Jogo de Adivinhação...")
    time.sleep(1)
    
    while True:
        # Jogar uma rodada
        resultado = jogar_rodada()
        
        # Perguntar se quer jogar novamente
        print("\n" + "=" * 50)
        print("🔄 Deseja jogar novamente?")
        print("1️⃣  Sim, quero jogar novamente!")
        print("2️⃣  Não, quero sair")
        
        while True:
            try:
                escolha = input("\n🎮 Digite sua escolha (1-2): ").strip()
                if escolha == '1':
                    print("\n🔄 Reiniciando o jogo...")
                    time.sleep(1)
                    break
                elif escolha == '2':
                    print("\n👋 Obrigado por jogar! Até a próxima!")
                    print("🎯 Espero que tenha se divertido!")
                    time.sleep(2)
                    return
                else:
                    print("❌ Por favor, escolha 1 ou 2.")
            except KeyboardInterrupt:
                print("\n\n👋 Até logo!")
                return

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Jogo interrompido. Até logo!")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        print("🔧 Por favor, tente executar o programa novamente.")
