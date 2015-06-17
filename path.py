# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# coding=utf-8

"""
An ideal bend path generator for using a robot to bend a tube around a template.
"""

__author__ = "Morten Lind"
__copyright__ = "SINTEF 2015"
__credits__ = ["Morten Lind"]
__license__ = "GPLv3"
__maintainer__ = "Morten Lind"
__email__ = "morten.lind@sintef.no"
__status__ = "Development"

import math3d as m3d

# All units in SI

class BendPathGenerator(object):

    def __init__(self, l_tube, r_template, angular_strain_rate=0.0):
        # The length from the template clamp to the tool clamp
        self.l = l_tube
        # Bending radius of the template and tube combination. This is
        # the distance from the template circular centre to the
        # centroid of the tube.
        self.r = r_template
        # The angular strain rate is the relative elongation per
        # angle. During bending a value > 0.0 will serve to maintain a
        # force through the tube.
        self.asr = angular_strain_rate
        # A reference system at the centre of the template bend with z
        # upward and x along the tube from the template clamp. This is
        # the natural reference system for computing the bending path.
        self._template_ref = m3d.Transform()
        # A reference system with origo at the template clamp in the
        # centre of the tube. Aligned witht the template reference
        # system.
        self._tube_ref = m3d.Transform()
        self._tube_ref.pos.z = self.r
        
    def __call__(self, theta, tube_ref=True):
        """When the tube has been bent to contact with the template over the
        angle 'theta', compute and return the pose of the natural
        tool. The natural tool is one which, in the unbent shape, is
        oriented as the tube reference system and translated the tube
        length along the x-direction. If 'tube_ref' is true, the
        resulting tool pose is returned in tube reference, otherwise
        it is returned in the natural template centre reference.
        """
        # The rotation generator in template reference
        rot = m3d.Transform(m3d.Orientation([0,theta,0]), m3d.Vector())
        # The contact point with correct orientation of the natural tool
        contact = rot * self._tube_ref
        # The arc lenght in contact to the contact point along the template
        contact_length = theta * self.r
        # The remaining, unbent part of the tube from the contact to
        # the grasp
        free_length = self.l - contact_length
        if free_length <= 0.0:
            raise Exception('Collision between tool and template!')
        # Offset the contact pose to the correct tool grasp pose along
        # the contact x-direction
        tool_pose = contact.copy()
        tool_pose.pos += (free_length + self.asr * theta) * contact.orient.vec_x
        if tube_ref == 'Tube':
            # Transform to tube reference
            return self._tube_ref.inverse * tool_pose
        else:
            # Return in template centre reference
            return tool_pose
            
def test():
    global tool_pos, theta, bpg
    import numpy as np
    import config as cfg
    from matplotlib import pyplot as plt
    #bpg = BendPathGenerator(0.8, 0.5)
    bpg = BendPathGenerator(cfg.tube_length, cfg.bend_radius)
    print("bpg = ",bpg)
    print("np.pi/2 =  ",np.pi/2)
    theta = np.linspace(0, np.pi/2, 10)
    print("theta = ",theta)
    print([bpg(th).pos for th in theta])
    tool_pos = np.array([bpg(th).pos.array for th in theta])
    print("Tool pos = \n",tool_pos)
    plt.plot(tool_pos[:,0], tool_pos[:,2])
    plt.show()

def test2():
    from math import pi
    import config as cfg
    from IPython import embed
    bpg = BendPathGenerator(cfg.tube_length, cfg.bend_radius)
    print(bpg(0))
    print(bpg(pi/2))
    
    embed()

if __name__ == '__main__':
    test()
    #test2()
