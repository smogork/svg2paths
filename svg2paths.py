import math

import argparse

from vectors import Vector2, Vector3
from svg_parse import convert_to_paths
from gcode_writer import GCodeWriter

def main(startZ: float, targetZ: float, jumpZ: float, filename: str, diameter: int, svg_file: str,
         scale: Vector2, origin: Vector2, rotation: float):


    paths = convert_to_paths(svg_file, 0.5, origin, scale, rotation / 180 * math.pi, targetZ, targetZ + jumpZ)

    paths.insert(0, Vector3(paths[0].x, paths[0].y, startZ))
    paths.insert(0, Vector3(0, 0, startZ))
    paths.append(Vector3(paths[-1].x, paths[-1].y, startZ))
    paths.append(Vector3(0, 0, startZ))

    writer = GCodeWriter()
    writer.SetCutterDiameter(diameter)
    writer.SaveCutterPath(filename, paths)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='svg2paths',
        description='Converts paths from SVG file to lines at GCode')

    parser.add_argument('svg_file', help="Path to svg file", type=str)  # positional argument
    parser.add_argument('filename', help="Filename to save", type=str)  # positional argument
    parser.add_argument('-z', "--plane-z", required=True, help="paths will be created on given Z", type=float)  # option that takes a value
    parser.add_argument('-s', "--start-z", required=True, help="secure height to start from", type=float)  # option that takes a value
    parser.add_argument('-j', "--jump-z", default=10, help="secure change at z to jump between lines", type=float)  # option that takes a value
    parser.add_argument("-d", "--diameter", default=1, help="Cutter diameter in milimiters", type=int)
    parser.add_argument("-ox", "--origin-x", default=0, help="Point that will correspond to SVG 0,0", type=float)
    parser.add_argument("-oy", "--origin-y", default=0, help="Point that will correspond to SVG 0,0", type=float)
    parser.add_argument("-sx", "--scale-x", default=1, help="X scale of image", type=float)
    parser.add_argument("-sy", "--scale-y", default=1, help="Y scale of image", type=float)
    parser.add_argument("-r", "--rotation", default=0, help="Rotation of image", type=float)

    args = parser.parse_args()
    main(args.start_z, args.plane_z, args.jump_z, args.filename, args.diameter, args.svg_file,
         Vector2(args.scale_x, args.scale_y), Vector2(args.origin_x, args.origin_y), args.rotation)

