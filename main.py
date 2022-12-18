from rectangle import Rectangle
import os
import random

def clean_string(string: str):
    """Return string without symbols "x,')(" ."""

    symbols = "x,')("
    for i in symbols:
        if i in string:
            string = string.replace(i, "")
    return string

def rect_dict(string: str) -> dict:
    """Converts string to rectangle dictionary and returns this dictionary"""

    rect_list = string.split()
    rect_list[1] = rect_list[1].replace(" ", "")
    res = {}
    res[rect_list[0]] = Rectangle(int(rect_list[1]), int(rect_list[2]))
    return res


if __name__ == "__main__":
    rectangle_dict = {}
    try:
        filename = "rectangles.txt"
        if not os.stat(filename).st_size:
            with open(filename, "r+") as file_object:
                rectangles = {}
                for num in range(1, 11):
                    key_word = f"rectangle_{num}"
                    rectangles[key_word] = Rectangle(random.randint(1, 10), random.randint(1, 10))
                for key, value in rectangles.items():
                    print((str(key), str(value)), file=file_object)

        with open(filename, "r") as file_object:
            for line in file_object:
                rect_string = clean_string(line)
                rectangle_dict.update(rect_dict(rect_string))


        for key, value in rectangle_dict.items():
            print(f"{key} = {value}")
        print("-" * 25)
        for key, value in rectangle_dict.items():
            print(f"{key}'s square = {value.square()}")
        print("-" * 25)
        print(f"Max rectangle is {max(rectangle_dict.values())}")
        print("-" * 25)
        print(f"Min rectangle is {min(rectangle_dict.values())}")
        print("-" * 25)
        print(f"Sum of all rectangles is {sum(rectangle_dict.values())}")
        print("-" * 25)
        for key, value in rectangle_dict.items():
            print(f"{key} * 2 = {value * 2}")
        print("-" * 25)
        print("Sorted rectangles")
        for value in sorted(rectangle_dict.values()):
            print(f"{value} = {value.square()}")
        print("-" * 25)

        for value in rectangle_dict.values():
            print(value * "")
        for value in rectangle_dict.values():
            print(value + "")


    except (FileNotFoundError, TypeError) as error:
        print(error)


