from collections import deque

class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        dead = set(deadends)
        if "0000" in dead:
            return -1
        
        q = deque()
        q.append(("0000", 0))
        visited = set("0000")
        
        while q:
            state, steps = q.popleft()
            
            if state == target:
                return steps
            
            for i in range(4):
                digit = int(state[i])
                
                for move in [-1, 1]:
                    new_digit = (digit + move) % 10
                    new_state = state[:i] + str(new_digit) + state[i+1:]
                    
                    if new_state not in visited and new_state not in dead:
                        visited.add(new_state)
                        q.append((new_state, steps + 1))
        return -1
                