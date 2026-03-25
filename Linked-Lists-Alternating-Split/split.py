class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    # Your code goes here.
    # Remember to return the context.
    if head is None or head.next is None:
        raise Exception('empty list')

    first = head
    second = head.next

    cur1 = first
    cur2 = second

    while cur1 and cur2:
        cur1.next = cur2.next
        cur1 = cur1.next

        if cur1:
            cur2.next = cur1.next
            cur2 = cur2.next

    return Context(first,second)
