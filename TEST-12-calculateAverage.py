def calc_average(nums):
    total = sum(nums) / len(nums)
    return(total)

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    print(calc_average(nums))  # calc_average() should return 3.0