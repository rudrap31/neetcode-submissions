from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        prereqs = [0] * numCourses
        blocking = {x: [] for x in range(numCourses)}
        res = []
        
        for course, pre in prerequisites:
            blocking[pre].append(course)
            prereqs[course] += 1


        dq = deque([c for c in range(numCourses) if prereqs[c] == 0])

        while dq:
            curc = dq.popleft()
            res.append(curc)
            for coursetofree in blocking[curc]:
                prereqs[coursetofree] -= 1
                if prereqs[coursetofree] == 0:
                    dq.append(coursetofree)
            
        if len(res) == numCourses:
            return res
        return []
                


        


