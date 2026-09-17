# contribute-leetcode-question
Minimum Window Subarray with Target Sum

Find the shortest subarray of arr whose sum is greater than or equal to target. Return the length of this subarray. If no such subarray exists, return -1.

Example 1

Input: arr = [2,3,1,2,4,3], target = 7
Output: 2
Explanation: The subarray [4,3] has sum = 7 and length = 2, which is the shortest.
Example 2

Input: arr = [1,1,1,1,1,1,1], target = 11
Output: -1
Explanation: No subarray has sum ≥ 11.
Example 3

Input: arr = [5,1,3,5,10,7,4,9,2,8], target = 15
Output: 2
Explanation: The subarray [10,7] has sum = 17 and length = 2.
Constraints

1 ≤ arr.length ≤ 10^5

1 ≤ arr[i] ≤ 1000

1 ≤ target ≤ 10^9
