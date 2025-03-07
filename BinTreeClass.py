class BinaryTree:
  def __init__(self):
      self.__root = None 
      self.__size = 0
  def __validate(self,location): 
      """Determines if location is inside the positional list class or a position"""
      if location._Position__member_of is self: 
        return location._Position__node 
      else:
        raise Exception("Not in list or not Position") 
  def __make_position(self,node):
    """Makes a position bubble to be used"""
    if type(node) != self.BinaryNode:   
      return None
    else:
      location = self.Position(self,node)
      return location 
  def add_root(self,value):
    """adds root to empty tree"""
    node = self.BinaryNode(value)
    
    
    
    if self.__root != None:
      raise Exception("Cannot add root if root already exists")
    else:  
      self.__root = node
      self.__size += 1
      location = self.__make_position(node)
      return location
  def add_left(self,parent,value):
    """Adds left child to tree to given"""
    node = self.BinaryNode(value)
    newpar = self.__validate(parent)
    if newpar._BinaryNode__left != None:
       raise Exception("Cannot add left if left already exists")
    else: 

      node._BinaryNode__set_parent(newpar)
      newpar._BinaryNode__set_left(node)
      self.__size += 1
      newnode = self.__make_position(node)
      return newnode
  def add_right(self,parent,value):
    """adds right child to given"""
    node = self.BinaryNode(value)
    newpar = self.__validate(parent)
    if newpar._BinaryNode__right != None:
       raise Exception("Cannot add right if right already exists")
    else: 

      node._BinaryNode__set_parent(newpar)
      newpar._BinaryNode__set_right(node)
      self.__size += 1
      newnode = self.__make_position(node)
      return newnode
  def is_root(self,node):
    """Checks if given is root"""
    node = self.__validate(node)
    if node is self.__root:
      return True
    else:
      return False  
  def is_leaf(self,node):
    """Checks if given is a leaf"""
    node = self.__validate(node)
    if node._BinaryNode__left != None or node._BinaryNode__right != None:
      return False
    else:
      return True
  def is_ancestor(self,ancestor,descendant):
    """checks if given is ancestor"""
    descendant = self.__validate(descendant)
    pointer = descendant
    if ancestor == descendant:
        return False
    while pointer != self.__root:
      if pointer == ancestor:
         return True
      pointer = pointer._BinaryNode__parent
    return False

  def are_siblings(self,sibling1,sibling2):
    """Checks if both givens are siblings"""
    sibling1 = self.__validate(sibling1)
    sibling2 = self.__validate(sibling2)
    if sibling1 is sibling2:
      return False
    if sibling1._BinaryNode__parent == sibling2._BinaryNode__parent:
      return True
   
    else: 
      return False  
  def num_children(self,node):
    """Checks number of children a node has"""
    node = self.__validate(node)
    children = 0
    if node._BinaryNode__left != None:
      children += 1
    if node._BinaryNode__right != None:
      children += 1
    return children      
  def get_root(self):
    """Returns root"""
    root = self.__make_position(self.__root)
    return root
  def get_left(self,node):
    """Returns left"""
    node = self.__validate(node)
    left = self.__make_position(node._BinaryNode__left)   
    return left
  def get_right(self,node):
    """returns right"""
    node = self.__validate(node)
    right = self.__make_position(node._BinaryNode__right)   
    return right  
  def get_parent(self,node):
    """Gets parent of given"""
    node = self.__validate(node)
    parent = self.__make_position(node._BinaryNode__parent)   
    return parent
  def get_children(self,node):
    """Gets children of given"""
    node = self.__validate(node)
    if node._BinaryNode__left != None or node._BinaryNode__right != None:
      left = self.__make_position(node._BinaryNode__left) 
      right = self.__make_position(node._BinaryNode__right) 
      children = []
      children.append(left)
      children.append(right)
      return children
    else:
      return None  
  def get_sibling(self,node):
    """Gets sibling of given"""
    node = self.__validate(node)
    parent = node._BinaryNode__parent
    if node == self.__root:
      return None
    if parent._BinaryNode__left == node:
      right = self.__make_position(parent._BinaryNode__right)
      return right
    if parent._BinaryNode__right == node:
      left = self.__make_position(parent._BinaryNode__left)
      return left
    return None
  def get_ancestors(self,node):
    """Gets ancestors of given"""
    node = self.__validate(node)
    pointer = node._BinaryNode__parent
    ancestors = []
    if node == self.__root:
      return None
    while pointer != self.__root:
      self.__make_position(pointer)
      ancestors.append(pointer)
      pointer = pointer._BinaryNode__parent
    ancestors.append(pointer)  
    return ancestors
  def get_depth(self,node):
    """Returns depth of tree"""
    ancestors = self.get_ancestors(node)
    if ancestors == None:
      return 0
    depth = len(ancestors)
    return depth   
  def replace(self,node,value):
    """Replaces value of node with given"""
    node = self.__validate(node)
    old = node._BinaryNode__value
    node._BinaryNode__value = value  
    return old
  def delete(self,node):
    """Removes node from tree"""
    node = self.__validate(node)
    if node._BinaryNode__left != None and node._BinaryNode__right != None:
      raise Exception("Cannot delete a node with two children")  
    
                

    value = node._BinaryNode__value
    parent = node._BinaryNode__parent

    if node._BinaryNode__left == None and node._BinaryNode__right == None:
      if node is self.__root:
        self.__root = None
      else:
        if parent._BinaryNode__left is node:
          parent._BinaryNode__set_left(None)
        else:
          parent._BinaryNode__set_right(None)
    
    else:
      if node is self.__root:
        if node._BinaryNode__left != None:
          child = node._BinaryNode__left
          self.__root = self.__root._BinaryNode__left
        else:
          child = node._BinaryNode__right
          self.__root = self.__root._BinaryNode__right
        

      else:
        if node._BinaryNode__left != None:
          child = node._BinaryNode__left
        else:
          child = node._BinaryNode__right

        if parent._BinaryNode__left is node:
          parent._BinaryNode__set_left(child)
        else:
          parent._BinaryNode__set_right(child)

      child._BinaryNode__set_parent(parent)

    
    node._BinaryNode__set_parent(node)
    self.__size -= 1
    return value


      

#def replace(): 
#def delete(): 
   
    
  def __str__(self):
      '''Convert root to string'''
      return str(self.__root)
  def __len__(self):
    """Returns size"""
    return self.__size
  class BinaryNode:
    def __init__(self,value):
      self.__value = value
      self.__parent = None
      self.__left = None
      self.__right = None
    def __set_parent(self,node):
      """Accepts node object and updates self.__parent"""
      if type(node) == type(self) or type(node) == type(None):
        self.__parent = node
      else:
        raise Exception("Invaild node type")
    def __set_left(self,node):
      """Accepts node object and updates self.__left"""
      if type(node) != type(self) and type(node) != type(None):
        raise Exception("Invaild node type") 

      if node is self:
        raise Exception("Node cannot be self")

      if self.__parent is node and node is not None:
         raise Exception("Node parent cannot be child")
      

      self.__left = node   

    def __set_right(self,node):
      """Accepts node object and updates self.__right"""
      if type(node) != type(self) and type(node) != type(None):
        raise Exception("Invaild node type") 
        
      if node is self:
          raise Exception("Invaild node type")

      if self.__parent is node and node is not None:
         raise Exception("Node parent cannot be child")


      self.__right = node     
    def __str__(self):
        '''Display to enable view for whole tree'''
        return f"|{self.__value}| \n({self.__value})L: {self.__left} \n({self.__value})R: {self.__right}"


  class Position:
    def __init__(self,member_of,node):
      self.__member_of = member_of
      self.__node = node
    def get_value(self):
      """Returns value of a node"""
      return self.__node._BinaryNode__value

    def __eq__(self,node1):
      """Returns true if node is equal to current node"""
      if node1 == self.__node:
        return True
      else:
        return False  
    def __ne__(self,node1):
      """Returns true if node is not equal to current node"""
      if node1 != self.__node:
        return True
      else:
        return False
    
    # Position Class
    def __str__(self):
      '''Display position as value in node'''
      return str(self.get_value())

    def __repr__(self):
      '''Display position when in collection'''
      return str(self)    