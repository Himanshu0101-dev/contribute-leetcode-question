class Solution:
    def minSubArrayLen(self, target: int, arr: list[int]) -> int:
        n = len(arr)
        left = 0
        s = 0
        ans = float('inf')

        for right in range(n):
            s += arr[right]
            while s >= target:
                ans = min(ans, right - left + 1)
                s -= arr[left]
                left += 1

        return -1 if ans == float('inf') else ans
