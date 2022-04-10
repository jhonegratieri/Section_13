
with open('arq.txt') as source_file:
    vowels = ['a', 'e', 'o', 'i', 'u']
    source_file.seek(0)

    try:
        with open('new_file.txt', 'x+') as new_file:

            for character in source_file.read():
                if character in vowels:
                    new_file.write('*')
                else:
                    new_file.write(character)

    except FileExistsError:
        print('File already exists.')
