from rectangle import Rectangle


if __name__ == "__main__":
    try:
        rect_1 = Rectangle(1, 2)
        rect_2 = Rectangle(2, 3)
        rects_sum = rect_1 + rect_2
        rects_mul_num = rect_2 * 2
        rects_mul = rect_1 * rect_2
    except TypeError:
        pass

    print(rects_sum)
    print(rects_mul_num)



