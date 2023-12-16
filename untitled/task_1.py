print("Введите число: ")
def print_pseudo_chessboard(size):
    for i in range(size, 0, -1):
        for j in range(1, size + 1):
            print(chr(j + 64) + str(i), end=' ')
        print()

size = int(input())
print_pseudo_chessboard(size)
