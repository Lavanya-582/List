'''


2)Write a program to create a list and display it. 
Input format:
Input consist of n+1 integers
First integer corresponds to the size of the list
Next n inputs corresponds to the elements in the list 
Output format: 
Output is an integer list
Sample Input
4 
1
2
3
4
'''
# Function to create and display the list
def create_and_display_list():
    # Input the size of the list
    n = int(input("Enter the size of the list: "))
    
    # Initialize an empty list
    my_list = []
    
    # Input the elements of the list
    print("Enter the elements of the list:")
    for _ in range(n):
        element = int(input())
        my_list.append(element)
    
    # Output the list
    print("The list is:", my_list)

# Call the function
create_and_display_list()
