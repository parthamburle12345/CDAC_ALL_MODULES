from random import randrange


def main():
    nums = [randrange(5000) for _ in range(10)]
    print(nums)

    even_nums = [n for n in nums if n%2 == 0]
    
    odd_nums = []
    for n in nums:
        if n%2:
            odd_nums.append(n)

    print()
    print(f'{even_nums=}')
    print(f'{odd_nums=}')

main()
