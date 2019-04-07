

class Solution:
    def firstMissingPositive(self, nums):
        #Base Case
        if 1 not in nums:
            return 1
        #Convert all negative and zeroes to 1
        # Replace negative numbers, zeros,
        # and numbers larger than n by 1s.
        # After this conversion nums will contain
        # only positive numbers.
        for index, each in enumerate(nums):
            if each <= 0 or each > len(nums):
                nums[index] = 1

        # Change the sign of eachth element, keeping in mind of duplicates
        # Can use hashset for the same but that increases space complexity by n
        # So rather use absolute value to make sure the sign remains intact for that
        # index
        for each in nums:
            each = abs(each)
            if each == len(nums):
                nums[0] = - abs(nums[0])
            else:
                nums[each] = - abs(nums[each])

        # All data cleaning has been done properly
        # Now check for the first positive value in the list
        # return the index of this value as that is the answer
        for i in range(1, len(nums)):
            if nums[i] > 0:
                return i
        # If not check if the answer is length of the list
        if nums[0] > 0:
            return len(nums)
        #Else return len +1 as that is the only possible solution
        return len(nums) + 1


if __name__ == "__main__":
    s = Solution()
    print(s.firstMissingPositive([3,4,-1,1]))