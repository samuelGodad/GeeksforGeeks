class Solution: 
    def select(self, arr, i):
        max=-1
        pos=0
        for j in range(i,0,-1):
            if max<arr[j]:
                max=arr[j]
                pos=j
        return pos
        # code here 
    
    def selectionSort(self, arr,n):
        for step in range(n):
            mins = step
            for j in range(step+1,n):
                if arr[mins]>arr[j]:
                    mins=j
            arr[step],arr[mins]=arr[mins],arr[step]
        return arr
        
