def attempt_float(x):
    try:
        return float(x)
    except (ValueError, TypeError) as e:
        return f'Erro: {e}'

def open_file(src_file: str, mode: str):
    '''Retorna a conexão com um arquivo'''
    try:
        return open(src_file, mode, encoding='utf-8')
    except Exception as e:
        print(f'Erro: {e}')

def write_file(text: str, src_file: str, mode: str):
    '''Escrever um texto no arquivo'''
    file = open_file(src_file, mode)
    try:
        file.write(text)
    except Exception as e:
        print(f'Erro: {e}')
    finally:
        file.close()

class IdadeInvalidaError(Exception):
    def __init__(self, idade):
        super().__init__(f"Idade Inválida: {idade}. A idade deve ser maior que 0.")

def verificar_idade(idade):
    if idade <= 0:
        raise IdadeInvalidaError(idade)
    print("Idade Validada!")

def main():
    try:
        write_file(
            'Aula 01/12/25\nTema: Tratamento de Erros e Exceções!',
            'relatorio.txt', 
            'w')
        verificar_idade(-5)
    except Exception as e:
        print(f'Erro: {e}')
    except IdadeInvalidaError as e:
        print(f'Erro: {e}')


if __name__ == "__main__":
    main()