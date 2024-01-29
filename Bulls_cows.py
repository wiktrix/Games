from random import choice

z = '0123456789'
x = choice(z[1:10])
for i in range(3):
    z = ''.join(z.split(x[i]))
    x += choice(z)

n = 0

while True:
    guess = input('Print your four-digit number: ')
    n += 1
    bulls = 0
    cows = 0
    for i in range(4):
        if x[i] == guess[i]:
            bulls += 1
        elif guess[i] in x:
            cows += 1
    print(guess + ' has ' + str(bulls) + ' bull(s) and ' + str(cows) + ' cow(s).')
    if bulls == 4:
        print(f'you won in {n} moves.')
        break