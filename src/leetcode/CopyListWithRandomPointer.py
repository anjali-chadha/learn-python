# https://leetcode.com/problems/copy-list-with-random-pointer/

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
# Algorithm1 - O(N) in Time and Space
# Iterative Solution: Maintain a mapping from old to new nodes as you traverse
# Single Pass
#
# Algorithm 2 - 
# O(1) space. However, modifies the original linked list
# Makes 3 passes
class Solution(object):
    
    def __init__(self):
        # Create a mapping from old to new
        self.visited = {}
        
        
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head: 
            return head
        
        oldN = head
        
        newN = RandomListNode(oldN.label)
        self.visited[oldN] = newN
        
        while oldN:
            newN.random = self.clone(oldN.random)
            newN.next = self.clone(oldN.next)
            newN = newN.next
            oldN = oldN.next
        
        return self.visited[head]
    
    
    def clone(self, oldN):
        if not oldN:
            return oldN
        
        if oldN not in self.visited:
            self.visited[oldN] = RandomListNode(oldN.label)
        
        return self.visited[oldN]
  
  # Algorithm 2
  def copyRandomList_2(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head: 
            return head
        
        # Pass 1 
        #insert new nodes at alternate places in original linked list
        ptr = head
        while ptr:
            newN = RandomListNode(ptr.label)
            
            newN.next = ptr.next
            ptr.next = newN
            ptr = newN.next
        
    
        #Pass 2
        # Link random pointers of new inserted node
        ptr = head
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next
        
        # Pass 3
        # Separate the two lists
        old_list = head
        new_list = head.next
        new_node = head.next
        while head:
            head.next = head.next.next
            new_node.next = new_node.next.next if new_node.next else None
            head = head.next
            new_node = new_node.next
        
        return new_list
