class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber < 27:
            return chr(ord('A') - 1 + columnNumber)
        val = list()
        columnNumber = columnNumber - 1
        while(True):
            val.append(columnNumber % 26)
            if (columnNumber < 26):
                break
            columnNumber = columnNumber // 26 - 1
        ans = list()
        for i in range(len(val)-1,-1,-1):
            ans.append(chr(ord('A') + val[i]))
        return "".join(ans)
