def cadastrar_livro(livros, titulo, autor, ano):
    livro = {
        'titulo': titulo,
        'autor': autor,
        'ano': ano
    }
    livros.append(livro)
    print(f"Livro '{titulo}' cadastrado com sucesso!")

# Função para listar todos os livros
def listar_livros(livros):
    if livros:
        print("Lista de livros:")
        for livro in livros:
            print(f"Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}")
    else:
        print("Nenhum livro cadastrado.")

# Função para buscar um livro por título
def buscar_por_titulo(livros, titulo):
    encontrados = [livro for livro in livros if titulo.lower() in livro['titulo'].lower()]
    if encontrados:
        print("Livros encontrados:")
        for livro in encontrados:
            print(f"Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}")
    else:
        print("Nenhum livro encontrado com esse título.")

# Função para remover um livro pelo título
def remover_livro(livros, titulo):
    livros_removidos = [livro for livro in livros if livro['titulo'].lower() == titulo.lower()]
    if livros_removidos:
        livros[:] = [livro for livro in livros if livro['titulo'].lower() != titulo.lower()]
        print(f"Livro '{titulo}' removido com sucesso!")
    else:
        print(f"Livro '{titulo}' não encontrado.")