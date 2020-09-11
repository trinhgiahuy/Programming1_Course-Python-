# TIE-02107 Introduction to Programming
# Huy Trinh Gia , giahuy.trinh@tuni.fi, student nr: 290290
# Solution of task 3.4: Aquarium
# A program that defines the water’s suitability for zebra fishes and
# return the average value of pH


def main():

    #get user input and analysis
    num_of_user_input=int(input("Enter the number of the measurements: "))
    if(num_of_user_input<=0):
        print("Error: the number must be expressed as a positive integer.")
    else:
        #i: counting variable
        #sum: the sum of all data
        #pre_data_input: the previous data
        i=1
        sum=0
        pre_data_input=0

        #a loop that get data from user_input
        while i<= num_of_user_input:
            i_convert=str(i)
            data_input=float(input("Enter the measurement result "+i_convert+": "))
            if(data_input>=6 and data_input<=8):
                sum+=data_input

                #analysis the absolte value of consecutive data
                if(i>1):
                    dif=abs(pre_data_input-data_input)
                    if(dif<=1):
                        pre_data_input=data_input
                        i+=1
                        continue
                    else:
                        print("The conditions are not suitable for zebra fishes.")
                        return 0
                else:
                    pre_data_input = data_input
                    i += 1
                    continue

            
            #print out the caution when the pH is not suitable
            else:
                print("The conditions are not suitable for zebra fishes.")
                return 0


        #print out the average pH value
        print("Conditions are suitable for zebra fishes. The average pH is {:0.2f}.".format(sum/num_of_user_input))

main()