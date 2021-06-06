class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        val = []
        for o in tokens:
            if o == "+":
                x = val.pop(-1)
                y = val.pop(-1)
                val.append(str(int(y) + int(x)))
            elif o == "-":
                x = val.pop(-1)
                y = val.pop(-1)
                val.append(str(int(y) - int(x)))
            elif o == "*":
                x = val.pop(-1)
                y = val.pop(-1)
                val.append(str(int(y) * int(x)))
            elif o == "/":
                x = val.pop(-1)
                y = val.pop(-1)
                val.append(str(int(int(y) / int(x))))
            else:
                val.append(o)
        return val[0]
            
                
