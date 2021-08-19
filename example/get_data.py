import pdal
import json

import sys
sys.path.append("./week6/USGS_3DEP_LIDAR_custom_package")
import os
os.chdir("./week6/USGS_3DEP_LIDAR_custom_package")
os.listdir()


PUBLIC_DATA_URL = "https://s3-us-west-2.amazonaws.com/usgs-lidar-public/"
REGION = "IA_FullState"
bounds = "([-93.756155, -93.747334], [41.918015, 41.921429])"
PUBLIC_ACCESS_PATH=f"{PUBLIC_DATA_URL}{REGION}/ept.json"
out_put_laz_path = "./example/data/laz/Iowa.laz"
out_put_tif_path = "./example/data/tif/Iowa.tif"
pipeline_path = "./example/get_data.json"



def get_raster_terrain(bounds:str , region:str , public_access_path =PUBLIC_ACCESS_PATH, output_filename_laz=out_put_laz_path, ouput_filename_tif = out_put_tif_path,pipeline_path =pipeline_path):

    with open(pipeline_path) as json_file:
        the_json = json.load(json_file)


    the_json['pipeline'][0]['bounds']=bounds
    the_json['pipeline'][0]['filename']=public_access_path
    the_json['pipeline'][3]['filename']=output_filename_laz
    the_json['pipeline'][4]['filename']=ouput_filename_tif

    pipeline = pdal.pipeline(json.dumps(the_json))
    try:
        exxec = pipeline.execute()
        metadata = pipeline.metadata

    except RuntimeError as e :
        print(e)
        print("run time error")
        pass

if (__name__== '__main__'):
    get_raster_terrain(bounds=bounds,region=REGION)
