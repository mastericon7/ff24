from random import randint
def packmake80():
    packopen80 = randint(1, 26)

    if packopen80 == 1:
        print('Linnea Bjorn - Sweden 81')
    elif packopen80 == 2:
        print('Pavel Sokolov - Czech Republic 80')
    elif packopen80 == 3:
        print('Anika Gupta - India 80')
    elif packopen80 == 4:
        print('Leonidas Papadopoulos - Greece 81')
    elif packopen80 == 5:
        print('Freya Jensen - Denmark 83')
    elif packopen80 == 6:
        print('Hiro Tanaka - Japan 85')
    elif packopen80 == 7:
        print('Anita Patel - Canada 86')
    elif packopen80 == 8:
        print('Matej Kolar - Croatia 83')
    elif packopen80 == 9:
        print('Isak Karlsson - Sweden 82')
    elif packopen80 == 10:
        print('Mia Andersson - Norway 87')
    elif packopen80 == 11:
        print('Arjun Rao - India 80')
    elif packopen80 == 12:
        print('Valentina Costa - Argentina 84')
    elif packopen80 == 13:
        print('Yuri Ivanov - Russia 80')
    elif packopen80 == 14:
        print('Irina Petrova - Bulgaria 81')
    elif packopen80 == 15:
        print('Lucas da Silva - Brazil 89')
    elif packopen80 == 16:
        print('Nadia Petrovic - Serbia 89')
    elif packopen80 == 17:
        print('Marco Hernandez - Spain 88')
    elif packopen80 == 18:
        print('Katarina Novak - Czech Republic 81')
    elif packopen80 == 19:
        print('Andrei Ionescu - Romania 80')
    elif packopen80 == 20:
        print('Elena Volkova - Ukraine 82')
    elif packopen80 == 21:
        print('David Alonso - Spain 88')
    elif packopen80 == 22:
        print('Ingrid Jorgensen - Norway 89')
    elif packopen80 == 23:
        print('Juan Martinez - Spain 87')
    elif packopen80 == 24:
        print('Lars Olsen - Denmark 84')
    elif packopen80 == 25:
        print('Maria Sanchez - Spain 88')
    elif packopen80 == 26:
        print('Ahmed Abadi - Egypt 87')

def packmake70():
    packopen70 = randint(1, 17)

    if packopen70 == 1:
        with open("playersdata.txt", "a") as f:
            print('Alex Diamante - Argentina 78', file=f)
    elif packopen70 == 2:
        with open("playersdata.txt", "a") as f:
            print('Maxime Roux - France 78', file=f)
    elif packopen70 == 3:
        print('Diego Fernandez - Spain 76')
    elif packopen70 == 4:
        print('Elena Costa - Brazil 75')
    elif packopen70 == 5:
        print('Andrei Petrov - Russia 74')
    elif packopen70 == 6:
        print('Sofia Kovač - Croatia 70')
    elif packopen70 == 7:
        print('Rafael Silva - Portugal 79')
    elif packopen70 == 8:
        print('Leila Hassan - Egypt 70')
    elif packopen70 == 9:
        print('Viktor Novak - Serbia 79')
    elif packopen70 == 10:
        print('Maya Chen - China 70')
    elif packopen70 == 11:
        print('Nikolai Volkov - Ukraine 75')
    elif packopen70 == 12:
        print('Carmen Morales - Mexico 72')
    elif packopen70 == 13:
        print('Matteo Bianchi - Italy 79')
    elif packopen70 == 14:
        print('Isabella Rojas - Colombia 74')
    elif packopen70 == 15:
        print('Lars Jansen - Netherlands 79')
    elif packopen70 == 16:
        print('Serena Montoya - Colombia 71')
    elif packopen70 == 17:
        print('Hassan Al-Mansur - Saudi Arabia 76')

def packmake90():
    packopen90 = randint(1, 6)

    if packopen90 == 1:
        print('Astrid Larsen - Norway 91')
    elif packopen90 == 2:
        print('Sergei Ortod - Russia 90')
    elif packopen90 == 3:
        print('Aisha Pablo - Spain 90')
    elif packopen90 == 4:
        print('Ivan Nikolav - Serbia 90')
    elif packopen90 == 5:
        print('Yuki Tanaka - Japan 90')
    elif packopen90 == 6:
        print('Alejandro Rodriguez - Argentina 92')

def clear_players_data():
    # Clear the content of playersdata.txt
    with open("playersdata.txt", "w") as f:
        f.write("")

def packblue70():
    makingblue70 = randint(1, 8)

    if makingblue70 == 1:
        packmake70()
    elif makingblue70 == 2:
        packmake80()
    elif makingblue70 == 3:
        packmake70()
    elif makingblue70 == 4:
        packmake70()
    elif makingblue70 == 5:
        packmake70()
    elif makingblue70 == 6:
        packmake70()
    elif makingblue70 == 7:
        packmake70()
    elif makingblue70 == 8:
        packmake80()
    
def packblue80():
    makingblue80 = randint(1, 6)

    if makingblue80 == 1:
        packmake80()
    elif makingblue80 == 2:
        packmake80()
    elif makingblue80 == 3:
        packmake90()
    elif makingblue80 == 4:
        packmake80()
    elif makingblue80 == 5:
        packmake80()
    elif makingblue80 == 6:
        packmake80()

def packblue90():
    makingblue90 = randint(1, 2)

    if makingblue90 == 1:
        packmake90()
    elif makingblue90 == 2:
        packmake90()