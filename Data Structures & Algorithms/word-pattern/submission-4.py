class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        i = 0
        j = 0
        dict1 = {}
        lists = s.split()

        if len(pattern) != len(lists):
            return False

        for i in range(len(pattern)):
            if pattern[i] in dict1:
                if dict1[pattern[i]] != lists[i]:
                    return False
            else:
                if lists[i] in dict1.values():
                    return False
                dict1[pattern[i]] = lists[i]
        return True

            
        