# Please enter the numbers separated by comma


numbers= input('enter the numbers separated by comma:')
list_num=numbers.split(',')#Split the input string into a list

odd_numbers =0
even_numbers =0
for i in list_num:
    if int(i)%2 == 0:
        even_numbers +=1
    else:
        odd_numbers +=1
print('number of even numbers:' , even_numbers)
print('number of odd numbers:' , odd_numbers)


