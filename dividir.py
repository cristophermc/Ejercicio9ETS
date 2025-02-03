def dividir(a: int, b: int) -> int:
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a // b  # División entera