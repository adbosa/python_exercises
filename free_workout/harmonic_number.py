''' A harmonic number is defined by 
    Hn= 1 + 1/2 + 1/3 + ... + 1/n
    Let's try doing the sum right to left
    and left to right to see the difference. '''

def main(number):
    lr_sum = 0
    rl_sum = 0 # Left to Right / Right to Left
    for i in range(1, number+1):
        lr_sum += 1/i # in ascending order
        rl_sum += 1/((number+1)-i) # in descending order
        difference = rl_sum - lr_sum

    print(f'In Left/Right = {lr_sum}')
    print(f'In Right/Left = {rl_sum}')
    print(f'The difference between = {difference}')

main(100)

# continue on https://is.gd/0a3Nsh
