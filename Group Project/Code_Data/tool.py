#import system modules
import arcpy
from arcpy import env

#set environment settings for input workspace.
env.workspace = "C:\\Users\\jsk\\Documents\\GGR321\\group project\\new"


# Local variables as parameters:
#city ward
city_boundary = arcpy.GetParameter(0)
#park shapefile
park = arcpy.GetParameter(1)
Toronto_Neighbourhoods = arcpy.GetParameter(2)
bufferZone= arcpy.GetParameterAsText(3)


#proceesses location
Buffer_park = "Buffer_parks.shp"
Erase_buffer = "Erase_buffer_park.shp"

Toronto_whole_Erase_Intersec_shp = arcpy.GetParameterAsText(4)

#sets projection to parks
sr = arcpy.SpatialReference("NAD 1983 UTM Zone 17N")
arcpy.DefineProjection_management(park, sr)

# Process: Buffer
arcpy.Buffer_analysis(park, Buffer_park, bufferZone, "FULL", "ROUND", "ALL", "", "PLANAR")

# Process: Erase
arcpy.Erase_analysis(city_boundary, Buffer_park, Erase_buffer)

# Process: Intersect
arcpy.Intersect_analysis([Erase_buffer, Toronto_Neighbourhoods], Toronto_whole_Erase_Intersec_shp, "ONLY_FID", "", "INPUT")

# Process: Add Geometry Attributes
arcpy.AddGeometryAttributes_management(Toronto_whole_Erase_Intersec_shp, "AREA_GEODESIC;CENTROID_INSIDE", "METERS", "SQUARE_KILOMETERS", "PROJCS['NAD_1983_UTM_Zone_17N',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-81.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]")

#delete temp files
arcpy.Delete_management(Buffer_park)
arcpy.Delete_management(Erase_buffer)









