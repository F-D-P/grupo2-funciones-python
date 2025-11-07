def potencia(base, exponente):
    if exponente < 0:
        return 1 / potencia(base, -exponente)
    else:
        return potencia(base, exponente)
