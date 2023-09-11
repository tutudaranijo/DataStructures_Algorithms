class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        # 2 pointers
        self.prev = prev
        self.next = next

# using doubly linked list


class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = ListNode(homepage)

    def visit(self, url: str) -> None:
        self.cur.next = ListNode(url, self.cur)  # self.cur is previous
        self.cur = self.cur.next

    def back(self, steps: int) -> str:
        while self.cur.prev and steps > 0:
            self.cur = self.cur.prev
            steps -= 1  # decrement
        return self.cur.val

    def forward(self, steps: int) -> str:
        while self.cur.next and steps > 0:
            self.cur = self.cur.next
            steps -= 1  # decrement
        return self.cur.val

# more efficient use array and stack


class BrowserHis:

    def __init__(self, homepage: str):
        self.i = 0
        self.len = 1  # true length
        self.history = [homepage]

    # *  constant time operations for all functions
    # * erasing forward history by soft deleting
    # *  use more memory but its pointing at new index/ number
    def visit(self, url: str) -> None:
        if len(self.history) < self.i+2:
            self.history.append(url)
        else:
            self.history[self.i+1] = url
        self.i += 1
        self.len = self.i + 1

    def back(self, steps: int) -> str:
        # calculate new position  make sure not less than 0
        self.i = max(self.i-steps, 0)
        return self.history[self.i]

    def forward(self, steps: int) -> str:
        self.i = min(self.i + steps, self.len - 1)  # dont get out pf bounds
        return self.history[self.i]
