from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    cand = []
    for i , num in enumerate(nums):
        leftnum = target - num
        if leftnum in cand:
            print([nums.index(leftnum), nums.index(num)])
            return
        cand.append(num)


if __name__ == "__main__":
    nums = list(map(int, input("nums = ").split()))
    target = int(input("target = "))
    twoSum( nums,target)