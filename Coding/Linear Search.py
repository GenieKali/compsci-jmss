__author__ = 'Eugenia'

list = [1,2,3,4,5,6,7,8,9,10]
search = int(input("Enter a number: "))

index = 0

for i in list:
    if i == search:
        print ("The index of the number is:",index)
    else:
        index += 1

        
if search not in list:
    print ("Number not in list")