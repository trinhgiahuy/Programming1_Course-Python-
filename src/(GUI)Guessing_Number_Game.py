#student name : Trinh Gia Huy
#studnet number : 290290
#TIE-02107
 
from tkinter import *
from tkinter import messagebox
import time
#the program is a guessing number game that the computer random a four-different-digit number
#the player has to guess the correct number based on the clues

#computer random a number and makes sure that the digits are all different
from random import randint
a=str(randint(1,9))
b=str(randint(0,9))
c=str(randint(0,9))
d=str(randint(0,9))
while a==b or b==c or c==d or a==d or a==c or b==d :
  a=str(randint(1,9))
  b=str(randint(0,9))
  c=str(randint(0,9))
  d=str(randint(0,9))
computer_number= a + b + c + d


class game_board():
    """
            We create a class game board including user interface elements, variables
            for the game and all methods that can be applied to the objects of the class.
    """

    def __init__(self):

        #General setting of the main program

        self.__MainBoard = Tk()
        self.__MainBoard.title("WELCOME TO THE GUESING NUMBER GAMER")

        #Assignment of the introduction and rules of the game
        Label(self.__MainBoard, text='-'*20).grid(row = 0)
        Label(self.__MainBoard, text="The programme will random a four-different-digit number.").grid(row = 1)
        Label(self.__MainBoard, text="You have to guess that number base on the number of TRUE and FALSE").grid(row = 2)
        Label(self.__MainBoard, text="TRUE: number of digits which is correct").grid(row = 3)
        Label(self.__MainBoard, text="FALSE: number of digits which is in wrong order but still in that number ").grid(row = 4)
        Label(self.__MainBoard, text='-' * 20).grid(row = 5)
        Label(self.__MainBoard, text="NOTE: 4 DIFFERENT DIGITS NUMBER").grid(row = 6)
        Label(self.__MainBoard, text="LETS START!!!").grid(row = 7)
        Label(self.__MainBoard, text="Enter your number:").grid(row = 8)

        #Assignment of the text variable and placing it in the main board
        self.__player_number = Entry(self.__MainBoard)
        self.__player_number.grid(row = 9)

        #Placing the bottons
        self.__check_player_number = Button(self.__MainBoard, text = "CHECK", command = self.checking_input, fg = 'green')
        self.__check_player_number.grid(row = 10, column = 1)
        self.__exit_button = Button(self.__MainBoard, text = "EXIT", command = self.exit, fg = 'red')
        self.__exit_button.grid(row = 11, column = 1)

        #the values being calculated
        self.__True = Label(self.__MainBoard)
        self.__True.grid(row = 12, column = 1)
        self.__True_result = Label(self.__MainBoard)
        self.__True_result.grid(row=12, column = 0)
        self.__False = Label(self.__MainBoard)
        self.__False.grid(row = 13, column = 1)
        self.__False_result = Label(self.__MainBoard)
        self.__False_result.grid(row=13, column=0)

        # Label(self.__MainBoard, text = computer_number).grid(row = 13)

    def checking_input(self):
        """
                This method reads the user input (the player's guessing number,
                checking if this number is correct.
                If not gives player clues for the correct number.
        """
        player_number = str(self.__player_number.get())

        #Checking to make sure the input is wrong based on the game rules
        if player_number == '':
            messagebox.showerror('Error', 'Please, enter a number!')
        elif len(player_number) != 4 and player_number != '':
            messagebox.showerror('Error', 'Please, enter number has 4 digits!')
        elif player_number[0] == '0':
            messagebox.showerror('Error', 'First digit can not be 0!')
        elif not player_number.isdigit():
            messagebox.showerror('Error', 'Please, enter integer number!')
        elif player_number[0]==player_number[1] or player_number[0]==player_number[2] or player_number[0]==player_number[3] or player_number[1]==player_number[2] or player_number[1]==player_number[3] or player_number[2]==player_number[3]:
            messagebox.showerror("Error", "Enter number has 4 DIFFERENT digits!")
        else:

                #true: the number of digit(s) in the player number that are correct
                #       (in both magnitude and order).
                #false: the number of digit(s) in the player number that have the
                #        magnitude correct but in the wrong order.

            true = 0
            false = 0
            check = 0
            computer_number_after = ''
            user_number_after = ''
            j = 0
            a = []
            while j < 4:
                i = 0
                while i < 4:
                    if computer_number[i] == player_number[j]:
                        if i == j:
                            true += 1
                            a.extend(str(i))
                            break
                    i += 1
                j += 1
            for i in a:
                    computer_number_after += computer_number[check:(int(i))]
                    user_number_after += player_number[check:(int(i))]
                    check = int(i) + 1
            computer_number_after += computer_number[check:4]
            user_number_after += player_number[check:4]
            k = 0
            if (true != 4):
                while k < len(computer_number_after):
                    m = 0
                    while m < len(computer_number_after):
                        if computer_number_after[m] == user_number_after[k]:
                            false += 1
                            break
                        m += 1
                    k += 1

            self.__True.configure(text = "TRUE")
            self.__True_result.configure(text = true)

            self.__False.configure(text = "FALSE")
            self.__False_result.configure(text = false)

            if true == 4:
                result = f"""YOU WON! \nTHE CORRECT NUMBER IS {computer_number}\n"""
                messagebox.showinfo('Result', result)


    def begin(self):
        self.__MainBoard.mainloop()

    def exit(self):
        self.__MainBoard.destroy()

def main():
    game = game_board()
    game.begin()
main()


