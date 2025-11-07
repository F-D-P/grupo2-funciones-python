from funciones.potenciaTempran import potenciaTempran

def test_potenciaTempran():
    assert potenciaTempran(2, 3) == 8
    assert potenciaTempran(5, 0) == 1
    assert potenciaTempran(3, -2) == 1/9