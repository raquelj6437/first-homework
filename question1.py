num = input('Enter numbers seperated by a comma: ') #prompts the user to enter numbers
num = num.split(',') #seperates number by comments
num = list(map(int, num)) #converts numbers in list into an integer

print(max(num))
print(min(num))
print(sum(num)/len(num)) #finds mean of numbers in list
