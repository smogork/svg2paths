from svg_parse import convert_to_paths
from VectorsPY import Vector2


if __name__ == '__main__':
    paths = convert_to_paths('test.svg', 10, Vector2(-15, -15), Vector2(0.1, 0.1), 0)
    print(paths)
