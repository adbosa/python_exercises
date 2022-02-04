def is_prime(num):
    for elemento in range(num-1, 2, -1):
        if num % elemento == 0:
            return False
    return True


user_num = int(input("Insira um número: "))
print(f"De 1 até {user_num}, são primos: ")
for i in range(1, user_num):
    if is_prime(i + 1):
        print(i + 1)
print()

