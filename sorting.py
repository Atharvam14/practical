
# Function for Selection Sort of elements

def Selection_Sort(marks):
    for i in range(len(marks)):

        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, len(marks)):
            if marks[min_idx] > marks[j]:
                min_idx = j

        # Swap the minimum element with the first element
        marks[i], marks[min_idx] = marks[min_idx], marks[i]

    print("Numbers after performing Selection Sort on the list : ")
    for i in range(len(marks)):
        print(marks[i])

# Function for Bubble Sort of elements

def Bubble_Sort(marks):
    n = len(marks)
    # Traverse through all array elements
    for i in range(n - 1):
        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if marks[j] > marks[j + 1]:
                marks[j], marks[j + 1] = marks[j + 1], marks[j]

    print("Numbers after performing Bubble Sort on the list :")
    for i in range(len(marks)):
        print(marks[i])

marks=[]
n = int(input("How many numbers do you want to sort? : "))
print("Enter the numbers(Press ENTER after every number): ")
for i in range(0, n):
    ele = float(input())
    marks.append(ele)  # adding the element

print("The numbers are : ")
print(marks)

flag=1;
while flag==1:
    print("\n---------------MENU---------------")
    print("1. Selection Sort")
    print("2. Bubble Sort")
    print("3. Exit")
    ch=int(input("\n\nEnter your choice (from 1 to 3) : "))

    if ch==1:
        Selection_Sort(marks)
        a=input("\nDo you want to continue(yes/no)? :")
        if a=="yes":
            flag=1
        else :
            print("\nThanks for using this program!")
            flag=0

        print("\nThanks for using this program!")
        flag=1

    elif ch==2:
        Bubble_Sort(marks)
        a=input("\nDo you want to continue(yes/no)? :")
        if a=="yes":
            flag=1
        else :
            print("\nThanks for using this program!")
            flag=0

    elif ch==3:
        print("\nThanks for using this program!!")
        flag=0

    else:
        print("\nEnter a valid choice!!")
        print("\nThanks for using this program!!")
        flag=0
