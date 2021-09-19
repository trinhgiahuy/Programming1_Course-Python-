# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to programming
# student name: Trinh Gia Huy
# student number: 290290
# Task: accesscontrol, program code template

DOORCODES = {'TC114': ['TIE'], 'TC203': ['TIE'], 'TC210': ['TIE', 'TST'],
             'TD201': ['TST'], 'TE111': [], 'TE113': [], 'TE115': [],
             'TE117': [], 'TE102': ['TIE'], 'TD203': ['TST'], 'TA666': ['X'],
             'TC103': ['TIE', 'OPET', 'SGN'], 'TC205': ['TIE', 'OPET', 'ELT'],
             'TB109': ['OPET', 'TST'], 'TB111': ['OPET', 'TST'],
             'TB103': ['OPET'], 'TB104': ['OPET'], 'TB205': ['G'],
             'SM111': [], 'SM112': [], 'SM113': [], 'SM114': [],
             'S1': ['OPET'], 'S2': ['OPET'], 'S3': ['OPET'], 'S4': ['OPET'],
             'K1705': ['OPET'], 'SB100': ['G'], 'SB202': ['G'],
             'SM220': ['ELT'], 'SM221': ['ELT'], 'SM222': ['ELT'],
             'secret_corridor_from_building_T_to_building_F': ['X', 'Y', 'Z'],
             'TA': ['G'], 'TB': ['G'], 'SA': ['G'], 'KA': ['G']}


class Accesscard:

    def __init__(self, id, name):
        """
        Constructor, creates a new object that has no access rights.
        :param id: card holders personal id (str)
        :param name: card holders name (str)

        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME OR THE
        PARAMETERS!
        """
        self.ID = id
        self.name = name
        self.list_access = []


    def info(self):
        """
        The method has no return value. It prints the information related to
        the access card in the format:
        id, name, access: a1,a2,...,aN
        for example:
        777, Thelma Teacher, access: OPET, TE113, TIE
        Note that the space characters after the commas and semicolon need to
        be as specified in the task description or the test fails.
        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME, THE
        PARAMETERS, OR THE PRINTOUT FORMAT!
        """
        str_accesscodes = ', '.join(i for i in self.list_access)
        print(f"{self.ID}, {self.name}, access: {str_accesscodes.strip()}")

    def simplified(self, dict_origin):
        """
        Remove overlapping access codes
        :param dict_origin: a dict_origin is a dictionary contains ID as key and list include roomcode and areacod
        :return:
        """

        list_final = []
        for item in dict_origin[self.ID]:
            list_ = []
            if item in DOORCODES.keys():
                if len(DOORCODES[item]) == 0:
                    if item not in list_final:
                        list_final.append(item)
                else:
                    for i in DOORCODES[item]:
                        if i in dict_origin[self.ID]:
                            list_.append(i)
                if len(list_) != 0:
                    for v in list_:
                        if v not in list_final:
                            list_final.append(v)
                else:
                    if item not in list_final:
                        list_final.append(item)
            else:
                if item not in list_final:
                    list_final.append(item)
        self.list_access = sorted(list_final)


    def get_name(self,dict_origin):
        """
        :return: Returns the name of the accesscard holder.
        """
        return self.name

    def add_access(self, new_access_code):
        """
        The method adds a new accesscode into the accesscard according to the
        rules defined in the task description.
        :param new_access_code: The accesscode to be added in the card.
        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME, THE
        PARAMETERS, OR THE RETURN VALUE! DON'T PRINT ANYTHING IN THE METHOD!
        """
        self.list_access.append(new_access_code)


    def check_access(self, door):
        """
        Checks if the accesscard allows access to a certain door.

        :param door: the doorcode of the door that is being accessed.
        :return: True: The door opens for this accesscard.
                 False: The door does not open for this accesscard.
        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME, THE
        PARAMETERS, OR THE RETURN VALUE! DON'T PRINT ANYTHING IN THE METHOD!
        """

        if door in self.list_access:
            return True

        else:
            for areacodes in DOORCODES[door]:
                if areacodes in self.list_access:
                    return True
                else:
                    return False

    def merge(self, card):
        """
        Merges the accesscodes from another accesscard to this accesscard.

        :param card: The accesscard whose access rights are added to this card.
        :return:
        """
        self.list_access += card.str_change_to_list()

def read_input():
    """
    Read the file input
    :return:a dict_origin is a dictionary contains ID as key and list include roomcode and areacode
            a dict_id is a dictionary contains ID as key and tuple include ID and name of card holder
    """

    dict_origin, dict_ID = {}, {}
    #try:
    with open('accessinfo.txt','r') as file:
        for row in file.read().splitlines():
            list_access_codes = []
            row = row.split(";")
            ID, name, access_codes = row[0], row[1], row[2]
            access_codes = access_codes.split(",")

            for code in access_codes:
                list_access_codes.append(code)
            dict_origin[ID] =list_access_codes
            dict_ID[ID] = Accesscard(ID, name)
    #except:
        #print("Error: file cannot be read")
    return dict_origin, dict_ID

def read_AREACODES():
    """
    :return: a list contains the areacodes (string)
    """

    AREACODES = []
    for key in DOORCODES.keys():
        for item in DOORCODES[key]:
            AREACODES.append(item)
    return AREACODES

def main():

    dict_origin, dict_ID = read_input()
    AREACODES = read_AREACODES()

    while True:
        line = input("command> ")

        if line == "":
            break

        strings = line.split()
        command = strings[0]

        if command == "list" and len(strings) == 1:
            for item in sorted(dict_ID.keys()):
                dict_ID[item].simplified(dict_origin)
                dict_ID[item].info()

        elif command == "info" and len(strings) == 2:
            card_id = strings[1]

            # check the imformation of the personal's card holder
            if card_id in dict_ID.keys():
                dict_ID[card_id].simplified(dict_origin)
                dict_ID[card_id].info()

            else:
                print("Error: unknown id.")

        elif command == "access" and len(strings) == 3:
            card_id = strings[1]
            door_id = strings[2]

            # Check that whether that personholder's card can access that room or not
            if card_id in dict_ID.keys():
                if door_id in DOORCODES.keys() or door_id in AREACODES:

                    dict_ID[card_id].simplified(dict_origin)
                    CardHolder = dict_ID[card_id].get_name(dict_origin)

                    if dict_ID[card_id].check_access(door_id):
                        print(f"Card {card_id} ( {CardHolder} ) has access to door {door_id}")
                    else:
                        print(f"Card {card_id} ( {CardHolder} ) has no access to door {door_id}")

                else:
                    print("Error: unknown doorcode.")
            else:
                print("Error: unknown id.")

        elif command == "add" and len(strings) == 3:
            card_id = strings[1]
            access_code = strings[2]

            #add doorcode or areacode to the personholer's card
            if card_id in dict_ID.keys():

                if access_code in DOORCODES.keys() or access_code in AREACODES:
                    dict_origin[card_id].append(access_code)
                    dict_ID[card_id].add_access(access_code)
                    dict_ID[card_id].simplified(dict_origin)
                else:
                    print("Error: unknown accesscode.")

            else:
                print("Error: unknown id.")

        elif command == "merge" and len(strings) == 3:
            card_id_to = strings[1]
            card_id_from = strings[2]

            # combine the areaacess from the secondperson's card to the firstperson's card
            if card_id_to in dict_ID.keys() and card_id_from in dict_ID.keys():
                dict_origin[card_id_to] += dict_origin[card_id_from]
                dict_ID[card_id_to].simplified(dict_origin)

            else:
                print("Error: unknown id.")

        elif command == "quit":
            print("Bye!")
            return
        else:
            print("Error: unknown command.")


main()
