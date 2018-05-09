import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

curve = IN[0]
curve1 = curve[0]
length = IN[1]
gap = IN[2]
numLoops = IN[3]


numLoops1 = int(numLoops[0])
lenGap = length + gap
p0 = curve1.PointAtChordLength(0, 0, True)
points = [p0]


for i in range(numLoops1):

	p1 = curve1.PointAtChordLength(lenGap, 0, True)
	points.append(p1)
	curve2 = curve1.SplitByPoints([p0,p1])
	
	for i in curve2:
		if i.Length > lenGap+10:
			curve1 = i
		else:
			continue
			

pointsP = Point.PruneDuplicates(points, 10)


pointsPS1 = pointsP[0:len(pointsP)-1]
pointsPE1 = pointsP[1:]

#lines = Line.ByStartPointEndPoint(pointsPS1,pointsPE1)
#linesTrim = 

OUT = pointsPS1, pointsPE1
