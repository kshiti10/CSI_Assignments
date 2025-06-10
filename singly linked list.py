# -*- coding: utf-8 -*-
"""
Created on Tue May 27 22:40:20 2025

@author: Kshitija
"""

class Node:
    # Class to represent a node in the linked list.
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # Class to represent the singly linked list.
    def __init__(self):
        self.head = None

    def add_node(self, data):
        # Adds a node to the end of the list.
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print(f"Added head node with data: {data}")
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        print(f"Added node with data: {data}")

    def print_list(self):
        # Prints all nodes in the list.
        if self.head is None:
            print("Linked list is empty.")
            return
        current = self.head
        print("Linked List:", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        # Deletes the nth node (1-based index).
        try:
            if self.head is None:
                raise IndexError("Cannot delete from an empty list.")

            if n <= 0:
                raise IndexError("Index should be 1 or greater.")

            if n == 1:
                deleted_data = self.head.data
                self.head = self.head.next
                print(f"Deleted head node with data: {deleted_data}")
                return

            current = self.head
            count = 1
            while current and count < n - 1:
                current = current.next
                count += 1

            if current is None or current.next is None:
                raise IndexError("Index out of range.")

            deleted_data = current.next.data
            current.next = current.next.next
            print(f"Deleted node {n} with data: {deleted_data}")
        except IndexError as e:
            print("Error:", e)


# Testing the LinkedList

if __name__ == "__main__":
    ll = LinkedList()

    # Adding nodes
    ll.add_node(10)
    ll.add_node(20)
    ll.add_node(30)
    ll.add_node(40)

    # Print list
    ll.print_list()

    # Delete valid node
    ll.delete_nth_node(2)
    ll.print_list()

    # Delete head
    ll.delete_nth_node(1)
    ll.print_list()

    # Delete with invalid index
    ll.delete_nth_node(10)

    # Delete from empty list
    ll.delete_nth_node(1)
    ll.delete_nth_node(1)
