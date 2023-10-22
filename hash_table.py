SIZE = 20
class DataItem:
    def __init__(self, data, key):
        self.data = data
        self.key = key
# Initialize the hash array with None values
hashArray = [None] * SIZE
# Create a dummy item to mark deleted cells in the hash table
dummyItem = DataItem(-1, -1)
# Variable to hold the item found in the search operation
item = None
# Hash function to calculate the hash index for the given key
def hashCode(key):
    return key % SIZE
# Function to search for an item in the hash table by its key
def search(key):
    # Calculate the hash index using the hash function
    hashIndex = hashCode(key)
    # Traverse the array until an empty cell is encountered
    while hashArray[hashIndex] is not None:
        if hashArray[hashIndex].key == key:
            # Item found, return the item
            return hashArray[hashIndex]
        # Move to the next cell (linear probing)
        hashIndex = (hashIndex + 1) % SIZE

    # If the loop terminates without finding the item, it means the item is not present
    return None
# Function to insert an item into the hash table
def insert(key, data):
    # Create a new DataItem object
    item = DataItem(data, key)
    # Calculate the hash index using the hash function
    hashIndex = hashCode(key)
    # Handle collisions using linear probing (move to the next cell until an empty cell is found)
    while hashArray[hashIndex] is not None and hashArray[hashIndex].key != -1:
        hashIndex = (hashIndex + 1) % SIZE
    # Insert the item into the hash table at the calculated index
    hashArray[hashIndex] = item
# Function to delete an item from the hash table
def deleteItem(item):
    key = item.key
    # Calculate the hash index using the hash function
    hashIndex = hashCode(key)
    # Traverse the array until an empty or deleted cell is encountered
    while hashArray[hashIndex] is not None:
        if hashArray[hashIndex].key == key:
            # Item found, mark the cell as deleted by replacing it with the dummyItem
            temp = hashArray[hashIndex]
            hashArray[hashIndex] = dummyItem
            return temp
        # Move to the next cell (linear probing)
        hashIndex = (hashIndex + 1) % SIZE

    # If the loop terminates without finding the item, it means the item is not present
    return None
# Function to display the hash table
def display():
    for i in range(SIZE):
        if hashArray[i] is not None:
            # Print the key and data of the item at the current index
            print(" ({}, {})".format(hashArray[i].key, hashArray[i].data), end="")
        else:
            # Print ~~ for an empty cell
            print(" ~~ ", end="")
    print()
if __name__ == "__main__":
    # Test the hash table implementation
    # Insert some items into the hash table
    insert(1, 20)
    insert(2, 70)
    insert(42, 80)
    insert(4, 25)
    insert(12, 44)
    insert(14, 32)
    insert(17, 11)
    insert(13, 78)
    insert(37, 97)

    # Display the hash table
    display()

    # Search for an item with a specific key (37)
    item = search(37)

    # Check if the item was found or not and print the result
    if item is not None:
        print("Element found:", item.data)
    else:
        print("Element not found")

    # Delete the item with key 37 from the hash table
    deleteItem(item)

    # Search again for the item with key 37 after deletion
    item = search(37)

    # Check if the item was found or not and print the result
    if item is not None:
        print("Element found:", item.data)
    else:
        print("Element not found")
