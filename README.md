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
* [Coffee_Coffee_Gallup]()
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