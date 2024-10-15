'''
3)Write a Python Program to find the largest number in a list
Input & Output Format:
Input consists of one list and one integer.
First input consists of a size of a list.
Second inputs corresponds to the size of the list.
Output consists of the largest element.
Sample Input:
5
1
2
3
6
5
Sample Output:
6
'''
# Function to find the largest number in a list
def find_largest_number(num_list):
    return max(num_list)

# Main program
if __name__ == "__main__":
    # Input size of the list
    size = int(input("Enter the size of the list: "))
    
    # Input elements of the list
    num_list = []
    for _ in range(size):
        num = int(input())
        num_list.append(num)
    
    # Find and print the largest number
    largest_number = find_largest_number(num_list)
    print(largest_number)
