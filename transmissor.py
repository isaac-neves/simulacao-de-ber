import numpy as np
# Importante para teste. Baseado nessa semente
rng = np.random.default_rng(42)

# bits_por_simbolo(mod) retorna a quantidade de bits por símbolo dependendo da quantidade símbolos possíveis
# k = log_2(M), sendo M quantidade de símbolos possíveis e k o quantidade de bits por símbolo
def bits_por_simbolo(mod):
    mod = mod.lower()

    if mod =="bpsk":
        return 1
    elif mod =="qpsk":
        return 2
    elif mod=="16qam":
        return 4
    else:
        raise ValueError("Modulção Inválida")

# gera uma quantidade de n bits aleatórios
def gerar_bits(n, rng):
    return rng.integers(0, 2, size=n)

# esta função mapeia os locais onde os bits vão ficar mantendo a conveção da energia média por símbolo igual a 1
def modular(bits, mod):

    bits = np.asarray(bits)

    if not np.all(np.isin(bits, [0, 1])):
        raise ValueError("Os bits devem ser 0 ou 1")

    k = bits_por_simbolo(mod)

    if len(bits) % k != 0:
        raise ValueError("Quantidade de bits incompatível com a modulação")

    mod = mod.lower()

    # BPSK
    if mod == "bpsk":

        simbolos = 1 - 2 * bits

    # QPSK
    elif mod == "qpsk":

        grupos = bits.reshape(-1, 2)

        I = 1 - 2 * grupos[:, 0]
        Q = 1 - 2 * grupos[:, 1]

        simbolos = (I + 1j * Q) / np.sqrt(2)

    # 16-QAM
    elif mod == "16qam":

        grupos = bits.reshape(-1, 4)

        niveis = np.array([3, 1, -3, -1])

        I = niveis[2 * grupos[:, 0] + grupos[:, 1]]
        Q = niveis[2 * grupos[:, 2] + grupos[:, 3]]

        simbolos = (I + 1j * Q) / np.sqrt(10)

    return np.asarray(simbolos, dtype=complex)
