def smallestSubWithSum(arr, sum): 
    current = 0
    start = 0
    end = 0

    n = len(arr)
    min_len = n + 1
    
    while(end < n):
        while(current <= sum and end < n):
            current += arr[end]
            end += 1

        while(current > sum and start < n):
            if (end - start < min_len):
                min_len = end - start
            
            current -= arr[start]
            start += 1
    return min_len
    

# test 
print(smallestSubWithSum([1,4,45,6,0,19], 51))

 

