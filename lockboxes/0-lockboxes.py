#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """ Method that determinates
    if all th boxescan be opened """

    if not boxes or not boxes[0]:
        return False

    open_box = set([0])
    pending_box = set([0])

    while pending_box:
        current_box = pending_box.pop()
        if 0 <= current_box < len(boxes):
            for key in boxes[current_box]:
                if key not in open_box:
                    open_box.add(key)
                    pending_box.add(key)
    return len(open_box) == len(boxes)
