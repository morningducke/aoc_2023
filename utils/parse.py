from typing import Iterator


def parse_lines(file_name: str) -> Iterator[str]:
    with open(file_name, "r") as f:
        for line in f:
            yield line.rstrip()

def parse_matrix(file_name: str) -> list[str]:
    return [line for line in parse_lines(file_name)]

def parse_matrices(file_name: str, sep="\n") -> Iterator[list[str]]:
    with open(file_name, "r") as f:
        matr = []
        for line in f:
            if line == sep:
                yield matr
                matr = []
            else:
                matr.append(line.rstrip())
        yield matr

    

