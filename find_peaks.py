# find index of  index of the max

def findPeaks(list):
    temp_peak_index_list = [list[0],0]               # give the list initial values      
    for i in range (1,len(list)): 
        if list[i] > temp_peak_index_list[0]:
            temp_peak_index_list[0] = list[i]      # store peak value into temp list
            temp_peak_index_list[1] = i            # store index of temp value into temp list
    return(temp_peak_index_list)                   # the function will retrun list of two values peak and its index



peak_index=findPeaks([1,4,5,12,1,4,2])    
print(f"the peak value of the list {peak_index[0]} and its index ={peak_index[1]} ")