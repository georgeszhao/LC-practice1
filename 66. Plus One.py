class Solution:
    """
    @param digits: a number represented as an array of digits
    @return: the result
    """
    def plusOne(self, digits):
        # write your code here
        i=len(digits)-1
        while i>=0:
            if digits[i]==9:
                digits[i]=0
            else:
                digits[i]+=1
                break
            i-=1
        if i==-1:
            return [1]+digits
        else:
            return digits

def execute() -> object:
    digits = [9,9,9]
    sol = Solution()
    print(sol.plusOne(digits))

if __name__ == "__main__":
    execute()
    