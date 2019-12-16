from dataclasses import dataclass
from typing import Any


@dataclass
class ListNode:
    data: Any = None
    next: Any = None

    def has_value(self, value):
        return self.data == value


@dataclass
class SinglyLinkedList:
    head: Any = None
    tail: Any = None
    length: int = 0

    def append(self, item):
        if item is None:
            return "Please provide valid value"
        node = ListNode(item)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def prepend(self, item):
        if item is None:
            return "Please provide valid value"
        node = ListNode(item)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1
        return "success"

    def insert(self, index, item):
        curr = self.head
        while curr is not None and index - 1 > 1:
            index -= 1
            curr = curr.next
        if index-1 > 1:
            print("Index does not exist")
        else:
            node = ListNode(item)
            node.next = curr.next
            curr.next = node

    def remove(self, item):
        index = 0
        if self.head is None:
            print("No nodes in the list")
            return
        prev = None
        curr = self.head
        while curr:
            index += 1
            if curr.data == item:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                curr.next = None
                print("Removed item at index", index)
                self.length -= 1
                return
            prev = curr
            curr = curr.next

    def reverse(self):
        if self.length < 2:
            return
        prev = self.head
        curr = self.head.next
        self.tail = prev
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            self.head.next = None
        self.head = prev

    def print_list(self):
        curr = self.head
        if curr is None:
            print("no nodes in the list")
        while curr is not None:
            print(curr.data)
            curr = curr.next


if __name__ == "__main__":
    linked_list = SinglyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.insert(5, 5)
    print("length of linked list ", linked_list.length)
    linked_list.reverse()
    linked_list.print_list()
