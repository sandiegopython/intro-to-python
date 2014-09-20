def print_factors(age):
    for i in range(1, age + 1):
        if age % i == 0:
            print(i)
            
print_factors(32)