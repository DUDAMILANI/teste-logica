def count_a_in_string(s):
    count = s.lower().count('a')
    return count

string = input("Informe uma string: ")
quantidade = count_a_in_string(string)

if quantidade > 0:
    print(f"A letra 'a' aparece {quantidade} vezes na string.")
else:
    print("A letra 'a' não aparece na string.")
