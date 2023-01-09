import numpy as np
from vectors import Vector3

class GCodeWriter:
    def __init__(self):
        self.__diameter = 1

    def __generateFilename(self, filename: str) -> str:
        res = divmod(self.__diameter, 10)
        ext = f".k{res[0]}{res[1]}"
        return filename + ext

    def __scalarAlmostEquals(self, a: float, b:float, eps: float):
        return abs(a - b) < eps

    def __vector3AlmostEquals(self, v: Vector3, w: Vector3, eps: float):
        return self.__scalarAlmostEquals(v.x, w.x, eps) and self.__scalarAlmostEquals(v.y, w.y, eps) and self.__scalarAlmostEquals(v.z, w.z, eps)

    def __generateGCodeLine(self, curPoint: Vector3, lastPoint: Vector3, lineNumber: int) -> str:
        res = f"N{lineNumber}G01"
        eps = 1e-3

        # Skipping null moves
        if self.__vector3AlmostEquals(curPoint, lastPoint, eps):
            return ""

        if not self.__scalarAlmostEquals(curPoint.x, lastPoint.x, eps):
            res += f"X{curPoint.x:.3f}"
        if not self.__scalarAlmostEquals(curPoint.y, lastPoint.y, eps):
            res += f"Y{curPoint.y:.3f}"
        if not self.__scalarAlmostEquals(curPoint.z, lastPoint.z, eps):
            res += f"Z{curPoint.z:.3f}"

        return res

    def SaveCutterPath(self, filename:str, points: np.ndarray[Vector3]) -> None:

        filepath = self.__generateFilename(filename)

        with open(filepath, "w") as output:
            lineNum = 0
            output.write(f"{self.__generateGCodeLine(points[0], Vector3(points[0].x + 1, points[0].y + 1, points[0].z + 1),lineNum)}\n")
            lineNum += 1
            lastPoint = points[0]

            for p in points:
                line = self.__generateGCodeLine(p, lastPoint, lineNum)
                if len(line) == 0:
                    continue
                output.write(f"{line}\n")
                lineNum += 1
                lastPoint = p

    def SetCutterDiameter(self, diameter: int) -> None:
        self.__diameter = diameter
