# check a single-listed list whether a palindrome

import sys
sys.path.append('singly_linklist')

from singly_linklist import singlylinklist

def reverse_list(head):
    rever_head = None
    while head:
        head_next = head._next
        head._next = rever_head
        rever_head = head        # 翻转链表，不要忘了幅值
        head = head_next
    return rever_head

def is_palindrome(l):
    l.print_all()
    slow = l._head
    fast = l._head

    position = 0
    while fast and fast._next:
        slow = slow._next
        fast = fast._next._next
        position +=1

    reverse_rest_list = reverse_list(slow)
    head_list = l._head
    is_palin = True
    while head_list and reverse_rest_list:
        if head_list.data == reverse_rest_list.data:   # 不可以用两个node直接比较，因为data可以相同，但是next指针指向的是地址，地址不同。
            head_list = head_list._next
            reverse_rest_list = reverse_rest_list._next
        else:
            is_palin = False
            break          #  必须加跳出条件，因为如果两个node的data不相同直接进入else，则会进入死循环

    return is_palin

if __name__=='__main__':
    # the result should be [False, True, True, True, True, True, False]
    test_str = ['ab', 'aa', 'aba', 'abba', 'abcba','asdfghjkjhgfdsa','asdfghjhgfds']
    flag_str = []
    for t_str in test_str:
        l = singlylinklist()
        for j in t_str:
            l.insert_value_to_tail(j)
        flag_str.append(is_palindrome(l))
    print(flag_str)