numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
  for j in range(2, i + 1):
    if i % j == 0 and i != j:
      not_primes.append(i)
      break
    elif i == j:
      primes.append(i)
    else:
      continue
print('Простые числа: ', primes)
print('Не простые числа: ', not_primes)
