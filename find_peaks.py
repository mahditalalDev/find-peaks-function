# find index of  index and the  max of the list

def findPeaks(list):                            #O(1)                            
    temp_peak_index_list = [list[0],0]          #O(1)      # give the list initial values      
    for i in range (1,len(list)):               #O(1en(list)) in my code the len of list Constant
        if list[i] > temp_peak_index_list[0]:   #O(1)
            temp_peak_index_list[0] = list[i]   #O(1)      # store peak value into temp list
            temp_peak_index_list[1] = i         #O(1)      # store index of temp value into temp list
    return(temp_peak_index_list)                #O(1)      # the function will return list of two values peak and its index



peak_index=findPeaks([1,4,5,12,1,4,2])          #O(1)
print(f"the peak value of the list {peak_index[0]} and its index ={peak_index[1]} ") #O(1)