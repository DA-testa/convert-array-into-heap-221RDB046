# python3


def build_heap(n, data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    for i in range(n // 2, -1, -1):
        j =i
        while j<n:
            leftCh = 2 * j + 1
            rightCh= 2 * j + 2
            if leftCh < n and data[leftCh] < data[j]:
                parent = leftCh
            else: 
                parent = j
            if rightCh < n and data[rightCh] < data[parent]:
                parent = rightCh
            
            if parent == j:
                break
            else:
                data[j], data[parent] = data[parent], data [j]
                swaps.append((j, parent))
                j = parent
    

    



    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    text = input()
    if text[0] == "I":
        # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
        swaps = build_heap(n, data)
    elif text[0] == "F":
        file_name = "tests/"
        file_name = file_name + input()
        if "a" in file_name:
            return
        with open(file_name, 'r')as file:
            n = int(file.readline())
            data = list(map(int, file.readline().strip().split()))
            assert len(data) == n
            swaps = build_heap(n,data)

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
