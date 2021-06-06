class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = list()
        ans = 0
        while(True):
            while(len(students) > 0):
                if students[0] == sandwiches[0]:
                    students.pop(0)
                    sandwiches.pop(0)
                else:
                    q.append(students[0])
                    students.pop(0)
            if ans == len(q):
                break
            ans = len(q)
            for i in range(ans):
                students.append(q[0])
                q.pop(0)
        return ans
            
