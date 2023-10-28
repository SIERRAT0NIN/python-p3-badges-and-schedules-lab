NAMES = ["alberto", "austin"]


def badge_maker(name):
    return f"Hello, my name is {name}."


def batch_badge_creator(names):
    badge_message = []
    for name in names:
        badge_message.append(f"Hello, my name is {name}.")
    return badge_message


batch_badge_creator(NAMES)


def assign_rooms(names):
    rooms = [
        f"Hello, {name}! You'll be assigned to room {room}!"
        for room, name in enumerate(names, start=1)
    ]
    return rooms


def printer(names):
    badges = batch_badge_creator(names)
    rooms_assignment = assign_rooms(names)
    for badge in badges:
        print(badge)
    for room in rooms_assignment:
        print(room)
