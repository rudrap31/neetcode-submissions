class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stk = []
        fleets = 0

        for i in range(len(position)):
            ctarget = target - position[i]
            t = ctarget / speed[i]
            stk.append((position[i], t))
        stk.sort()
        
        while stk:
            __, time = stk.pop()

            while stk and time >= stk[-1][1]:
                stk.pop()
            fleets += 1
        
        return fleets




        