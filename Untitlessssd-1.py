"""""
def capitparagraph(paragraph):
    
    if not paragraph:
        return ""

    result = list(paragraph)  # Converte a string para uma lista de caracteres para facilitar a modificação
    capitalize_next = True

    for i in range(len(result)):
        char = result[i]

        # Verifica se o caractere atual é uma letra
        is_letter = ('a' <= char <= 'z') or ('A' <= char <= 'Z')

        if capitalize_next and is_letter:
            result[i] = char.upper()
            capitalize_next = False
        elif char in '.?!':
            capitalize_next = True

    return "".join(result) # Junta a lista de caracteres de volta em uma string

paragraph = input("enter the sentence?")
capitalized_paragraph = capitparagraph(paragraph)
print(capitalized_paragraph)
"""""



def cost_to_fill(tank_size, fuel_level, price_per_gallon):

    cost =(tankSize-fuelLevel)*pricePerGallon
    co=format(cost, ".2f")
    return co   

        
