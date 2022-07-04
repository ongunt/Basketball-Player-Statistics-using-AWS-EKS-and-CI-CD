import logging
from config import Config
from types import SimpleNamespace

import pandas as pd


logger = logging.getLogger('statistics_engine')

libs = None


def init():
    global libs
    libs = SimpleNamespace()

    # logger.info("Setting up cache...")
    libs.responses_cache = {}
    libs.responses_cache_hits_count = 0

    libs.coordinate_data = pd.read_csv(Config.data_location)
