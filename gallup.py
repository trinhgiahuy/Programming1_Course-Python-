# TIE-02107 Introduction to Programming
# Huy Trinh Gia , giahuy.trinh@tuni.fi, student nr: 290290
# Solution of task 6.2
# A program that conducts some calculations for the responses.
# median value, and how many drivers receive fine


def read_input(list):
    """Analysis the input and return a list that contains number of coffe except 0 and also the number of 0 cups of coffee

    :param: list: input list want to analyse
    :return a list contains data after remove all 0 values
            a number of 0 value
    """
    list_complete = []
    count = 0

    #sort the list and remove 0 value
    for i in range(0, len(list)):
        if list[i] != "0":
            list_complete.append(int(list[i]))
        else:
            count += 1

    return list_complete, count

def find_max_value(list):
    """ Find the max value in a list


    :param list: input a list want to analysis
    :return: the max value
    """

    #get the max value
    max_value = sorted(list)[-1]
    return max_value

def find_most_common(list):
    """Find the common value
    :param list: list that want to analysis
    :return: the number of commmon vale
    """


    value = sorted(list)[-1]

    for k in range(len(list)):
        if list[k] == value:
            return k+1

def sum_value(list):
    """Function that caculate the sum of all data in the list

    :param list that want to analysis:
    :return: the sum of all data in the list
    """

    sum = 0

    for k in range(len(list)):
        sum += list[k]

    return sum

def check_count(int):
    """ A function that analysis input and print out message

    :param int:
    :return: no return
    """

    if(int!=0):
        print(f"Removed {int} non-coffee-drinkers responses")
        print()

def main():

    data_list = []
    new_list = []

    print("Enter one response per line. End by entering an empty row.")
    user_input = " "
    while user_input != "":
        user_input = input()
        data_list.append(user_input)

    data_list.remove(data_list[-1])

    data_list_complete, count = read_input(data_list)
    data_list_complete = sorted(data_list_complete)
    check_count(count)

    if count != len(data_list):

            #analysing specific input and cases
            print("Information related to coffee drinkers:")
            if len(data_list) == 1:
                print("{} #".format(data_list[0]))
                print("The greatest response: {} cups of coffee per day".format(data_list[0]))
                print("The most common response: {} cups of coffee per day".format(data_list[0]))
                if int(data_list[0]) <= 4:
                    print("None of the respondents drink too much coffee")
                else:
                    print("100.0% of the respondents drink more than 4 cups of coffee per day")
            else:
                number_list = [0]
                temp = 1
                index = 0
                copy_data_list_complete = []
                for ele in range(len(data_list_complete)):
                    copy_data_list_complete.append(data_list_complete[ele])
                while len(copy_data_list_complete) > 0:
                    if copy_data_list_complete[0] == temp:
                        number_list[index] += 1
                        copy_data_list_complete.remove(copy_data_list_complete[0])
                    else:
                        temp = copy_data_list_complete[0]
                        for i in range(temp - index - 1):
                            number_list.append(0)
                        index = len(number_list) - 1
                copy_number_list = []

                for ele in range(len(number_list)):
                    copy_number_list.append(number_list[ele])
                i = 0

                while i < len(copy_number_list):
                    if (copy_number_list[i]) != 0:
                        break
                    i += 1

                #prints a graphic presentation of the distribution of the responses
                for j in range(i, len(number_list)):
                    if j < 9:
                        if number_list[j] != 0:
                            print(" {} {}".format(j + 1, number_list[j] * "#"))
                        else:
                            print(" {}".format(j + 1))
                    else:
                        if number_list[j] != 0:
                            print("{} {}".format(j + 1, number_list[j] * "#"))
                        else:
                            print("{}".format(j + 1))

                #get specific data using defined function
                max_value = find_max_value(data_list_complete)
                most_common = find_most_common(number_list)
                new_list = number_list[4:]
                sub_sum = sum_value(new_list)
                total_sum = sum_value(number_list)

                #print out all necessary imformation after analysis
                print("\nThe greatest response: {} cups of coffee per day".format(max_value))
                print("The most common response: {} cups of coffee per day".format(most_common))
                print("{:0.1f}% of the respondents drink more than 4 cups of coffee per day".format(sub_sum / total_sum * 100))


main()