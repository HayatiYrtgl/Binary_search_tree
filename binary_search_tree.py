# node  class
class Node:
	
	# const
	def __init__(self, value):
		
		self.value = value
		self.left = None
		self.right = None


# balanced binary search tree
class BinarySearchTree:
	
	# const
	def __init__(self):
		
		# create root node
		self.root = None
		
	# insert method
	def insert(self, value):
		
		# new_node
		new_node =Node(value)
		
		# root node querry
		if self.root is None:
			
			self.root = Node(value)
			return True
			
		else:
			
			# create temporary node
			temp_node = self.root
			
			# if root node equals to new node don't change anything
			if temp_node.value == new_node.value:
				return False
			
			# with infinity loop insert right or left of root and other nodes
			while True:
				
				# add left side
				if new_node.value < temp_node.value:
					
					if temp_node.left is None:
					
						temp_node.left = new_node
						return True
				
					temp_node = temp_node.left
				
				else:
					
					# add right side
					if temp_node.right is None:
						
						temp_node.right = new_node
						return True
						
					temp_node = temp_node.right
					
	# min of nodes
	def min_node(self):
			
			# if left of root node is none it means root node is minumun
			if self.root.left is None:
					return self.root.value
			
			# else go until end of left nodes
			else:
					n = self.root.left
					
					while True:
						
						if n.left is None:
							return n.value
						
						n = n.left
						
	# max of nodes
	def max_node(self):
			
			if self.root.right is None:
					return self.root.value
			
			else:
					n = self.root.right
					
					while True:
						
						if n.right is None:
							return n.value
						
						n = n.right
	
	def contains(self, value):
			
			temp_node = self.root
			
			while temp_node:
					
					if value < temp_node.value:
						
						temp_node = temp_node.left
					
					elif value > temp_node.value:
						
						temp_node = temp_node.right
					
					else:
						
						return True
				
			return True if temp_node else False
