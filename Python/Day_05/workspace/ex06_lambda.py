nums = [10, 3, 49, 39, 60, 704, 39, 385, 6789, 876]

def is_even(n):
    return n%2 == 0

# print(f"{is_even(77)=}")
# print(f"{is_even(78)=}")

even_nums = filter(is_even, nums)
print(list(even_nums))

odd_nums = filter(lambda n:n%2, nums)
print(list(odd_nums))