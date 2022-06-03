user_input = input("Please input some text and press <ENTER>\n")

output = ""
my_list = list(user_input)
string_len = len(user_input)
x = 0

while x < string_len:
    if x % 2:
        output = output + my_list[x]
    x+=1

print(output)