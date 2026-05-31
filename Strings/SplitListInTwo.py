class Solution:
    def splitArr(self,  nums : list[int]) -> bool:
        freq = {}



        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
            
            if freq[nums[i]] > 2:
                return False
        
        return True


        
    

def main():
    sol = Solution()
    print(sol.splitArr([1,1,2,2,3,4]))
    print(sol.splitArr([1,1,1,2,2,3,3,4,4,5,6,7,7]))


if __name__ == "__main__":
    main()

            

            
