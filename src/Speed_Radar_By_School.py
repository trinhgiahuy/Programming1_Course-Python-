from math import *
list=[]

def ask(limit):
    """" Ask user's input
    @param limit(int): the speed limit
    @return an list containing speeds limit
    """
    if(limit<0):
        print("The speed limit must be expressed as a positive integer.")
        return
    elif limit == 0:
        print("The speed limit must be expressed as a positive integer.")
        return []
    else:
        print("Enter the results of the speed measurements, finish with an empty line:")
        while True:
            counting = input()
            if (counting == ""):
                break
            # add all user's input into a list
            else:
                list.append(int(counting))

        return list

array=[]

def caculation(limit):
    """ Caculate data and remove data speed which is lower than 20km/h
    :param limit:
    :return:count
    """

    msg=ask(limit)
    count=0
    # caculating data in the list
    for i in range(0,len(msg)):
        if msg[i]<20:
            count+=1
        else:
            array.append(msg[i])
            continue
    if(count!=0):
        print("Ignored {} measurement results whose values were under 20 km/h".format(count))

    return count


fine_list=[]

def statistic(limit, array):
    """
    Caculating range, median, 
    :param limit,array:
    :param array: 
    :print: range, median, list contain speed that need fine ticket
    """
    # caculate range
    if len(array) > 0:
        maxValue = max(array)
        minValue = min(array)
        print("Range:",maxValue-minValue)

        array1 = sorted(array)

        length=len(array1)
        index= (length/2) - 1

    # caculate median
        if(length%2!=0):
            print("Median: {:0.1f}".format(array1[ceil(index)]))
        else:
            print("Median: {:0.1f}".format((((array1[int(index)]))+array1[int(index+1)])/2))
        count_M=0
        count_N=0
        for k in range(len(array)):
            if(array[k]>=limit+8 and array[k]<limit+20):
                count_N+=1
                fine_list.append(array[k])
            if array[k]>=limit+20:
                count_M+=1
                fine_list.append(array[k])
            continue
        #sort data speed which need fine ticket
        if(count_N>0):
            print("The on-the-spot-fine for speeding would have been issued to {} drivers".format(count_N))
        if(count_M>0):
            print("The fine for speeding would have been issued to {} drivers".format(count_M))
        if(len(fine_list)>0):
            print("Speeders in the order of measurements:")
            for f in range(len(fine_list)):
                print(fine_list[f])

def main():
    limit = int(input("Enter the speed limit for the measurement location: "))

    caculation(limit)

    statistic(limit, array)


main()

