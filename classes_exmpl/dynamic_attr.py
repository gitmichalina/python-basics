def main():
    john = {
        "name": "John Doe",
        "position": "Python Developer",
        "salary": 80000,
        "hire_date": "2020-01-01",
        "is_manager": False,
    }

    john_record = Record()

    for field, value in john.items():
        setattr(john_record, field, value)


    john_record.new_attribute = "siemka"
    print(vars(john_record))
    # {'name': 'John Doe', 'position': 'Python Developer', 'salary': 80000,
    # 'hire_date': '2020-01-01', 'is_manager': False, 'new_attribute': 'siemka'}


class Record:
    """Hold a record of data."""


if __name__ == "__main__":
    main()