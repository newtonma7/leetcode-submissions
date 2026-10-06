class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preSums = {0 : 1}
        currSum = 0
        ans = 0

        for n in nums:
            currSum += n

            diff = currSum - k

            if diff in preSums:
                ans += preSums[diff]
                
            preSums[currSum] = preSums.get(currSum, 0) + 1
        
        return ans

            
