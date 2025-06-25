class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        strs.sort(key=len)
        min_word = strs[0]
        
        for i in range(len(min_word), 0, -1):
            prefix = min_word[:i]
            is_common = True
            for word in strs:
                if not word.startswith(prefix):
                    is_common = False
                    break
            if is_common:
                return prefix
        
        return ""
