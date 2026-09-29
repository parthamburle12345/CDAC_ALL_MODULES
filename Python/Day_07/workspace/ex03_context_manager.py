filename = 'c:/users/dac/desktop/understandingrecursion.java'

# with open(filename) as f1:
#     lines = f1.readlines()  # eager fetch/read
#     for i, line in enumerate(lines):
#         print(f'{i+1}\t{line}', end='')

#     # f1.close() is called automatically, while exiting the `with` block


with open(filename) as f1:
    i = 0
    for line in f1:     # lazily reads one line at a time
        if line.strip().startswith('void'):
            break

        print(f'{i+1}\t{line}', end='')
        i+=1

    # f1.close() is called automatically, while exiting the `with` block

print()