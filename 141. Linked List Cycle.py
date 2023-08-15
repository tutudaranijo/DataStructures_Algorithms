class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # * this is using the tortuise and hare algorithm
        # * eventually they will meet if its a cycle because it close the gap by one each time

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next  # ! moves one step
            fast = fast.next.next  # ! moves two steps
            if slow == fast:
                return True

        return False
