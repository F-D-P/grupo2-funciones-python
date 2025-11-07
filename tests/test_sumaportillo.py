from funciones.sumaportillo import sumaportillo

def test_sumaportillo():
    assert sumaportillo(3, 5) == 8
    assert sumaportillo(-2, 2) == 0
    assert sumaportillo(0, 0) == 0