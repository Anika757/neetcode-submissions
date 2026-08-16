class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        answer = []
        for num in nums:
            if num in dict1.keys():
                dict1[num] = dict1[num] + 1
            else:
                dict1[num] = 1
        sortedlist = sorted(dict1.values(), reverse=True)
        for z in range(0,k):
            for i,j in dict1.items():
                if j == sortedlist[z]:
                    answer.append(i)
                    dict1[i] = 0
        return answer