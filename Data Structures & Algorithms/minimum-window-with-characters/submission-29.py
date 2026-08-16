#i have letters in T
#i want to find a substring in S that contains all the letters of T
#i start from the fisrt letter, check if its in T.
#if it is, start the substring, if its not move onto the next letter
#i want to do this until all substrings are checked through s


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict1 = {}
        left = 0
        right = 0
        satisfied = 0
        subset = ""
        shortest = len(s)
        answer = ""
        for char in t:
            if char in dict1.keys():
                dict1[char] = dict1[char] + 1
            else:
                dict1[char] = 1
        required = len(dict1)
        for right in range(len(s)):
            if s[right] in dict1.keys():
                dict1[s[right]] = dict1[s[right]] - 1
                if dict1[s[right]] == 0:
                    satisfied += 1
            if required == satisfied:
                subset = s[left:right + 1]

            while satisfied == required:
                if s[left] in dict1.keys():
                    dict1[s[left]] = dict1[s[left]] + 1
                    if dict1[s[left]] == 1:
                        satisfied -= 1
                
                subset = s[left:right + 1]
                if int(len(subset)) <= int(shortest):
                    answer = str(subset)
                    shortest = int(len(subset))
                left += 1

        return answer


            


            



            




                

