class Solution:
    def goodTriplet(self, arr : list[int], a : int, b : int, c : int) -> int:

        # i ---- j ---- k
        count = 0
        freq = [0] * 1001

        n = len(arr)


        for j in range(n - 1):
            for k in range(j + 1, n):
                if abs(arr[j] - arr[k]) <= b:
                    highest_floor = max(arr[j] - a, arr[k] - c)
                    lowest_ceiling = min(arr[j] + a, arr[k] + c)
                    highest_floor = max(0, highest_floor)
                    lowest_ceiling = min(1000, lowest_ceiling)

                    if highest_floor <= lowest_ceiling:
                        count += sum(freq[highest_floor : lowest_ceiling + 1])
            freq[arr[j]] += 1
        return count
    

def main():
    sol = Solution()
    print(sol.goodTriplet([3,0,1,1,9,7], 7, 2, 3))


if __name__ == "__main__":
    main()