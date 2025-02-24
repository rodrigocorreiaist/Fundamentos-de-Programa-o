# TAD Intersecão

Letras = "ABCDEFGHIJKLMNOPQRS"


def cria_intersecao(col, lin):
    """A função recebe um caracter e um inteiro, verifica se são argumentos válidos e retorna uma interseção"""

    if type(col) != str or type(lin) != int:
        raise ValueError("cria_intersecao: argumentos invalidos")
    elif col not in Letras or 1 > lin > 19:
        raise ValueError("cria_intersecao: argumentos invalidos")
    elif len(col) != 1:
        raise ValueError("cria_intersecao: argumentos invalidos")
    else:
        intersecao = (col, lin)
        return intersecao


def obtem_col(i):
    """Devolve a coluna da interseção"""

    return i[0]


def obtem_lin(i):
    "Devolve a linha da interseção"

    if len(i) == 3:
        return i[1] + i[2]
    if len(i) == 2:
        return i[1]


def eh_intersecao(arg):
    """Verifica se o arg dado é interseção"""

    return (
        isinstance(arg, tuple)
        and len(arg) == 2
        and isinstance(obtem_col(arg), str)
        and len(arg[0]) == 1
        and arg[0].isalpha()
        and arg[0].isupper()
        and isinstance(obtem_lin(arg), int)
    )


def intersecoes_iguais(i1, i2):
    """Verifica se as duas interseções dadas são iguais"""

    if i1 == i2:
        return True
    else:
        return False


def intersecao_para_str(i):
    """Converte a interseção dada para string"""

    novoi = str(obtem_col(i)) + str(obtem_lin(i))
    return novoi


def str_para_intersecao(s):
    """Converte uma string para interseção"""

    i = (obtem_col(s), int(obtem_lin(s)))
    return i


def obtem_intersecoes_adjacentes(i, l):
    """Devolve um tuplo com as interseções adjacacentes a i"""

    letra = obtem_col(i)
    numero = obtem_lin(i)

    numerogoban = obtem_lin(l)

    indice_letra = ord(obtem_col(l)) - ord("A")
    nlinhas = indice_letra + 1
    ncolunas = numerogoban
    intersecoes_adjacentes = ()

    intersecao_acima = (letra, numero - 1)
    intersecao_esquerda = (chr(ord(letra) - 1), numero)
    intersecao_direita = (chr(ord(letra) + 1), numero)
    intersecao_abaixo = (letra, numero + 1)

    if letra == "A" and numero == nlinhas:
        intersecoes_adjacentes = (intersecao_acima, intersecao_direita)

    if letra == "A" and numero < nlinhas and numero > 1:
        intersecoes_adjacentes = (
            intersecao_acima,
            intersecao_direita,
            intersecao_abaixo,
        )

    if letra == "A" and numero == 1:
        intersecoes_adjacentes = (intersecao_direita, intersecao_abaixo)

    if letra > "A" and nlinhas > numero > 1:
        intersecoes_adjacentes = (
            intersecao_acima,
            intersecao_esquerda,
            intersecao_direita,
            intersecao_abaixo,
        )

    if letra > "A" and numero == 1:
        intersecoes_adjacentes = (
            intersecao_esquerda,
            intersecao_direita,
            intersecao_abaixo,
        )
    if letra > "A" and numero == nlinhas:
        intersecoes_adjacentes = (
            intersecao_acima,
            intersecao_esquerda,
            intersecao_direita,
        )

    if letra == (chr(ord("A") + ncolunas - 1)) and numero == nlinhas:
        intersecoes_adjacentes = (intersecao_acima, intersecao_esquerda)
    if letra == (chr(ord("A") + ncolunas - 1)) and numero == 1:
        intersecoes_adjacentes = (intersecao_esquerda, intersecao_abaixo)
    if letra == (chr(ord("A") + ncolunas - 1)) and nlinhas > numero > 1:
        intersecoes_adjacentes = (
            intersecao_acima,
            intersecao_esquerda,
            intersecao_abaixo,
        )

    return intersecoes_adjacentes


def ordena_intersecoes(t):
    """Recebe um tuplo de interseções e devolve-o de acordo com a ordem de leitura"""

    def comparador(tup):
        return tup[1], tup[0]

    def comparacao(tup1, tup2):
        return (comparador(tup1) > comparador(tup2)) - (
            comparador(tup1) < comparador(tup2)
        )

    tuplos_ordenados = sorted(t, key=comparador)
    return tuple(tuplos_ordenados)


# TAD pedra


def cria_pedra_branca():
    """Devolve a pedra pertencente ao jogador branco"""

    return "O"


def cria_pedra_preta():
    """Devolve a pedra pertencente ao jogador preto"""

    return "X"


def cria_pedra_neutra():
    """Devolve uma pedra neutra"""

    return "."


def eh_pedra(arg):
    """Verifica se o arg é uma pedra"""

    return arg in ("O", "X", ".")


def eh_pedra_branca(p):
    """Verfica se a pedra pertence ao jogador branco"""
    if p == cria_pedra_branca():
        return True
    else:
        return False


def eh_pedra_preta(p):
    """Verifica se a pedra pertence ao jogador preto"""

    if p == cria_pedra_preta():
        return True
    else:
        return False


def pedras_iguais(p1, p2):
    """Verifica se 2 pedras são iguais"""

    if p1 == p2:
        return True
    else:
        return False


def pedra_para_str(p):
    """Devolce a cadeia de caracteres consoante o jogador dono da pedra"""

    if eh_pedra(p):
        return p
    else:
        return "."


def eh_pedra_jogador(p):
    """Verifica se a pedra é de um jogador"""

    if p != ".":
        return eh_pedra(p) and (eh_pedra_branca(p) or eh_pedra_preta(p))


# TAD Goban


def cria_goban_vazio(n):
    """Devolve um goban vazio de tamanho n x n"""

    if n not in (9, 13, 19) or not isinstance(n, int):
        raise ValueError("cria_goban_vazio: argumento invalido")
    linha_vazia = ["."] * n
    goban = [linha_vazia.copy() for _ in range(n)]
    return goban


def cria_goban(n, ib, ip):
    """Devolve um goban de tamannho n x n com as interseções ocupadas com pedras"""

    if not isinstance(n, int) or n not in (9, 13, 19):
        raise ValueError("cria_goban: argumentos invalidos")

    if not isinstance(ib, tuple) or not isinstance(ip, tuple):
        raise ValueError("cria_goban: argumentos invalidos")

    def dentro_limites(intersecao):
        letra, numero = intersecao
        return "A" <= letra <= chr(ord("A") + n - 1) and 1 <= numero <= n

    if any(not dentro_limites(intersecao) for intersecao in ib + ip):
        raise ValueError("cria_goban: argumentos invalidos")
    if any(
        not isinstance(intersecao, tuple) or len(intersecao) != 2
        for intersecao in ib + ip
    ):
        raise ValueError("cria_goban: argumentos invalidos")

    if any(
        not intersecao[0].isalpha()
        or not intersecao[0].isupper()
        or not isinstance(intersecao[1], int)
        or intersecao[1] < 1
        for intersecao in ib + ip
    ):
        raise ValueError("cria_goban: argumentos invalidos")

    if len(ib) != len(set(ib)) or len(ip) != len(set(ip)):
        raise ValueError("cria_goban: argumentos invalidos")

    if any(intersecao in ip for intersecao in ib):
        raise ValueError("cria_goban: argumentos invalidos")

    # Funções auxiliares
    def obtem_letra(intersecao):
        return ord(obtem_col(intersecao)) - ord("A")

    # Cria o tabuleiro vazio
    tabuleiro = cria_goban_vazio(n)

    # Coloca as pedras no tabuleiro
    for intersecao in ib:
        coluna_br, linha_br = obtem_letra(intersecao), obtem_lin(intersecao)
        tabuleiro[coluna_br][linha_br - n - 1] = "O"

    for intersecao in ip:
        coluna_pr, linha_pr = obtem_letra(intersecao), obtem_lin(intersecao)
        tabuleiro[coluna_pr][linha_pr - n - 1] = "X"

    return tabuleiro


def cria_copia_goban(t):
    """Recebe um goban e devolve uma cópia"""

    copia = cria_goban_vazio(len(t))
    for i in range(len(t)):
        for j in range(len(t)):
            copia[i][j] = t[i][j]
    return copia


def obtem_ultima_intersecao(g):
    """Função que obtém a última interseção do goban"""
    associacao = {}
    letra = "A"

    for tuplo in g:
        associacao[letra] = tuplo
        letra = chr(ord(letra) + 1)

    ultimaletra = chr(ord(letra) - 1)
    ultelemento = len(g[0])
    intersecao = (ultimaletra, ultelemento)

    return intersecao


def obtem_pedra(g, i):
    """Devolve a pedra corresponde à interseção"""

    n = len(g)
    col, linha = obtem_col(i), obtem_lin(i) - n
    col = ord(col) - ord("A")
    return g[col][linha - 1]


def obtem_cadeia(g, i):
    """Devolve um tuplo formado pela cadeia de pedras que passa pela interseção i"""

    def dentro_limites(v, h):
        return 0 <= v < ncolunas and 0 <= h < nlinhas

    def vizinhos(v, h):
        return [(v - 1, h), (v + 1, h), (v, h - 1), (v, h + 1)]

    ncolunas = len(g)
    nlinhas = len(g[0])

    letra = obtem_col(i)
    numero = obtem_lin(i)
    v, h = ord(letra) - ord("A"), numero - 1

    visitados = {(v, h)}
    to_check = [(v, h)]

    while to_check:
        pos = to_check.pop()
        for vizinho_v, vizinho_h in vizinhos(*pos):
            if (
                dentro_limites(vizinho_v, vizinho_h)
                and g[vizinho_v][vizinho_h] == obtem_pedra(g, i)
                and (vizinho_v, vizinho_h) not in visitados
            ):
                visitados.add((vizinho_v, vizinho_h))
                to_check.append((vizinho_v, vizinho_h))

    cadeia = [((chr(v + ord("A")), h + 1)) for v, h in sorted(visitados)]
    return ordena_intersecoes(tuple(cadeia))


def coloca_pedra(g, i, p):
    """Modifica o goban, colocando a pedra p na interseção i"""

    coluna = ord(obtem_col(i).upper()) - ord("A")
    g[coluna][obtem_lin(i) - 1] = p
    return g


def remove_pedra(g, i):
    """Modifica o goban, removendo a pedra p da interseção i"""

    coluna = ord(obtem_col(i).upper()) - ord("A")
    g[coluna][obtem_lin(i) - 1] = "."
    return g


def remove_cadeia(g, t):
    """Modifica o goban, removendo a cadeia t do goban"""

    for tuplos in t:
        coluna = ord(obtem_col(tuplos).upper()) - ord("A")
        g[coluna][obtem_lin(tuplos) - 1] = "."
    return g


def eh_goban(g):
    """Verifica se o argumento dado é um goban"""

    if not isinstance(g, list):
        return False
    if len(g) < 1:
        return False
    if not isinstance(g[0], list):
        return False
    if len(g[0]) < 1:
        return False
    rows = len(g)
    cols = len(g[0])

    for row in g:
        if len(row) != cols:
            return False
        for cell in row:
            if cell not in ("O", "X", "."):
                return False
    return True


def eh_intersecao_valida(g, i):
    """Verifica se i é uma interseção válida para o goban dado"""

    letra, numero = i
    if letra in Letras[: len(g)]:
        for tuplos in g:
            if len(letra) == 1 and 0 <= numero <= len(tuplos):
                return True
    return False


def gobans_iguais(g1, g2):
    """Verifica se os 2 gobans dados são iguais"""

    if not eh_goban(g1) or not eh_goban(g2):
        return False
    if g1 == g2:
        return True


def goban_para_str(g):
    """Devolve a cadeia de caracteres que representa o goban dado"""

    nlinhas = len(g)
    ncolunas = len(g[0])

    resfinal = " "
    resfinal += "  " + " ".join(Letras[:ncolunas]) + "\n"

    for linha in range(nlinhas - 1, -1, -1):
        resfinal += f"{linha + 1:2}"
        for coluna in range(ncolunas):
            if g[coluna][linha] == "O":
                resfinal += " O"
            elif g[coluna][linha] == "X":
                resfinal += " X"
            elif g[coluna][linha] == ".":
                resfinal += " ."
        resfinal += f"  {linha + 1}" + "\n"

    resfinal += "   " + " ".join(Letras[:ncolunas])

    return resfinal


def obtem_territorios(g):
    """Devolve um tuplo formado por tuplos com as interseções de cada território de g"""

    def dentro_limites(v, h):
        return 0 <= v < ncolunas and 0 <= h < nlinhas

    def vizinhos(v, h):
        return [(v - 1, h), (v + 1, h), (v, h - 1), (v, h + 1)]

    ncolunas = len(g)
    nlinhas = len(g[0])

    tipo = "."

    visitados = set()
    territorios = []

    for v in range(ncolunas):
        for h in range(nlinhas):
            if g[v][h] == "." and (v, h) not in visitados:
                territorio = []
                to_check = [(v, h)]
                while to_check:
                    pos = to_check.pop()
                    territorio.append((chr(pos[0] + ord("A")), pos[1] + 1))
                    visitados.add(pos)
                    for vizinho_v, vizinho_h in vizinhos(*pos):
                        if (
                            dentro_limites(vizinho_v, vizinho_h)
                            and g[vizinho_v][vizinho_h] == tipo
                            and (vizinho_v, vizinho_h) not in visitados
                        ):
                            to_check.append((vizinho_v, vizinho_h))
                territorios.append(sorted(territorio, key=lambda x: (x[1], x[0])))

    return tuple(
        tuple(territorio)
        for territorio in sorted(territorios, key=lambda x: (x[0][1], x[0][0]))
    )


def obtem_adjacentes_diferentes(goban, t):
    """Devolve o tuplo ordenado formado pelas interseções do tuplo t consoante forem livres ou ocupadas"""

    def eh_pedra_livre(goban, intersecao):
        v = ord(obtem_col(intersecao).upper()) - ord("A")
        return goban[v][len(goban) - obtem_lin(intersecao)] == "."

    def obtem_adjacentes(goban, intersecao):
        v, h = obtem_col(intersecao), obtem_lin(intersecao)
        v = ord(v.upper()) - ord("A")
        intersecoes_adjacentes = []
        for i, j in [(v - 1, h), (v + 1, h), (v, h - 1), (v, h + 1)]:
            if 0 <= i < len(goban) and 0 <= j < len(goban[0]):
                intersecoes_adjacentes.append((i, j))
        return [(chr(i + ord("A")), len(goban) - j) for i, j in intersecoes_adjacentes]

    adjacentes = set()
    for intersecao in t:
        for adjacente in obtem_adjacentes(goban, intersecao):
            if eh_pedra_livre(goban, intersecao):
                if not eh_pedra_livre(goban, adjacente):
                    adjacentes.add(adjacente)
            elif not eh_pedra_livre(goban, intersecao):
                if eh_pedra_livre(goban, adjacente):
                    adjacentes.add(adjacente)
    return tuple(sorted(adjacentes))


def jogada(g, i, p):
    """Modifica o goban, colocando a pedra do jogador p na interseçao i, removendo as pedras do outro jogador pertencentes às cadeias adjacentes de i sem liberdades"""

    def eh_pedra_livre(goban, intersecao):
        v, h = obtem_col(intersecao), obtem_lin(intersecao)
        v = ord(v.upper()) - ord("A")
        return goban[v][len(goban) - h] == "."

    def remove_cadeia_sem_liberdades(goban, cadeia, jogador):
        for intersecao in cadeia:
            v, h = obtem_col(intersecao), obtem_lin(intersecao)
            v = ord(v.upper()) - ord("A")
            if goban[v][len(goban) - h] == jogador:
                goban[v][len(goban) - h] = "."
        return goban

    v, h = obtem_col(i), obtem_lin(i)
    v = ord(v.upper()) - ord("A")

    coloca_pedra(g, i, p)

    cadeia = obtem_cadeia(g, i)

    # Remove cadeias sem liberdades do jogador contrário adjacentes à interseção
    if eh_pedra_branca:
        jogador_contrario = "X"
    else:
        jogador_contrario = "O"

    for adjacente in obtem_adjacentes_diferentes(g, cadeia):
        adjacente_v, adjacente_h = obtem_col(adjacente), obtem_lin(adjacente)
        adjacente_v = ord(adjacente_v.upper()) - ord("A")
        if g[adjacente_v][len(g) - adjacente_h] == jogador_contrario:
            cadeia_adjacente = obtem_cadeia(g, adjacente)
            if all(
                not eh_pedra_livre(g, intersecao) for intersecao in cadeia_adjacente
            ):
                g = remove_cadeia_sem_liberdades(g, cadeia_adjacente, jogador_contrario)

    return g


def obtem_pedras_jogadores(goban):
    """Devolve o tuplo com 2 inteiros, correspondeste ao número de pedras colocadas por jogador no goban"""

    contador_branco, contador_preto = 0, 0

    for linha in goban:
        for intersecao in linha:
            if eh_pedra_branca(intersecao):
                contador_branco += 1
            elif eh_pedra_preta(intersecao):
                contador_preto += 1

    return (contador_branco, contador_preto)


def calcula_pontos(goban):
    """Devolve as pontuações de cada jogador"""

    # Inicializa contadores de pontos para jogadores branco (O) e preto (X)
    pontos_branco, pontos_preto = 0, 0

    # Percorre o goban e conta as pedras de cada jogador para calcular os pontos
    for linha in goban:
        for intersecao in linha:
            if eh_pedra_branca(intersecao):
                pontos_branco += 1
            elif eh_pedra_preta(intersecao):
                pontos_preto += 1

    # ver territorios de cada jogaodor
    return (pontos_branco, pontos_preto)


def eh_jogada_legal(g, i, p, l):
    """Verifica se a jogada é legal"""

    # Criar um novo Goban para simular a jogada
    ng = cria_copia_goban(g)

    coloca_pedra(ng, i, p)

    direcoes = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def tem_liberdade(g, letra, numero, p):
        def busca_liberdade(l, n):
            # Verifica se a interseção está dentro do tabuleiro e se é uma interseção livre
            return 0 <= l < len(g) and 0 <= n < len(g) and g[n][l] == "."

        # Verifica se a pedra tem liberdade em pelo menos uma das direções adjacentes
        for dx, dy in direcoes:
            nova_letra, novo_numero = letra + dx, numero + dy
            if busca_liberdade(nova_letra, novo_numero):
                return True

    # Verificar a regra do suicídio
    if not tem_liberdade(ng, obtem_col(i), obtem_lin(i), p):
        return False
    # Verificar a regra da repetição (Ko)
    if ng == l:
        return False

    return False


"""rever aqui"""


def turno_jogador(g, p, l):
    """Função que permite dar os inputs para cada jogada ao jogador p"""

    while True:
        print(f"Escreva uma intersecao ou 'P' para passar  {p}")
        escolha = input().strip().upper()

        if escolha == "P":
            return False  # Jogador passou a vez
        elif eh_jogada_legal(g, str(escolha), p, l):
            coloca_pedra(obtem_col(escolha), obtem_lin(escolha), p)
            return True  # Jogada realizada com sucesso
        else:
            print("Jogada inválida. Tente novamente.")


def go(n, tb, tn):
    """Função principal que permite jogar o jogo go"""

    jogador_atual = "B"  # Inicia com o jogador branco
    ultimo_tabuleiro = None
    g = cria_goban_vazio(n)
    while True:
        print(f"Branco (O) tem {calcula_pontos('O')} pontos")
        print(f"Preto (X) tem {calcula_pontos('X')} pontos")
        print(goban_para_str(g))

        while True:
            escolha = (
                input(
                    f"Jogador {jogador_atual}: Escreva uma intersecao ou 'P' para passar [{jogador_atual}]: "
                )
                .strip()
                .upper()
            )
            if escolha == "P":
                break
            intersecao = escolha
            if jogada(g, intersecao, jogador_atual):
                break
            else:
                print("Jogada inválida. Tente novamente.")

        if escolha == "P" and ultimo_tabuleiro == g:
            # Ambos os jogadores passaram consecutivamente
            return calcula_pontos("O") > calcula_pontos("X")

        jogador_atual = (
            cria_pedra_branca()
            if jogador_atual == cria_pedra_preta
            else cria_pedra_preta()
        )
        ultimo_tabuleiro = cria_copia_goban(g)
        # Mantém uma cópia do estado atual do tabuleiro
