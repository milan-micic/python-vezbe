# inventory.py
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
  print("Inventory:")
  item_total = 0
  for k, v in inventory.items():
    item_total+=v
    print(str(v)+' x '+k)
  print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
  for item in addedItems:
    inventory.setdefault(item,0)
    inventory[item] = inventory[item] + 1
  return inventory

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

