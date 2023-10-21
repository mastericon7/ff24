from random import randint
levelme = 5
levelen = 5


selected_team = randint(1, 3)
if selected_team == 1:
    uniteddc = teamrating = 22
elif selected_team == 2:    
    mancounty = teamrating = 72
elif selected_team == 3:
    houston = teamrating = 49

if teamrating <= 30:
    levelme = 5
elif teamrating <= 50:
    levelme = 4
elif teamrating <= 70:
    levelme = 3
elif teamrating <= 89:
    levelme = 2
elif teamrating <= 99:
    levelme = 1


if levelme == 5:
    if levelen ==5:
        lev5match = randint(0, 3)
        leven5match = randint(0, 3)
    elif levelen == 4:
        lev5match = randint(0, 5)
        leven5match = randint(0, 6)
    elif levelen == 3:
        lev5match = randint(0, 4)
        leven5match = randint(0, 6)
    elif levelen == 2:
        lev5match = randint(0, 3)
        leven5match = randint(0, 7)
    elif levelen == 1:
        lev5match = randint(0, 1)
        leven5match = randint(0, 8)
    print(lev5match, leven5match)
if levelme == 4:
    if levelen ==5:
        lev5match = randint(0, 7)
    elif levelen == 4:
        lev5match = randint(0, 5)
    elif levelen == 3:
        lev5match = randint(0, 4)
    elif levelen == 2:
        lev5match = randint(0, 3)
    elif levelen == 1:
        lev5match = randint(0, 1)
    print(lev5match, leven5match)
if levelme == 3:
    if levelen ==5:
        lev5match = randint(0, 7)
    elif levelen == 4:
        lev5match = randint(0, 5)
    elif levelen == 3:
        lev5match = randint(0, 4)
    elif levelen == 2:
        lev5match = randint(0, 3)
    elif levelen == 1:
        lev5match = randint(0, 1)
    print(lev5match, leven5match)
if levelme == 2:
    if levelen ==5:
        lev5match = randint(0, 7)
    elif levelen == 4:
        lev5match = randint(0, 5)
    elif levelen == 3:
        lev5match = randint(0, 4)
    elif levelen == 2:
        lev5match = randint(0, 3)
    elif levelen == 1:
        lev5match = randint(0, 1)
    print(lev5match, leven5match)
if levelme == 1:
    if levelen ==5:
        lev5match = randint(0, 7)
    elif levelen == 4:
        lev5match = randint(0, 5)
    elif levelen == 3:
        lev5match = randint(0, 4)
    elif levelen == 2:
        lev5match = randint(0, 3)
    elif levelen == 1:
        lev5match = randint(0, 1)
    print(lev5match, leven5match)