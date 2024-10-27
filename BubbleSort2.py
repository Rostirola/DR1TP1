def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def testBubbleSort():
    # Teste 1: Lista desordenada
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", arr1)
    bubbleSort(arr1)
    print("Lista ordenada:", arr1)
    print()

    # Teste 2: Lista já ordenada
    arr2 = [1, 2, 3, 4, 5]
    print("Lista original:", arr2)
    bubbleSort(arr2)
    print("Lista ordenada:", arr2)
    print()

    # Teste 3: Lista em ordem decrescente
    arr3 = [10, 9, 8, 7, 6, 5]
    print("Lista original:", arr3)
    bubbleSort(arr3)
    print("Lista ordenada:", arr3)
    print()

    # Teste 4: Lista com valores repetidos
    arr4 = [5, 1, 4, 2, 8, 5, 2]
    print("Lista original:", arr4)
    bubbleSort(arr4)
    print("Lista ordenada:", arr4)
    print()

    # Teste 5: Lista com um único elemento
    arr5 = [3]
    print("Lista original:", arr5)
    bubbleSort(arr5)
    print("Lista ordenada:", arr5)
    print()

    # Teste 6: Lista vazia
    arr6 = []
    print("Lista original:", arr6)
    bubbleSort(arr6)
    print("Lista ordenada:", arr6)
    print()

testBubbleSort()
