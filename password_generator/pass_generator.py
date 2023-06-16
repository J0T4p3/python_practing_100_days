"""
    My python password generator CLI tool.
"""
import random

special_chars = [
    33,
    34,
    35,
    36,
    37,
    38,
    39,
    40,
    41,
    42,
    43,
    44,
    45,
    46,
    47,
    58,
    59,
    60,
    61,
    62,
    63,
    64,
    91,
    92,
    93,
    94,
    95,
    96,
    123,
    124,
    125,
    126,
]
upper_case_chars = [
    65,
    66,
    67,
    68,
    69,
    70,
    71,
    72,
    73,
    74,
    75,
    76,
    77,
    78,
    79,
    80,
    81,
    82,
    83,
    84,
    85,
    86,
    87,
    88,
    89,
    90,
]
lower_case_chars = [
    97,
    98,
    99,
    100,
    101,
    102,
    103,
    104,
    105,
    106,
    107,
    108,
    109,
    110,
    111,
    112,
    113,
    114,
    115,
    116,
    117,
    118,
    119,
    120,
    121,
    122,
]
# List with all the vogals, lower or uppercase
vogals = lower_case_chars + upper_case_chars
numbers = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57]

# A complete ASCII items list
complete_list = lower_case_chars + upper_case_chars + special_chars + numbers

pass_length = input(
    "Selecione a quantidade de caracteres da sua senha,"
    " no mínimo 8 (não selecione nada para 8):"
)
pass_length = 0 if pass_length == "" else pass_length

char_count = input("Selecione a quantidade de caracteres especiais:")

int_count = input("Selecione a quantidade de números:")


def addToPass(list_of_items, items):
    """
    Receives a list and the item quantity to get from it, returning as a string of
    new items
    """
    items_to_add = ""
    for _ in range(items):
        # Get a random position from the list and add the item inside it to the string
        list_item_position = round(random.randrange(len(list_of_items)))
        items_to_add += chr(list_of_items[list_item_position])
    return items_to_add


def createPassword(pass_length=8, char_count=0, int_count=0):
    # Caso o valor em pass_lenght seja menor que 8 ou vazio, recebe 8
    pass_length = 8 if pass_length == "" or int(pass_length) < 8 else int(pass_length)
    # Tratamento de variáveis para caso de valores incorretos
    char_count = 0 if char_count == "" else int(char_count)
    int_count = 0 if int_count == "" else int(int_count)
    # Vogais utilizam o restante não utilizado da senha
    vogals_count = pass_length - (char_count + int_count)

    final_pass = ""
    # If the user wont select nothing, a totally random pass is created
    if char_count == 0 and int_count == 0:
        final_pass = addToPass(complete_list, pass_length)
        return final_pass
    else:
        if (char_count + int_count) > pass_length:
            print("Quantidade de caracteres inválida")
        # Add to the pass strings with the amount of each category selected by the user
        if char_count > 0:
            special_chars_to_pass = addToPass(special_chars, char_count)
            final_pass += special_chars_to_pass
        if int_count > 0:
            int_to_pass = addToPass(numbers, int_count)
            final_pass += int_to_pass
        if vogals_count >= 0:
            vogals_to_pass = addToPass(vogals, vogals_count)
            final_pass += vogals_to_pass

        # Shuffles the final list to make it totally random
        final_password = "".join(random.sample(final_pass, len(final_pass)))

        return final_password


try:
    user_pass = createPassword(pass_length, char_count, int_count)
except Exception as e:
    print("deu ruim")
    print(e)

print(user_pass)
