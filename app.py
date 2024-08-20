import os

restaurantes = [{'nome':'Bar do Zé','categoria':'lanchonete', 'ativo':False},
                {'nome':'Angu do Gosma','categoria':'comida típica', 'ativo': True},
                {'nome':'Buteco do João','categoria':'comida exótica', 'ativo': False}]

def exibir_nome_do_programa():
    """
    Exibe o nome do programa em um formato estilizado.
    """
    print("""
╔═══╗──╔╗───────╔═══╗
║╔═╗║──║║───────║╔══╝
║╚══╦══╣╚═╦══╦═╗║╚══╦╗╔╦══╦═╦══╦══╦══╗
╚══╗║╔╗║╔╗║╔╗║╔╝║╔══╩╬╬╣╔╗║╔╣║═╣══╣══╣
║╚═╝║╔╗║╚╝║╚╝║║─║╚══╦╬╬╣╚╝║║║║═╬══╠══║
╚═══╩╝╚╩══╩══╩╝─╚═══╩╝╚╣╔═╩╝╚══╩══╩══╝
───────────────────────║║
───────────────────────╚╝""")

def exibir_opcoes():
    """
    Exibe as opções disponíveis no menu principal.
    """
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar ou desativar restaurantes')
    print('4. Sair\n')

def finalizar_app():
    """
    Exibe uma mensagem de encerramento do aplicativo.
    """
    exibir_subtitulo('Encerrando o aplicativo\n')

def voltar_ao_menu_principal():
    """ Solicita uma tecla para voltar ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    """
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcao_invalida():
    """
    Exibe mensagem de opção inválida e retorna ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    """
    print('Opção invalida\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    """
    Exibe um subtítulo estilizado.
    
    Args:
        texto (str): O texto a ser exibido como subtítulo.
    """
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    """
    Essa função é responsável por cadastrar um novo restaurante 
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes
    """
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_do_restaurante = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria_do_restaurante, 'ativo': False}
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    restaurantes.append(dados_do_restaurante)
    voltar_ao_menu_principal()

def listar_restaurantes():
    """
    Lista os restaurantes presentes na lista 
    
    Outputs:
    - Exibe a lista de restaurantes na tela
    """
    exibir_subtitulo('Restaurantes cadastrados:')

    print(f"{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status")

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurante = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo_restaurante} ')
    voltar_ao_menu_principal()

def alternar_estado_do_restaurante():
    """
    Altera o estado ativo/desativado de um restaurante 
    
    Outputs:
    - Exibe mensagem indicando o sucesso da operação
    """
    exibir_subtitulo('Alternando o estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('Restaurante não foi encontrado')
    voltar_ao_menu_principal()

def escolher_opcao():
    """
    Solicita e executa a opção escolhida pelo usuário 
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    """
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_do_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    """
    Função principal que exibe o nome do programa, as opções e aguarda a escolha do usuário.
    """
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()