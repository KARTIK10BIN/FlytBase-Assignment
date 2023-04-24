#!/usr/bin/env python
import time
from flyt_python import api

drone = api.navigation(timeout=120000)  # instance of flyt droneigation class

# at least 3sec sleep time for the drone interface to initialize properly
time.sleep(3)

print('SECTION - B')
print('MISSION PLAN : Takeoff at 10m, move in triangle trajectory of side 10m, and land')

print('Arming drone')
drone.arm()

print('Taking Off')
takeoff = drone.take_off(10.0)

print(' Moving in triangle trajectory of side 10m')
drone.position_set(8.660, 5, 0, relative=True)
drone.position_set(-8.660, 5, 0, relative=True)
drone.position_set(0, -10, 0, relative=True)

print('Landing')
drone.land(async=True)

print('Dis-arming drone')
drone.disarm()

# shutdown the instance
drone.disconnect()