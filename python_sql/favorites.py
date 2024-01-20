import csv

def load_csv_as_dictionary():
    with open('favorites.csv', 'r') as file:
        reader = csv.DictReader(file)
        # next(reader, None) to ignore the first row
        c = 0
        java = 0
        python = 0
        for row in reader:
            favorite = row["language"]
            if favorite == "Java":
                java += 1
            elif favorite == "Python":
                python += 1
            elif favorite == "c":
                c += 1
    print(f"Java: {java}, Python: {python}, c: {c}")

def load_csv_as_list():
    with open('favorites.csv', 'r') as file:
        reader = csv.reader(file)
        # next(reader, None) to ignore the first row
        for row in reader:
            favorite = row[1]
            print(favorite)


if __name__ == '__main__':
    load_csv_as_dictionary()