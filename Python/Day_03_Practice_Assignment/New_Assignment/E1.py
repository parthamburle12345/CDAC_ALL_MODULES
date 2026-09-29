"""
The Wizard's Magic Bag
Scenario: A wizard has a magic bag containing a sequence of items:
 ["staff", "potion", "spellbook"]. When the wizard steps through a magic portal,
   two things happen:

A new item enters the bag (prompts the user to input the item name to append to the end).
The oldest item in the bag (at index 0) is dissolved and ejected. 
Write a program to simulate this portal transition and print the final bag contents.
Sample Input: (User inputs "amulet")
Sample Output:
Portal transition activated!
Ejected oldest item: staff
Current items in the magic bag: ['potion', 'spellbook', 'amulet']

"""

bag=["staff", "potion", "spellbook"]

print("Portal transition activated!")
new_item=input("enter a new item:")
bag.append(new_item)
remove=bag.pop(0)

print(f"{remove} item is removed")


print("Current items in the magic bag:", bag)