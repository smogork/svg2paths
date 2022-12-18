import numpy as np
import argparse

from vectors import Vector3
from gcode_writer import GCodeWriter

def main(startZ: float, targetZ: float, filename: str, diameter: int):
    t = np.array([Vector3(10, 3, 5), Vector3(10, 3, 2), Vector3(10, 2, 3), Vector3(1, 6, 3)])

    writer = GCodeWriter()
    writer.SetCutterDiameter(3)
    writer.SaveCutterPath("test", t)

    print(t)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='svg2paths',
        description='Converts paths from SVG file to lines at GCode')

    parser.add_argument('filename', help="Filename to save")  # positional argument
    parser.add_argument('-z', "--plane-z", required=True, help="paths will be created on given Z")  # option that takes a value
    parser.add_argument('-s', "--start-z", required=True, help="secure height to start from")  # option that takes a value
    parser.add_argument("-d", "--diameter", default=1, help="Cutter diameter in milimiters")

    args = parser.parse_args()
    main(args.start_z, args.plane_z, args.filename, args.diameter)

