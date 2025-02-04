from func import *

def menu():
    livros = [] 
    while True:
        print("\n--- Gerenciador de Livros ---")
        print("1. Cadastrar livro")
        print("2. Listar livros")
        print("3. Buscar livro por título")
        print("4. Remover livro")
        print("5. Sair")
        
        opcao = input("Escolha uma opção (1-5): ")
        
        if opcao == '1':
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            ano = input("Digite o ano de publicação: ")
            cadastrar_livro(livros, titulo, autor, ano)
        elif opcao == '2':
            listar_livros(livros)
        elif opcao == '3':
            titulo_busca = input("Digite o título para busca: ")
            buscar_por_titulo(livros, titulo_busca)
        elif opcao == '4':
            titulo_remover = input("Digite o título do livro a ser removido: ")
            remover_livro(livros, titulo_remover)
        elif opcao == '5':
            print("Saindo do gerenciador de livros. Até mais!")
            break
        else:
            print("Opção inválida, tente novamente.")

menu()