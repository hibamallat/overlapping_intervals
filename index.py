"""
Write a function merge_intervals(intervals), where intervals is an array of arrays.
The functions merges overlapping intervals and returns a list of the merged intervals. 
"""
#array = [[1,3] , [2,4] , [6,8]]
#array = [[1,5] , [2,6] , [8,10] , [9,12]]
array = [[1,3] , [6,8] , [2,4]]

def merge_intervals(intervals):

    intervals = sorted(intervals)

    merged_list = [] 

    for i in range (len(intervals) - 1):

        start_index = intervals[i+1][0]

        end_index = intervals[i][1]

        if  start_index <= end_index :
            merged_list.append([intervals[i][0] , intervals[i+1][1]])
        else:
            merged_list.append(intervals[i+1])
                       
    return merged_list
print(array)
print(merge_intervals(array))