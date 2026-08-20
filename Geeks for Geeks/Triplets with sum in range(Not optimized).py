class Solution:
   
    def countTriplets(self, arr: list[int], l: int, r: int) -> int:
        freq = 0

        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                for k in range(j+1,len(arr)):
                    sum = arr[i] + arr[j] + arr[k]
                    if l <= sum <=r:
                        freq+=1

        return freq
        