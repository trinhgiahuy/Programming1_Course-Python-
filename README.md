# Programming1_Course_Projects_Shorcut
A Python course 

## Table of contents
* [General info](#general-info)
* [Outline](#outline)


## General info
This directory comprise all markable projects (written in Python) of the course [programming-1-introduction-programming](https://www.tuni.fi/en/study-with-us/programming-1-introduction-programming-tampere-summer-school-2021)
-----
## Outline
* [Guessing Number Game](https://github.com/trinhgiahuy/Programming1_Course-Python-/blob/master/src/(GUI)Guessing_Number_Game.py)

  The topic of this project is not fixed, but rather, everyone can implement a graphical userinterface in the style they want, on the basis of their own abilities and interests. The task description will, however, give an idea on how complicated the implemented userinterface should be to achieve different grades.

  Additionally, we have set the following minimum requirements to the program:

  * A calculator is not a valid topic for a project.
  * A program that has already been implemented as an example during course materials would not be a valid topic for a project i.e. lecture example in Tkinter, programming task in the Tkinter round, nor a program edited from the aforementioned programs by developing them a little further. If you wish, you can, however, implement a graphical userinterface to one of the programs you implemented during the course which did not originally contain a graphical userinterface.
  * The program must include interaction with the user and it must be possible for the user to give incorrect entries. The program has to react to them fluently. In error situations, the user must receive a clear error notification. The execution of the program is thus not meant to end, but after the error, the user must have an opportunity to continue giving new entries.
  * The program must process the errors in a way that the Pycharm console does not display Python errormessages.
-----
* [Coffee_Gallup]()
Finnish people drink too much coffee. The authorities are concerned and decided to investigate the situation by arranging a gallup to find out some accurate numbers. Gallup asks each passing person, how many cups of coffee, they drink on a daily basis and writes down the response. Implement a program that conducts some calculations for the responses.

First the program prints:

```
Enter one response per line. End by entering an empty row.
```

and reads the integers entered by the user until the user wants to finish entering the numbers and enters an empty row to mark this.
First the program removes the responses of non-coffee-drinkers. If there are values to be removed, their number is announced to the user by printing:

```
Removed X non-coffee-drinkers responses
```

where X is replaced with the number of the measurement results.
If there are responses left, the program prints interesting information related to coffee drinking habits. First the program prints the text:

`Information related to coffee drinkers:`

After this, the program prints a graphic presentation of the distribution of the responses. The graphic presentation is a bar diagram, that contains a bar for each number inside the range of the response (between the smallest and the largest response). The first thing at the left of each line of the graphic representation is the value of the response printed in a 2-character-wide column. After this, the program prints one space, and after this the character "#" as many times as there are responses with this value. The presentation of the graphic visualization can be seen more specifically in the example run in the end of the task description. After the graphic presentation print one empty line. Example, when the responses entered are: 2, 1, 2, 5, 1, 1

```
 1 ###
 2 ##
 3 
 4 
 5 #
 
```
The recommendation is that you should not drink more than 4 cups of coffee per day. Next, the program prints the largest response, the most common response, and the percentage of the respondents that drink more than 4 cups of coffee per day:

```
The greatest response: X cups of coffee per day
The most common response: Y cups of coffee per day
Z% of the respondents drink more than 4 cups of coffee per day
```

where X, Y, and Z are replaced with correct values. If there are more than one most common responses, the smallest value of these responses is printed. The percentage value is printed to one decimal. Percentage value is printed only if it is greater than zero. If none of the respondents drink more than 4 cups of coffee per day, the printout is:

```
None of the respondents drink too much coffee
```
------
* [Shopping_basket_template](https://github.com/trinhgiahuy/Programming1_Course-Python-/blob/master/src/shopping_basket_template.py)

### Print store information
Command letter **S** prints stores and their product information. Both the store names and the product names must be printed in an alphabetical order:
```
Input command (S, P, C, Q): S
Herkkuduo
    cereal                2.12 e
    coffee                3.59 e
    eggs                  1.59 e
    fish                  1.10 e
    grapes                2.90 e
    macaroni              0.22 e
    milk                  0.82 e
    potatos               2.00 e
Lidl
    bread                 0.95 e
    coffee                2.99 e
    eggs                  1.00 e
    macaroni              0.19 e
    milk                  0.70 e
    potatos               2.11 e
    tuna                  1.29 e
S-market
    bread                 0.70 e
    coffee                3.27 e
    eggs                  1.14 e
    fish                  1.20 e
    macaroni              0.24 e
    milk                  0.81 e
    potatos               2.49 e
    tuna                  1.29 e
```
Input command (S, P, C, Q):
To make sure the output is correctly formatted you should use the format operation something like this:
```
"    {:<15s} {:>10.2f} e".format(...)
```
or formatted string:
```
f"    {...:<15s} {...:>10.2f} e"
```
Documentation for the **format** method might be helpful if the two suggestions above are not clear to you. The automated tester will be extremely uptight about the output looking exactly correct.

### Printing all available/known products
Command letter **P** prints all the products available in an aplhabetical order. After the name of the product its cheapest price should be printed with two decimals. Output should look like:
```
Input command (S, P, C, Q): P
Available products:
    bread                 0.70 e
    cereal                2.12 e
    coffee                2.99 e
    eggs                  1.00 e
    fish                  1.10 e
    grapes                2.90 e
    macaroni              0.19 e
    milk                  0.70 e
    potatos               2.00 e
    tuna                  1.29 e
```
Input command (S, P, C, Q): Q

### The cheapest seller for specified shopping basket's content
Command letter **C** reads the shopping basket's content from the user and figures out which store/stores sell it for the cheapets price.
```
Input command (S, P, C, Q): C
Input product names separated by a white space:
grapes coffee fish
The cheapest price for this shopping basket: Herkkuduo for 7.59 e

Input command (S, P, C, Q):
```
If more than one store sells the shopping basket's content equally cheap, the output should look like:
```
Input command (S, P, C, Q): C
Input product names separated by a white space:
eggs milk bread
Multiple stores sell this basket for 2.65 e: Lidl, S-market

Input command (S, P, C, Q):
```
The store names should be printed in an alphabetical order and the price of the basket with two decimals.

If there exists no store selling all the products in the basket, the following message should be printed:
```
Input command (S, P, C, Q): C
Input product names separated by a white space:
onion milk grapes
There is no store selling all those products.

Input command (S, P, C, Q):
```
-----
* [Routing_Protocol_Simulator](https://github.com/trinhgiahuy/Programming1_Course-Python-/blob/master/src/Routing_Protocol_Simulator.py)

![](https://github.com/trinhgiahuy/Programming1_Course-Python-/blob/master/img/routing_protocol.png?raw=true)

## Commands
When the program is started, it will first request the name of the input file according to the example below. If the user does not enter a filename, the program is started with no routers defined at all. First, implement a version that always starts with no routers defined. Later on you will also implement reading the router data from the input file. The final version of the program can be used both with or without entering a filename.

After requesting the input file, the program waits for a command from the user. If the user enters an unknown command the program will print an error message defined in the program code template. The command Q quits.
```
Network file:
> asd
Erroneous command!
Enter one of these commands:
NR (new router)
P (print)
C (connect)
NN (new network)
PA (print all)
S (send routing tables)
RR (route request)
Q (quit)
> Q
Simulator closes.
```

## NR (new router)
Define a new class called Router. Implement a constructor that takes the name of the router as a string parameter. This is the only parameter. The constructor is automatically tested when you submit your solution and the test fails if the parameters are not as instructed.

Later on, you need to add methods for adding neighbouring routers and the routing table for the router. You can add the attributes for storing these also later on, when you know how the router works.

Implement the command "NR", that will create a new router in the program according to the following example. When a new router is created it does not have connections to neighbour routers and its routing table is empty. The object is stored in the program so that it exists when the next commands are executed.
```
Network file:
> NR
Enter a new name: R1
> Q
Simulator closes.
```
If there is a router already defined by the same name, no new router is created and the user is provided with an error message:
```
Network file:
> NR
Enter a new name: R1
> NR
Enter a new name: R1
Name is taken.
> NR
Enter a new name: R6
> Q
Simulator closes.
```
## P (print)
Implement the command "P" that prints the name of the router and its neighbour routers and the routing table. If there is no router with this name, an error message will be provided for the user.

Implement the method print_info, that has no parameters and prints the information in the following format.
```
Network file:
> NR
Enter a new name: R1
> P
Enter router name: R1
  R1
    N:
    R:
> P
Enter router name: R8
Router was not found.
> Q
Simulator closes.
```
So far, we haven't added any neighbouring routers or anything in the routing table. Therefore, there is only empty space after the strings "N:" and "R:" in the example printouts.

## C (connect)
Implement the command "C", that connects two routers with each other. After the execution of this command, these two routers are neighbours to each other. This command requests names of two routers and adds the information about a new neighbouring router to both of them.

Implement the method add_neighbour, that has a router object as a parameter. It adds the name of the new neighbour router into the information of the router for which the method is called. This method only adds the neighbour to the router it is called for (it doesn't modify the state of both the objects but only one object, thus you need to call this method separately for both of the routers).

Each router can have multiple neighbouring routers. The neighbouring routers are printed in an alphabetical order and the names are separated by commas and spaces.

Add an attribute for storing the information related to the neighbouring routers and the printing of its content in the print_info-method.
```
Network file:
> NR
Enter a new name: R1
> NR
Enter a new name: R2
> NR
Enter a new name: R7
> C
Enter 1st router: R1
Enter 2nd router: R7
> C
Enter 1st router: R2
Enter 2nd router: R7
> P
Enter router name: R1
  R1
    N: R7
    R:
> P
Enter router name: R2
  R2
    N: R7
    R:
> P
Enter router name: R7
  R7
    N: R1, R2
    R:
> Q
Simulator closes.
```
## NN (new network)
Implement the command "NN", that adds a new network for a router. When a network is added, the router will be its edge router. This means that the distance between this router and the network is 0.

The edge router is the only router that can directly access this network. If you want to connect to this network you need to connect through the edge router. In the figure in the beginning of the task description, the router R3 is the edge router of the network 194.194.201.0 and the router R1 is the edge router of two networks. The distance of R2 to all of these three networks is 1.

Practically, if R1 and R2 are neighbours, and R2 is the edge router of the network 100, then the distance from R2 to network 100 is 0 (zero) and the distance from R1 to network 100 is 1 (one). At this point, do not implement a feature that transfers the information related to the networks to the neighbouring routers. Adding a network to a router only affects the state of this one router-object. The network appears in the routing table of this router when the information is printed.

Implent the method add_network, that has the parameters address of the network (str) and the distance to the network (int). Add an attribute for storing the routing table and the printing of its content in the method print_info.
```
Network file:
> NR
Enter a new name: R1
> NN
Enter router name: R1
Enter network: 100
Enter distance: 0
> P
Enter router name: R1
  R1
    N:
    R: 100:0
> NR
Enter a new name: R3
> C
Enter 1st router: R1
Enter 2nd router: R3
> P
Enter router name: R1
  R1
    N: R3
    R: 100:0
> P
Enter router name: R3
  R3
    N: R1
    R:
> Q
Simulator closes.
```
## PA (print all)
Implement the command "PA", that prints the information related to all the routers in an alphabetical order according to their names. This command naturally uses the method print_info that was implemented earlier.
```
Network file:
> NR
Enter a new name: R1
> NR
Enter a new name: R2
> NR
Enter a new name: R3
> PA
  R1
    N:
    R:
  R2
    N:
    R:
  R3
    N:
    R:
> C
Enter 1st router: R1
Enter 2nd router: R2
> NN
Enter router name: R3
Enter network: 300
Enter distance: 0
> PA
  R1
    N: R2
    R:
  R2
    N: R1
    R:
  R3
    N:
    R: 300:0
> Q
Simulator closes.
```
## Reading the input file
Implement the reading of the input file and creating router objects according to the information stored in the file.

The format of the files is: name!neighbour1;neighbour2...;neighbourN!network1:distance1;network2:distance2;...

Content of the line:

  1. The line always contains two exclamation marks
  2. The name of the router is on the left side of the first exclamation mark
  3. Between the exclamation marks there are the names of the neighbouring routers separated by semicolons or nothing if there are no neighbouring routers
  4. The neighbour-relationships is listed twice in the file: in the lines of both the routers
  5. On the right side of the later exclamation mark there is the content of the routing table
Examples of legal input file lines:
```
  R1!!
  R1 is a router that has no neighbours and no networks.

  R1!R2!
  R1 is a router that has the neighbour router R2. R1 has no networks.

  R1!!100:0
  R1 is a router that has no neighbours, but has the network 100 by
  the distance 0, i.e. R1 is the edge router of the netowork 100.

  R1!R2;R5;R9!200:0
  R1 is a router that has neighbours R2, R5 and R9.
  R1 also has the network 200 by the distance 0 (= edge router).
```
You can download input files representing different kinds of networks here: network1.txt, network2.txt, network3.txt

Using the previous inputfiles the program has to work like this:
```
Network file: network1.txt
> PA
  R1
    N: R2
    R:
  R2
    N: R1
    R:
  R3
    N:
    R: 300:0
> Q
Simulator closes.
```
```
Network file: network2.txt
> PA
  R1
    N: R2
    R: 100:0
  R2
    N: R1, R3
    R:
  R3
    N: R2, R4
    R:
  R4
    N: R3
    R:
  R5
    N:
    R: 500:0
> Q
Simulator closes.
```
```
Network file: network3.txt
> PA
  R1
    N:
    R: 100:0
  R2
    N: R3, R4
    R:
  R3
    N: R2
    R: 110:0
  R4
    N: R2, R5
    R:
  R5
    N: R4, R6
    R:
  R6
    N: R5, R7
    R:
  R7
    N: R6
    R: 700:0
> Q
Simulator closes.
```
If the file can not be opened or it contains a line which is not in the format described above, an error message is printed and program ends immediately.
```
Network file: a_file_that_doesnt_exist.txt
Error: the file could not be read or there is something wrong with it.
```
## S (send)
Real routers communicate with eachother in most of the routing protocols so that after some time interval all the routers send the content of their routing table to their neighbouring routers. The router looks through all the routing information it receives from its neighbour and if needed modifies its own routing table accordingly. This way the routers sustain information about the network state. The information about disconnected connections and new faster routes propagates from router to its neighbours.

Implement the command "S", that requests the name of a router and gives this router a command to send its routing table to its neigbouring routers. Using this command, the student of of computer networking could study how the routing tables are modified when the routers communicate with eachother.

Implement the method receive_routing_table, that has a router-object as its parameter. The method adds the content of the other router's routing table into its own routing table.

When the command "S" is executed, this method is to be called for the router's neighbours. If you want R1 to send its routing table to R2, you will call the method receive_routing_table of the object R2 and give the the object R1 as a parameter. This means R2 receives the routing table when R1 sends it. When this command "S" is executed, a method call is handled by all the receiving routers, i.e. all the neighbouring routers of the router that sends its routing table.
```
Network file: network1.txt
> PA
  R1
    N: R2
    R:
  R2
    N: R1
    R:
  R3
    N:
    R: 300:0
> S
Sending router: R3
> PA
  R1
    N: R2
    R:
  R2
    N: R1
    R:
  R3
    N:
    R: 300:0
> C
Enter 1st router: R3
Enter 2nd router: R2
> PA
  R1
    N: R2
    R:
  R2
    N: R1, R3
    R:
  R3
    N: R2
    R: 300:0
> S
Sending router: R3
> PA
  R1
    N: R2
    R:
  R2
    N: R1, R3
    R: 300:1
  R3
    N: R2
    R: 300:0
> S
Sending router: R2
> PA
  R1
    N: R2
    R: 300:2
  R2
    N: R1, R3
    R: 300:1
  R3
    N: R2
    R: 300:0
> Q
Simulator closes.
```
Another example including more networks:
```
Network file: network3.txt
> PA
  R1
    N:
    R: 100:0
  R2
    N: R3, R4
    R:
  R3
    N: R2
    R: 110:0
  R4
    N: R2, R5
    R:
  R5
    N: R4, R6
    R:
  R6
    N: R5, R7
    R:
  R7
    N: R6
    R: 700:0
> C
Enter 1st router: R1
Enter 2nd router: R2
> PA
  R1
    N: R2
    R: 100:0
  R2
    N: R1, R3, R4
    R:
  R3
    N: R2
    R: 110:0
  R4
    N: R2, R5
    R:
  R5
    N: R4, R6
    R:
  R6
    N: R5, R7
    R:
  R7
    N: R6
    R: 700:0
> S
Sending router: R1
> PA
  R1
    N: R2
    R: 100:0
  R2
    N: R1, R3, R4
    R: 100:1
  R3
    N: R2
    R: 110:0
  R4
    N: R2, R5
    R:
  R5
    N: R4, R6
    R:
  R6
    N: R5, R7
    R:
  R7
    N: R6
    R: 700:0
> S
Sending router: R3
> PA
  R1
    N: R2
    R: 100:0
  R2
    N: R1, R3, R4
    R: 100:1, 110:1
  R3
    N: R2
    R: 110:0
  R4
    N: R2, R5
    R:
  R5
    N: R4, R6
    R:
  R6
    N: R5, R7
    R:
  R7
    N: R6
    R: 700:0
> S
Sending router: R2
> PA
  R1
    N: R2
    R: 100:0, 110:2
  R2
    N: R1, R3, R4
    R: 100:1, 110:1
  R3
    N: R2
    R: 100:2, 110:0
  R4
    N: R2, R5
    R: 100:2, 110:2
  R5
    N: R4, R6
    R:
  R6
    N: R5, R7
    R:
  R7
    N: R6
    R: 700:0
> S
Sending router: R4
> PA
  R1
    N: R2
    R: 100:0, 110:2
  R2
    N: R1, R3, R4
    R: 100:1, 110:1
  R3
    N: R2
    R: 100:2, 110:0
  R4
    N: R2, R5
    R: 100:2, 110:2
  R5
    N: R4, R6
    R: 100:3, 110:3
  R6
    N: R5, R7
    R:
  R7
    N: R6
    R: 700:0
> S
Sending router: R5
> PA
  R1
    N: R2
    R: 100:0, 110:2
  R2
    N: R1, R3, R4
    R: 100:1, 110:1
  R3
    N: R2
    R: 100:2, 110:0
  R4
    N: R2, R5
    R: 100:2, 110:2
  R5
    N: R4, R6
    R: 100:3, 110:3
  R6
    N: R5, R7
    R: 100:4, 110:4
  R7
    N: R6
    R: 700:0
> Q
Simulator closes.
```
## RR (route request)
Implement the command "RR", that tells if a certain router has a connection to a certain network.

Implement the method has_route, that has the network name (str) as a parameter and prints the following information on the screen.
```
Network file: network2.txt
> PA
  R1
    N: R2
    R: 100:0
  R2
    N: R1, R3
    R:
  R3
    N: R2, R4
    R:
  R4
    N: R3
    R:
  R5
    N:
    R: 500:0
> RR
Enter router name: R1
Enter network name: 100
Router is an edge router for the network.
> RR
Enter router name: R1
Enter network name: 500
Route to the network is unknown.
> S
Sending router: R1
> PA
  R1
    N: R2
    R: 100:0
  R2
    N: R1, R3
    R: 100:1
  R3
    N: R2, R4
    R:
  R4
    N: R3
    R:
  R5
    N:
    R: 500:0
> RR
Enter router name: R2
Enter network name: 100
Network 100 is 1 hops away
> S
Sending router: R2
> S
Sending router: R3
> PA
  R1
    N: R2
    R: 100:0
  R2
    N: R1, R3
    R: 100:1
  R3
    N: R2, R4
    R: 100:2
  R4
    N: R3
    R: 100:3
  R5
    N:
    R: 500:0
> RR
Enter router name: R4
Enter network name: 100
Network 100 is 3 hops away
> Q
Simulator closes.
```
-----
# MORE PROJECT CAN BE FOUND IN [`src`](https://github.com/trinhgiahuy/Programming1_Course-Python-/tree/master/src) directory