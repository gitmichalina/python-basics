from functools import reduce


def main():

    my_list = [1, 2, 3, 4, 5, 6]

    # lambda stored in variable then used as argument
    square_func = lambda a: a * a
    mapped_list = list(map(square_func, my_list))
    print(mapped_list)

    # lambda directly passed as argument
    mapped_list_2 = list(map(lambda a: a * a, my_list))
    print(mapped_list_2)

    # mapping two lists simultaneously
    even_list = [2, 4, 6]
    odd_list = [1, 3, 5]
    mapped = list(map(lambda a, b: a + b, odd_list, even_list))
    print(mapped)

    # filter only divisible by 2
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = list(filter(lambda a: a % 2 == 0, nums))
    print(result)

    # reduce used to calculate sum of all elements
    nums = [1, 1, 1, 2]
    result = reduce(lambda a, b: a + b, nums)
    print(result)

    # list comprehension
    nums = [1, 2, 3, 4]
    new_list = [x for x in nums]
    print(new_list)
    new_list_2 = [x + 1 for x in nums]
    print(new_list)

    # list comprehension with condition (filter)
    nums = [1, 2, 3, 4]
    new_list = [x for x in nums if x % 2 == 0]

    sizes = ['Short', 'Medium', 'Large']
    persons = ['Men', 'Women']
    tuples_with_all_combinations = [(s, p) for s in sizes for p in persons]
    print(tuples_with_all_combinations)






if __name__ == '__main__':
    main()