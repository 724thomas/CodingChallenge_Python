#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        ans=[]
        while head:
            ans.append(head)
            head=head.getNext()
        for h in ans[::-1]:
            h.printValue()