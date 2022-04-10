
def search_and_count(file_text, characacter):

    with open(file_text) as file:
        file.seek(0)
        count = 0

        for i in file.read():
            if i.lower() == characacter.lower():
                count += 1

        return count


character = input('Enter a character: ')
print(f"the character '{character}' entered was found {search_and_count('arq.txt', character)} times in the text file.")
