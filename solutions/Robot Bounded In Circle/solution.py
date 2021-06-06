class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        def dist(x,y):
            return x*x+y*y
        def move(inst, x, y, face):
            if inst == "G":
                if face == 0:
                    y+=1
                elif face == 1:
                    x+=1
                elif face == 2:
                    y-=1
                else:
                    x-=1
            elif inst == "R":
                face = (face+1) % 4
            else:
                face = (4 + (face-1)) % 4
            return (x,y,face)
        x = 0
        y = 0
        face = 0
        lens = [0]
        flag = 0
        for i in range(100):
            for inst in instructions:
                x,y,face = move(inst, x, y, face)
            lens.append(dist(x,y))
            if lens[-1] <= lens[-2]:
                flag = 1
                break
        # print(lens)
        if flag == 1:
            return True
        else:
            return False
        
