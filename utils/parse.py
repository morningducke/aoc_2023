def parse_lines(file_name: str):
    with open(file_name, "r") as f:
        for line in f:
            yield line.rstrip()

def parse_matrix(file_name: str) -> list[str]:
    return [line for line in parse_lines(file_name)]
    

