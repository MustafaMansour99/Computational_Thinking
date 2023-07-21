def swapNodes(head, k):
        p1=head
        p2=head
        for _ in range(k-1):
            p2=p2.next
        temp=p2
        while p2.next:
            p1=p1.next
            p2=p2.next
        temp2=p1

        temp.val,temp2.val=temp2.val,temp.val
        return head