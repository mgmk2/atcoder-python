s = input()
w = ['Sunny', 'Cloudy', 'Rainy']
for i, wi in enumerate(w):
    if s == wi:
        idx = (i + 1) % 3
        break
print(w[idx])
