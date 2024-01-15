def transpose(matr: list[str]) -> list[str]:
    return ["".join(row) for row in zip(*matr)]

def row_reverse(matr: list[str]) -> list[str]:
    return ["".join(reversed(row)) for row in matr]