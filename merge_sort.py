

class MergeSort(object):

    def divide(self, full_list):
        list_length = len(full_list)

        if list_length <= 1:
            return full_list
        else:
            mid = list_length // 2
            left_half = full_list[0:mid]
            right_half = full_list[mid:]
            first_list = self.divide(left_half)
            second_list = self.divide(right_half)

            return self.merge(first_list, second_list)

    def merge(self, list_one, list_two):
        length_one, length_two = len(list_one), len(list_two)
        i, j, sorted_list = 0, 0, []

        while (i < length_one) or (j < length_two):

            if (i < length_one) and (j < length_two):

                if list_one[i] <= list_two[j]:
                    sorted_list.append(list_one[i])
                    i += 1
                else:
                    sorted_list.append(list_two[j])
                    j += 1

            elif i < length_one:
                sorted_list.append(list_one[i])
                i += 1
            else:
                sorted_list.append(list_two[j])
                j += 1

        return sorted_list

if __name__ == '__main__':
    numbers = [9, -2, 10, 50, -30, 40]
    print("Before {}".format(numbers))
    sort_obj = MergeSort()
    new_list = sort_obj.divide(numbers)

    print("After {}".format(new_list))
