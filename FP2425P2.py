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

    if not (type(col) == str and type(lin) == int and col in letras_col and 1 <= lin <= 10):
        raise ValueError("cria_posicao: argumentos invalidos")
    return col + str(lin)

def obtem_pos_col(pos):

    """
    A função obtem_pos_col recebe uma posição e devolve a letra da coluna correspondente.
    O argumento pos é do tipo str.
    A função retorna a coluna da posição, que é do tipo str.
    """

    return str(pos[0])

def obtem_pos_lin(pos):

    """
    A função obtem_pos_lin recebe uma posição e devolve o número da linha correspondente.
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

    return type(arg) == str and arg[0] in letras_col and arg[1:].isnumeric() and 1 <= int(arg[1:]) <= 10 

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

    return ord(letra_coluna) - ord("a") # A letra 'a' corresponde ao índice 0. E os restantes vêm por comparação.

def tamanho_lado_tabuleiro_aux(n):

    """
    A função auxiliar tamanho_lado_tabuleiro recebe um número de órbitas e devolve o tamanho das linhas e das colunas do tabuleiro.
    O valor do tamanho das linhas e das colunas é igual.
    O argumento n é do tipo int.
    """

    return 2 * n

def indice_orbita_aux(posicao, n):

    """
    A função indice_orbita_aux é uma função auxiliar que recebe uma posição e o número de órbitas.
    Os argumentos posicao e n são do tipo string e inteiro.
    A função retorna o índice da órbita onde se encontra a posicao (ou seja, do tipo inteiro).
    NOTA: A orbital interior é a de índice 0.
    """
    # Localização da posição no tabuleiro.
    col = obtem_pos_col(posicao)
    lin = obtem_pos_lin(posicao)
    # Índices da linha e da coluna da posição.
    index_coluna_pos = indice_coluna_posicao_aux(col)
    index_linha_pos = indice_linha_posicao_aux(lin)
    tamanho_lado = tamanho_lado_tabuleiro_aux(n)
    
    # O tuplo da posição surge como índice da linha, índice da coluna.
    posicao = (index_linha_pos, index_coluna_pos)

    # Descobrir a orbital da posição.
    # Dividindo o tabuleiro ao meio, obtemos a posição espelhada.
    # A posição espelhada é a posição que está no tabuleiro.
    posicao_espelhada = (min(posicao[0], tamanho_lado - 1 - posicao[0]), min(posicao[1], tamanho_lado - 1 - posicao[1]))

    posicao_diagonal_invertida = (min(posicao_espelhada[0], posicao_espelhada[1]), min(posicao_espelhada[0], posicao_espelhada[1])) 
    orbita_invertida = posicao_diagonal_invertida[0]
    orbita = n - orbita_invertida - 1 # Os índices da órbita começam na mais interior.

    return orbita

def eh_posicao_valida(p, n):

    """
    A função eh_posicao_valida recebe uma posição e um número de órbitas do tabuleiro e verifica se a posição é válida.
    Os argumentos são do tipo str e int, respetivamente.
    A função retorna um valor booleano.
    """
    col = obtem_pos_col(p)
    lin = obtem_pos_lin(p)
    index_coluna_p = indice_coluna_posicao_aux(col)

    return 0 < lin <= 2 * n and  0 < index_coluna_p <= 2 * n and 2 <= n <= 5

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
        condicao_linha_esperada = 0 <= index_linha < tamanho_lado
        condicao_coluna_esperada = 0 <= index_coluna < tamanho_lado
        if not condicao_linha_esperada or not condicao_coluna_esperada: # verificamos se entramos nas ortogonais ou adjacentes.
            continue

        # verificar ortogonais
        condicao_ortogonal = variacao[0] == 0 or variacao[1] == 0
        if not d and not condicao_ortogonal:
            continue

        # Conversão índices das linhas e colunas para posição.
        nova_col = chr(index_coluna + ord("a")) 
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
        orbita = indice_orbita_aux(p, n)

        # ordem de prioridade de ordenação de posições (orbita, linha, coluna)
        return (orbita, index_linha_pos, index_coluna_pos) 
    
    tuplo_ordenado = sorted(t, key = lambda x: computa_valores(x, n))

    return tuplo_ordenado


# 2.º TAD

pedras = (-1, 1, 0) # tuplo com todas as pedras possíveis

def cria_pedra_branca():

    """
    A função cria_pedra_branca cria uma pedra branca.
    A função retorna o valor da pedra branca, ou seja, um inteiro.
    """

    return pedras[0]

def cria_pedra_preta():

    """
    A função cria_pedra_preta cria uma pedra preta.
    A função retorna o valor da pedra preta, ou seja, um inteiro.
    """

    return pedras[1]

def cria_pedra_neutra():

    """
    A função cria_pedra_neutra cria uma pedra neutra.
    A função retorna o valor da pedra neutra, ou seja, um inteiro.
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
    O argumento p é do tipo int.
    A função retorna um valor booleano.
    """

    return p == cria_pedra_branca()

def eh_pedra_preta(p):

    """
    A função eh_pedra_preta recebe uma pedra e verifica se é preta.
    O argumento p é do tipo int.
    A função retorna um valor booleano.
    """

    return p == cria_pedra_preta()

def pedras_iguais(p1, p2):

    """
    A função pedras_iguais recebe duas pedras e verifica se são iguais.
    Os argumentos são do tipo int.
    A função retorna um valor booleano.
    """

    return eh_pedra(p1) and eh_pedra(p2) and p1 == p2

def pedra_para_str(p):

    """
    A função pedra_para_str recebe uma pedra e devolve a pedra em formato de string.
    O argumento p é do tipo int.
    A função retorna a pedra do jogador em formato de string.
    """

    return ('O' if eh_pedra_branca(p) else 'X' if eh_pedra_preta(p) else ' ')

def inverte_pedra(p):

    """
    A função inverte_pedra recebe uma pedra e inverte a pedra.
    O argumento p é do tipo int.
    A função retorna a pedra invertida.
    """

    return - p

def eh_pedra_jogador(p): 
    
    """
    A função eh_pedra_jogador recebe uma pedra e verifica se é de um jogador.
    A função retorna um valor booleano.
    """

    return p == cria_pedra_branca() or p == cria_pedra_preta() 

def pedra_para_int(p):

    """
    A função pedra_para_int recebe uma pedra e devolve um inteiro correspondente.
    O argumento p é do tipo str.
    A função retorna um inteiro.
    """

    return (-1 if eh_pedra_branca(p) else 1 if eh_pedra_preta(p) else 0)

def str_para_pedra(str):

    """
    A função str_para_pedra recebe uma string e devolve a pedra correspondente.
    O argumento str é do tipo str.
    A função retorna a pedra do jogador em formato inteiro.
    """
    pedra_preta = cria_pedra_preta() # Conversão para a pedra preta
    if pedra_para_str(pedra_preta) == str:
        return pedra_preta
    
    pedra_branca = cria_pedra_branca() # Conversão para a pedra branca
    if pedra_para_str(pedra_branca) == str:
        return pedra_branca
    
    return cria_pedra_neutra() # Conversão para a pedra neutra

# 3.º TAD

def cria_tabuleiro_vazio(n):

    """
    A função cria_tabuleiro_vazio recebe o número de órbitas e devolve o tabuleiro vazio.
    O argumento n é do tipo int.
    A função retorna um dicionário, que representa um tabuleiro com todas as posições vazias.
    A função verifica se o argumento é válido, caso contrário, devolve um erro.
    """

    tabuleiro_final = {} 

    if not((type(n) == int) and 2 <= n <= 5):
        raise ValueError('cria_tabuleiro_vazio: argumento invalido')
    
    for index_col in range(0, (2 * n)):
        tabuleiro_linhas = {} 
        for index_lin in range (1, ( 2 * n) + 1):
            tabuleiro_linhas[index_lin] = cria_pedra_neutra()
        tabuleiro_final[letras_col[index_col]] = tabuleiro_linhas

    return tabuleiro_final

def cria_tabuleiro(n, tp, tb):

    """
    A função cria_tabuleiro recebe o número de órbitas, as posições das pedras pretas e brancas e devolve o tabuleiro.
    Os argumentos são do tipo n --> int e tb, tp --> tuple.
    A função retorna um dicionário, que representa um tabuleiro com as posições das pedras.
    A função verifica se os argumentos são válidos, caso contrário, devolve um erro.
    """

    condicao_tuplos = (type(tp) == tuple and type(tb) == tuple and 2 <= n <= 5)
    if not condicao_tuplos:
        raise ValueError('cria_tabuleiro: argumentos invalidos')
    
    condicao_tuplo_pretas = all(eh_posicao(elemento) for elemento in tp) 
    condicao_tuplo_brancas = all(eh_posicao(elemento) for elemento in tb) 
    
    if not (condicao_tuplo_pretas and condicao_tuplo_brancas):
        raise ValueError('cria_tabuleiro: argumentos invalidos')
    
    tabuleiro = cria_tabuleiro_vazio(n)
    
    for p in tp:

        col = obtem_pos_col(p)
        lin = obtem_pos_lin(p)
        index_lin = indice_linha_posicao_aux(lin)
        index_col = indice_coluna_posicao_aux(col)

        tabuleiro[letras_col[index_col]][index_lin + 1] = cria_pedra_preta()
    
    for p in tb:

        col = obtem_pos_col(p)
        lin = obtem_pos_lin(p)
        index_lin = indice_linha_posicao_aux(lin)
        index_col = indice_coluna_posicao_aux(col)

        tabuleiro[letras_col[index_col]][index_lin + 1]= cria_pedra_branca()

    return tabuleiro


def cria_copia_tabuleiro(t):

    """
    A função cria_copia_tabuleiro recebe um tabuleiro e devolve uma cópia do tabuleiro.
    O argumento t é do tipo dict.
    A função retorna um dicionário, cópia do tabuleiro, t.
    """

    t_novo = {} 

    for col in t:
        t_novo[col] = {}
        for lin in t[col]:
            t_novo[col][lin] = t[col][lin]

    return t_novo

def obtem_numero_orbitas(t):

    """
    A função obtem_numero_orbitas recebe um tabuleiro e devolve o número de órbitas.
    O argumento t é do tipo dict.
    A função retorna um inteiro, número de órbitas.
    """

    return len(t) // 2

def obtem_pedra(t, p):

    """
    A função obtem_pedra recebe um tabuleiro e uma posição e devolve a pedra correspondente.
    Os argumentos são do tipo dict e str, respetivamente.
    A função retorna a pedra do tabuleiro na posição p, que é do tipo str.
    """

    col = obtem_pos_col(p)
    lin = obtem_pos_lin(p)

    return t[col][lin]

def obtem_linha_horizontal(t, p):

    """
    A função obtem_linha_horizontal recebe um tabuleiro e uma posição.
    Os argumentos são do tipo dict e str, respetivamente.
    A função retorna um tuplo com as posições, e respetivos valores, da linha onde se encontra a posição.
    """

    tuplo_posicoes_horizontal = ()
    lin = obtem_pos_lin(p)

    for index_coluna in range(0, len(t)):
        posicao = cria_posicao(letras_col[index_coluna], lin)
        valor = obtem_pedra(t, posicao)
        tuplo_posicao_valor = ((posicao, valor),)
        tuplo_posicoes_horizontal += tuplo_posicao_valor

    return tuplo_posicoes_horizontal

def obtem_linha_vertical(t, p): 

    """
    A função obtem_linha_vertical recebe um tabuleiro e uma posição.
    Os argumentos são do tipo dict e str, respetivamente.
    A função retorna um tuplo com as posições, e respetivos valores, da coluna onde se encontra a posição.
    """

    col = obtem_pos_col(p)
    tuplo_posicoes_vertical = ()

    for linha in range(1, len(t) + 1):
        posicao = cria_posicao(col, linha)
        valor = obtem_pedra(t, posicao)
        tuplo_posicoes_vertical += ((posicao, valor),)

    return tuplo_posicoes_vertical

def obtem_linhas_diagonais(t, p):

    """
    A função obtem_linhas_diagonais recebe um tabuleiro e uma posição.
    Os argumentos são do tipo dict e str, respetivamente.
    A função retorna um tuplo com as posições, e respetivos valores, das diagonais e antidiagonais onde se encontra a posição.
    """

    col = obtem_pos_col(p)
    lin = obtem_pos_lin(p)

    # tuplo com os índices da coluna da posição (pos) e da linha da posição (pos).
    pos_index = (indice_coluna_posicao_aux(col), indice_linha_posicao_aux(lin)) 
    pos_inicial_index = pos_index
    fora_tab = False

    # calcular posicao inicial
    while not fora_tab:
        pos_inicial_index = (pos_inicial_index[0] - 1, pos_inicial_index[1] - 1) 
        if not ( 0 <= pos_inicial_index[0] < len(t) and 0 <= pos_inicial_index[1] < len(t) ): # Verificar se o índice está dentro dos limites.
            fora_tab = True

    pos_atual_index = pos_inicial_index
    fora_tab = False

    # criar diagonal
    tuplo_diagonais = ()
    while not fora_tab:
        pos_atual_index = (pos_atual_index[0] + 1, pos_atual_index[1] + 1)
        if not ( 0 <= pos_atual_index[0] < len(t) and 0 <= pos_atual_index[1] < len(t) ):
            fora_tab = True
            continue # Interrompe a iteração atual e continua para a próxima iteração
        pos_nova_col = letras_col[pos_atual_index[0]]
        pos_nova_lin = pos_atual_index[1] + 1
        pos_nova = cria_posicao(pos_nova_col, pos_nova_lin)
        valor = obtem_pedra(t, pos_nova)
        tuplo_diagonais += ((pos_nova, valor),)

    pos_inicial_index = pos_index
    fora_tab = False

    # calcular posicao inicial 
    while not fora_tab:
        pos_inicial_index = (pos_inicial_index[0] - 1, pos_inicial_index[1] + 1)
        if not ( 0 <= pos_inicial_index[0] < len(t) and 0 <= pos_inicial_index[1] < len(t) ):
            fora_tab = True

    pos_atual_index = pos_inicial_index
    fora_tab = False

    # criar antidiagonal
    tuplo_antidiagonais = ()
    while not fora_tab:
        pos_atual_index = (pos_atual_index[0] + 1, pos_atual_index[1] - 1) # Atualização dos índices da linha e da coluna, contrário das diagonais, fazemos menos uma linha.
        if not ( 0 <= pos_atual_index[0] < len(t) and 0 <= pos_atual_index[1] < len(t) ):
            fora_tab = True
            continue

        pos_nova_col = letras_col[pos_atual_index[0]]
        pos_nova_lin = pos_atual_index[1] + 1
        pos_nova = cria_posicao(pos_nova_col, pos_nova_lin)
        valor = obtem_pedra(t, pos_nova)
        tuplo_antidiagonais += ((pos_nova, valor),)

    return (tuplo_diagonais, tuplo_antidiagonais)

tuplo_quadrantes = ((True, False), (True, True), (False, True), (False, False)) # Carcterização de cada quadrante

tuplo_quadrante_movimentos = ( # Movimentos possíveis em cada quadrante (numeração dos quadrantes é feita no sentido horário)
    ((1, 0),(0, 1)), # 1.º quadrante
    ((-1, 0),(0, 1)), # 2.º quadrante
    ((-1, 0), (0, -1)), # 3.º quadrante
    ((1, 0), (0, -1)))  # 4.º quadrante

def obtem_orbita(t, p):

    """
    A função obtem_orbita é uma função auxiliar que recebe um tabuleiro e uma posição.
    Os argumentos são do tipo dict e str, respetivamente.
    A função retorna um tuplo com as posições da órbita onde se encontra a posição. 
    """

    col = obtem_pos_col(p)
    lin = obtem_pos_lin(p)
    n = obtem_numero_orbitas(t)

    index_coluna = indice_coluna_posicao_aux(col)
    index_linha = indice_linha_posicao_aux(lin)
    index_orbita = indice_orbita_aux(p,n)
    tamanho_lado = tamanho_lado_tabuleiro_aux(obtem_numero_orbitas(t))

    posicao_inicial_index = (index_coluna, index_linha)
    posicao_atual_index = posicao_inicial_index
    posicoes_orbita = ()

    while posicao_atual_index != posicao_inicial_index or len(posicoes_orbita) == 0:
        
        index_linha_passa_metade = posicao_atual_index[1] >= (tamanho_lado // 2)
        index_coluna_passa_metade = posicao_atual_index[0] >= (tamanho_lado // 2) 

        tuplo_index_passa_metade = (index_coluna_passa_metade, index_linha_passa_metade)

        quadrante = tuplo_quadrantes.index(tuplo_index_passa_metade) # Determinar o quadrante onde se encontra a posição.
        movimentos = tuplo_quadrante_movimentos[quadrante] # Movimentos possíveis no quadrante.

        for movimento in movimentos:
            posicao_nova_index = (posicao_atual_index[0] + movimento[0], posicao_atual_index[1] + movimento[1])

            # Verificar se a posição nova está dentro do tabuleiro.
            if not (0 <= posicao_nova_index[0] < tamanho_lado and 0 <= posicao_nova_index[1] < tamanho_lado): 
                continue

            posicao_nova = cria_posicao(letras_col[posicao_nova_index[0]], posicao_nova_index[1] + 1)
            index_orbita_posicao_nova = indice_orbita_aux(posicao_nova, n)

            if index_orbita_posicao_nova == index_orbita: # Verificar se a posição nova está na órbita.
                posicoes_orbita += (posicao_nova, )
                posicao_atual_index = posicao_nova_index # Atualização da posição atual.
                break

    return posicoes_orbita


def obtem_posicoes_pedra(t, j):

    """
    A função obtem_posicoes_pedra recebe um tabuleiro e uma pedra.
    Os argumentos são do tipo dict e int, respetivamente.
    A função retorna um tuplo com as posições onde se encontra a pedra.
    """
    tuplo_posicoes_j = ()
    n = obtem_numero_orbitas(t)

    for coluna in t:
        for linha in t[coluna]:
            if t[coluna][linha] == j:
                tuplo_posicoes_j += (cria_posicao(coluna, linha),)

    return ordena_posicoes(tuplo_posicoes_j, n)

def coloca_pedra(t, j, p):

    """
    A função coloca_pedra recebe um tabuleiro, uma posição, e uma pedra e coloca a pedra na posição.
    Os argumentos são do tipo dict, int e str, respetivamente.
    A função retorna um dicionário, tabuleiro, com a pedra colocada na posição.
    """

    col_j = obtem_pos_col(j)
    lin_j = obtem_pos_lin(j)

    t[col_j][lin_j] = p

    return t
    

def remove_pedra(t, p):

    """
    A função remove_pedra recebe um tabuleiro e uma posição e remove a pedra da posição.
    Os argumentos são do tipo dict e str, respetivamente.
    A função retorna um dicionário, tabuleiro, com a pedra removida da posição.
    """

    col_p = obtem_pos_col(p)
    lin_p = obtem_pos_lin(p)

    t[col_p][lin_p] = cria_pedra_neutra()

    return t

def eh_tabuleiro(arg):

    """
    A função eh_tabuleiro recebe um argumento e verifica se é um tabuleiro válido.
    O argumento arg é do tipo universal.
    A função retorna um valor booleano.
    """

    if not (type(arg) == dict and 4 <= len(arg) <= 10):
        return False
    
    for col in arg:
        if not (col in letras_col and type(arg[col]) == dict and 4 <= len(arg[col]) <= 10):
            return False
        for lin in arg[col]:
            if not (1 <= lin <= 10 and eh_pedra(arg[col][lin])):
                return False
    return True
        

def tabuleiros_iguais(t1, t2):

    """
    A função tabuleiros_iguais recebe dois tabuleiros e verifica se são iguais.
    Os argumentos são do tipo dict.
    A função retorna um valor booleano.
    """

    if not eh_tabuleiro(t1) or not eh_tabuleiro(t2):
        return False
    
    if t1.keys() != t2.keys(): # Verificação das colunas.
        return False
    
    for col in t1:
        if t1[col].keys() != t2[col].keys(): # Verificação das linhas.
            return False
        for lin in t1[col]:
            if t1[col][lin] != t2[col][lin]: # Verificação das pedras.
                return False
            
    return True
                    

def tabuleiro_para_str(t):

    """
    A função tabuleiro_para_str recebe um tabuleiro e devolve o tabuleiro em formato de string.
    O argumento t é do tipo dict.
    A função retorna o tabuleiro em formato de string.
    """

    representacao_tab = ''
    n = obtem_numero_orbitas(t)


    linha_colunas = '   '.join(t.keys()) # concatenação das letras das colunas com um espaçamento definido.
    representacao_tab += '    ' + linha_colunas + '\n' 
    separador_linhas = '    ' + '   '.join(map(lambda x: '|', t.keys())) + '\n'

    for linha in range(1, 2 * n + 1):

        posicoes_formatadas = []
        for coluna in t:
            posicoes_formatadas += ['[' + pedra_para_str(t[coluna][linha]) + ']'] # representaçao das pedras em formato de string.

        representacao_tab += f"{linha:02}" + ' ' + '-'.join(posicoes_formatadas) + '\n' # representação das linhas do tabuleiro.
        if linha < 2 * n:
            representacao_tab += separador_linhas # representação do separador de linhas do tabuleiro.
    
    representacao_tab = representacao_tab.rstrip() # eliminação de espaços em branco no final do tabuleiro.
    return representacao_tab

def move_pedra(t, p1, p2):

    """
    A função move_pedra recebe um tabuleiro e duas posições e move a pedra da primeira posição para a segunda.
    Os argumentos são do tipo dict e str.
    A função retorna um dicionário, tabuleiro, com a pedra movida.
    """
    # primeira posição:
    col_p1 = obtem_pos_col(p1)
    lin_p1 = obtem_pos_lin(p1)

    col_p2 = obtem_pos_col(p2)
    lin_p2 = obtem_pos_lin(p2)

    t[col_p2][lin_p2] = t[col_p1][lin_p1]
    t[col_p1][lin_p1] = cria_pedra_neutra()

    return t

def obtem_posicao_seguinte(t, p, s):

    """
    A função obtem_posicao_seguinte recebe um tabuleiro, uma posição e um booleano.
    Os argumentos são do tipo dict, str e bool.
    Se a condição s for True, a função devolve a posição seguinte no sentido horário.
    Caso contrário, devolve a posição seguinte no sentido anti-horário.
    A função retorna a posição seguinte, que é do tipo str.
    """

    orbita_posicao = obtem_orbita(t, p)
    index_orbita_posicao = orbita_posicao.index(p) # índice da posição na órbita.

    variacao = 1 if s else -1
    index_posicao_seguinte = (index_orbita_posicao + variacao) % len(orbita_posicao)

    return orbita_posicao[index_posicao_seguinte]

def roda_tabuleiro(t):

    """
    A função roda_tabuleiro recebe um tabuleiro e roda todas as posições uma posição no sentido anti-horário.
    O argumento t é do tipo dict.
    A função retorna um dicionário, tabuleiro, com as novas posições.
    """
    backup_tabuleiro = cria_copia_tabuleiro(t)

    for col in backup_tabuleiro:
        for linha in backup_tabuleiro[col]: 
            posicao_atual = cria_posicao(col, linha) 

            # Obter a posição seguinte no sentido anti-horário.
            posicao_seguinte = obtem_posicao_seguinte(backup_tabuleiro, posicao_atual, False) 
            pedra = obtem_pedra(backup_tabuleiro, posicao_atual)

            t = coloca_pedra(t, posicao_seguinte, pedra)

    return t

def verifica_linha_pedras(t, p, j, k):

    """
    A função verifica_linha_pedras recebe um tabuleiro, uma posição, uma pedra e um inteiro.
    A função verifica se existem k pedras seguidas na linha (horizontal, vertical, diagonal) da posição.
    Os argumentos são do tipo dict, str, str e int, respetivamente.
    A função retorna um valor booleano.
    """

    linha_pos = obtem_linha_horizontal(t, p)
    coluna_pos = obtem_linha_vertical(t, p)
    diagonais_antidiagonais = obtem_linhas_diagonais(t, p)
    diagonal_pos = diagonais_antidiagonais[0]
    antidiagonal_pos = diagonais_antidiagonais[1]
    posicoes_jog = obtem_posicoes_pedra(t, j)

    def conta_pecas_consecutivas_aux(elementos):

        """
        
        A função conta_pecas_consecutivas é uma função auxiliar à função verifica_linhas_pedras que recebe um argumento (elementos).
        A função devolve um booleano:
            True se existirem k ou mais peças consecutivas do jogador (j) e False caso contrário.
        
        """

        contador = 0
        passou_posicao = False

        for (posicao_atual, _) in elementos: # Procurar no elemento se existem k ou mais peças do jogador.
            if posicao_atual == p:
                passou_posicao = True

            if posicao_atual in posicoes_jog:
                contador += 1
            else:
                contador = 0
                passou_posicao = False

            if contador >= k and passou_posicao:
                return True
        return False
    
    # Chamar a função conta_pecas_consecutivas para as linhas, colunas, diagonais e antidiagonais.
    if conta_pecas_consecutivas_aux(linha_pos) or conta_pecas_consecutivas_aux(coluna_pos) or conta_pecas_consecutivas_aux(diagonal_pos) or conta_pecas_consecutivas_aux(antidiagonal_pos):
        return True
    else:
        return False

def eh_vencedor(t, j):

    """
    A função eh_vencedor recebe um tabuleiro e um jogador e verifica se o jogador é vencedor.
    O jogador é vencedor se tiver uma linha completa com as suas pedras.
    Os argumentos são do tipo dict e str, respetivamente.
    A função retorna um valor booleano.
    """
    posicoes_jogador = obtem_posicoes_pedra(t, j)
    n = obtem_numero_orbitas(t)
    tamanho_lado = tamanho_lado_tabuleiro_aux(n)

    for posicao in posicoes_jogador:
        if verifica_linha_pedras(t,posicao, j, tamanho_lado): # Verificar se o jogador tem uma linha completa.
            return True
    return False

def eh_fim_jogo(t):

    """
    A função eh_fim_jogo recebe um tabuleiro e verifica se o jogo terminou.
    O jogo termina se um dos jogadores for vencedor ou se não existirem posições vazias.
    O argumento t é do tipo dict.
    A função retorna um valor booleano.
    """

    for j in (cria_pedra_branca(), cria_pedra_preta()):
        if eh_vencedor(t, j): # Verificar se um dos jogadores é vencedor.
            return True

    for col in t: 
        for lin in t[col]:
            if t[col][lin] == 0: # Verificar se existem posições livres.
                return False
            
    return True
            
def posicoes_livres_aux(t):

    """
    A função posicoes_livres_aux é uma função auxiliar, que recebe um tabuleiro e devolve um tuplo com as posições livres.
    O argumento t é do tipo dict.
    A função retorna um tuplo com as posições livres, que são do tipo str.
    """
    posicoes_livres = ()
    for coluna in t:
        for linha in t[coluna]:
            if t[coluna][linha] == cria_pedra_neutra():
                posicoes_livres += (cria_posicao(coluna, linha),)

    return posicoes_livres

def escolhe_movimento_manual(t):

    """
    A função escolhe_movimento_manual recebe um tabuleiro.
    O argumento t é do tipo dict.
    A função retorna uma string com a posições válida escolhida pelo jogador.
    """

    posicao_valida = False # Inicialização da variável que verifica se a posição é válida.
    while not posicao_valida: 
        posicao_esolhida = input('Escolha uma posicao livre:') # Mensagem ao jogador.
        if posicao_esolhida in posicoes_livres_aux(t): # Verificação da posição introduzida.
            return posicao_para_str(posicao_esolhida)

def escolhe_movimento_auto(t, j, lvl):

    """
    A função escolhe_movimento_auto recebe um tabuleiro, uma pedra e uma estratégia.
    Os argumentos são do tipo dict, str e str, respetivamente.
    A função retorna uma string com a posição válida escolhida automaticamente.
    """

    def estrategia_escolhida_facil_aux():

        """
        A função estrategia_facil_aux é uma função auxiliar à função escolhe_movimento_auto.
        A função retorna um tuplo com as posições que satisfazem as condições da estratégia fácil.
        ESPECIFICIDADES DA ESTRATÉGIA FÁCIL:
        - Se existir pelo menos uma posição (após rotação) que fique adjacente a uma pedra do jogador, a função escolhe essa posição.
        - Caso contrário, a função escolhe uma posição livre.
        """

        copia_tabuleiro = cria_copia_tabuleiro(t) # Cópia do tabuleiro.
        tabuleiro_rodado = roda_tabuleiro(copia_tabuleiro) # Rodar o tabuleiro.
        posicoes_livres = posicoes_livres_aux(tabuleiro_rodado) # Obter as posições livres.
        posicoes_jog = obtem_posicoes_pedra(tabuleiro_rodado, j) # Obter as posições do jogador. 
        tuplo_posicoes_adj_jog = () # Tuplo que vai conter as posições adjacentes às posições do jogador. 
        n = obtem_numero_orbitas(t)

        for posicao_jog in posicoes_jog:
            posicoes_adj_jog = obtem_posicoes_adjacentes(posicao_jog, n, True) # Obter as posições adjacentes às posições do jogador.
            for posicao_adj_jog in posicoes_adj_jog:
                if posicao_adj_jog in posicoes_livres: # Verificar se a posição adjacente está livre.
                    tuplo_posicoes_adj_jog += (posicao_adj_jog,)

        posicoes_escolhidas = ()
        if len(tuplo_posicoes_adj_jog) != 0:
            posicoes_escolhidas = tuplo_posicoes_adj_jog     
        else:
            posicoes_escolhidas = posicoes_livres

        # Transformador de posições: obter a posição seguinte no sentido horário.
        posicoes_convertidas = map(lambda x: obtem_posicao_seguinte(tabuleiro_rodado, x, True), posicoes_escolhidas) 

        return ordena_posicoes(posicoes_convertidas, n)

    def estrategia_escolhida_normal_aux():

        """
        A função estrategia_normal_aux é uma função auxiliar à função escolhe_movimento_auto.
        A função retorna um tuplo com as posições que satisfazem as condições da estratégia normal.
        ESPECIFICIDADES DA ESTRATÉGIA NORMAL:
        - É determinado o maior valor de L <= k, tal que o jogador consiga colocar L peças consecutivas:
            - Se existir, pelo menos, uma posição que após rotação permita obter uma linha com L peças consecutivas:
                - A função escolhe essa posição.
            - Caso contrário, a função escolhe uma posição que impossibilite o adversário de obter uma linha com L peças consecutivas.     
        """
        
        copia_tabuleiro_l = cria_copia_tabuleiro(t) # Cópia do tabuleiro.
        tabuleiro_rodado_l = roda_tabuleiro(copia_tabuleiro_l) # Rodar o tabuleiro.
        copia_tabuleiro_adv = cria_copia_tabuleiro(tabuleiro_rodado_l) 
        tabuleiro_rodado_adv = roda_tabuleiro(copia_tabuleiro_adv) # Rodar o tabuleiro duas vezes.
        
        tuplo_posicoes_l = () 
        tuplo_posicoes_adv = () 

        posicoes_livres_l = posicoes_livres_aux(tabuleiro_rodado_l) # Obter as posições livres.
        posicoes_livres_adv = posicoes_livres_aux(tabuleiro_rodado_adv) # Obter as posições livres.

        n = obtem_numero_orbitas(t)

        for l in range(2 * n, 0, -1): # Percorrer as valores de l, que vão de k até 1.
            for posicao_livre in posicoes_livres_l:
                novo_tabuleiro = cria_copia_tabuleiro(tabuleiro_rodado_l) # Cópia do tabuleiro.

                # Caso do jogador:
                tabuleiro_hipotetico = coloca_pedra(novo_tabuleiro, posicao_livre, j)
                chegou_ao_l = verifica_linha_pedras(tabuleiro_hipotetico, posicao_livre, j, l) # Verificar se chegou a l peças.
                if chegou_ao_l:
                    tuplo_posicoes_l += (posicao_livre, ) # Adicionar a posição ao tuplo.

            for posicao_livre in posicoes_livres_adv:   
                novo_tabuleiro = cria_copia_tabuleiro(tabuleiro_rodado_adv) # Cópia do tabuleiro.
                # Caso do adversário:
                tabuleiro_hipotetico_adv = coloca_pedra(novo_tabuleiro, posicao_livre, - j)
                chegou_ao_l_adv = verifica_linha_pedras(tabuleiro_hipotetico_adv, posicao_livre, -j, l)
                if chegou_ao_l_adv:
                    tuplo_posicoes_adv += (posicao_livre, )

            if len(tuplo_posicoes_l) != 0: # Serve para não retornar um tuplo vazio para as posições do jogador.
                posicoes_convertidas = map(lambda x: obtem_posicao_seguinte(tabuleiro_rodado_l, x, True), tuplo_posicoes_l)
                return ordena_posicoes(posicoes_convertidas, n)
            
            elif len(tuplo_posicoes_adv) != 0: # Serve para não retornar um tuplo vazio para as posições do adversário.
                posicoes_convertidas_1 = map(lambda x: obtem_posicao_seguinte(tabuleiro_rodado_adv, x, True), tuplo_posicoes_adv)
                posicoes_convertidas_2 = map(lambda x: obtem_posicao_seguinte(tabuleiro_rodado_l, x, True), posicoes_convertidas_1)
                return ordena_posicoes(posicoes_convertidas_2, n)

        return ()

    possibilidades = ()
    n = obtem_numero_orbitas(t) 

    # Posições correspondentes à estratégia escolhida.
    if lvl == "facil":
        possibilidades = estrategia_escolhida_facil_aux()
    elif lvl == "normal":
        possibilidades = estrategia_escolhida_normal_aux()

    posicao_escolhida_auto = ordena_posicoes(possibilidades, n)[0] 
    
    return posicao_escolhida_auto

def orbito(n, modo, jog):

    """
    A função orbito é a função principal do jogo Orbito.
    A função orbito recebe o número de órbitas, o modo de jogo e o jogador.
    Os argumentos são do tipo int, str e str, respetivamente.
    """


    condicao_esperada = type(modo) == str and type(jog) == str # verificar modos

    if not condicao_esperada:
        raise ValueError('orbito: argumentos invalidos')

    else:
        jog_convertido = str_para_pedra(jog) # Conversão do jogador para inteiro.
        jog_adv = inverte_pedra(jog_convertido) # Conversão do jogador adversário.
        modos_computador = ('facil', 'normal')           
        print(f"Bem-vindo ao ORBITO-{n}.")
        if modo in modos_computador:
            print(f"Jogo contra o computador ({modo}).")
            if jog_convertido == 1:
                print("O jogador joga com 'X'.")
            else:
                print("O jogador joga com 'O'.")
        else:
            print(f"Jogo para dois jogadores.")

        tab_atual = cria_tabuleiro_vazio(n) # Criação do tabuleiro vazio.

        jogador_atual = str_para_pedra('X') # Inicialização do jogador das pretas pretas.
        
        representacao_tab_inicio = tabuleiro_para_str(tab_atual) # Representação do tabuleiro inicial.
        print(representacao_tab_inicio)
        

        while not eh_fim_jogo(tab_atual): # Enquanto o jogo não terminar.
            if modo in modos_computador:
                if jog_convertido == jogador_atual: # Ronda do jogador humano

                    print("Turno do jogador.")
                    escolha_posicao_jog = escolhe_movimento_manual(tab_atual) # Escolha da posição pelo jogador - manualmente.
                    tab_atual = coloca_pedra(tab_atual, escolha_posicao_jog, jog_convertido) # Marcação da posição escolhida pelo jogador, manualmente.

                
                else: # Ronda do jogador automático

                    print(f"Turno do computador ({modo}):") # Turno do computador.
                    # Escolha da posição pelo computador - de acordo com a estratégia escolhida.

                    posicao_auto = escolhe_movimento_auto(tab_atual,jog_adv, modo) 
                    tab_atual = coloca_pedra(tab_atual, posicao_auto, jog_adv) 
            else:
                pedra_jogador_str = pedra_para_str(jogador_atual)
                print(f"Turno do jogador '{pedra_jogador_str}'.")
                escolha_posicao_jog = escolhe_movimento_manual(tab_atual)
                tab_atual = coloca_pedra(tab_atual, escolha_posicao_jog, jogador_atual)

            tab_atual = roda_tabuleiro(tab_atual) # Rodar o tabuleiro.
            print(tabuleiro_para_str(tab_atual)) # Representação do tabuleiro após a marcação da posição.

            jogador_atual = inverte_pedra(jogador_atual) # Alternância dos jogadores.

            
        # Resultado final do jogo.
        jog_j_ganhou = False
        jog_adv_ganhou = False

        for posicao in obtem_posicoes_pedra(tab_atual, jog_convertido):

            if verifica_linha_pedras(tab_atual, posicao, jog_convertido, 2 * n):
                jog_j_ganhou = True
            
        for posicao in obtem_posicoes_pedra(tab_atual, jog_adv):
            if verifica_linha_pedras(tab_atual, posicao, jog_adv, 2 * n):
                jog_adv_ganhou = True
            
        if jog_j_ganhou == jog_adv_ganhou:
            print('EMPATE')
            return 0
        
        elif jog_j_ganhou:
            if modo in modos_computador:
                print('VITORIA')
            else:
                jog_convertido_str = pedra_para_str(jog_convertido)
                print(f"VITORIA DO JOGADOR '{jog_convertido_str}'") 
            return jog_convertido
        
        else:
            if modo in modos_computador:
                print('DERROTA')
            else:
                jog_convertido_str = pedra_para_str(jog_adv)
                print(f"VITORIA DO JOGADOR '{jog_convertido_str}'") 
            return jog_adv