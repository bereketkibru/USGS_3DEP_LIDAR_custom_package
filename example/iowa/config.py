from pathlib import Path


class Config:
  RANDOM_SEED = 27
  ROOT_PATH = Path("./")
  REPO = "https://github.com/bereketkibru/USGS_3DEP_LIDAR_custom_package.git"
  LOG_FILE = ROOT_PATH / "log/3deplog.log"
  DATA_PATH = ROOT_PATH / "data/"
  ASSETS_PATH = ROOT_PATH / "assets/"
  LAZ_PATH = DATA_PATH / "laz"
  TIF_PATH = DATA_PATH / "tif"
  SHP_PATH = DATA_PATH / "shp"
  IMG_PATH = DATA_PATH / "img"