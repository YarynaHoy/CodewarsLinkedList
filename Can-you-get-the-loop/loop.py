def loop_size(node):
    slow = node.next
    fast = node.next.next

    while slow != fast:
        slow = slow.next
        fast = fast.next.next

    k = 1
    cur = slow.next

    while cur != slow:
        cur = cur.next
        k += 1

    return k
