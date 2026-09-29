def main():
    txt = 'vinod bangalore vinay hassan vinod chennai bangalore chennai bangalore bangalore'

    word = input('Enter a word to search: ')

    j = 0
    while True:
        i = txt.find(word, j)
        if i == -1:
            break

        print(f'`{word}` found in the given text at index {i}')
        j = i + 1

    if j == 0:
        print(f'`{word}` is not found in the given text')


print('='*80)
main()
