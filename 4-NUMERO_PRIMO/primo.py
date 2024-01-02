number = input("Escribe un número: ")
number = int(number)

num_list = list(range(2,number))
#print(type(num_list))
#print(num_list)

for i in num_list:
    if number % i == 0:
        print("El número no es primo, porque es divisible por " + str(i))
        break
else:
    print("El número es PRIMO")
    






    # if i == number:
    #     continue
    # elif number % i == 0:
    #     print("El número seleccionado no es primo " + str(i))
    #     break
    # else:
    #     print("Es un número PRIMO ")