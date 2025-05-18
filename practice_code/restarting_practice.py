def gen_nums(num):
    for num in range(num):
        yield num

nums = gen_nums(19)
print(next(nums))
print(next(nums))