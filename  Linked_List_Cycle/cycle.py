def hasCycle(head):
        pointer1=head
        pointer2=head
        while pointer2 and pointer2.next:
            pointer1=pointer1.next
            pointer2=pointer2.next.next
            if pointer1==pointer2:
                return True
        return False