programming_dictionary = {
    "Bug": "An error in a program that prevents the prgram from running as expected.",
    "Function": "A place of code that you can easily call over and over again.",
}

# Pegar items de um dicionario
# print(programming_dictionary["Function"])

# Adicionando novos items em um dicionario
programming_dictionary["Loop"] = "The action of doing something over and over again."
# print(programming_dictionary)

# Criando um dicionario vazio
empty_dictionary = {}

# Limpando um dicionario existinte
# programming_dictionary = {}
# print(programming_dictionary)

# Editando um item em um dicionario
# programming_dictionary["Bug"] = "A moth in you computer."
# print(programming_dictionary)

# Loop em um dicionario
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
