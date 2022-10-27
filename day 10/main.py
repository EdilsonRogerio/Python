def format_name(f_name, l_name):
    f = f_name.title()
    l = l_name.title()
    return f"Hello {f} {l}!"

f_name = input("First name: ")
l_name = input("Last name: ")

formated_full_name = format_name(f_name=f_name, l_name=l_name)

print(formated_full_name)