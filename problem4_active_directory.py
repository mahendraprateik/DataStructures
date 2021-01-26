class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


user_check_dict = {}

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    # Invalid user case
    if len(user) == 0:
        print("Please provide a non-empty user name")
        return

    # Invalid group case
    if group is None:
        print("Please provide a valid group object")
        return

    if user == group.get_name() or user in group.get_users():
        return True
    if len(group.groups) == 0:
        user_check_dict[group.get_name()] = False
        return False

    else:
        for g in group.get_groups():
            if g in user_check_dict:
                continue
            found = is_user_in_group(user, g)

    return found


# Test cases - Regular

print(is_user_in_group(sub_child_user, child)) # True
print(is_user_in_group(sub_child_user, parent))  # True
print(is_user_in_group("Some User", sub_child))  # False


# Test cases - Edge

# Empty user and group
print(is_user_in_group("", child)) # Empty user name warniing

# Invalid group object
print(is_user_in_group("", None)) # Invalid group object warning
