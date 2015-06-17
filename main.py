# -*- coding: utf-8 -*-
#The code is suppose to run in main
from path import BendPathGenerator
#from person import Person
from IPython import embed


if __name__ == "__main__":
#    person = Person('Ole','Jorgensen')
#    p=person
    global tool_pos, theta, bpg
    import numpy as np
    import config as cfg
    from matplotlib import pyplot as plt
    #bpg = BendPathGenerator(0.8, 0.5)
    bpg = BendPathGenerator(cfg.tube_length, cfg.bend_radius)
    theta = np.linspace(0, np.pi/2, 10)
    print([bpg(th).pos for th in theta])
    tool_pos = np.array([bpg(th).pos.array for th in theta])
    plt.plot(tool_pos[:,0], tool_pos[:,2])
    plt.show()
    embed()