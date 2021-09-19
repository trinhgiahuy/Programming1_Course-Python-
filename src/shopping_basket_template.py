"""
TIE-02101 Ohjelmointi 1 / TIE-02107 Programming 1
Template for kauppakori/shopping basket project
ari.suntioinen@tuni.fi 2020-02-16
"""

DEFAULT_FILENAME = "products.txt"



#DATA_sTRUCTURE 1 : A dict take store as a key and value is dict
# {"Lidl"//str: ["bread : 0.95//float", "coffee: 2.99" , ...] }, "S_market": ["bread" : }}

#data_structure 2 : A dict take name of food as key and value is a list of store:
# {"bread": ["Lidl","S_market"], "egg":["Herkkudo","S_market"]}

#data_Struct 3 : Cheap dict // Th dong gia
#{"bread" : "Lidl", "tuna" : "Lidl,S_market"] }



#Command P : data struct 1
#Command S : data struct 1
#command C : struct 2 + 1




# TODO:
# Define all the helper functions here. The following function
# stubs were useful when we were implementing our own version.
# You can use them if you feel like it, but you are not required to do so.
#
# NOTE!
# The functions below are by no means the only functions you will need.
# They are just meant to help you to understand some of the useful operations
# which are needed in the implementation of this project.


def read_inputfile(filename = DEFAULT_FILENAME):
    # TODO:
    # Read the input file and create a suitable data structure
    # based on then contents of the file. Return the data structure.
    # Selecting and understanding the data structure required to
    # implement this program is probably the most critical part
    # of the project.  Give it a good thought before rushing ahead
    # and starting to write your code.

    store_dict={}
    #food_list =[]
    food_dict={}
    #store_list=[]
    try:
        with open(filename,"r") as file_object:
            for row in file_object:
                field = row.rstrip().split(":")

                name_store = str(field[0])
                store_product_items = field[1]+":"+field[2]

                #a store_dict use store name as a key and list contains string of product and value
                if name_store not in store_dict:
                    store_dict[name_store]=[]
                    store_dict[name_store].append(store_product_items)
                else:
                    store_dict[name_store].append(store_product_items)

                #a food_dict contains food as key and list of store(string) as value
                if field[1] not in food_dict:
                    food_dict[str(field[1])]=[]
                    food_dict[field[1]].append(field[0])
                else:
                    food_dict[field[1]].append(field[0])


        return store_dict,food_dict
    except:
        print("There was an error in reading the input file!")
        return None

def get_price(food,store,input_data):
    for values in input_data[store]:    #value la string "fish:1.2"
        values_list=values.split(":")
        if(food == values_list[0]):
            return float(values_list[1])


def print_price_info(product, price):
    # TODO:
    # Replace the ???s with the correct format strings so that
    # the product and price information is printed as required in
    # the task description.

    print("    {:<15s} {:>10.2f} e".format(product, price))


def print_selections(data_input):
    for k in sorted(data_input.keys()):
        print(k)
        for values in sorted(data_input[k]):  #value la 1 string "fish:1.2"
                values_list=values.rstrip().split(":")
                product_name =str(values_list[0])
                price = float(values_list[1])
                print_price_info(product_name,price)

def print_known_products(data_input,data_input_2):
    for key in sorted(data_input.keys()):
        data_store_list=data_input[key].split(",")
        print_price_info(key, get_price(key,data_store_list[0],data_input_2))


def read_shopping_basket():   #data_input la food_dict
    print("Input product names separated by a white space:")
    basket=[]
    user_input=input("")
    if(user_input.find(" ") < 0):
        basket.append(user_input)
    else:
        field=user_input.rstrip().split(" ")
        for item in field:
            if item not in basket:
                basket.append(item)
    return basket           #basket la 1 list chua nhung string la product

    # TODO:
    # Read and return the contents of the shopping basket here.
def calculate_basket_price(selection, basket):
    """
    This function is used to calculate the total price of the
    content of the shopping basket for a particular store.

    Parameters:
        selection:
            A data structure containing information about all the
            products and their prices in one store. Could possibly be
            implemented as a dict with product name as a key and
            price as a payload.

        basket:
            A data structure containing all the items a customer
            has collected in their shopping basket. Could possibly be
            implemented as a list of strings.

    Return value:
        The price of the shopping basket (float) or None if
        the store's selection of products doesn't include all the
        items in the basket.
    """
    final_price=0
    for key,value in selection.items():
        for item in basket:
            if item == key:
                final_price += value
    return final_price

final_dict={}
def find_cheapest_stores(store_dict_copy):   #input_data la food dict
    multi_store = []
    basket = read_shopping_basket()
    # i1 = 0
    # i2 = 0
    # for ite in range(len(basket)):
    #     if(basket[ite] in input_data.keys()):
    #         if(basket[ite] in unique_list):
    #             store_constant=input_data[basket[ite]][0]
    #             final_dict[ite]=store_constant
    #         else:
    #             try:
    #                 cheap_dict_list=cheap_dict[basket[ite]].split(",")
    #                 final_dict[basket[ite]]=cheap_dict_list[0]
    #                 for i in range(len(cheap_dict_list)):
    #                     if(cheap_dict_list[i] not in cheap_dict_list):
    #                         multi_store.append(cheap_dict_list[i])                          #multistore la 1 list chua nhieu string la store
    #                 i1+=1
    #             except:
    #                 final_dict[basket[ite]]=cheap_dict[basket[ite]]
    #                 i2+=1
    #
    #     else:
    #         print("There is no store selling all those products.")
    #
    # if(i1!=0):
    #     print("Multiple stores sell this basket for {} e: {}, {}".format(calculate_basket_price(store_dict, final_dict),multi_store[0],multi_store[1]))
    # else:
    #     print("The cheapest price for this shopping basket: {} for {} e".format(cheap_dict[basket[0]],calculate_basket_price(store_dict,final_dict)))

    # common=find_the_common(basket,store_dict_copy)
    # i1=0
    # for i in range(len(basket)):
    #     if(basket[i] in input_data.keys()):
    #         if(len(common)!=0):
    #             final_dict[basket[i]]=input_data[basket[i]]
    #             i1+=1
    #         else:
    #             final_dict[basket[i]]=cheap_dict[basket[i]]
    #     else:
    #         print("There is no store selling all those products.")
    for k1, v1 in store_dict_copy.items():
        # for k2 in v1.keys():
        multi_store1 = []
        for item in basket:
            if item in v1.keys():
                multi_store1.append(k1)
        if len(multi_store1) == len(basket):
            multi_store.append(k1)

    if len(multi_store) != 0:
        cheapest = 100000
        new_price = 0
        new_store = []
        store_string = " ,"
        for store in multi_store:
            new_price = calculate_basket_price(store_dict_copy[store], basket)
            if new_price < cheapest:
                cheapest = new_price
                new_store.clear()
                new_store.append(store)
            elif new_price == cheapest:
                new_store.append(store)

        if len(new_store) == 1:
            print ("The cheapest price for this shopping basket:",new_store[0],"for",cheapest,"e")
        else:
            for item in sorted(new_store):
                store_string += item + ", "
            print ("Multiple stores sell this basket for",cheapest,"e:", store_string[2:len(store_string)-2])

    else:
        print ("There is no store selling all those products.")

def find_the_common(basket,input_data):
    for i in range(len(basket)):
        if(len(input_data[basket[i]]==1)):
            return input_data[basket[i]]



cheap_dict = {}
unique_list = []
def main():
    # TODO:
    # Call a function which reads the input file products.txt here.
    # That function should return a data structure containing all the
    # information read from the input file.  Choose the data structure
    # carefully so you will be able to implement all the required operations.


    store_dict , food_dict = read_inputfile("products.txt")
    food_dict_copy=food_dict.copy()
    store_dict_copy={}






    for key in food_dict_copy.keys():
        if(len(food_dict_copy[key])==1):
            cheap_dict[key]=food_dict_copy[key][0]
        elif(len(food_dict_copy[key])==2):
            price_1=get_price(key,food_dict_copy[key][0],store_dict)
            price_2=get_price(key,food_dict_copy[key][1],store_dict)
            if(price_1>price_2):
                cheap_dict[key]=food_dict_copy[key][1]
            elif(price_1==price_2):
                cheap_dict[key]=food_dict_copy[key][0]+","+food_dict_copy[key][1]
            else:
                cheap_dict[key]=food_dict_copy[key][0]
        else:
            price_1 = get_price(key, food_dict_copy[key][0], store_dict)
            price_2 = get_price(key, food_dict_copy[key][1], store_dict)
            price_3 = get_price(key, food_dict_copy[key][2], store_dict)
            if(price_1==price_2):
               cheap_dict[key]=food_dict_copy[key][0]+","+food_dict_copy[key][1]
            elif(price_1==price_3):
                cheap_dict[key]=food_dict_copy[key][0]+","+food_dict_copy[key][2]
            elif(price_2==price_3):
               cheap_dict[key]=food_dict_copy[key][1]+","+food_dict_copy[key][2]
           #elif((price_2==price_3 and price_3==price_1):
           #     cheap_dict[key]=food_dict_copy[0]+","+food_dict_copy[1]+food_dict_copy[2]
            else:
                if(price_1<price_2):
                    if(price_1<price_3):
                        cheap_dict[key]=food_dict_copy[key][0]
                    else:
                        cheap_dict[key]=food_dict_cop[key][2]
                else:
                    if(price_2>price_3):
                        cheap_dict[key]=food_dict_copy[key][2]
                    else:
                        cheap_dict[key]=food_dict_copy[key][1]
    for key in food_dict.keys():
        if (len(food_dict[key]) == 1):
            unique_list.append(key)

    for k, v in store_dict.items():
        for i in range(len(v)):
            v_list = v[i].split(":")  # v[1] = 'fish:1.2'
            if k not in store_dict_copy:
                store_dict_copy[k] = {}
                store_dict_copy[k][v_list[0]] = float(v_list[1])
            else:
                store_dict_copy[k][v_list[0]] = float(v_list[1])

    #
    # print(store_dict)
    # print(food_dict)
    # print(cheap_dict)
    # print (unique_list)
    # print(store_dict_copy)
    # print(food_dict_copy)
    #cheap_dict la 1 dict key la food value la string cua 1 hay nhieu cua hang
    print("Welcome to the shopping basket optimization app!")
    print("Available commands:")
    print(" S Print all the [S]tores with their available products")
    print(" P Print all the [P]roducts available in all the stores")
    print(" C Show the [C]heapest seller for a specified shopping basket")
    print(" Q [Q]uit")

    # a,b = read_inputfile("product")
    # print (a)
    # print (b)


    while True:
        print()

        command = input("Input command (S, P, C, Q): ")

        if command == "S":
            print_selections(store_dict)

        elif command == "P":
            print("Available products:")
            print_known_products(cheap_dict,store_dict)

        elif command == "C":
            find_cheapest_stores(store_dict_copy)
        elif command == "Q":
            print("Bye!")
            return

        else:
            print("Unknown command!?!")


main()
