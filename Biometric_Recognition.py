

###############################################################################
# read_biometric_registry(filename)
# =========================================
# Function reads the biometric information from the file whose name is in
# the parameter filename. The read information will be parsed and saved in
# the data structure that is in the variable called result. The coder has
# to define the data structure by him/herself.
# After successfully reading the file and saving its contents in the data
# structure, the function returns the result. If there's an error, None is
# returned.
#
# PLEASE NOTE:
# (a) Implement all parts of the code that say TODO.
# (b) The data structure returned by the function must be something that
#     that nests lists and/or dicts. That is the wole point of this project:
#     to use nested data structures.
###############################################################################

def read_biometric_registry(filename):
    result ={}  # TODO initialize your data structure here

    handled_passports = []

    try:
        with open(filename, "r") as file_object:
            for row in file_object:
                fields = row.rstrip().split(";")

                if len(fields) != 8:
                    print("Error: there is a wrong number of fields "
                          "in the file:")
                    print("'", row, "'", sep="")
                    return None

                name = fields[0] + ", " + fields[1]
                passport = fields[2]
                key_of_result = name + ";" +passport
                if passport in handled_passports:
                    print("Error: passport number", passport,
                          "found multiple times.")
                    return None
                else:
                    handled_passports.append(passport)

                biometrics = []

                for i in range(3, 8):
                    try:
                        id_value = float(fields[i])
                    except ValueError:
                        print("Error: there's a non-numeric value on the row:")
                        print("'", row, "'", sep="")
                        return None

                    if 0 <= id_value <= 3.0:
                        biometrics.append(float(id_value))  #list
                    else:
                        print("Error: there is an erroneous value in the file:")
                        print("'", row, "'", sep="")
                        return None

                # TODO:
                # save the read information in the result data structure
                    result[key_of_result] = biometrics #{first, last;passport:[5 values]}
        return result

    except FileNotFoundError:
        print("Error: file", filename, "could not be opened.")
        return None


###############################################################################
# TODO
###############################################################################
def execute_match(registry):
    # TODO remove "pass" and write your own code here
    # result is a dict that contains key__result là 1 string và value là 1 list 5 phần tử :
    """value_array = []
    for v in result.values():
        value_array.append(v)
    count = 0
    result_array = []
    for k in range(len(value_array) - count):
        count_value = value_array[count]
        if (value_array[k + 1] == count_value):
            print("{%s:%s}" % ())
        else:
            continue
        count += 1"""
    value = []
    value_map=[]
    key_map=[]
    result_match = {}
    nhi=0
    for k,v in registry.items():
        value.append(v)
        value_map.append(v)
        key_map.append(k)
    final_value =0
    lst=[]
    while True:
        if(len(value)!=0):
            for item in value:
                euclidean_distance = 0
                for i in range(5):
                    euclidean_distance += (value[final_value][i] - item[i])**2
                if euclidean_distance**(1/2) <0.1:
                    if value[final_value] != item:
                        lst.append(item)
            if len(lst) != 0:
                lst.insert(0,value[final_value])
                for ele in lst:
                    number = value_map.index(ele)
                    result_match[key_map[number]]=ele
                    no=value.index(ele)

                    del value[no]
                print("Probably the same person:")
                for key in result_match.keys():
                    value_str = ';'.join([str("{:.2f}".format(i)) for i in result_match[key]])
                    print("%s;%s" % (key, value_str))
                print()
                lst.clear()
                result_match.clear()
                nhi+=1
            else:
                del value[final_value]
        else:
            if nhi == 0:
                print("No matching persons were found.")
            break

    ###############################################################################
# TODO
###############################################################################
def execute_search(registry):
    # TODO remove "pass" and write your own code here
    while True:
        try:
            id_value_input = input("enter 5 measurement points separated by semicolon: ").rstrip().split(";")
            len(id_value_input) == 5
            result_search = {}
            for key in registry.keys():
                euclidean_distance = 0
                for i in range(5):
                    euclidean_distance += (float(id_value_input[i]) - float(registry[key][i])) ** 2
                if euclidean_distance ** (1/2) < 0.1:
                    result_search.update({key:registry[key]})
            if len(result_search) != 0:
                print("Suspects found:")
                for key in result_search.keys():
                    value_str = ';'.join([str("{:.2f}".format(i)) for i in result_search[key]])
                    print("%s;%s" % (key, value_str))
                print()
                break
            else:
                print("No suspects were found.")
                print()
                break
        except ValueError:
            print("Error: enter floats only. Try again.")
        except IndexError:
            print("Error: wrong number of measurements. Try again.")

###############################################################################
# command_line_user_interface
# Very simple user interface. It might be good to add some helper functions.
#
###############################################################################
def command_line_user_interface(registry):
    while True:
        command = input("command [search/match/<enter>] ")
        if command == "":
            return
        elif command == "match":
            execute_match(registry)
        elif command == "search":
            execute_search(registry)
        else:
            print("Error: unknown command '", command,
                  "': try again.", sep="")


###############################################################################
# main()                                                                      #
# ======                                                                      #
# Main program for the project. You're not supposed to edit this.
#
###############################################################################
def main():
    registry_file = input("Enter the name of the registry file: ")
    result={}
    biometric_registry = read_biometric_registry(registry_file)
    if biometric_registry is not None:
        command_line_user_interface(biometric_registry)


main()
