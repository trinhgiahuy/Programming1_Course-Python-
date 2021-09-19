#studentname: Trinh Gia Huy
#studentnumber: 290290
#project15.2 :Routing protocol simulator


class Router:

    def __init__(self, name):
        """
        Create the attributes for the Router object:
            - self.__name: the object's name
            - self.__neighbour: the list of the router's neighbours
            - self.__routing_table: the diction
        :param name: str, the router's name
        """
        self.__name = name
        self.__neighbour = []
        self.__routing_table = {}

    def print_info(self):
        """
        Print all the details related to the object.
        """
        print("  " + self.__name)
        print("  " + len(self.__name) * " " + "N: "
              + ", ".join(sorted(self.__neighbour)))
        # Create a new list whose element is in the form "address:distance"
        routing_table_list = []
        for key in self.__routing_table:
            routing_table_list.append(key + ":" + str(self.__routing_table[key]))
        print("  " + len(self.__name) * " " + "R: "
              + ", ".join(sorted(routing_table_list)))

    def add_neighbour(self, neighbour_object):
        """
        Add the name of another Router object that is a
        neighbour of the current object.
        :param Router, neighbour_object: the neighbouring object
        """
        self.__neighbour.append(neighbour_object.name())

    def add_network(self, address, distance):
        """
        Create a new network link between the router and the
        network address.
        :param address: str, the network IP address
        :param distance: int, the distance from the current
        router to that address
        """
        self.__routing_table[address] = distance

    def receive_routing_table(self, router_name):
        """
        Get the routing table from the sending router, then add
        new addresses and corresponding distances if those
        addresses are not in the current router's table.
        :param router_name: Router, the sending router
        """
        connection = router_name.routing_table()
        for new_network in connection:
            if new_network not in self.__routing_table:
                # Add new address but remember that the distance is one step further
                self.__routing_table[new_network] = connection[new_network] + 1

    def has_route(self, name_of_network):
        """
        Check if the router is connected to the network or not.
        :param name_of_network: str, the network address
        """
        if name_of_network not in self.__routing_table:
            print("Route to the network is unknown.")
        elif self.__routing_table[name_of_network] == 0:
            print("Router is an edge router for the network.")
        else:
            print("Network", name_of_network, "is",
                  self.__routing_table[name_of_network], "hops away")

    def name(self):
        """
        Return the object's name.
        :return: str
        """
        return self.__name

    def neighbour(self):
        """
        Return the neighbours of the object.
        :return: list
        """
        return self.__neighbour

    def routing_table(self):
        """
        Return the routing table of the object.
        :return: dict
        """
        return self.__routing_table


def read_input_file(filename, new_dict):
    with open(filename, "r") as file:
        rows = file.readlines()
        for row in rows:
            info = row.split("!")
            # Check if any row is not in the right form
            if len(info) != 3:
                raise TypeError
            else:
                # Create a new object for each row and add it into the dict
                new_router = Router(info[0])
                new_dict[info[0]] = new_router
                # If any neighbour exists
                if info[1] != "":
                    neighbour_list = info[1].split(";")
                    for neighbour in neighbour_list:
                        new_router.add_neighbour(Router(neighbour))
                # If any network is connected
                if info[2] != "":
                    # Get the list of the data
                    network_list = info[2].split(";")
                    for network in network_list:
                        network_info = network.split(":")
                        # Check if the data piece is in the form "address:distance"
                        if len(network_info) == 2:
                            new_router.add_network(network_info[0], int(network_info[1]))
        return new_dict


def main():

    routerfile = input("Network file: ")
    # Create a big dict that consists of element with the name of the Router
    # object as the key whose value is the Router object
    router_dict = {}

    try:
        # Any input file is given or the program starts from nothing
        if routerfile != "":
            router_dict = read_input_file(routerfile, {})

    except:
        print("Error: the file could not be read or there is something wrong with it.")

    else:
        while True:
            command = input("> ")
            command = command.upper()

            if command == "P":
                name_to_print = input("Enter router name: ")

                if name_to_print not in router_dict:
                    print("Router was not found.")
                else:
                    router_dict[name_to_print].print_info()

            elif command == "PA":
                for name in sorted(router_dict):
                    router_dict[name].print_info()

            elif command == "S":
                router_to_communicate = input("Sending router: ")

                # Get the neighbouring info from the current object
                its_neighbour = router_dict[router_to_communicate].neighbour()
                for router_to_receive in its_neighbour:
                    router_dict[router_to_receive].receive_routing_table(router_dict[router_to_communicate])

            elif command == "C":
                router1 = input("Enter 1st router: ")
                router2 = input("Enter 2nd router: ")

                router_dict[router1].add_neighbour(router_dict[router2])
                router_dict[router2].add_neighbour(router_dict[router1])

            elif command == "RR":
                router_to_check = input("Enter router name: ")
                network_to_check = input("Enter network name: ")

                router_dict[router_to_check].has_route(network_to_check)

            elif command == "NR":
                router_name = input("Enter a new name: ")

                if router_name in router_dict:
                    print("Name is taken.")
                else:
                    # Create a new object and put it into the beginning dictionary
                    new_router = Router(router_name)
                    router_dict[router_name] = new_router

            elif command == "NN":
                router_to_add_network = input("Enter router name: ")
                network_address = input("Enter network: ")
                network_distance = int(input("Enter distance: "))

                router_dict[router_to_add_network].add_network(network_address, network_distance)

            elif command == "Q":
                print("Simulator closes.")
                return

            else:
                print("Erroneous command!")
                print("Enter one of these commands:")
                print("NR (new router)")
                print("P (print)")
                print("C (connect)")
                print("NN (new network)")
                print("PA (print all)")
                print("S (send routing tables)")
                print("RR (route request)")
                print("Q (quit)")


main()
