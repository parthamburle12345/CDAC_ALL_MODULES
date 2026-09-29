from vinutils import line

line()

nums = [100, 200]

def calc_sum():
    # global nums
    total = sum(nums)
    print(f'{total=}')

calc_sum()
# print(f'{total=}')  # total is a local variable of the function calc_sum
print(sum(nums))
