import random

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = []

    def _generateId(self):
        return random.randint(0, 99999999)

    def add_member(self, member):
        if 'id' not in member:
            member['id'] = self._generateId()
        member['last_name'] = self.last_name
        self._members.append(member)

    def delete_member(self, id):
        member = self.get_member(id)
        if member:
            self._members.remove(member)
            return True
        return False

    def update_member(self, id, member_info):
        member = self.get_member(id)
        if member:
            index = self._members.index(member)
            self._members[index] = member_info
            return True
        return False

    def get_member(self, id):
        for member in self._members:
            if member['id'] == id:
                return member
        return None

    def get_all_members(self):
        return self._members