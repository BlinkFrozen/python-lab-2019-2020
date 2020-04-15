def pascal_triangle(n):
    array = []

    for row in range(1, n + 1):
        array.append(1)
        for i in range(row - 2, 0, -1):
            array[i] += array[i - 1]
        print(" ".join(map(str, array)))


def euler_triangle(n):
    for i in range(n + 1):
        for k in range(i + 1):
            print(calculate_euler(i, k), end=' ')
        print()


def calculate_euler(n, k):
    if k == 0:
        return 1
    elif k == n:
        return 0
    elif n - 1 == k:
        return 1
    else:
        return (k + 1) * calculate_euler(n - 1, k) + (n - k) * calculate_euler(n - 1, k - 1)
