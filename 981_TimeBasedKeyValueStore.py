class TimeMap:

    def __init__(self):
       self.timeDict = {}
        
    # stores the [value,timestamp] of a key 
    def set(self, key: str, value: str, timestamp: int) -> None:
        # if the key doesnt exist already we create an empty list to store the later values in
        if key not in self.timeDict:
            self.timeDict[key] = []

        # after that we append onto that list, NOTE: The timestamps are in increasing order by default 
        self.timeDict[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:

        #default res value is ""
        res = ""
        # dictonary get method, [] will be returned if nothing is found
        values = self.timeDict.get(key,[])
      
        # now we binary search
        l,r = 0, len(values)-1

        while l <= r:
            m = (l+r)//2
            if values[m][1] == timestamp:
                # we found the answer so break out
                res = values[m][0]
                break
            elif values[m][1] < timestamp:
                # we havent found the answer yet but we need a closest value thats less than it so update the res
                res = values[m][0]
                l = m+1
            elif values[m][1] > timestamp:
                # the answer is too large so keep going 
                r = m-1

        return res
            
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)