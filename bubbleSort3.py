def bubbleSortStrings(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def testBubbleSortStrings():
    # Teste 1: Lista desordenada de strings
    arr1 = ["banana", "apple", "cherry", "date"]
    print("Lista original:", arr1)
    bubbleSortStrings(arr1)
    print("Lista ordenada:", arr1)
    print()

    # Teste 2: Lista já ordenada de strings
    arr2 = ["apple", "banana", "cherry", "date"]
    print("Lista original:", arr2)
    bubbleSortStrings(arr2)
    print("Lista ordenada:", arr2)
    print()

    # Teste 3: Lista em ordem decrescente de strings
    arr3 = ["zebra", "yellow", "x-ray", "wolf", "apple"]
    print("Lista original:", arr3)
    bubbleSortStrings(arr3)
    print("Lista ordenada:", arr3)
    print()

    # Teste 4: Lista com strings repetidas
    arr4 = ["apple", "banana", "banana", "cherry", "apple"]
    print("Lista original:", arr4)
    bubbleSortStrings(arr4)
    print("Lista ordenada:", arr4)
    print()

    # Teste 5: Lista com um único elemento
    arr5 = ["apple"]
    print("Lista original:", arr5)
    bubbleSortStrings(arr5)
    print("Lista ordenada:", arr5)
    print()

    # Teste 6: Lista vazia
    arr6 = []
    print("Lista original:", arr6)
    bubbleSortStrings(arr6)
    print("Lista ordenada:", arr6)
    print()

testBubbleSortStrings()
