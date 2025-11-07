def potenciaTempran(base, exponente):
    """Devuelve la potencia de un número elevado a otro."""
    if exponente < 0:
        return 1 / (base ** -exponente)
    else:
        return base ** exponente