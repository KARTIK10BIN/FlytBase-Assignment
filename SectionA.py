#!/usr/bin/env python
import time
from flyt_python import api

drone = api.navigation(timeout=120000)  # instance of flyt droneigation class

# at least 3sec sleep time for the drone interface to initialize properly
time.sleep(3)

print('SECTION - A')
print('MISSION PLAN : Takeoff at 5m, move in square trajectory of side 6.5m, and land')

print('Arming drone')
drone.arm()

print('Taking Off')
takeoff = drone.take_off(5.0)

print(' Moving in square trajectory of side 6.5m')
drone.position_set(6.5, 0, 0, relative=True)
drone.position_set(0, 6.5, 0, relative=True)
drone.position_set(-6.5, 0, 0, relative=True)
drone.position_set(0, -6.5, 0, relative=True)

print('Landing')
drone.land(async=True)

print('Dis-arming drone')
drone.disarm()

# shutdown the instance
drone.disconnect()