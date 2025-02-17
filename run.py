import shapefile_processing_functions as spf

# Read the shapefile

# Path to the shapefile
shapefile_path = "/Users/prao/GitHub_Repos/SRP_TVA/SRP_TVA_data/ReEDS_data/shapefiles/US_PCA.shp"

# Read the shapefile
gdf = spf.read_shapefile(shapefile_path)

# Get the columns of the GeoDataFrame
columns = spf.get_shapefile_columns(gdf)

# Print the columns
print(columns)

# Print the first few rows of the GeoDataFrame
spf.print_first_rows(gdf)

# Filter and save specific regions
regions_to_filter = ["p10", "p13", "p27", "p28", "p39", "p40", "p52", "p53", "p94", "p95", "p96", "p97"]
output_directory = "/Users/prao/GitHub_Repos/SRP_TVA/SRP_TVA_data/ReEDS_data/filtered_shapefiles"

# spf.filter_and_save_regions(shapefile_path, output_directory, regions_to_filter, "rb")

# print("p10 centroid: ", spf.get_shapefile_centroid("/Users/prao/GitHub_Repos/SRP_TVA/SRP_TVA_data/ReEDS_data/filtered_shapefiles/p10.shp"))
# print("p13 centroid: ", spf.get_shapefile_centroid("/Users/prao/GitHub_Repos/SRP_TVA/SRP_TVA_data/ReEDS_data/filtered_shapefiles/p13.shp"))
# print("p27 centroid: ", spf.get_shapefile_centroid("/Users/prao/GitHub_Repos/SRP_TVA/SRP_TVA_data/ReEDS_data/filtered_shapefiles/p27.shp"))
# print("p28 centroid: ", spf.get_shapefile_centroid("/Users/prao/GitHub_Repos/SRP_TVA/SRP_TVA_data/ReEDS_data/filtered_shapefiles/p28.shp"))
# print("p39 centroid: ", spf.get_shapefile_centroid("/Users/prao/GitHub_Repos/SRP_TVA/SRP_TVA_data/ReEDS_data/filtered_shapefiles/p39.shp"))
# print("p40 centroid: ", spf.get_shapefile_centroid("/Users/prao/GitHub_Repos/SRP_TVA/SRP_TVA_data/ReEDS_data/filtered_shapefiles/p40.shp"))
# print("p52 centroid: ", spf.get_shapefile_centroid("/Users/prao/GitHub_Repos/SRP_TVA/SRP_TVA_data/ReEDS_data/filtered_shapefiles/p52.shp"))
# print("p53 centroid: ", spf.get_shapefile_centroid("/Users/prao/GitHub_Repos/SRP_TVA/SRP_TVA_data/ReEDS_data/filtered_shapefiles/p53.shp"))
# print("p94 centroid: ", spf.get_shapefile_centroid("/Users/prao/GitHub_Repos/SRP_TVA/SRP_TVA_data/ReEDS_data/filtered_shapefiles/p94.shp"))
# print("p95 centroid: ", spf.get_shapefile_centroid("/Users/prao/GitHub_Repos/SRP_TVA/SRP_TVA_data/ReEDS_data/filtered_shapefiles/p95.shp"))
# print("p96 centroid: ", spf.get_shapefile_centroid("/Users/prao/GitHub_Repos/SRP_TVA/SRP_TVA_data/ReEDS_data/filtered_shapefiles/p96.shp"))
# print("p97 centroid: ", spf.get_shapefile_centroid("/Users/prao/GitHub_Repos/SRP_TVA/SRP_TVA_data/ReEDS_data/filtered_shapefiles/p97.shp"))
