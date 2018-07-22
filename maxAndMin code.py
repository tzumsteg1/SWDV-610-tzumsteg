def findMax(listA):
    #Searches through the list to determine if there are more than one value.
    #If there is one value, that is the maximum value so it will return that value
    if len(listA) == 1:
        return listA[0]
    
    #If there is more than one term, the system will search through the entire list for the maximum
    else:
        maximum = max(listA[0:])
        
        return maximum

def findMin(listA):
    #Searches through the list to determine if there are more than one value.
    #If there is one value, that is the minimum value so it will return that value
    if len(listA) == 1:
        return listA[0]
    
    #If there is more than one term, the system will search through the entire list for the minimum
    else:
        minimum = min(listA[0:])
        return minimum

def main():
    #The following line will allow the user to input their own list. delete the pound symbols to run this system and comment out the list below
    ##listA = eval(input('Enter a list of numbers: '))
    
    ##This is a test list, if you want to run your own list, comment the next line out and delete the pound symbols above.
    listA = [1, 2, 4, 6, 7, 88, -1, 10]
    
    #Displays the list
    print(listA)
    
    #Displays the maximum value
    print("The maximum value is: ", findMax(listA))
    
    #Displays the minimum value
    print("The minimum value is: ", findMin(listA))
    
main()
    
    