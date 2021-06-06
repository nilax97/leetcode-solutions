class Solution:
    def defangIPaddr(self, address: str) -> str:
        solution = "";
        value = address.split(".")
        solution = solution + value[0]
        for i in range(1,len(value)):
            solution = solution + "[.]";
            solution = solution + value[i];
        return solution
