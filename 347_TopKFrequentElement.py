class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # make a defaultdict 0
        # key is the number, value is the occurance i.e. {0:2,1:1} for 0,0,1
        k_freq = defaultdict(int)
        k_list = []
    
        # update until all values have been added
        for num in nums:
            k_freq[num] += 1

        # sort the dict based on values using sorted(), takes in each dict k:v pair, sorts on the value using kv[1]
        k_sorted = sorted(k_freq.items(),key=lambda kv:kv[1])

        # return k most frequent vals, iterating backwards through k_sorted
        for i in range(k):
            # len() - 1 to not be out of bounds
            val = k_sorted[(len(k_sorted)-1) - i]
            k_list.append(val[0])

        return k_list
