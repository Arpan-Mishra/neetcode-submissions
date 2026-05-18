class Solution:
    def confusingNumber(self, n: int) -> bool:
        num_str = str(n)

        confusing_nums = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}

        new_num = ''

        for i in num_str[::-1]:
            num = confusing_nums.get(i, -1)
            if num!=-1:
                new_num+=str(num)
            else:
                return False

        print(new_num)
        if int(new_num)!=n:

            return True
        else:
            return False
