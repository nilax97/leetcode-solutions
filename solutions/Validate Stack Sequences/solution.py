class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        while(True):
            # print(stack,pushed,popped)
            if len(popped) > 0 and len(stack) > 0:
                if stack[-1] == popped[0]:
                    stack.pop(-1)
                    popped.pop(0)
                    continue
            if len(pushed) > 0:
                stack.append(pushed.pop(0))
                continue
            if (len(pushed) == 0 and len(popped)==0):
                break
            return False
        return True
