def reverseList(listB):
    #Lambda is a temporary function. In this case, it is taking the given list and appending it in reverse order
    reverse = lambda l: (reverse (l[1:]) + l[:1] if l else [])
    #after it has reversed the order, the following line prints the list in reverse order
    print (reverse (listB))

def main():
    
    #default list
    listB = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    reverseList(listB)

main()