import random


def create_sheets(
    respondents=5,
    items_number=5,
    average_lower_range=2,
    average_upper_range=4,
    maximum_score=5,
):
    sheets = []
    for _ in range(respondents):
        this = []
        avg = 0
        while not (avg > average_lower_range and avg < average_upper_range):
            this = [random.randint(1, maximum_score) for _ in range(items_number)]
            avg = sum(this) / len(this)
        sheets.append((this, avg))

    return sheets

def main():
    sheets = create_sheets(respondents=1000, items_number=10)
    if not sheets:
        exit(1)

    with open("sheets.txt", "w+") as f:
        f.write("\n".join([f"Numbers: {nums}, Average: {avg}" for nums, avg in sheets]))

if __name__ == "__main__":
    main()
