import clr

# Import RevitAPI
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

# Import DocumentManager and TransactionManager
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

# Import ToDSType(bool) extension method
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

# Unwrap
input = UnwrapElement( IN[0] )
elements = []
#force input into list
try:
	for e in input:
		if e.Category.Name == "Structural Framing":
			elements.append(e)
except:
	if input.Category.Name == "Structural Framing": 
		elements.append(input)
	

	
# Start Transaction
doc = DocumentManager.Instance.CurrentDBDocument
TransactionManager.Instance.EnsureInTransaction(doc)

for e in elements:
	Autodesk.Revit.DB.Structure.StructuralFramingUtils.DisallowJoinAtEnd(e, 0)
	Autodesk.Revit.DB.Structure.StructuralFramingUtils.DisallowJoinAtEnd(e, 1)

# End Transaction
TransactionManager.Instance.TransactionTaskDone()

# Wrap
OUT = elements
