import re


def display_help():
    print(
        """
                Certificate maker
    
    Para executar o programa corretamente, é necessário
    informar três argumentos ao chamar o executável:

    - Caminho para o arquivo CSV com os dados a ser lido
    - Caminho para o template HTML a ser preenchido
    - Caminho para a imagem a ser usada de plano de fundo
    - Padrão de nome dos arquivos gerados (ex.: "DATE - NAME")

        """
    )

def display_invalid_path(path):
    print("O caminho: %s é inválido\n" % path)

def validate_args(argv):
    if len(argv) != 5:
        display_help()
        return False

    get_pattern = lambda ext: "^(C:|.)(\\\\[^/\\\\?%*:|\\\"<>,;=\s]{1,}){1,}(.[A-Za-z0-9])*.("+ext+")$"
    ext = ['csv', 'html', 'png|jpg|jpeg|webp']

    for i in range(1, 4):
        pattern = get_pattern(ext[i-1])
        if not re.search(pattern, argv[i]):
            display_invalid_path(argv[i])
            return False

    return True
