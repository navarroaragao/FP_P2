# This is the Python script for your project

# 1.º TAD

letras_col = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j') # tuplo com todas as letras possíveis para as colunas

def cria_posicao(col, lin):

    """
    A função cria_posicao recebe dois argumentos, uma coluna e uma linha, e devolve a posição correspondente.
    Os argumentos coluna e lista são do tipo (str) e (int), respetivamente.
    A função retorna uma posição do tipo str, que é a junção da coluna e da linha.
    A função verifica se os argumentos são válidos, caso contrário, devolve um erro.
    """

    if not (isinstance(col, str) and isinstance(lin, int) and col in letras_col and 1 <= lin <= 10):
        raise ValueError("cria_posicao: argumentos invalidos")
    return col + str(lin)

def obtem_pos_col(pos):

    """
    A função obtem_pos_col recebe uma posição e devolve a coluna correspondente.
    O argumento pos é do tipo str.
    A função retorna a coluna da posição, que é do tipo str.
    """

    return str(pos[0])

def obtem_pos_lin(pos):

    """
    A função obtem_pos_lin recebe uma posição e devolve a linha correspondente.
    O argumento pos é do tipo str.
    A função retorna a linha da posição, que é do tipo int.
    """

    return int(pos[1:])

def eh_posicao(arg):

    """
    A função eh_posicao recebe um argumento e verifica se é uma posição válida.
    O argumento é do tipo universal.
    A função retorna um valor booleano.
    """

    return isinstance(arg, str) and arg[0] in letras_col and 1 <= arg[1] <= 10

def posicoes_iguais(p1, p2):

    """
    A função posicoes_iguais recebe duas posições e verifica se são iguais.
    As posições são do tipo str.
    A função retorna um valor booleano.
    """

    return obtem_pos_col(p1) == obtem_pos_col(p2) and obtem_pos_lin(p1) == obtem_pos_lin(p2)

def posicao_para_str(pos):

    """
    A função posicao_para_str recebe uma posição e devolve a posição em formato de string.
    O argumento pos é do tipo str.
    A função retorna a posição em formato de string.
    """

    return str(pos)

def str_para_posicao(str): 

    """
    A função str_para_posicao recebe uma string e devolve a posição correspondente. 
    """

    return str
 
def indice_linha_posicao_aux(num_linha):
    
    """
    A função auxiliar indice_linha_posicao recebe um número de linha e devolve o índice correspondente.
    O argumento num_linha é do tipo int.
    """

    return num_linha - 1

def indice_coluna_posicao_aux(letra_coluna):

    """
    A função auxiliar indice_coluna_posicao recebe uma letra de coluna e devolve o índice correspondente.
    O argumento letra_coluna é do tipo str.
    """

    return ord(letra_coluna) - ord("a")

def tamanho_lado_tabuleiro_aux(n):

    """
    A função auxiliar tamanho_lado_tabuleiro recebe um número de órbitas e devolve o tamanho das linhas e das colunas do tabuleiro.
    O valor do tamanho das linhas e das colunas é igual.
    O argumento n é do tipo int.
    """

    return 2 * n

def eh_posicao_valida(p, n):

    """
    A função eh_posicao_valida recebe uma posição e um número de órbitas do tabuleiro e verifica se a posição é válida.
    Os argumentos são do tipo str e int, respetivamente.
    A função retorna um valor booleano.
    """

    return 0 < obtem_pos_lin(p) <= 2 * n and 2 <= n <= 5

def obtem_posicoes_adjacentes(p, n, d):

    """
    A função obtem_posicoes_adjacentes recebe uma posição, um número de órbitas e um valor booleano e devolve as posições adjacentes.
    Os argumentos são do tipo str, int e bool, respetivamente.
    A função retorna um tuplo com as posições adjacentes, se a condição d for True. 
    Caso contrário, retorna um tuplo com as posições ortogonais adjacentes.
    """

    col = obtem_pos_col(p)
    lin = obtem_pos_lin(p)
    tuplo_adjacentes = ()

    tamanho_lado = tamanho_lado_tabuleiro_aux(n)

    index_linha_pos = indice_linha_posicao_aux(lin)
    index_coluna_pos = indice_coluna_posicao_aux(col)

    variacoes = ((0, -1), (1, -1), (1, 0), # coordenadas de simulações de vetores que representam transformações para chegar às adjacentes.
                 (1, 1), (0, 1), (-1, 1),
                 (-1, 0), (-1, -1))
    for variacao in variacoes:
        index_coluna = index_coluna_pos + variacao[0]
        index_linha = index_linha_pos + variacao[1]

        # condição que verifica se está dentro do tabuleiro
        condicao_linha_esperada = 0 <= index_linha <= tamanho_lado
        condicao_coluna_esperada = 0 <= index_coluna <= tamanho_lado
        if not condicao_linha_esperada or not condicao_coluna_esperada: # verificamos se entramos nas ortogonais ou adjacentes.
            continue

        # verificar ortogonais
        condicao_ortogonal = variacao[0] == 0 or variacao[1] == 0
        if not d and not condicao_ortogonal:
            continue

        # verificação das condições para que a posição adjacente seja válida.
        nova_col = chr(index_coluna + ord("a")) # Conversão índices das linhas e colunas para posição.
        nova_lin = index_linha + 1
        nova_posicao = cria_posicao(nova_col, nova_lin) 

        if not posicoes_iguais(p, nova_posicao): # Verificação se a posição não é igual à posição nova.
            tuplo_adjacentes += (nova_posicao,)

    return tuplo_adjacentes

def ordena_posicoes(t, n):

    """
    A função ordena_posicoes recebe um tuplo de posições e o número de órbitas do tabuleiro e devolve o tuplo ordenado.
    Os argumentos são do tipo tuplo e int, respetivamente.
    A função retorna um tuplo com as posições ordenadas.
    """
    def computa_valores(p, n):
        col = obtem_pos_col(p)
        lin = obtem_pos_lin(p)
        index_coluna_pos = indice_coluna_posicao_aux(col)
        index_linha_pos = indice_linha_posicao_aux(lin)
        tamanho_lado = tamanho_lado_tabuleiro_aux(n)

        posicao = (index_linha_pos, index_coluna_pos)
        posicao_espelhada = (min(posicao[0], tamanho_lado - 1 - posicao[0]), min(posicao[1], tamanho_lado - 1 - posicao[1]))
        posicao_diagonal = (min(posicao_espelhada[0], posicao_espelhada[1]), min(posicao_espelhada[0], posicao_espelhada[1])) 
        orbital_invertida = posicao_diagonal[0]
        orbital = n - orbital_invertida - 1 

        return (orbital, index_linha_pos, index_coluna_pos)
    

    tuplo_ordenado = sorted(t, key = lambda x: computa_valores(x, n))


    return tuplo_ordenado

    #tuplo_distancias = sorted(tuplo_distancias, key = lambda x: (x[1], x[0]))


# 2.º TAD

pedras = ('O', 'X', ' ') # tuplo com todas as pedras possíveis

def cria_pedra_branca():

    """
    A função cria_pedra_branca cria uma pedra branca.
    A função retorna uma posição com a string "O".
    """

    return pedras[0]

def cria_pedra_preta():

    """
    A função cria_pedra_preta cria uma pedra preta.
    A função retorna uma posição com a string "X".
    """

    return pedras[1]

def cria_pedra_neutra():

    """
    A função cria_pedra_neutra cria uma pedra neutra.
    A função retorna uma posição com a string " ".
    """

    return pedras[2]

def eh_pedra(arg):

    """
    A função eh_pedra recebe um argumento e verifica se é uma pedra válida.
    O argumento arg é do tipo universal.
    """

    return arg in pedras

def eh_pedra_branca(p):

    """
    A função eh_pedra_branca recebe uma pedra e verifica se é branca.
    O argumento p é do tipo str.
    A função retorna um valor booleano.
    """

    return p == 'O'

def eh_pedra_preta(p):

    """
    A função eh_pedra_preta recebe uma pedra e verifica se é preta.
    A função retorna um valor booleano.
    """

    return p == 'X'

def pedras_iguais(p1, p2):

    """
    A função pedras_iguais recebe duas pedras e verifica se são iguais.
    Os argumentos são do tipo str.
    A função retorna um valor booleano.
    """

    return eh_pedra(p1) and eh_pedra(p2) and p1 == p2

def pedra_para_str(p):

    """
    A função pedra_para_str recebe uma pedra e devolve a pedra em formato de string.
    O argumento p é do tipo str.
    A função retorna a pedra do jogador em formato de string.
    """

    return ('O' if eh_pedra_branca(p) else 'X' if eh_pedra_preta(p) else ' ')

def eh_pedra_jogador(p):
    
    """
    A função eh_pedra_jogador recebe uma pedra e verifica se é de um jogador.
    O argumento p é do tipo str.
    A função retorna um valor booleano.
    """

    return p in ('O', 'X')

def pedra_para_int(p):

    """
    A função pedra_para_int recebe uma pedra e devolve um inteiro correspondente.
    O argumento p é do tipo str.
    A função retorna um inteiro.
    """

    return (-1 if eh_pedra_branca(p) else 1 if eh_pedra_preta(p) else 0)


# 3.º TAD

def cria_tabuleiro_vazio(n):

    """
    A função cria_tabuleiro_vazio recebe o número de órbitas e devolve o tabuleiro vazio.
    O argumento n é do tipo int.
    A função retorna um dicionário, que representa um tabuleiro com todas as posições vazias.
    A função verifica se o argumento é válido, caso contrário, devolve um erro.
    """

    tabuleiro = {} 
    if not(isinstance(n, int) and 2 <= n <= 5):
        raise ValueError('cria_tabuleiro_vazio: argumento invalido')
    for index_letras in range(0, len(letras_col) + 1):
        for index_linhas in range(1, n * 2 + 1):
            tabuleiro[cria_posicao(letras_col[index_letras], index_linhas)] = cria_pedra_neutra()
    return tabuleiro

def cria_tabuleiro(n, tp, tb):

    """
    A função cria_tabuleiro recebe o número de órbitas, as posições das pedras pretas e brancas e devolve o tabuleiro.
    Os argumentos são do tipo n --> int e tb, tp --> tuple.
    A função retorna um dicionário, que representa um tabuleiro com as posições das pedras.
    A função verifica se os argumentos são válidos, caso contrário, devolve um erro.
    """

    tabuleiro = cria_tabuleiro_vazio(n)
    
    if not (isinstance(tp, tuple) and isinstance(tb, tuple) and 2 <= n <= 5):
        raise ValueError('cria_tabuleiro: argumentos invalidos')

    for pedras_tp in range(0, len(tp) + 1):
        tabuleiro[tp[pedras_tp]] = cria_pedra_preta() # cria o tabulerio com as pedras pretas

    for pedras_tb in range(0, len(tb) + 1):
        tabuleiro[tb[pedras_tb]] = cria_pedra_branca() # cria o tabuleiro com as pedras brancas

def cria_copia_tabuleiro(t):

    """
    A função cria_copia_tabuleiro recebe um tabuleiro e devolve uma cópia do tabuleiro.
    O argumento t é do tipo dict.
    A função retorna um dicionário, cópia do tabuleiro, t.
    """

    t_novo = t
    return t_novo

def obtem_numero_orbitas(t):

    """
    A função obtem_numero_orbitas recebe um tabuleiro e devolve o número de órbitas.
    O argumento t é do tipo dict.
    A função retorna um inteiro, número de órbitas.
    """

    return (len(t) // 4) ** 1/2

def obtem_pedra(t, p):

    """
    A função obtem_pedra recebe um tabuleiro e uma posição e devolve a pedra correspondente.
    Os argumentos são do tipo dict e str, respetivamente.
    A função retorna a pedra do tabuleiro na posição p, que é do tipo str.
    """

    return str(t[p])
