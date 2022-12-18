from svgpathtools import svg2paths
import numpy as np
import VectorsPY as vpy


def read_file(path: str):
    paths, _ = svg2paths(path)
    return paths


def parse(path: str, bezier_segments: int) -> [[np.imag]]:
    paths = read_file(path)
    letters = []

    for path in paths:
        points = []
        for segment in path:
            poly = segment.poly()
            if poly.order == 1:  # line
                points.append(poly(0))
                points.append(poly(1))
            else:  # bezier segment
                for i in np.linspace(0, 1, bezier_segments):
                    points.append(poly(i))
        letters.append(points)
    return letters


def convert_to_paths(filepath: str, bezier_segments: int, origin: vpy.Vector2,
                     scale: vpy.Vector2, rotation: float) -> [[vpy.Vector2]]:
    letters = parse(filepath, bezier_segments)
    paths = []

    for letter in letters:
        letter_path = []
        for point in letter:
            coord = vpy.Vector2(np.real(point), np.imag(point))
            # apply scale
            coord.x *= scale.x
            coord.y *= scale.y
            # apply rotation
            coord.x = np.cos(rotation) * coord.x + np.sin(rotation) * coord.y
            coord.y = -np.sin(rotation) * coord.x + np.cos(rotation) * coord.y
            # apply translation
            coord.x += origin.x
            coord.y += origin.y
            letter_path.append(coord)
        paths.append(letter_path)

    return paths

