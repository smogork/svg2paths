from svgpathtools import svg2paths, Arc
import numpy as np
import vectors as vpy


def read_file(path: str):
    paths, _ = svg2paths(path)
    return paths


def parse(path: str, bezier_precision: float) -> [[np.imag]]:
    paths = read_file(path)
    letters = []

    for path in paths:
        points = []
        prev_segment = None
        for segment in path:
            if prev_segment is not None and abs(prev_segment.point(1) - segment.point(0)) > 1e-6:
                letters.append(points)
                points = []
            if isinstance(segment, Arc):
                minX, maxX, minY, maxY = segment.bbox()
                bezier_segments = int(max(2, ((maxX - minX) + (maxY - minY)) / bezier_precision))
                for i in np.linspace(0, 1, bezier_segments):
                    points.append(segment.point(i))
            else:
                poly = segment.poly()
                if poly.order == 1:  # line
                    points.append(poly(0))
                    points.append(poly(1))
                else:  # bezier segment
                    minX, maxX, minY, maxY = segment.bbox()
                    bezier_segments = int(max(2, ((maxX - minX) + (maxY - minY)) / bezier_precision))
                    for i in np.linspace(0, 1, bezier_segments):
                        points.append(poly(i))

            prev_segment = segment
        letters.append(points)
    return letters


def convert_to_paths(filepath: str, bezier_precision: float, origin: vpy.Vector2,
                     scale: vpy.Vector2, rotation: float, depth: float, safe_height: float) -> [vpy.Vector3]:
    letters = parse(filepath, bezier_precision)
    paths = []

    for letter in letters:
        letter_path = []
        for point in letter:
            coord = vpy.Vector3(np.real(point), -np.imag(point), depth)
            # apply scale
            coord.x *= scale.x
            coord.y *= scale.y
            # apply rotation
            xx =  np.cos(rotation) * coord.x - np.sin(rotation) * coord.y# CHWDP - chuj w dupe pythonowi
            coord.y = np.sin(rotation) * coord.x + np.cos(rotation) * coord.y
            coord.x = xx
            # apply translation
            coord.x += origin.x
            coord.y += origin.y
            letter_path.append(coord)

        if len(paths) > 0:
            prev = paths[-1]
            next = letter_path[0]
            paths.append(vpy.Vector3(prev.x, prev.y, safe_height))
            paths.append(vpy.Vector3(next.x, next.y, safe_height))

        paths.extend(letter_path)

    return paths

