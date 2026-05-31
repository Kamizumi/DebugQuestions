class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        while num >= 10:

            curr_sum = 0
            #E.g 38
            while num > 0:
                curr_sum += num % 10 #This gets the last digit -> 8
                num = num // 10 #Grabs the number in front of the last digit -> 3
            
            num = curr_sum
        
        return num


def main():
    sol = Solution()
    print(sol.addDigits(38))
    print(sol.addDigits(1234567))


if __name__ == "__main__":
    main()