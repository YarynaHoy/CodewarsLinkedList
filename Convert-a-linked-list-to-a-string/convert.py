'''
Convert-a-linked-list-to-a-string.convert
'''
def stringify(node):
    '''
    convers node to str
    '''
    if node is None:
        return 'None'
    result = ''
    cur = node

    while cur is not None:
        result += str(cur.data) +' -> '
        cur = cur.next

    return result + 'None'
