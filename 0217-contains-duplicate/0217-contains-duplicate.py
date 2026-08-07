class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for val in nums:
            if val not in hashmap:
                hashmap[val] = 1
            else:
                return True
        return False