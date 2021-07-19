"""Сканирование лунной поверхности."""
import os


def read_file(path: str) -> list:
    """Чтение из файла."""
    with open(path, "r") as file:
        data = file.readlines()
    data = [s.rstrip("\n") for s in data]
    matrix = list()
    for string in data:
        line = [int(i) for i in string.split()]
        matrix.append(line)
    return matrix


def smooth_surface(i: int, j: int, n: int, m: int, matrix: list) -> None:
    """Сглаживание поверхности."""
    if i < 0 or j < 0 or i >= n or j >= m:
        return
    if matrix[i][j] == 0:
        return
    else:
        matrix[i][j] = 0
    smooth_surface(i + 1, j, n, m, matrix)
    smooth_surface(i, j + 1, n, m, matrix)
    smooth_surface(i - 1, j, n, m, matrix)
    smooth_surface(i, j - 1, n, m, matrix)


def calculate(matrix: list) -> int:
    """Подсчет кратеров."""
    crater_counter = 0
    n = len(matrix)
    m = len(matrix[0])
    if n == 0:
        return 0
    for i in range(0, n):
        for j in range(0, m):
            if matrix[i][j] == 1:
                crater_counter += 1
                smooth_surface(i, j, n, m, matrix)
    return crater_counter


if __name__ == "__main__":
    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "data.txt")
    data = read_file(filename)
    print(calculate(data))
