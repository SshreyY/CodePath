#Notes:
# - increment by 1 if the string contains bouncy and flouncy
# - decrement by 1 if the string contains trouncy and pouncy
# - initial tigger is = 1 (counter variable)
# - if, elif and else 
# - edge case for wild cards, skip

def final_value_after_operations(operations):
    tigger = 1
    
    for ops in operations:
        if(ops == "bouncy" or ops == "flouncy"):
            tigger = tigger + 1
        elif(ops == "trouncy" or ops == "pouncy"):
            tigger = tigger - 1
    return tigger


operations = ["trouncy", "flouncy", "flouncy"]
final_value_after_operations(operations)

operations = ["bouncy", "bouncy", "flouncy"]
final_value_after_operations(operations)