""" Assignment number 1. Linked list conformed by nodes with the value and the next node.


"""

import math

class Node(object):
	""" Every node (element) to build the linked list with the current value and the next node """
	def __init__(self, value=None, next=None):
		self.value = value
		self.next = next

	def get_value(self):
		return self.value

	def get_next(self):
		return self.next

	def set_next(self, next):
		self.next = next


class LinkedList(object):
	def __init__(self, head = None):
		self.head = head

	# Add a new element to the linked list. Set the head with the new value
	def add(self, value):
		""" Add new node to the linked list. If it's the first time, the next node will be None 
		:param value: node content
		"""
		node = Node(value, self.head)
		self.head = node

	# Remove the node with the value
	def remove(self, node):
		""" remove the node from the LinkedList
		"""
		current = self.head
		previous = None
		# search the node with the data. 
		# Keep in mind the previous to validate when it is head so point the new head
		while current:
			if id(current) == id(node):
				break
			else:
				previous = current
				current = current.get_next()
		if current is None:
			raise ValueError('No se encontro el elemento')
		if previous is None:
			self.head = current.get_next()
		else:
			previous.set_next(current.get_next())


	def get_prior(self):
		""" To get the head node of the list
		:return: the head node. The last one is the head in the list.
		"""
		return self.head
	# Get the node next to the node with match with the value
	def get_next(self, node):
		""" Get the node next to the recieved in parameter
		:param node: Type Node to search in the list
		:return: The node next to the param node
		"""
		current = self.head
		while current:
			if id(current) == id(node):
				return current.get_next()
			else:
				current = current.get_next()

		if current is None:
			raise ValueError('No se encontro el elemento')

l = LinkedList()
l.add(111)
l.add(222)
l.add(333)
l.add(444)
l.add(555)
l.add(111)
l.add(123)
current = l.get_prior()
a = 0
while current:
	print(str(id(current))+"- "+str(vars(current)))
	if current.get_value() == 555: a = current
	current = l.get_next(current)
print(str(a))
l.remove(a)
current = l.get_prior()
while current:
	print(str(id(current))+"- "+str(vars(current)))
	current = l.get_next(current)
