class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item

    def get_by_category(self, category):
        items = [item for item in self.inventory if item.category == category]
        return items 

    def swap_items(self, vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False
        self.remove(my_item)
        self.add(their_item)
        vendor.remove(their_item)
        vendor.add(my_item)
        return True

    def swap_first_item(self, vendor):
        if not self.inventory or not vendor.inventory:
            return False
        self.inventory[0], vendor.inventory[0] = vendor.inventory[0], self.inventory[0]
        return True
