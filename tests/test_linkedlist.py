# coding: utf-8
"""test utils."""
from __future__ import unicode_literals

from unittest import TestCase

from adcat.linkedlist import LinkedNode


class LinkedListTest(TestCase):

    def test_create(self):
        node = LinkedNode(1)

        node2 = LinkedNode(2)

        node.next = node2
        self.assertEqual(node.val, 1)
        self.assertEqual(node.next.val, 2)
