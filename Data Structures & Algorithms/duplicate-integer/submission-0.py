class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
# time1: O(size2) - brute force  / space1: O(1)
#        for i in range(len(nums)):
#            for j in range(i + 1, len(nums)):
#                if nums[i] == nums[j]:
#                    return True
#        return False
# time2: O(sizelogsize) - sorting, better solution / space2: O(1)
#        nums.sort()
#        for i in range(1, len(nums)):
#            if nums[i] == nums[i-1]:
#                return True
#        return False
# time3: O(size) - HashSet, add each element there and check if already added / 
# space3: 0(size) - the memory usage will be up to the size of the array
        hashset = set()
        for value in nums:
            if value in hashset:
                return True
            hashset.add(value)
        return False    
