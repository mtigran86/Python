string_to_cut = input("Please, input some text here\n")
num = input("Please, input number\n")

try:
    num_of_sym_to_cut = int(num)
    new_text = string_to_cut[num_of_sym_to_cut:]
    if num_of_sym_to_cut > len(string_to_cut):
        print("\n---===   Тhe entered number is greater than the number of characters in the string   ===---")
    elif num_of_sym_to_cut < 0:
        print("\n---===   Тhe entered number is negative.   ===---")
        print(f"Result: {new_text}")
    else:
        print(f"\nResult: {new_text}")
except ValueError:
    print("\n---===   Please, input only integers   ===---")