class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index=0
        n=0
        while index<len(nums):
            if nums[index]==val:
                del(nums[index])
                n+=1
                continue
            elif nums[index]!=val:
                index+=1
                continue
        k=len(nums)
        return k


        