#Ввести число, вивести його розряди та їх множники.
number = int(input('Введіть своє число'))
digits = []          #числа
multipliers = []     #множинники
while number > 0:
    digit = number % 10
    digits.append(digit)
    multiplier = 10 ** len(str(number)) // 10
    multipliers.append(multiplier)
    number //= 10
multipliers.reverse()
for i in range(len(digits)):
    print(digits[i], "*", multipliers[i], "=", digits[i] * multipliers[i])