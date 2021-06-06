class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if(len(nums)==1):
            if nums[0]==target:
                return 0
            else:
                return -1
        targetp = -1
        start = 0
        end = len(nums)-1
        while(start<=end):
            mid = (start + end)//2
            if(mid==len(nums)-1):
                break
            if nums[mid] > nums[mid+1]:
                targetp = mid
                break
            if nums[start] > nums[mid]:
                end = mid-1
            else:
                start = mid+1
        if targetp != -1:
            new_arr = nums[targetp+1:] + nums[:targetp+1]
        else:
            new_arr = nums
        start = 0
        print(new_arr)
        end = len(new_arr) - 1
        while(start<=end):
            mid = (start + end)//2
            print(mid,new_arr[mid],target)
            if new_arr[mid]==target:
                return (mid+targetp+1)%len(nums)
            elif target < new_arr[mid]:
                end = mid -1
                continue
            else:
                start = mid + 1
                continue
        return -1
