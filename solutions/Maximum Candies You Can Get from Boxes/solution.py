class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], 
        initialBoxes: List[int]) -> int:
        ans = 0
        closed_boxes = list()
        while(len(initialBoxes)>0):
            # print(initialBoxes,closed_boxes,status)
            box = initialBoxes.pop(0)
            if status[box]==0:
                closed_boxes.append(box)
            else:
                ans += candies[box]
                for key in keys[box]:
                    if status[key]==0:
                        status[key]=1
                for conbox in containedBoxes[box]:
                    initialBoxes.append(conbox)
            clbox2 = list()
            for clbox in closed_boxes:
                if status[clbox]==1:
                    initialBoxes.append(clbox)
                else:
                    clbox2.append(clbox)
            closed_boxes = clbox2
        return ans
                    
            
