# Problem 445 on Leetcode, Add Two Numbers II
# Runtime: 72 ms, faster than 73.27% of Python online submissions for Add Two Numbers II.
# Memory Usage: 11.8 MB, less than 7.53% of Python online submissions for Add Two Numbers II.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        def lltolist(l) :
            arr = []
            while l :
                arr.append(l.val)
                l = l.next
            return arr
        
        def sumlists(l1, l2) :
            arr = []
            c = 0
            p1 = 0
            p2 = 0
            for i in range(1,max(len(l1), len(l2))+2) :
                if (i > len(l1)) :
                    p1 = 0
                else :
                    p1 = l1[-i]
                    
                if (i > len(l2)) :
                    p2 = 0
                else :
                    p2 = l2[-i]
                    
                add = p1 + p2 + c
                arr.insert(0, (add)%10)
                c = (add)/ 10
            if (arr[0] == 0) :
                arr.remove(0)
            return arr
               
        def listtoll(arr) :
            node = ListNode(arr[-1])
            for i in range(2,len(arr)+1) :
                new = ListNode(arr[-i])
                new.next = node
                node = new
            return node
         
        arr1 = lltolist(l1)
        arr2 = lltolist(l2)
        sumlist = sumlists(arr1, arr2)
        sumll = listtoll(sumlist)
        return sumll
