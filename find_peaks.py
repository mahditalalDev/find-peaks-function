# find index of max

def findPeaks(list):
    peak = list[0]
    temp_index = 0
    for i in range (1,len(list)): 
        if list[i] > peak :
            peak = list[i]
            temp_index = i
    return(temp_index)
print(findPeaks([1,2,3,5,1]))