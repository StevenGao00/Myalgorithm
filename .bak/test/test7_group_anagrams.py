class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = {}
        for i in strs:
            b = ''.join(sorted(i))
            if b in res:
                res[b] += [i]
            else:
                res[b] = [i]
        return [res[i] for i in res]
if __name__=='__main__':
    strs = ["eat","tea","tan","ate","nat","bat"]
    A = Solution()
    res = A.groupAnagrams(strs)
    print(res)
