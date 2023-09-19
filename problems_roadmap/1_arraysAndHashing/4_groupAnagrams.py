# https://leetcode.com/problems/group-anagrams/
# For those who don't know what is defaultdict(list). It means "Defining a dictionary with values as a list
# Also it will give you error so dont forget to use this in your code.
# from collections import defaultdict

def groupAnagrams(strs):
    from collections import defaultdict

    ans = defaultdict(list)

    for s in strs:
        cnt = [0] * 26

        for chr in s:
            cnt[ord(chr) - ord('a')] += 1

        ans[tuple(cnt)].append(s)
    
    return ans.values()