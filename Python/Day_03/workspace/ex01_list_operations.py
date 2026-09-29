print("=" * 80)

nums = [10, 12, 34]

new_nums = nums + [50, 39, 56]
print(nums)
print(new_nums)

n = int(input('Enter a number to search: '))
if n not in new_nums:
    print(f'{n} not found in the new list')
else:
    print(f'{n} is found at index {new_nums.index(n)}')

new_nums = nums * 3
print(new_nums)


nums += [99, 88, 77] # nums.extend([99, 88, 77])
print(f'{nums=}')