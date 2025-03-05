n = int(input())
sequence = ""
number = 1

while len(sequence) < n:
    sequence += str(number) * number
    number += 1

elements = sequence[:n]

print(f"Первые {n} элементов последовательности: {elements}")
