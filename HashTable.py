from LinkedList import LinkedList

class HashTable:

  def __init__(self, size):
    self.size = size
    self.arr = self.create_arr(size)


  # 1️⃣ TODO: Complete the create_arr method.

  # Each element of the hash table (arr) is a linked list.
  # This method creates an array (list) of a given size and populates each of its elements with a LinkedList object.

  def create_arr(self, size):
    arr = []
    # for each element in the list you want it to be a linked list object
    for i in range(size):
      new_linkedlist = LinkedList()
      arr.append(new_linkedlist)

    return arr


  # 2️⃣ TODO: Create your own hash function.

  # Hash functions are a function that turns each of these keys into an index value that we can use to decide where in our list each key:value pair should be stored. 

  def hash_func(self, key):
    # 1. Get the first letter of the key and lower case it 
    first_letter = key[0].lower()

    # 2. Calculate the distance from letter a
    distance_from_a = ord(first_letter) - ord('a')

    # 3. Mod it to make sure it is in range
    index = distance_from_a % self.size

    # returns index 
    return index



  # 3️⃣ TODO: Complete the insert method.

  # Should insert a key value pair into the hash table, where the key is the word and the value is a counter for the number of times the word appeared. When inserting a new word in the hash table, be sure to check if there is a Node with the same key in the table already.

  def insert(self, key, value):
    # dictionaries / hash tables store "key value pairs"
    # finding the index where key value pair should be placed
    key_hash = self.hash_func(key)

    # linear probing 
    # check if the bucket/slot is empty
    if self.arr[key_hash] == None:

      # this assigns the key value to the slot
      self.arr[key_hash] = (key, value)
      return key_hash
      
    # if its taken (bucket) loop
    else:
      # pointer is going to look and see if the bucket has something in it
      ptr = (key_hash + 1 ) % self.size

      # base condition
      while ptr != key_hash: 
        # if the next spot is open take that
        if self.arr[ptr] == None:
          self.arr[ptr] = (key, value)
          return ptr

        # incrimenting pointer by 1 and making sure it doesnt exceed the size
        else:
          ptr = (ptr + 1) % self.size
        
      print("Table is full!")
      return -1


  # 4️⃣ TODO: Complete the print_key_values method.

  # Traverse through the every Linked List in the table and print the key value pairs.

  # For example: 
  # a: 1
  # again: 1
  # and: 1
  # blooms: 1
  # erase: 2

  def print_key_values(self):
    if self.arr == None:
      print("empty")
      return -1
    else:
      for i in range(self.size):
        print(i)