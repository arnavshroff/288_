from controller import Robot
from controller import Keyboard

robot = Robot()
kb = Keyboard()

# create unique identifier for each device
motorA = robot.getDevice("A motor")
motorB = robot.getDevice("B motor")
motorC = robot.getDevice("C motor")
motorD = robot.getDevice("D motor")
motorE = robot.getDevice("E motor")
motorF = robot.getDevice("F motor")




timestep = int(robot.getBasicTimeStep())
kb.enable(timestep)

motorA_pos = 0
motorB_pos = 0
motorC_pos = 0
motorD_pos = 0
motorE_pos = 0
motorF_pos = 0


# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    key_pressed = kb.getKey()   

    # write code to move the joints with keyboard
    if(key_pressed == 49):
        motorA_pos += 0.005
    if(key_pressed == 50):
        motorA_pos -= 0.005
        
    motorA.setPosition(motorA_pos)
    
    if(key_pressed == 51):
        motorB_pos += 0.005
    if(key_pressed == 52):
        motorB_pos -= 0.005
        
    motorB.setPosition(motorB_pos)
    
    if(key_pressed == 53):
        motorC_pos += 0.005
    if(key_pressed == 54):
        motorC_pos -= 0.005
        
    motorC.setPosition(motorC_pos)
    
    if(key_pressed == 55):
        motorD_pos += 0.005
    if(key_pressed == 56):
        motorD_pos -= 0.005
        
    motorD.setPosition(motorD_pos)
    
    if(key_pressed == 57):
        motorE_pos += 0.005
    if(key_pressed == 48):
        motorE_pos -= 0.005
        
    motorE.setPosition(motorE_pos)
    
    if(key_pressed == 81):
        motorF_pos += 0.005
    if(key_pressed == 87):
        motorF_pos -= 0.005
        
    motorF.setPosition(motorF_pos)
     
     
     
     
     
     
     
     
     
     
     
     