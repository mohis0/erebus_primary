from controller import Robot
import struct

# Create robot instance
robot = Robot()
timeStep = 32

# Declare communication link between the robot and the controller
emitter = robot.getDevice("emitter")

# --------------------------------------------------
# Delay function (milliseconds)
# --------------------------------------------------
def delay(ms):
    initTime = robot.getTime()  # starting time in seconds
    while robot.step(timeStep) != -1:
        if (robot.getTime() - initTime) * 1000.0 > ms:
            break

# --------------------------------------------------
# Battery reporting function
# --------------------------------------------------
def report_battery(word):
    # Optional: stop robot or move to known pose
    # go(0, 0)  # Uncomment if you have a go() function

    delay(2000)  # Wait for 2 seconds before sending the report

    starter = b"V"                 # Message start identifier
    BatteryType = word.encode()     # e.g. "H" , "S", "U"

    # Pack two characters into the message
    message = struct.pack("c c", starter, BatteryType)

    emitter.send(message)
    delay(1000)

# --------------------------------------------------
# Example usage
# --------------------------------------------------

# Keep controller alive
while robot.step(timeStep) != -1:
    # Report a battery type
    report_battery("H")
    report_battery("S")
    report_battery("U")
    pass
