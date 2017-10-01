def merge(left, right):
    result = []
    n, m = 0, 0
    while n < len(left) and m < len(right):
        if left[n] <= right[m]:
            result.append(left[n])
            n += 1
        else:
            result.append(right[m])
            m += 1

    result += left[n:]
    result += right[m:]
    return result

def sort(seq):
    if len(seq) <= 1:
        return seq
    else:
        middle = int(len(seq) / 2)
        left = sort(seq[:middle])/Users/Kelele67/Desktop/C-Interfaces-and-Implementations/src
        right = sort(seq[middle:])
        return merge(left, right)

if __name__ == '__main__':
    arr = [4, 3, 9, 6, 7, 7]
    print (sort(arr))