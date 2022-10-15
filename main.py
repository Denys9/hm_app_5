
try:
    start = int(input("Введіть початкове число - "))
    end = int(input("Введіть кінечне число - "))
    counter = 0
    for i in range(start, end) :
        counter = 0
        if i ==1:
            print(i,"\t", end = " " )
            continue
        for j in range(1, i+1):
            if i%j==0:
                counter+=1
        if counter==2:
           print(i, "\t", end = " ")

except Exception as ex:
    print(f'Eror information: {ex}')
