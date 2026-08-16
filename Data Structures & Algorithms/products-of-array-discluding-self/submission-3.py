class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final = []
        for i in range(len(nums)):
            answer = 1
            reducednums = nums[:i] + nums[i+1:]
            for num in reducednums:
                answer = (answer * num)
            final.append(answer)
        return final

