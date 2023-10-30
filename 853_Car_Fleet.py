class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        position_speed = []
        for i in range(len(position)):
            position_speed.append((position[i], speed[i]))
            
        position_speed.sort(reverse=True)
        
        ans_stack = []
        for p, s in position_speed:
           dist = target - p
           if not ans_stack:
               ans_stack.append(dist*1.0/s)
           elif dist/s > ans_stack[-1]:
                ans_stack.append(dist*1.0/s)
        print(ans_stack)
        return len(ans_stack)
    

s = Solution()
s.carFleet(10, [6,8], [3,2])