num1 = input("Please, input 1st number \n")
num2 = input("Please, input 2nd number \n")

if num1.isdigit and num2.isdigit:
    number_1 = int(num1)
    number_2 = int(num2)
    #product
    print(f"{number_1} * {number_2} = {number_1 * number_2}")
    #sum
    print(f"{number_1} + {number_2} = {number_1 + number_2}")
    #subtract
    print(f"{number_1} - {number_2} = {number_1 - number_2}")
    #exponentiation
    print(f"{number_1} ** {number_2} = {number_1 ** number_2}")
else:
    print("Please, input only numbers")

if num2 ==0:
    print("Devision by 0 !")
else:
    #division
    print(f"{number_1} / {number_2} = {number_1 / number_2}")
    #remainder
    print(f"{number_1} // {number_2} = {number_1 // number_2}")    
    #remainder
    print(f"{number_1} % {number_2} = {number_1 % number_2}")