def calc_sum_of_multiples_3_and_5(number):
    list_of_multiples = []

    for i in range(0, number):
        if i % 3 == 0 or i % 5 == 0:
            list_of_multiples.append(i)

    return sum(list_of_multiples)

print(calc_sum_of_multiples_3_and_5(1000))