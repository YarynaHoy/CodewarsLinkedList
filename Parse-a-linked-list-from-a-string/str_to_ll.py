from preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    if list_repr == 'None':
        return None

    val = list_repr.split(' -> ')
    val = [v for v in val if v != 'None']

    head = None
    for v in val[::-1]:
        head = Node(int(v), head)

    return head
