from re import X


user_input = input("Please enter text an press ENTER\n")

filter = user_input.split()

def filter_integers(string_to_filter):
    export_list = []
    for i in range(len(string_to_filter)):
        try:
            if type(int(string_to_filter[i])) is int and int(string_to_filter[i]) > 0:
                export_list.append(string_to_filter[i])
        except ValueError:
            x=X
    return export_list


print(filter_integers(filter))