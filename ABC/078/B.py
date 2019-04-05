x, y, z = map(int, input().split())
print(max(0, (x - 2 * z - y) // (y + z) + 1))
