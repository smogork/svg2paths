# SVG2PATHS

Simple converter from SVG paths objects to GCode paths (only XYZ points).
It is designed to create engravings on 3C milling machine, so every point will be at given Z value.
Only points where paths are discontinued Z value will increase Z coordinate.
It is really useful for text and simple images engravings.

## Prameters

Typical usage looks like this
```
    python svg2paths.py test.svg sinus -z 24.5 -s 50 -j 10 -ox -55 -oy 65 -sx 0.25 -sy 0.25 -r -90
```

Required parameters:
1. Source SVG file
2. Target paths filename
3. Start Z position for safe path start (`-s`)
4. Target Z value of engraving (`-z`)

Optional parameters (default values in parathesis):
1. Diameter of a cutter (`-d 1`)
2. Z value increase between discontinuity (`-j 10`)
3. Origin point `(x,y)` corresponding to SVG `(0,0)` (`-ox 0.0 -oy 0.0`)
4. Scale `(sx,sy)` of imported paths (`-sx 1.0 -sy 1.0`)
5. Rotation of imported paths in degrees (`-r 0`)

## Examples

GNU:

![obraz](https://user-images.githubusercontent.com/35574506/208318084-bc108ea1-ab4d-4b2a-b108-223ad1afb047.png)

Text:
