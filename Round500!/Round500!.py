from typing import Optional
import c4d 
import math

def main():

    if not op:
        c4d.gui.MessageDialog("Select an object!")
        return

    #initializing vars
    position = op[c4d.ID_BASEOBJECT_REL_POSITION]
    rotation = op[c4d.ID_BASEOBJECT_REL_ROTATION]

    positionRound = 0.05 #step size
    rotationRound = 0.05 #step size

    #modifying
    for i in range(3):

        position[i] = round(position[i] / positionRound) * positionRound

        rotation[i] = math.degrees(rotation[i])
        rotation[i] = round(rotation[i] / rotationRound) * rotationRound
        rotation[i] = math.radians( rotation[i])

    #transferring
    op.SetAbsPos(position)
    op.SetAbsRot(rotation)
    
    c4d.EventAdd()

if __name__ == '__main__':
    main() 
