class Solution:
    def maxSubArraySum(self, arr, N):
        # todo for neg all
        all_neg = []
        for i in arr:
            if i < 0:
                all_neg.append(i)
            if i >= 0:
                break

        if len(arr) == len(all_neg):
            all_neg.sort()
            e = all_neg[len(all_neg) - 1]
            return e


        # todo for non neg and positive
        else:
            max = 0
            current = 0
            for i in arr:
                current += i

                if current > max:
                    max = current

                if current < 0:
                    current = 0
            return max

def main():
    T = int(input())
    while (T > 0):
        n = int(input())

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr, n))

        T -= 1


if __name__ == "__main__":
    main()
