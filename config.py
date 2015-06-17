# -*- coding: utf-8 -*-
"""
Config file for mix2 prosjekt lab
"""

from math import pi
import math

import math3d as m3d

robot_ip = "192.168.1.100"
force_sensor_ip = "192.168.1.102"

robot_payload = 1.0, (0, 0, 0.18)  # in kg and position in m

# griper, center of hole in griper
robot_tcp = m3d.Transform()
robot_tcp.pos = (0, 0, 0.243)
# calib object
robot_tcp_calib = m3d.Transform()
robot_tcp_calib.pos = (0, 0, 0.156)


tube_diameter = 0.063  # from pipelife do not change
bend_radius = tube_diameter * 3.5  # formel from pipelife, should be exact
# Form might not have exacyly the expected diameter....
form_radius = tube_diameter * 3
start_extension = 0.010
extension = 0.01 / (pi / 2)
tube_length = 0.435 + start_extension  # this is length from top of form to robot tcp
theta = pi / 2  # we want to bend 90degrees, do not change

# where we pick tube, from jogging
pick_pos = [0.227,
 -0.1868917706953159,
 0.188]


# This is two points for 0 and x direction, found by jogging with calib tool
calib_point1 = [0.22885551995648182,
                0.7528823563944315,
                0.3055893026112024]

calib_point2 = [0.3295538352543739,
                0.8567955568777109,
                0.30526465941437936]

calib_point1 = m3d.Vector(calib_point1)
calib_point2 = m3d.Vector(calib_point2)

# simple math to tranform robot csys to our new 0 point and x direction
vec1 = m3d.Vector(1, 0, 0)
print("Vec1 = ", vec1)
vec2 = calib_point2 - calib_point1
vec2.normalize()
print("Vec2 = ", vec2)
calib_angle = math.acos(vec1 * vec2)
print("Calib rotation angle is : ", calib_angle)
robot_csys = m3d.Transform()
robot_csys.pos = calib_point1
robot_csys.orient.rotate_zb(calib_angle)

# transformation from our 0 to center of form. Found out this was easier to understand robot coordinates,
# but should maybe be changed back
# measure with robot and calib object and changed to keep correct distance from form at end of move
calib_to_zero = [0.279, -0.113, 0.014]
calib_to_zero[2] = calib_to_zero[2] - form_radius

robot_csys.pos += robot_csys.orient * m3d.Vector(calib_to_zero)
robot_csys.orient.rotate_zb(pi)  # rotate our coordinate system 180 degrees


robot_initj = [-1.9244898001300257,
 -1.246505085621969,
 1.2064332962036133,
 1.6100200414657593,
 1.5707341432571411,
 -1.123030964528219]

#robot_tool_z = [-pi, 0, 0]
# this is close to -pi,0,0 but not quite, adapter is not really correct
robot_tool_z = [ 3.140740877119804,
 -0.06686663632889207,
 -0.0005149521388340898]



# -*- coding: utf-8 -*-

