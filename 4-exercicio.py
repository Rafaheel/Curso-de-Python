variavel = input("Digite alguma coisa: ")
print(f"O tipo primitivo deste valor é {type(variavel)}")
print(f"So tem espaços? {variavel.isspace()}")
print(f"É numerico? {variavel.isnumeric()}")
print(f"É alfabetico? {variavel.isalpha()}")
print(f"É alfanumerico? {variavel.isalnum()}")
print(f"Esta um maisuculas? {variavel.isupper()}")
print(f"Esta um minusculas? {variavel.islower()}")
print(f"Esta capitalizada? {variavel.istitle()}")
