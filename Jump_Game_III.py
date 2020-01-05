# Problem 1306 on Leetcode, Jump Game III
# Runtime: 204 ms, faster than 80.50% of Python online submissions for Jump Game III.
# Memory Usage: 17.1 MB, less than 100% of Python online submissions for Jump Game III.

# Uses a BFS approach with pruning if a branch leads to an already explored index
class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        q = [start]
        mem = set([start])
        while len(q) > 0 :
            if arr[q[0]] == 0 : return True
            for i in [1,-1] :
                v = q[0] + (i * arr[q[0]])
                if 0 <= v < len(arr) :
                    if v not in mem :
                        mem.add(v)
                        q.append(v)
            q.pop(0)
        return False
                        
