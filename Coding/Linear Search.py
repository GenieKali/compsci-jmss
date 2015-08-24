__author__ = 'Eugenia'

list = [1,2,3,4,5,6,7,8,9,10]
search = int(input("Enter a number: "))

index = 0
found = False

for i in list:
    if i == search:
        found = True
        print ("Index of the number is", index)
    else:
        index += 1
if found == False:
    print ("Number not found")