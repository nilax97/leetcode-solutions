class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        def maxLen(arr, n):  
            hash_map = {}   
            curr_sum = 0 
            max_len = 0 
            ending_index = -1 
          
            for i in range (0, n):  
                if(arr[i] == 0):  
                    arr[i] = -1 
                else:  
                    arr[i] = 1 
          
            for i in range (0, n):  
                curr_sum = curr_sum + arr[i]  
                if (curr_sum == 0):  
                    max_len = i + 1 
                    ending_index = i  
                if curr_sum in hash_map:  
                    if max_len < i - hash_map[curr_sum]: 
                        max_len = i - hash_map[curr_sum] 
                        ending_index = i 
                else:  
                    hash_map[curr_sum] = i   

            for i in range (0, n):  
                if(arr[i] == -1):  
                    arr[i] = 0 
                else:  
                    arr[i] = 1 
          
            return max_len
        
        n = len(nums)
        return maxLen(nums,n)
