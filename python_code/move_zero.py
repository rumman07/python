def move_zero(arr):
    count = 0 
    for num in arr:
        if num != 0:
            arr[count] = num
            count += 1 
    arr[count:] = [0] * (len(arr) - count)
    return arr 