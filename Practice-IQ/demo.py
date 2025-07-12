### Practice interview questions on Python.

## Ques 1. To find prime numbers from the list of numbers

# Sol 1.

# number = int(input("Please enter number of your choice: "))

# if number <= 1:
#     print ("Please enter any positive number greater than 1")
# else:
#     for i in range(2, number):
#         if number%i == 0:
#             print("Given number is not prime number.")
#             break
#     else:
#         print(f"Given number is prime number {number}")

## Ques 2. How to sort elements in a given list in asscending order ?

# Sol 2.

# M0 || Sorting in Ascending order.

# my_list=[11, 12, 1, 7, 10]

# for i in range(len(my_list)):
#     for j in range(len(my_list)-1):
#         if my_list[j] > my_list[i]:
#            my_list[i],my_list[j] = my_list[j],my_list[i]

# print(my_list)

# M1 || Using inbuilt function || Sorting in Ascending order.

# my_list=[11, 12, 1, 7, 10]

# sorted_list=sorted(my_list)
# print(sorted_list)

# M2 || By initializing empty array || Sorting in Ascending order.

# my_list=[11, 12, 1, 7, 10]

# emp=[]
# while my_list:
#     smallest = my_list[0]
#     for i in my_list:
#         if i < smallest:
#             smallest = i
#     emp.append(smallest)
#     my_list.remove(smallest)

# print(emp)

## Ques 3. How to sort elements in a given list in descending order ?

# Sol 3.

# M0 
# my_list=[11, 12, 1, 7, 10]

# new_sorted_list=sorted(my_list, reverse=True)
# print(new_sorted_list)

# M1
# my_list=[11, 12, 1, 7, 10]

# emp=[]
# while my_list:
#     largest=my_list[0]
#     for i in my_list:
#         if i > largest:
#             largest = i
#     emp.append(largest)
#     my_list.remove(largest)

# print(emp)

# M2
# my_list=[11, 12, 1, 7, 10]

# for i in range(len(my_list)):
#     for j in range(len(my_list)-1):
#         if my_list[j] < my_list[i]:
#             my_list[i],my_list[j] = my_list[j],my_list[i]

# print(my_list)

## Ques 4. How to find duplicate elements, unique elements and sort unique elements in ascending order?

# Sol: 4 : Method 1

# Calculating duplicate elements in an array /list.

# my_list=[70, 1, 2, 3, 55, 1, 3, 90]
# dup=[]
# not_dup=[]

# for i in my_list:
#     if my_list.count(i) > 1 and i not in dup:
#         dup.append(i)

# print(dup)

# Calculating a new list / array without duplicates.

# for i in my_list:
#     if i not in not_dup:
#         not_dup.append(i)

# print(not_dup) 

# FUrther we are going to arrange elements in ascending order.

# emp=[]
# while not_dup:
#     smallest = not_dup[0]
#     for j in not_dup:
#         if j < smallest:
#             smallest = j 
#     emp.append(smallest)
#     not_dup.remove(smallest)

# print(emp)

# Method -2 

# my_new_arr=[11, 2, 99, 22, 2, 100, 99]

# modify_list=set(my_new_arr)
# print(modify_list)
# asc_sort=sorted(modify_list)
# print(asc_sort)
# des_sort=sorted(modify_list, reverse=True)
# print(des_sort)


# Ques 5. How to find 2nd largest element in the given list?

# Sol 5 .

# dummy_list=[1, 22, 4, 90, 100, 89]
# sort_arr=sorted(dummy_list)
# print(sort_arr)
# print(sort_arr[-2])

# Ques 6. Printing Fibonacci series & also calculating nth fibonacci number ?
# Sol 6.

# Method 1 : Using for loop.

# num=int(input("Please enter the number of your choice. "))
# n1=0 # Meaning value of 1st element of series.
# n2=1 # Meaning value of 2nd element in the series.

# if num <= 0:
#     print("Please enter the valid number. ")
# elif num == 1:
#     print(n1)
# elif num == 2:
#     print(n2)
# else:
#     for i in range(num):
#         total = n1 + n2
#         n1=n2
#         n2=total
#         print(total) # To print entire fiboncaci series.
#     # print(total) # To print last or final element of fibonacci series.

# Method 2 : Using while loop.

# num=int(input("Please enter the number of your choice. "))
# n1=0 # Meaning value of 1st element of series.
# n2=1 # Meaning value of 2nd element in the series.
# counter=0

# if num <= 0:
#     print("Please enter the valid number. ")
# elif num == 1:
#     print(n1)
# elif num == 2:
#     print(n2)
# else:
#     while counter < num:
#         total = n1 + n2
#         n1=n2
#         n2=total
#         counter += 1
#         print(total) # To print entire fiboncaci series.
#     # print(total) # To print last or final element of fibonacci series.

# Method 3 : Using recursion.

# def fib(n):
#     if n <=0:
#         print("Please enter positive natural number. ")
#     elif n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# n=int(input("Please enter your input. "))
# print(fib(n)) # To print final element of fibonacci series.

# # for i in range(n): # To print entire series till the value of n.
# #     print(fib(i))

# Ques 7. How to reverse a list, string, number using in built function & without inbuilt function & also check 
# palindrome case whereever possible ?

# Sol 7:

############# For List / Array in python ######################################################

# Method 1 & Condition 1.... Using inbuilt function.

# my_list=[1, 2, 3, 2, 1]

# new_list=my_list[::-1]
# print(new_list)

# Method 2 & Condition 2.... Without using inbuilt function.

# start = 0                   # Initialize start with index 0
# end = len(my_list) - 1      # Initialize end with the index of the last element

# while start < end:
#     my_list[start], my_list[end] = my_list[end], my_list[start]  # Swap the elements at the start and end.

#     # Move the pointers towards the center
#     start += 1
#     end -= 1

# print(my_list)

# Method 3 & Condition 3.....  Check if given list is pallindrome or not

# start = 0
# end = len(my_list)-1
# while start < end:
#     if my_list[start] != my_list[end]:
#         print("The given list is not Pallindrome. ")
#         break
#     start += 1
#     end -= 1
# else:
#     print("Given list is Pallindrome. ")

############# For String in python ####################################################################

# Method 1 & Condition 1.... Using inbuilt function. [ Reversing the string .]

# my_str = "malayalam"  # Tesed with abcd, madam etc.
# new_str = ""

# new_str = my_str[::-1]
# print(new_str)

# Method 2 & Condition 2.... Without using inbuilt function.

# for i in my_str:
#     #print(i)
#     new_str = i + new_str
# print(new_str)

# Method 3 & Condition 3.....  Check if given string is pallindrome or not

# if new_str == my_str:
#     print("The original string is pallindrome. ")
# else:
#     print("The original string is not pallindrome. ")


############# For Number / Integer in python ################################################# 

# Method 1 & Condition 1.... Using inbuilt function. [ Reversing the Number.]

# my_num = str(123)
# rev_num=int(my_num[::-1])
# print(rev_num)

# Method 2 & Condition 2.... Without using inbuilt function.

# my_num = 343
# temp = my_num
# rev = 0

# while my_num > 0:
#     rem = my_num%10
#     rev = rev*10 + rem
#     my_num = my_num//10

# print(rev)

# # Method 3 & Condition 3.....  Check if given number is pallindrome or not.

# if ( rev == temp ):
#     print("Given number is palindrome. ")
# else:
#     print("Given number is not pallindrome. ")

# Ques 8 : Check if the given number is Armstrong or not ?

# Sol 8 :

test_num=153
temp=test_num
rev=0
order= len(str(test_num))

while test_num > 0:
    rem = test_num%10
    rev = rev + rem**order
    test_num = test_num//10

print(rev)

if ( rev == temp ):
    print("The given number is armstrong number. ")
else:
    print("The given number is not armstrong number. ")