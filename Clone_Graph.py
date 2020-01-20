# Problem 133 on Leetcode, Clone Graph
# Runtime: 44 ms, faster than 97.33% of Python online submissions for Clone Graph.
# Memory Usage: 12.1 MB, less than 100.00% of Python online submissions for Clone Graph.

# This approach uses a BFS to traverse the graph, storing each node visited
# in a hash map, mapping the original node to the new node

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node is None : return 
        rnode = Node(val=node.val)
        q = [node]
        mem = {node : rnode}
        while q :
            for n in q[0].neighbors :
                if n not in mem :
                    tmp = Node(val=n.val)
                    mem[n] = tmp
                    mem[q[0]].neighbors.append(tmp)
                    q.append(n)
                else :
                    mem[q[0]].neighbors.append(mem[n])
            q.pop(0)
        return rnode
