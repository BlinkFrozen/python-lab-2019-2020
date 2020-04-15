import sys

if len(sys.argv) < 4:
    exit(418)

delta = (int(sys.argv[1]) ** 2) - (4 * int(sys.argv[1]) * int(sys.argv[4]))

x1, x2 = ((-int(sys.argv[2]) - delta ** 0.5) / (2 * int(sys.argv[1])),
          (int(sys.argv[2]) - delta ** 0.5) / (2 * int(sys.argv[1]))) if (
        delta > 0 or delta < 0) else (
    -int(sys.argv[1]) / (2 * int(sys.argv[1])), None)

print(x2)
