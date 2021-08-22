import json
import laspy
import pandas as pd
import geopandas as gpd
from config import Config
from logger import get_logger


class FileHandler():

  def __init__(self):
    self._logger = get_logger("FileHandler")

  def save_csv(self, df, name, index=False):
    try:
      path = Config.ASSETS_PATH / str(name + '.csv')
      df.to_csv(path, index=index)
      self._logger.info(f"{name} is saved successfully in csv format")
    except Exception:
      self._logger.exception(f"{name} save failed")

  def read_csv(self, name, missing_values=[]):
    try:
      path = Config.ASSETS_PATH / str(name + '.csv')
      df = pd.read_csv(path, na_values=missing_values)
      self._logger.info(f"{name} read successfully")
      return df
    except FileNotFoundError:
      self._logger.exception(f"{name} not found")

  def read_gdf(self, name):
    try:
      self._logger.info(f"{name} start reading")
      path = Config.GEO_PATH / str(name + '.geojson')
      df = gpd.read_file(path)
      self._logger.info(f"{name} read successfully")
      return df
    except FileNotFoundError:
      self._logger.exception(f"{name} not found")

  def read_json(self, name):
    try:
      path = Config.ASSETS_PATH / str(name + '.json')
      with open(path, 'r') as json_file:
        json_obj = json.load(json_file)
      self._logger.info(f"{name} read successfully")
      return json_obj
    except Exception:
      self._logger.exception(f"{name} not found")

  def read_txt(self, name):
    try:
      path = Config.ASSETS_PATH / str(name + '.txt')
      with open(path, "r") as f:
        text_file = f.read().splitlines()
      self._logger.info(f"{name} read successfully")
      return text_file
    except Exception:
      self._logger.exception(f"{name} not found")

  def read_point_data(self, name) -> dict:
    try:
      path = Config.LAZ_PATH / str(name + '.laz')
      print(path)
      las = laspy.read(path)
      self._logger.info(f"{name} read successfully")
      return las
    except Exception:
      self._logger.exception(f"{name} not found")
  def save_shp(self, df, name, index=False):
    try:
      path = Config.SHP_PATH / str(name + '.shp')
      gpd.to_file(path)
      self._logger.info(f"{name} is saved successfully in csv format")
    except Exception:
      self._logger.exception(f"{name} save failed")