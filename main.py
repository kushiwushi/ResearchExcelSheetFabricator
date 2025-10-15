import random

# Sheet fabricator


def main(
    respondents, items_number, average_lower_range, average_upper_range, maximum_score
):
    items_number_list = [0] * items_number
    i = 0
    x = 0

    while items_number_list[-1] == 0:
        random_number = random.randint(1, maximum_score)

        items_number_list[i] = random_number

        if i != items_number:
            i += 1

    result = sum(items_number_list) / items_number

    if average_lower_range < result < average_upper_range:
        if x != respondents:
            print(f"Numbers: {items_number_list}, Average: {result}")
            with open("results.txt", "a") as file:
                file.write(f"Numbers: {items_number_list}, Average: {result} \n")
            x += 1
            main()
    else:
        main()


main()
