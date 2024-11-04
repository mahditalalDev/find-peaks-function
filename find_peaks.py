# find index of  index and the  peaks of the list

def findPeaks(list):
    temp_peaks_list=[]
    temp_index_peak_list=[]
    for i in range(len(list)-1):
        if i==0:
            continue
        if list[i] > list[i-1] and list[i] > list[i+1]:
            temp_peaks_list.append(list[i])
            temp_index_peak_list.append(i)
        
    print(temp_peaks_list)
    print(temp_index_peak_list)
findPeaks([0,4,2,10,4,5])