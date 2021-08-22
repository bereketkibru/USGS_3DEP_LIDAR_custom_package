import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import geopandas as gpd
from logger import get_logger
from file_handler import FileHandler
import sys

logger = get_logger('Visulaize')
logger.info("Starts Visualize script")

class Visulaize:
    def __init__(self,geoData="farm" ) -> None:
        try:
            self.logger = get_logger(__name__)
            self.geoData = geoData
            self.file_handler = FileHandler()
            logger.info('Successfully Starts Visualize Class Object')
        except Exception as e:
            logger.exception('Failed to Start Visualize Class Object')
            sys.exit(1)
    
    def plot_3d_map(self):    
        gdf = self.file_handler.read_gdf(self.geoData)
        gdf.crs = "epsg:4326"
        x = gdf.geometry.x
        y = gdf.geometry.y
        z = gdf.elevation
        points = np.vstack((x, y, z)).transpose()
        factor=10
        decimated_points = points[::factor]
        fig, ax = plt.subplots(1, 1, figsize=(12, 10))
        ax = plt.axes(projection='3d')
        ax.scatter(decimated_points[:,0], decimated_points[:,1], decimated_points[:,2],  s=0.01, color="blue")
        plt.savefig('./data/img/plot.png', dpi=300, bbox_inches='tight')
        plt.show()
if(__name__ == '__main__'):
    visulize = Visulaize()
    visulize.plot_3d_map()


