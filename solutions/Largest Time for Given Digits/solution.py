class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        def validtime(hour, mins, maxtime):
            if hours < 24 and mins<60:
                time = hours*60 + mins;
                if time > maxtime:
                    maxtime = time
            return maxtime
        maxtime = 0.0
        for i in range(0,4):
            for j in range(0,4):
                if i==j:
                    continue
                for k in range(0,4):
                    if i==k or j==k:
                        continue
                    for l in range(0,4):
                        if i==l or j==l or k==l:
                            continue
                        hours = A[i]*10 + A[j]
                        mins = A[k]*10 + A[l]
                        maxtime = validtime(hours,mins, maxtime)
        hours = int(maxtime / 60)
        mins = int(maxtime % 60)
        # print(hours,mins,maxtime)
        if maxtime == 0.0 and (A[0]+A[1]+A[2]+A[3])>0:
            return ""
        else:
            hours_str = str(hours)
            mins_str = str(mins)
            if hours<10:
                hours_str = "0" + str(hours)
            if mins<10:
                mins_str = "0" + str(mins)
            return hours_str + ":" + mins_str
                        
