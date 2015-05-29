import string
import random


error_character = 'z'


def generate_random():
    rand_str = ''
    string_list = [random.choice(string.ascii_letters) for i in range(1000)]
    rand_str = ''.join(string_list)

    return rand_str


def process_input(input_str):

    for char in input_str:

        try:
            assert char != error_character
        except AssertionError:
            return input_str

    return False


def delta_test(s):

    if error_character in s:
        return True
    else:
        return False


def delta_debugging(input_str):
    assert delta_test(input_str) is True  # noqa

    i = 2
    while len(input_str) >= 2:
        start = 0
        sub_length = len(input_str) / i
        flag = False

        while start < len(input_str):
            test_string = input_str[:start] + input_str[start + sub_length:]

            if delta_test(test_string):
                input_str = test_string
                i = max(i - 1, 2)
                break
            start += sub_length

        if not flag:
            i = min(i * 2, len(input_str))
            if i == len(input_str):
                break

    return input_str


if __name__ == '__main__':

    while True:
        rand_str = generate_random()
        failed_input = process_input(rand_str)

        if failed_input:
            break

    error_string = delta_debugging(failed_input)
    print("Has the error: {} \n\n\n\n\n\n\n\n".format(failed_input))
    print("Simplified: {}".format(error_string))
