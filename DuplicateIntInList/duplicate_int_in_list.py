# accept the size of the int array
# accept the values and return the duplicate

class DuplicateIntInList:

    # read the input
    def get_user_input(self):
        # user_input_str = input("Enter the comma separated list of integers: ")
        user_input_list = []
        print("Enter an integer or q to quit:")
        while True:
            user_input_int = input()
            if user_input_int == 'q':
                break
            try:
                user_input_list.append(int(user_input_int))
            except ValueError:
                print('Invalid input please enter integer or "q" to quit')
        return user_input_list

    # find the duplicates
    def find_duplicates(self, user_input_list):
        sorted_user_input = sorted(user_input_list)
        dup_list = []

        for index in range(0, len(sorted_user_input)-1):
            if sorted_user_input[index] == sorted_user_input[index+1]:
                dup_list.append(sorted_user_input[index])

        # return the duplicates
        return sorted(set(dup_list))


if __name__ == "__main__":
    obj_find_dup = DuplicateIntInList()
    my_user_input_list = obj_find_dup.get_user_input()
    print(f"User input: {my_user_input_list}")
    print(f'List of duplicate integers: {obj_find_dup.find_duplicates(my_user_input_list)}')
