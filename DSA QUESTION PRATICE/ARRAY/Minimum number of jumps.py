class Solution:
    def minJumps(self, arr, n):
        if len(arr) == 1:
            return 0

        end = arr[0]
        jump = 0
        big = arr[0]
        for i in range(1,len(arr)-1):
            end-=1
            big = max(big,i+arr[i])
            if(end == 0):
                jump+=1
                big= end-i
        jump+=1

        return jump

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr,n)
        print(ans)