from random import randint

def game():
    levelme = 5
    levelen = 5
    enselected_team = randint(1, 3)
    if enselected_team == 1:
        uniteddc = enteamrating = 22
        print('uniteddc')
    elif enselected_team == 2:    
        mancounty = enteamrating = 72
        print('man county')
    elif enselected_team == 3:
        houston = enteamrating = 51
        print('houston')

    if enteamrating <= 30:
        levelen = 5
    elif enteamrating <= 50:
        levelen = 4
    elif enteamrating <= 70:
        levelen = 3
    elif enteamrating <= 89:
        levelen = 2
    elif enteamrating <= 99:
        levelen = 1
    selected_team = randint(1, 3)
    if selected_team == 1:
        ronaldu = teamrating = 22
        print('myteam')
    elif selected_team == 2:    
        pessi = teamrating = 72
        print('myteam')
    elif selected_team == 3:
        benzemaa = teamrating = 51
        print('myteam')
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
    # Code for matches
    if levelme == 5:
        if levelen == 5:
            lev5match = randint(0, 3)
            leven5match = randint(0, 3)
        elif levelen == 4:
            lev5match = randint(0, 5)
            leven5match = randint(0, 6)
        elif levelen == 3:
            lev5match = randint(0, 3)
            leven5match = randint(0, 6)
        elif levelen == 2:
            lev5match = randint(0, 2)
            leven5match = randint(0, 7)
        elif levelen == 1:
            lev5match = randint(0, 2)
            leven5match = randint(0, 8)
        if lev5match > leven5match:
            print(f'My team: {lev5match} Enemy team: {leven5match}, 3 points')
        elif lev5match == leven5match:
            print(f'My team: {lev5match} Enemy team: {leven5match}, 1 points')
        elif lev5match < leven5match:
            print(f'My team: {lev5match} Enemy team: {leven5match}, 0 points')
    if levelme == 4:
        if levelen ==5:
            lev4match = randint(0, 4)
            leven4match = randint(0, 3)
        elif levelen == 4:
            lev4match = randint(0, 3)
            leven4match = randint(0, 3)
        elif levelen == 3:
            lev4match = randint(0, 3)
            leven4match = randint(0, 4)
        elif levelen == 2:
            lev4match = randint(0, 2)
            leven4match = randint(0, 5)
        elif levelen == 1:
            lev4match = randint(0, 2)
            leven4match = randint(0, 6)
        if lev4match > leven4match:
            print(f'My team: {lev4match} Enemy team: {leven4match}, 3 points')
        elif lev4match == leven4match:
            print(f'My team: {lev4match} Enemy team: {leven4match}, 1 points')
        elif lev4match < leven4match:
            print(f'My team: {lev4match} Enemy team: {leven4match}, 0 points')
    if levelme == 3:
        if levelen == 5:
            lev3match = randint(0, 5)
            leven3match = randint(0, 2)
        elif levelen == 4:
            lev3match = randint(0, 5)
            leven3match = randint(0, 3)
        elif levelen == 3:
            lev3match = randint(0, 4)
            leven3match = randint(0, 4)
        elif levelen == 2:
            lev3match = randint(0, 3)
            leven3match = randint(0, 4)
        elif levelen == 1:
            lev3match = randint(0, 2)
            leven3match = randint(0, 5)
        if lev3match > leven3match:
            print(f'My team: {lev3match} Enemy team: {leven3match}, 3 points')
        elif lev3match == leven3match:
            print(f'My team: {lev3match} Enemy team: {leven3match}, 1 points')
        elif lev3match < leven3match:
            print(f'My team: {lev3match} Enemy team: {leven3match}, 0 points')
    if levelme == 2:
        if levelen == 5:
            lev2match = randint(0, 7)
            leven2match = randint(0, 2)
        elif levelen == 4:
            lev2match = randint(0, 6)
            leven2match = randint(0, 2)
        elif levelen == 3:
            lev2match = randint(0, 5)
            leven2match = randint(0, 3)
        elif levelen == 2:
            lev2match = randint(0, 4)
            leven2match = randint(0, 4)
        elif levelen == 1:
            lev2match = randint(0, 3)
            leven2match = randint(0, 5)
        if lev2match > leven2match:
            print(f'My team: {lev2match} Enemy team: {leven2match}, 3 points')
        elif lev2match == leven2match:
            print(f'My team: {lev2match} Enemy team: {leven2match}, 1 points')
        elif lev2match < leven2match:
            print(f'My team: {lev2match} Enemy team: {leven2match}, 0 points')
    if levelme == 1:
        if levelen == 5:
            lev1match = randint(0, 8)
            leven1match = randint(0, 2)
        elif levelen == 4:
            lev1match = randint(0, 7)
            leven1match = randint(0, 2)
        elif levelen == 3:
            lev1match = randint(0, 6)
            leven1match = randint(0, 3)
        elif levelen == 2:
            lev1match = randint(0, 5)
            leven1match = randint(0, 3)
        elif levelen == 1:
            lev1match = randint(0, 4)
            leven1match = randint(0, 4)
        if lev1match > leven1match:
            print(f'My team: {lev1match} Enemy team: {leven1match}, 3 points')
        elif lev1match == leven1match:
            print(f'My team: {lev1match} Enemy team: {leven1match}, 1 points')
        elif lev1match < leven1match:
            print(f'My team: {lev1match} Enemy team: {leven1match}, 0 points')