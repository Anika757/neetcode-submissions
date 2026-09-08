class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dict1 = {}
        for c in text:
            if c in "balon":
                if c in dict1.keys():
                    dict1[c] += 1
                else:
                    dict1[c] = 1
        
        if len(dict1) < 5:
            return 0

        count = dict1["l"] // 2
        count1 = dict1["o"] //2
        return min(count,count1)