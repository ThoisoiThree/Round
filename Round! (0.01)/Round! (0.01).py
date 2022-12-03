from typing import Optional
import c4d 
import math

def main():
    
    #Code by Thoisoi Three https://vk.com/lighting.techdirector
    #Logo by Alexey Golod https://vk.com/golodvk

    if not op:
        c4d.gui.MessageDialog("Select an object!")
        return

    #initializing vars
    position = op[c4d.ID_BASEOBJECT_REL_POSITION]
    rotation = op[c4d.ID_BASEOBJECT_REL_ROTATION]

    positionRound = 2 #how many signs are after comma
    rotationRound = 2 #how many signs are after comma

    #modifying
    for i in range(3):

        position[i] = round(position[i], positionRound)

        rotation[i] = math.degrees(rotation[i])
        rotation[i] = round(rotation[i], rotationRound)
        rotation[i] = math.radians( rotation[i])

    #transferring
    op.SetAbsPos(position)
    op.SetAbsRot(rotation)
    
    c4d.EventAdd()

if __name__ == '__main__':
    main() 
