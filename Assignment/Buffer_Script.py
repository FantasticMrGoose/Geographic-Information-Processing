#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      zhouzir1
#
# Created:     14/11/2019
# Copyright:   (c) zhouzir1 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#imports the arcpy module
import arcpy

#setting the workspace environment
from arcpy import env
env.workspace = "\\\\medusa\\StudentWork\\zhouzir1\\GGR321\\A3Part5\\"

#ensures spatial analyst extension is enabled for buffer tool
if arcpy.CheckExtension("Spatial") == "Available":
    arcpy.AddMessage("Checking out Spatial")
    arcpy.CheckOutExtension("Spatial")
else:
    arcpy.AddError("Unable to get spatial analyst extension")
    arcpy.AddMessage(arcpy.GetMessages(0))
    sys.exit(0)

# Getting the user to input their feature class
InFc = arcpy.GetParameter(0)

# setting the parameter and output for feature to points
PointLocation = arcpy.GetParameter(1)
PointsOutput = "FC_to_Points"

# getting user to input their desired parameters for buffer
BuffDist = arcpy.GetParameter(2)
LineSide = arcpy.GetParameterAsText(3)
LineEnd = arcpy.GetParameterAsText(4)
Dissolve = arcpy.GetParameterAsText(5)
DissolveField = arcpy.GetParameter(6)
method = arcpy.GetParameterAsText(7)

# getting user to specify output for their buffer zone
BufferZone = arcpy.GetParameterAsText(8)

# converts the input feature class to points, generating the points at the center
arcpy.FeatureToPoint_management (InFc, PointsOutput, PointLocation)

# creates the buffer zone of the points based on user parameter input
arcpy.Buffer_analysis (PointsOutput, BufferZone, BuffDist, LineSide, LineEnd, Dissolve, DissolveField, method)

#removes temporary files
if arcpy.Exists(BuffPts):
 arcpy.Delete_management(BuffPts)



