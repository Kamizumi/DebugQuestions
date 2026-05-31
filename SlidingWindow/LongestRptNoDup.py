from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indexed = Counter()
        l = 0
        res = 0

        for r in range(len(s)):
            right = s[r]
            if s[r] in indexed:
                l = max(indexed[right] + 1, l)
            indexed[right] = r
            res = max(res, r - l + 1)
        
        return res

def main():
    sol = Solution()
    print(sol.lengthOfLongestSubstring("xyzxyz"))

if __name__ == "__main__":
    main()

            



        