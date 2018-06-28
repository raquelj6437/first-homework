a = input('Enter words or letters or sentances: ') #prompts user to enter characters
a = sorted(a,key=a.count,reverse=True) #sorts list by frequency of each character

def char_frequency(str1): #organizes frequency of character with its character
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

print(char_frequency(a)) #prints frequency count
