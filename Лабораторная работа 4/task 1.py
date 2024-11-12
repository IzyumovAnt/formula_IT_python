import json


FILENAME = "input.json"


def task() -> float:
    """Функция дял нахождения суммы произведений двух значений в каждом словаре"""
    with open(FILENAME) as input_file:
        json_data = json.load(input_file)

        products = [item["score"] * item["weight"] for item in json_data]
        return round(sum(products), 3)


if __name__ == '__main__':
    print(task())
