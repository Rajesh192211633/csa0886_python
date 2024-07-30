def print_linked_list(node):
    numbers = []
    while node is not None:
        numbers.append(node.val)
        node = node.next
    return numbers


l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])
result = addTwoNumbers(l1, l2)
print(print_linked_list(result))  
