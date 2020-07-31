def RemoveNthNodeFromEnd(head, num):
    '''
    Time: O(N)
    Space: O(1)
    '''
    ptrA = ptrB = temp = head
    count = 1
    while count <= num:
        ptrB = ptrB.next
        count += 1
    if ptrB is None:
        head.val = head.next.val
        head.next = head.next.next
        return
    while ptrB.next is not None:
        ptrB = ptrB.next
        ptrA = ptrA.next
    ptrA = ptrA.next.next
