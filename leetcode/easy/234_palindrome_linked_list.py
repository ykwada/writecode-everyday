# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if not head or not head.next:
            return True
        
        # Step 1: 中央を見つける
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: 後半部分の連結リストを反転する
        prev = None
        current = slow
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        # Step 3: 前半と後半を比較する（prev が反転した後半の先頭）
        left = head
        right = prev
        while right:  # 後半部分がある間ループ
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True
