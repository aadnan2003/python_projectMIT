families = []

def add_family(name, members, aid_type):
    family = {
        "name": name,
        "members": members,
        "aid_type": aid_type,
        "received": False
    }
    families.append(family)

def show_families():
    for family in families:
        print(f"name: {family['name']}, members: {family['members']},aid_type: {family['aid_type']},
              recevid? {family['received']}"
              )

def mark_as_received(name):
    for family in families:
        if family['name'] == name:
            family['received'] = True
            print(f"updated  {name} 'to' received")
            return
    print("Not Found")

def search_family(name):
    for family in families:
        if family['name'] == name:
            print(family)
            return
    print("Not Found ")

add_family("Mohamed", 6, "clothes")
add_family("Mahmoud", 4, "Food")
show_families()
mark_as_received("Mohamed")
search_family("Mahmoud")
