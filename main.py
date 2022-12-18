import numpy as np

from vectors import Vector3
from gcode_writer import GCodeWriter

def main():
    t = np.array([Vector3(10, 3, 5), Vector3(10, 3, 2), Vector3(10, 2, 3), Vector3(1, 6, 3)])

    writer = GCodeWriter()
    writer.SetCutterDiameter(3)
    writer.SaveCutterPath("test", t)

    print(t)

if __name__ == '__main__':
    main()

