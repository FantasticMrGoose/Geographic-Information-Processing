#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      zhouzir1
#
# Created:     10/11/2019
# Copyright:   (c) zhouzir1 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Import arcpy module, this add all of the ArcGIS function to
# Python, they are not incldued by default. ArcGIS must be installed
# on the computer you use this script with.
import arcpy

# We need to make sure we have the Spatial Analyst Extension Checked
arcpy.CheckOutExtension("Spatial")

# Local variables:
# First we will define our existing raster files files
# Note: We will save the path to the files as a variable so we
# Only need to enter this information once, and we will concatenate
# Additonal strings to create variables with the names
path = "\\\\medusa\\StudentWork\\zhouzir1\\GGR321\\GGR321_Assignment-3 Data\\Part3\\"

# The location of the trailhead
TrailHead = path + "TrailHead.shp"

# Your selected best sightseeing location in the last step as the destination
# You need to change the file name from "CandidateSpot_X" to the name of the best sightseeing location
# CandidateSpot_A? CandidateSpot_B? CandidateSpot_C?
Destination = path + "CandidateSpot_C.shp"

# The Slope Cost Raster that you created
# Uou may need to change the file name
# If it is inside a folder you need to include the folder e.g.
# "foldername\\filename.tif"
SlopeCost = path + "speed_costdistanceV2.tif"

# The Land Use Cost Raster that you created
# You may need to change the file name
LandCost = path + "Land_CostDistance.tif"

# Now we will define file names that we will use
# when we create new files.

# This is the file name for our weighted SlopeCost
tSLC_tif = path + "tSLC.tif"

# This is the file name for our weighted LandUse Cost
tLCC_tif = path + "tLCC.tif"

# File name for the combined weighted file
Cost_tif = path + "Cost.tif"

# Cost Distance
CostDist_tif = path + "CostDist.tif"

# Cost Back Link
CostDist_bl_tif = path + "CostDist_bl.tif"

# Least Cost Path
LeastPath_tif = path + "LeastPath.tif"

# Polygon from converting cost path to shapefile
LPath_poly = path + "LPathPoly.shp"


# Process:

# Instead of Weighted Overlay, this approach multiples each
# raster by a weight (that equals 1) and then adds the two
# weighted rasters together

# created a list based on the influence desired
# note that slopeList and landuseList have reversed positions
# this ensures that when the for loop occurs, the indexed values add up to 1

slopeList = [0.9,0.75,0.65,0.55,0.45,0.35,0.25,0.1]
landuseList = [0.1,0.25,0.35,0.45,0.55,0.65,0.75,0.9]
# parameters for raster to polyline

# since there are 8 pairs, we want to loop through 8 times, hence the range 8
for x in range(8):
    #attributes the indexed value to the variable "s" and "l" for the time being
    s = slopeList[x]
    l = landuseList[x]
    # creates a file for every weight pair based on their weight in that file
    # for example, the first loop will generate tSLC_0.9_0.1.tif which shows
    # the influence from slope and land use in the file name, but keep in mind
    # that there is no influence from land use in tSLC_tif since we are only
    # creating the weight of the slope raster
    Cost_tif = path + "Cost" + str(s) + "_" + str(l) + ".tif"
    CostDist_tif = path + "CostDist" + str(s) + "_" + str(l) + ".tif"
    CostDist_bl_tif = path + "CostDist_bl" + str(s) + "_" + str(l) + ".tif"
    LeastPath_tif = path + "LeastPath" + str(s) + "_" + str(l) + ".tif"
    LP_poly = path + "LP_poly" + str(s) + "_" + str(l) + ".shp"
    # Process: Times for land cover
    # Used to multiple the land cover cost by the weight
    arcpy.gp.Times_sa(s, SlopeCost, tSLC_tif)
    arcpy.gp.Times_sa(l, LandCost, tLCC_tif)
    arcpy.gp.Plus_sa(tSLC_tif, tLCC_tif, Cost_tif)
    arcpy.gp.CostDistance_sa(TrailHead, Cost_tif, CostDist_tif, "", CostDist_bl_tif, "", "", "", "")
    arcpy.gp.CostPath_sa(Destination, CostDist_tif, CostDist_bl_tif, LeastPath_tif, "EACH_CELL", "Id")
    arcpy.RasterToPolyline_conversion(path + "LeastPath" + str(s) + "_" + str(l) + ".tif", LP_poly, "ZERO", "0", "SIMPLIFY", "Value")
    # Deletes both the tSLC and TLCC file since they only contain their own
    # respective weight
    # could also remove cost and cost distance if all we wanted is the least path
    if arcpy.Exists(path + "tSLC.tif"):
        arcpy.Delete_management(path + "tSLC.tif")
    if arcpy.Exists(path + "tLCC.tif"):
        arcpy.Delete_management(path + "tLCC.tif")





