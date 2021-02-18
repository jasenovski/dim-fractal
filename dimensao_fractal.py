import numpy as np
import metodo_minimos_quadrados as mmq


def dim_frac(frame, dims_frame):

    """É recomendado utilizar este algoritmo para frames quadrados"""

    eixo_h = [0]
    eixo_v = [0]
    num_divisoes = int(np.log2(dims_frame[0]))
    for i in range(num_divisoes):
        E = 1/2 ** (i + 1)
        N = 0
        salto = int(dims_frame[0] * E)
        for j in range(int(1 / E)):
            # 'j' corre na direção das linhas
            for k in range(int(1 / E)):
                # 'k' corre na direção das colunas

                # 'n' é a contagem de pixels que valem 1 (um). Sendo que os pixels que valem 1 representam o objeto
                n = 0
                for l in range(salto):
                    num_linha = j * salto + l
                    ini_col = k * salto
                    fim_col = (k * salto) + salto
                    linha = frame[num_linha][ini_col:fim_col]
                    n = n + np.sum(linha)
                    if n > 0:
                        break
                if n > 0:
                    N = N + 1

        eixo_h.append(np.log2(1 / E))

        if N > 0:
            eixo_v.append(np.log2(N))
        else:
            eixo_v.append(N)

    coef_ang, coef_lin = mmq.mmq_reta(np.array(eixo_h), np.array(eixo_v))

    if coef_ang == -0:
        coef_ang = 0

    return coef_ang
