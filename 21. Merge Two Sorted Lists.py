class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()  # * dummy node so you dont have to worry about edgecase
        tail = dummy

        while list1 and list2:  # ! comparing the list
            if list1.val < list2.val:
                tail.next = list1  # this is list 1 node
                list1 = list1.next  # update the pointer
            else:
                tail.next = list2  # same thing but list2 is inserted
                list2 = list2.next
            tail = tail.next  # update tail pointer regardless

        if list1:  # ! find the non empty list and add to end of list
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next


# running it
# Create instances of ListNode
nodes_one = [ListNode(val) for val in [1, 2, 4]]
nodes_two = [ListNode(val) for val in [1, 3, 4]]

# Link the ListNode instances together
for i in range(len(nodes_one) - 1):
    nodes_one[i].next = nodes_one[i + 1]
for i in range(len(nodes_two) - 1):
    nodes_two[i].next = nodes_two[i + 1]

# Create instances of Solution and call mergeTwoLists
solution = Solution()
merged_list = solution.mergeTwoLists(nodes_one[0], nodes_two[0])

# Print the merged linked list
while merged_list:
    print(merged_list.val, end=" -> ")
    merged_list = merged_list.next
