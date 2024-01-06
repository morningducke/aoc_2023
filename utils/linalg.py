def transpose(matr: list[str]) -> list[str]:
    return ["".join(row) for row in zip(*matr)]