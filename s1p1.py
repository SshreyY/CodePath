#print("Hello World")
# Notes:
# For loop, goes through each of the string => checks to match target
# Return index 
# Edge case: 0 items return -1
def linear_search(items, target):
    if(items is None):
        return -1
    
    for i in range(len(items)):
        if(items[i] == target):
            return i
    return -1

# Example Code
items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target = 'hunny'
linear_search(items, target)

items = ['bed', 'blue jacket', 'red shirt', 'hunny']
target = 'red balloon'
linear_search(items, target)
