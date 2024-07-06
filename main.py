print("1st program")
print(9 ** 0.5 * 5)

print("2nd program")
print(9.99 > 9.98 and 1000 != 1000.1)

print("3rd program")
print((1234 // 10 % 100) + (5678 // 10 % 100))

print("4th program")
print(int(13.42) == int(42.13 * 100) % 100)

print("4th program")
print((int(13.42) == int(42.13 * 100) % 100) or (int(13.42 * 100) % 100) == int(42.13))

print("4th program 2nd ver")
print((int(13.42) == int(42.13 * 100) % 100) and (int(13.42 * 100) % 100) != int(42.13))  #and - строгий оператор, поэтому при изменении на != будет значение False
print((int(13.42) == int(42.13 * 100) % 100) or (int(13.42 * 100) % 100) != int(42.13))   #or - не строгий оператор, при наличии хотя бы одного True значение будет True
