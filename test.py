# -*- coding: utf-8 -*-
#hhehe
# -*- coding: utf-8 -*-
import urx
from IPython import embed

if __name__ == "__main__":
    try:
        robot = urx.Robot("192.168.1.100")
        r = robot
        print("Robot object is available as robot or r")
        embed()
    finally:
        robot.close()
