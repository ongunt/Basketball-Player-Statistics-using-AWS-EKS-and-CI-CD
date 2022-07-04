from typing import List

from pydantic import BaseModel, Field


class RelativeMeasurementsSerializer(BaseModel):
    main_player_id: int = Field(None, alias="main_player_id")
    relative_player_id: int = Field(None, alias="relative_player_id")
    all_measured_timestamps: List[int] = Field([], alias='all_timestamps')
    all_measured_speeds: List[float] = Field([], alias='all_relative_speeds in m\s')
    all_measured_velocity_x: List[float] = Field([], alias='all_relative_velocity_x')
    all_measured_velocity_y: List[float] = Field([], alias='all_relative_velocity_y')
    class Config:
        allow_population_by_field_name = True


class StatsSerializer(BaseModel):
    player_id: int = Field(None, alias="player_id")
    distance_covered: float = Field(None, alias="distance covered in m")
    average_speed: float = Field(None, alias="average_speed in m per s")
    all_momentary_speed: List[float] = Field([], alias="all_momentary_speed in m\s")
    all_momentary_acceleration: List[float] = Field([], alias="all_momentary_acceleration")
    all_measured_horizontal_acceleration: List[float] = Field([], alias='all_measured_horizontal_acceleration')
    all_measured_vertical_acceleration: List[float] = Field([], alias='all_measured_vertical_acceleration')
    class Config:
        allow_population_by_field_name = True

class PlotSerializer(BaseModel):
    player_id: int = Field(None, alias="player_id")
    byte_image: float = Field(None, alias="byte_image")

    class Config:
        allow_population_by_field_name = True