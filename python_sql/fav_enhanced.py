import csv


def load_csv_as_dict_then_sorted_by_value():
    with open('favorites.csv', 'r') as file:
        reader = csv.DictReader(file)
        counts = dict()
        for row in reader:
            favorite = row["language"]
            if favorite in counts:
                counts[favorite] += 1
            else:
                counts[favorite] = 1

    def get_value(language):
        return counts[language]

    for favorite in sorted(counts, key=lambda language: counts[language], reverse=True):
        print(f"{favorite}: {counts[favorite]}")


def load_csv_as_dictionary():
    with open('favorites.csv', 'r') as file:
        reader = csv.DictReader(file)
        counts = dict()
        for row in reader:
            favorite = row["language"]
            if favorite in counts:
                counts[favorite] += 1
            else:
                counts[favorite] = 1

    for favorite in sorted(counts):
        print(f"{favorite}: {counts[favorite]}")


if __name__ == '__main__':
    load_csv_as_dict_then_sorted_by_value()
