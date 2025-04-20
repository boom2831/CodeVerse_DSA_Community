import heapq
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        min_heap = []
        
        
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))
        
        
        dummy = ListNode(-1)
        current = dummy
        
       
        while min_heap:
            val, idx, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next
         
            if node.next:
                heapq.heappush(min_heap, (node.next.val, idx, node.next))
        
        return dummy.next

def to_linked_list(lst: List[int]) -> Optional[ListNode]:
    dummy = ListNode(-1)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def print_linked_list(node: Optional[ListNode]) -> None:
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")


sol = Solution()


lists = [[1,4,5], [1,3,4], [2,6]]
linked_lists = [to_linked_list(lst) for lst in lists]
result = sol.mergeKLists(linked_lists)
print_linked_list(result)  # Expected Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6 -> None

# Test Case 2: Empty input
result = sol.mergeKLists([])
print_linked_list(result)  # Expected Output: None


lists = [[]]
linked_lists = [to_linked_list(lst) for lst in lists]
result = sol.mergeKLists(linked_lists)
print_linked_list(result)  # Expected Output: None
