import random

# Lista de caracteres para a senha
caracteres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
              'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
              '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
              '!', '"', '#', '$', '%', '&','*','@']

try:
    # Exibindo a mensagem de boas-vindas em verde
    bemVindo = "\033[92m" + r"""
      ________                         .___                 .___                            .__                   
     /  _____/  ________________     __| _/___________    __| _/____     ______ ____   ____ |  |__ _____    ______
    /   \  ____/ __ \_  __ \__  \   / __ |/  _ \_  __ \  / __ |/ __ \   /  ___// __ \ /    \|  |  \\__  \  /  ___/
    \    \_\  \  ___/|  | \// __ \_/ /_/ (  <_> )  | \/ / /_/ \  ___/   \___ \\  ___/|   |  \   Y  \/ __ \_\___ \ 
     \______  /\___  >__|  (____  /\____ |\____/|__|    \____ |\___  > /____  >\___  >___|  /___|  (____  /____  >
            \/     \/           \/      \/                   \/    \/       \/     \/     \/     \/     \/     \/ 
    """ + "\033[0m"  # Resetando a cor para o padrão
    print(bemVindo)

    tamanho = int(input('Informe o tamanho da senha: '))
    senha = ''

    for i in range(tamanho):
        aleatorio = random.choice(caracteres)
        senha = senha + aleatorio

    # Exibindo mensagem de sucesso em azul
    print('\033[94mSenha gerada com sucesso! Esta é sua senha segura:\033[0m')

    # Exibindo a senha em negrito
    print('\033[1m' + senha + '\033[0m')  # Resetando a formatação

except:
    # Exibindo mensagem de erro em vermelho
    print('\033[91mOcorreu algum erro!\033[0m')
