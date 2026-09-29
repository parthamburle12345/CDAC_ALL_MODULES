def main():
    nums = [554, 4928, 2870, 2967, 4675, 3093, 3129, 4033, 4312, 2089]
    halves = [n//2 for n in nums]
    squares = [n*n for n in nums]

    print(f'{nums=}')
    print(f'{halves=}')
    print(f'{squares=}')

main()
