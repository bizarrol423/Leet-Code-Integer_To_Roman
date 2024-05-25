# link to ex https://leetcode.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, num: int) -> str:
        dict_number = {
            1:'I',
            2:'II',
            3:'III',
            4:'IV',
            5:'V',
            6:'VI',
            7:'VII',
            8:'VIII',
            9:'IX',
            10:'X',
            20:'XX',
            30:'XXX',
            40:'XL',
            50:'L',
            60:'LX',
            70:'LXX',
            80:'LXXX',
            90:'XC',
            100:'C',
            200:'CC',
            300:'CCC',
            400:'CD',
            500:'D',
            600:'DC',
            700:'DCC',
            800:'DCCC',
            900:'CM',
            1000:'M',
            2000:'MM',
            3000:'MMM',
        }
        len_num = len(str(num))-1
        ret = ''
        for i in range(len(str(num))):
            razrad = 10 ** (len_num - i)
            razrad = (num // razrad % 10) * razrad
            for j in dict_number:
                if not(razrad-j):
                    ret += dict_number[j]
                    break
        return ret

if __name__ == "__main__":
    num = 2436
    print(Solution.intToRoman(Solution,num))