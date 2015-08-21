__author__ = 'Eugenia'
numbers = [1,2,3,4,5,6,7,8,9,10]

search = int(input("Type a number to search for: "))

def mid(testlist):
    length = len(testlist)
    middle = length // 2
    return middle

test = mid(numbers)

#numbers[test] refers to the number under the index
#(5 in this case which corresponds to the number 6 in the list

if numbers[test] == search:
    print("Found the number in one go, the index is:",search - 1)

else:
    while mid(numbers) != search:
        if numbers[test] == search:
            print ("The index is: ", search - 1)

        elif numbers[test] > search:
            new = numbers[:test]
            new1 = mid(new)


        elif numbers[test] < search:
            new = numbers[test:]
            new1 = mid(new)

        else:
            print ("Number not found")

