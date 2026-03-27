def loop_size(node):
    slow = node.next
    fast = node.next.next

    while slow != fast:
        slow = slow.next
        fast = fast.next.next

    count = 1
    current = slow.next

    while current != slow:
        current = current.next
        count += 1

    return count
