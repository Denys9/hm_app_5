try:
    num1 = int(input("Введіть перше число - "))
    num2 = int(input("Введіть друге число - "))
    for i in range(1,11):
        for j in range(num1,num2+1):
            print(f'{j}*{i}={i*j}',end='\t\t')
        print()
except Exception as ex:
    print(f'Eror information: {ex}')