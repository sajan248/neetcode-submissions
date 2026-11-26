class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupMap = {}
        for num in nums:
            if num not in dupMap:
                dupMap[num] = 1
                
            else:
                dupMap[num] = dupMap.get(num) + 1
        
        for count in dupMap.values():
            if count > 1:
                return True
        return False
        


        