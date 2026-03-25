from preloaded import Node

def swap_pairs(head):
    if head is None or head.next is None:
        return head

    new = head.next
    prev = None
    cur = head

    while cur and cur.next:
        nxt = cur.next
        next_pair = nxt.next
        nxt.next = cur
        cur.next = next_pair

        if prev:
            prev.next = nxt

        prev = cur
        cur = next_pair

    return new
