
with open('arq.txt') as file:
    file.seek(0)
    number_of_vowels = 0
    number_of_consonant = 0

    for character in file.read():
        if character.lower() in ['a', 'e', 'o', 'i', 'u']:
            number_of_vowels += 1

        elif character != ' ':
            number_of_consonant += 1

    print(f'The read file has {number_of_vowels} vowels and {number_of_consonant} consonants.')
