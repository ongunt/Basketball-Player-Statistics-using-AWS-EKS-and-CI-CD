from flask import Blueprint, request


from statistics_engine import distance_and_average_speed, momentan_speed, momentan_relative_velocity,plot_momentan_speed,plot_relative_speed, plot_player_speed_change,momentan_acceleration,player_vertical_acceleration,player_horizontal_acceleration
from serializers import RelativeMeasurementsSerializer, StatsSerializer, PlotSerializer
import preloaded


StatisticsController = Blueprint("current_statistics", __name__)


@StatisticsController.route('/relative_stats', methods=['GET'])
def get_relative_measurements_of_an_user():
    args = request.args
    try:
        player_id1 = int(args.get('player_id1'))
        player_id2 = int(args.get('player_id2'))
    except Exception:
        return None

    df = preloaded.libs.coordinate_data
    relative_measurements = momentan_relative_velocity(player_id1, player_id2, df)
    return_format = RelativeMeasurementsSerializer(main_player_id=player_id1,
                                                   relative_player_id=player_id2,
                                                   all_measured_timestamps=relative_measurements["ts"].tolist(),
                                                   all_measured_speeds=relative_measurements["speed"].tolist(),
                                                   all_measured_velocity_x=relative_measurements["velocity_x"],
                                                   all_measured_velocity_y=relative_measurements["velocity_y"],
                                                   )
    return return_format.dict(by_alias=True)



@StatisticsController.route('/stats', methods=['GET'])
def get_all_stats_of_an_user():
    args = request.args
    try:
        player_id = int(args.get('player_id'))
    except Exception:
        return None

    df = preloaded.libs.coordinate_data
    distance_covered, avg_speed = distance_and_average_speed(player_id, df)
    all_speeds = momentan_speed(player_id, df)
    all_acceleration=momentan_acceleration(player_id,df)
    all_measured_vertical_acceleration=player_vertical_acceleration(player_id,df)
    all_measured_horizontal_acceleration=player_horizontal_acceleration(player_id,df)
    return_format = StatsSerializer(player_id=player_id,
                                    distance_covered=distance_covered,
                                    average_speed=avg_speed,
                                    all_momentary_speed=all_speeds.tolist(),
                                    all_momentary_acceleration=all_acceleration.tolist(),
                                    all_measured_vertical_acceleration=all_measured_vertical_acceleration.tolist(),
                                    all_measured_horizontal_acceleration=all_measured_horizontal_acceleration.tolist())

    return return_format.dict(by_alias=True)


@StatisticsController.route('/relative_speed_plots', methods=['GET'])
def get_relative_speed_plots_of_an_user():
    args = request.args
    try:
        player_id = int(args.get('player_id'))
    except Exception:
        return None

    df = preloaded.libs.coordinate_data

    byte_image=plot_relative_speed(player_id, df)

    return byte_image

@StatisticsController.route('/player_speed_plot', methods=['GET'])
def get_speed_plot_of_an_user():
    args = request.args
    try:
        player_id = int(args.get('player_id'))
    except Exception:
        return None

    df = preloaded.libs.coordinate_data

    byte_image=plot_momentan_speed(player_id, df)

    return byte_image


@StatisticsController.route('/player_acceleration_plot', methods=['GET'])
def get_acceleration_plot_of_an_user():
    args = request.args
    try:
        player_id = int(args.get('player_id'))
    except Exception:
        return None

    df = preloaded.libs.coordinate_data

    byte_image=plot_player_speed_change(player_id, df)

    return byte_image