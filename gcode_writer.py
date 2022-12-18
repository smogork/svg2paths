import numpy as np
from vectors import Vector3

class GCodeWriter:
    def __init__(self):
        self.__diameter = 1

    def __generateFilename(self, filename: str) -> str:
        res = divmod(self.__diameter, 10)
        ext = f".k{res[0]}{res[1]}"
        return filename + ext

    def __generateGCodeLine(self, curPoint: Vector3, lastPoint: Vector3, lineNumber: int) -> str:
        res = f"N{lineNumber}G01"

        if curPoint.x != lastPoint.x:
            res += f"X{curPoint.x:.3f}"
        if curPoint.y != lastPoint.y:
            res += f"X{curPoint.y:.3f}"
        if curPoint.z != lastPoint.z:
            res += f"X{curPoint.z:.3f}"

        return res

    def SaveCutterPath(self, filename:str, points: np.ndarray[Vector3]) -> None:

        filepath = self.__generateFilename(filename)

        with open(filepath, "w") as output:
            lineNum = 0
            output.write(f"{self.__generateGCodeLine(points[0], Vector3(points[0].x + 1, points[0].y + 1, points[0].z + 1), lineNum)}\n")
            lineNum += 1
            lastPoint = points[0]

            for p in points:
                output.write(self.__generateGCodeLine(p, lastPoint, lineNum))
                lineNum += 1
                lastPoint = p

    def SetCutterDiameter(self, diameter: int) -> None:
        self.__diameter = diameter
