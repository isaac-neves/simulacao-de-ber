import numpy as np 

# esta função recebe do transmissor o símbolo e a quantidade de bits por símbolo, retornando o sinal acrescido do ruido baseado no canal escolhido e na relação entre E_b e dep do ruido
def aplicar_canal(s, ebn0_db, k, canal, rng):

    s = np.asarray(s, dtype=complex)

    if s.ndim != 1:
        raise ValueError("O sinal deve ser unidimensional")

    if k not in (1, 2, 4):
        raise ValueError("Valor de k inválido")

    canal = canal.lower()

    # 1. Conversão de Eb/N0 para escala linear
    gamma_b = 10 ** (ebn0_db / 10)

    # 2. Cálculo de N0
    N0 = 1 / (k * gamma_b)

    # 3. Variância por dimensão
    sigma = np.sqrt(N0 / 2)  
    s = np.asarray(s, dtype=complex)

    if s.ndim != 1:
        raise ValueError("O sinal deve ser unidimensional")

    if k not in (1, 2, 4):
        raise ValueError("Valor de k inválido")

    canal = canal.lower()

    # 4. Geração do ruído complexo
    ruido = sigma * (
        rng.standard_normal(len(s))
        + 1j * rng.standard_normal(len(s))
    )

    # 5. Escolha do modelo de canal
    if canal == "awgn":

        h = np.ones(len(s), dtype=complex)

    elif canal == "rayleigh":

        h = (
            rng.standard_normal(len(s))
            + 1j * rng.standard_normal(len(s))
        ) / np.sqrt(2)

    else:
        raise ValueError("Canal inválido")

    # 6. Sinal recebido
    r = h * s + ruido

    return r, h
