class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, currentcombo, currentsum):
            if currentsum == target:
                result.append(currentcombo[:])
                return
            if currentsum > target:
                return

            for i in range(start, len(nums)):
                currentcombo.append(nums[i])
                backtrack(i, currentcombo, currentsum + nums[i])
                currentcombo.pop()

        backtrack(0,[],0)
        return result
            



        