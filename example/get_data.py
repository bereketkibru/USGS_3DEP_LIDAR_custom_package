import pdal
import json


from boundaries import Boundaries


class Lidar_Data_Fetch:

    def __init__(self, public_data_url, fetch_json_path="./get_data.json") -> None:
        self.public_data_url = public_data_url
        self.fetch_json_path = fetch_json_path
        self.out_put_laz_path = "./data/laz/Iowa.laz"
        self.out_put_tif_path = "./data/tif/Iowa.tif"

    def __readFetchJson(self, path: str) -> dict:
        try:
            with open(path, 'r') as json_file:
                dict_obj = json.load(json_file)
            return dict_obj

        except FileNotFoundError as e:
            print('FETCH_JSON_FILE_NOT_FOUND')

    def getPipeline(self, region: str, bounds: Boundaries):
        fetch_json = self.__readFetchJson(self.fetch_json_path)
        BOUND = "([-93.756155, 41.918015], [-93.747334, 41.921429])"

        boundaries = bounds.getBoundStr()

        full_dataset_path = f"{self.public_data_url}{region}/ept.json"

        fetch_json['pipeline'][0]['filename'] = full_dataset_path
        fetch_json['pipeline'][0]['bounds'] = BOUND

        fetch_json['pipeline'][3]['filename'] = self.out_put_laz_path
        fetch_json['pipeline'][4]['filename'] = self.out_put_tif_path

        pipeline = pdal.Pipeline(json.dumps(fetch_json))

        return pipeline

    def runPipeline(self, region: str, bounds: Boundaries):
        pipeline = self.getPipeline(region, bounds)

        try:
            pipeline.execute()
            metadata = pipeline.metadata
            log = pipeline.log
        except RuntimeError as e:
            print(e)

