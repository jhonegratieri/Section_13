
with open('arq.txt', 'a+') as arquivo:
    while True:
        notes = input('Type your notes. To exit enter 0: ')
        if notes == '0':
            break
        arquivo.write(notes + '\n')

    arquivo.seek(0)
    print(arquivo.read())
