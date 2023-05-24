def selection_sort(list1):
    # Traverse through all array elements
    for i in range(len(list1)-1):
        # Find the minimum element in the remaining unsorted array
        smallest = i
        for j in range(i+1, len(list1)):
            if list1[j] < list1[smallest]:
                smallest = j
                # Swap the found minimum element with the first element
        list1[i], list1[smallest] = list1[smallest], list1[i]

list1 = []
n = int(input('How many numbers do you want in the list: '))
for _ in range(n):
    number = int(input('Enter a number: '))
    list1.append(number)

selection_sort(list1)
print('Sorted list is:', list1)
