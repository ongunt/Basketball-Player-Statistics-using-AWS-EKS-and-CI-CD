from os import environ


class Config:
    DEBUG = False
    PRODUCTION = False
    TESTING = True

    data_location = environ.get('Coordinate_Data_Location', "positions (1).csv")
