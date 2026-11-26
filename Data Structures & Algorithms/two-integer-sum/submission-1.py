class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Pair each number with its original index: [[num, index], ...]
        A = []
        for idx, num in enumerate(nums):
            A.append([num, idx])
            
        A.sort()  # Sorts A in-place by the first element (num)

        i, j = 0, len(A) - 1

        while i < j:
            cur = A[i][0] + A[j][0]
            if cur == target:
                return [min(A[i][1], A[j][1]),
                        max(A[i][1], A[j][1])]
            elif cur < target:
                i += 1
            else:
                j -= 1
        return []
