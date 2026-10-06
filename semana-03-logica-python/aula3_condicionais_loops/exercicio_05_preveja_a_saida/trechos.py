# Rode este arquivo só DEPOIS de escrever suas previsões em README.md

print("--- Trecho A ---")
for i in range(1, 6):
    if i % 2 == 0:
        continue
    print(i)

print("--- Trecho B ---")
n = 0
while n < 10:
    n += 3
    if n == 6:
        break
    print(n)

print("--- Trecho C ---")
total = 0
for i in range(1, 5):
    if i == 3:
        continue
    total += i
print(total)

print("--- Trecho D ---")
for i in range(3):
    for j in range(2):
        print(i, j)
