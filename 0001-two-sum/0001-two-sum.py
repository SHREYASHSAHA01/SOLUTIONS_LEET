#leet
class Solution(object):
    def twoSum(self, nums, target):
        arr = []
        for idx, num in enumerate(nums) :
            arr.append((num,idx))
        arr = sorted(arr)
        left = 0
        right = len(nums) - 1
        while left < right :
            total = arr[left][0] + arr[right][0]
            if total == target :
                return (arr[left][1],arr[right][1])
            elif total > target :
                right -= 1
            else:
                left += 1