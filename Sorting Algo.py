import tkinter as tk
import sys
import time as t
import random

sys.setrecursionlimit(10000)

root = tk.Tk()
root.geometry("350x655")
root.resizable(0, 0)
frame1 = tk.Frame(root)


root.title("Sorting Algorithms")
#---RULES
tk.Label(
    text = "Please follow the below rules for sorting numbers:"
).pack()

tk.Label(
    text = "1.)Enter a single number -> ADD ENTRY"
).pack()

tk.Label(
    text = "2.)If you enter wrong number -> RESET"
).pack()

tk.Label(
    text = "3.)Then Choose ascending or descending"
).pack()

tk.Label(
    text = "4.) Finally select desired SORTING ALGORITHM."
).pack()

label1 = tk.Label(
    text="  Please enter the numbers you wish to sort:  "
)

entry1 = tk.Entry(
    frame1,
    width = 6
)

showComp = tk.Label(
    text = " "
)

label1.pack()
frame1.pack()
entry1.pack(side = tk.LEFT)

lst = list()

showNum = tk.Label(
    text=" "
)

def rand_entry():
    global lst
    value = random.randint(0,999)
    lst.append(value)
    showNum["text"] = lst

def add_to_list():
    global lst
    getting = entry1.get()
    print(getting)
    lst.append(getting)
    print(lst)
    showNum["text"] = lst

def reset_list():
    lst.clear()
    showNum["text"] = "Please add some numbers, again!"

ranButton = tk.Button(
    frame1,
    text="Randomize",
    command=rand_entry
).pack( side = tk.RIGHT)

resetButton = tk.Button(
    frame1,
    text = "Reset Entry",
    command = reset_list
).pack( side = tk.RIGHT)

addButton = tk.Button(
    frame1,
    text="Add Entry",
    command=add_to_list
).pack( side = tk.RIGHT)


showNumLabel = tk.Label(
    text="The numbers for sorting are:"
).pack()

showNum.pack()

v = tk.IntVar()
v.set(0)

orientations = [
    "Descending",
    "Ascending"
]

choice = 0


def ShowChoice():
    global choice
    if v.get() == 0:
        choice = 0
    else:
        choice = 1
    print(choice)


tk.Label(root,
         text="""Choose your orientation:""",
         justify=tk.LEFT,
         padx=20).pack()

for val, orientations in enumerate(orientations):
    tk.Radiobutton(root,
                   text=orientations,
                   padx=20,
                   variable=v,
                   command=ShowChoice,
                   value=val).pack()

resDisplay = tk.Label(
    text=" "
)

resTime = tk.Label(
)

# ALGORITHMS - start
def sel_sort():
    global lst
    t0 = t.time()
    A=lst
    for i in range(len(A)):
        min_idx = i
        for j in range(i + 1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]
    print(A)
    if choice:
        resDisplay["text"] = A
    else:
        A.reverse()
        resDisplay["text"] = A
    t1 = t.time()-t0
    resTime["text"] = t1
    showComp["text"] = "O(n^2)"

def bubble_sort():
    t0 = t.time()
    global lst
    global choice
    for passesLeft in range(len(lst) - 1, 0, -1):
        for i in range(passesLeft):
            if choice:
                if lst[i] > lst[i + 1]:
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
            else:
                if lst[i] < lst[i + 1]:
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
    resDisplay["text"] = lst
    t1 = t.time()-t0
    resTime["text"] = t1
    showComp["text"] = "O(n^2)"


def insertion_sort():
    global lst
    t0 = t.time()
    for step in range(1, len(lst)):
        key = lst[step]
        j = step - 1
        if choice:
            while j >= 0 and key < lst[j]:
                lst[j + 1] = lst[j]
                j = j - 1
        else:
            while j >= 0 and key > lst[j]:
                lst[j + 1] = lst[j]
                j = j - 1
        lst[j + 1] = key
    resDisplay["text"] = lst
    t1 = t.time() - t0
    resTime["text"] = t1
    showComp["text"] = "O(n^2)"


def merge_sort():
    t0 = t.time()
    global lst
    global choice
    if choice:
        mergeSortAsc(lst)
    else:
        mergeSortDsc(lst)
    resDisplay["text"] = lst
    t1 = t.time() - t0
    resTime["text"] = t1
    showComp["text"] = "O(n log(n))"

def mergeSortAsc(arr=lst):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        mergeSortAsc(L)
        mergeSortAsc(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def mergeSortDsc(arr=lst):
    if arr is None:
        arr = lst
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        mergeSortDsc(L)
        mergeSortDsc(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] > R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def quick_sort():
    t0 = t.time()
    global lst
    global choice
    arr = lst
    n = len(arr)
    quickSort(arr, 0, n - 1)
    if choice:
        resDisplay["text"] = arr
    else:
        arr.reverse()
        resDisplay["text"] = arr
    t1 = t.time()-t0
    resTime["text"] = t1
    showComp["text"] = "O(n^2)"

def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):


        if arr[j] < pivot:

            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def quickSort(arr, low, high):
    if low < high:

        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


def heap_sort():
    global lst
    t0 = t.time()
    arr = lst
    global choice
    heapSort(arr)
    if choice:
        resDisplay["text"] = arr
    else:
        arr.reverse()
        resDisplay["text"] = arr
    t1 = t.time() - t0
    resTime["text"] = t1
    showComp["text"] = "O(n log(n))"


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    if l < n and arr[i] < arr[l]:
        largest = l


    if r < n and arr[largest] < arr[r]:
        largest = r


    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap


        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def lt_sort():
    t0 = t.time()
    global lst
    arr = lst
    global choice
    radixSort(arr)
    if choice:
        resDisplay["text"] = arr
    else:
        arr.reverse()
        resDisplay["text"] = arr
    t1 = t.time() - t0
    resTime["text"] = t1
    showComp["text"] = "O(k n)"


def countingSort(arr, exp1):
    n = len(arr)

    output = [0] * (n)

    count = [0] * (10)

    for i in range(0, n):
        index = (arr[i] / exp1)
        count[(index) % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] / exp1)
        output[count[(index) % 10] - 1] = arr[i]
        count[(index) % 10] -= 1
        i -= 1

    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]


def radixSort(arr):
    max1 = max(arr)
    exp = 1
    while max1 / exp > 0:
        countingSort(arr, exp)
        exp *= 10

# ALGORITHMS - end

tk.Label(
    text="Select the algorithm:"
).pack()

btn_selection = tk.Button(
    text="Selection Sort",
    command = sel_sort
).pack()

btn_bubble = tk.Button(
    text="Bubble Sort",
    command=bubble_sort
).pack()

btn_insertion = tk.Button(
    text="Insertion Sort",
    command=insertion_sort
).pack()

btn_merge = tk.Button(
    text="Merge Sort",
    command=merge_sort
).pack()

btn_quick = tk.Button(
    text="Quick Sort",
    command = quick_sort
).pack()

btn_heap = tk.Button(
    text="Heap Sort",
    command = heap_sort
).pack()

btn_lt = tk.Button(
    text="Linear time Sort"
).pack()

tk.Label(
    text="Resulting sorted list:"
).pack()

resDisplay.pack()

tk.Label(
    text = "Time elpased in seconds is:"
).pack()

resTime.pack()

tk.Label(
    text="Complexity of the Algorithm is:"
).pack()
showComp.pack()

tk.Label(
    text = " ------------------------------------ "
).pack()

tk.Label(
    text = "Program written by A. Waqas, Roll No. 18103020, CSE 4th Sem"
).pack()
tk.Label(
    text = "Dr. B.R. Ambedkar N.I.T. Jalandhar, India"
).pack()

root.mainloop()
