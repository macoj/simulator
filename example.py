__author__ = 'marcos'


def pso():
    """
    PSO.jar runs particles evaluations dimensions function topology mechanism [mechanism_parameter]
    > TOPOLOGY
     0: GLOBAL 1: RING 2: RANDOM 3: VON_NEUMANN 4: THREESOME_PARTNERS 5: NSOME_PARTNERS
    > MECHANISM
     0: NONE 1: DYNAMIC_2011
    """
    commands = []
    topologies = [("global", 0), ("ring", 1), ("vonneumann", 3)]
    runs = 30
    functions = range(1, 21)
    evaluations = 1000000
    dimensions = 1000
    particles = 100
    for topology in topologies:
        for function in functions:
            commands += ["java -jar PSO/jar/pso.jar 1 %d %d %d %d %d 0 > %s_F%02d_%02d.teste " %
                         (particles, evaluations, dimensions, function, topology[1],
                         topology[0], function, r) for r in range(runs)]
    return commands
"""
execfile("simulator.py")
execfile("example.py")
print "The commands: " + str(pso())
Simulator.execute(pso(), number_of_processes=10, delay_between=5)
"""