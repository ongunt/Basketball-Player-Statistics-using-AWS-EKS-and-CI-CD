import pandas as pd
import numpy as np
from typing import List, Dict, Any
import io
from flask import Flask, request, jsonify
from flask.logging import create_logger
import logging

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import io

from flask import Flask, send_file, make_response
from math import sqrt



def momentan_speed(player_id: int, df: pd.DataFrame) -> List[float]:
    distance = []
    player_df = df[df["player_id"] == player_id]
    pd.to_datetime(player_df['ts'], unit='ms')
    x = np.array(player_df["x"])
    y = np.array(player_df["y"])
    distance.append(0)
    for i in range(len(x) - 1):
        distance.append(sqrt((x[i] - x[i + 1]) ** 2 + (y[i] - y[i + 1]) ** 2))
    pd.to_datetime(player_df['ts'], unit='ms')
    ts = np.array(player_df["ts"])
    sn = (ts[2] - ts[1]) / 2000
    speed = distance / sn
    return speed
def momentan_acceleration(player_id: int, df: pd.DataFrame) -> List[float]:
    distance = []
    player_df = df[df["player_id"] == player_id]
    pd.to_datetime(player_df['ts'], unit='ms')
    x1= np.array(player_df["x"])
    y1 = np.array(player_df["y"])
    distance.append(0)
    velocity_xm=[]
    velocity_ym=[]
    velocity_xm.append(0)
    velocity_ym.append(0)
    for i in range(len(x1)-1):
        velocity_x=(x1[i]-x1[i+1])
        velocity_y=(y1[i]-y1[i+1])
        velocity_xm.append(velocity_x)
        velocity_ym.append(velocity_y)
        distance.append(sqrt(velocity_x**2+velocity_y**2))

    ts=np.array(player_df["ts"])
    sn=(ts[2]-ts[1])/2000
    speed=distance/sn
    acceleration=np.insert(np.diff(speed),0, 0)
    acceleration_x=np.insert(np.diff(velocity_xm),0, 0)
    acceleration_y=np.insert(np.diff(velocity_ym),0, 0)
    return acceleration
def player_vertical_acceleration(player_id: int, df: pd.DataFrame) -> List[float]:
    distance = []
    player_df = df[df["player_id"] == player_id]
    pd.to_datetime(player_df['ts'], unit='ms')
    x1= np.array(player_df["x"])
    y1 = np.array(player_df["y"])
    distance.append(0)
    velocity_xm=[]
    velocity_ym=[]
    velocity_xm.append(0)
    velocity_ym.append(0)
    for i in range(len(x1)-1):
        velocity_x=(x1[i]-x1[i+1])
        velocity_y=(y1[i]-y1[i+1])
        velocity_xm.append(velocity_x)
        velocity_ym.append(velocity_y)
        distance.append(sqrt(velocity_x**2+velocity_y**2))

    ts=np.array(player_df["ts"])
    sn=(ts[2]-ts[1])/2000
    speed=distance/sn
    acceleration=np.insert(np.diff(speed),0, 0)
    acceleration_x=np.insert(np.diff(velocity_xm),0, 0)
    acceleration_y=np.insert(np.diff(velocity_ym),0, 0)
    return acceleration_y

def player_horizontal_acceleration(player_id: int, df: pd.DataFrame) -> List[float]:
    distance = []
    player_df = df[df["player_id"] == player_id]
    pd.to_datetime(player_df['ts'], unit='ms')
    x1= np.array(player_df["x"])
    y1 = np.array(player_df["y"])
    distance.append(0)
    velocity_xm=[]
    velocity_ym=[]
    velocity_xm.append(0)
    velocity_ym.append(0)
    for i in range(len(x1)-1):
        velocity_x=(x1[i]-x1[i+1])
        velocity_y=(y1[i]-y1[i+1])
        velocity_xm.append(velocity_x)
        velocity_ym.append(velocity_y)
        distance.append(sqrt(velocity_x**2+velocity_y**2))

    ts=np.array(player_df["ts"])
    sn=(ts[2]-ts[1])/2000
    speed=distance/sn
    acceleration=np.insert(np.diff(speed),0, 0)
    acceleration_x=np.insert(np.diff(velocity_xm),0, 0)
    acceleration_y=np.insert(np.diff(velocity_ym),0, 0)
    return acceleration_x




def distance_and_average_speed(player_id: int, df: pd.DataFrame) -> (float, float):
    distance = 0
    player_df = df[df["player_id"] == player_id]
    pd.to_datetime(player_df['ts'], unit='ms')
    x = np.array(player_df["x"])
    y = np.array(player_df["y"])
    for i in range(len(x) - 1):
        distance = distance + sqrt((x[i] - x[i + 1]) ** 2 + (y[i] - y[i + 1]) ** 2)
    ts = np.array(player_df["ts"])
    sn = (ts[-1] - ts[1]) / 2000
    speed = distance / sn
    return distance, speed


def momentan_relative_velocity(player_id1: int, player_id2: int, df: pd.DataFrame) -> Dict[str, Any]:
    distance = []
    player_df1 = df[df["player_id"] == player_id1]
    pd.to_datetime(player_df1['ts'], unit='ms')
    player_df2 = df[df["player_id"] == player_id2]
    pd.to_datetime(player_df2['ts'], unit='ms')
    x1 = np.array(player_df1["x"])
    y1 = np.array(player_df1["y"])
    x2 = np.array(player_df2["x"])
    y2 = np.array(player_df2["y"])
    distance.append(0)
    velocity_xm = []
    velocity_ym = []
    velocity_xm.append(0)
    velocity_ym.append(0)
    for i in range(len(x1) - 1):
        velocity_x = (x1[i] - x1[i + 1]) - (x2[i] - x2[i + 1])
        velocity_y = (y1[i] - y1[i + 1]) - (y2[i] - y2[i + 1])
        velocity_xm.append(velocity_x)
        velocity_ym.append(velocity_y)
        distance.append(sqrt(velocity_x ** 2 + velocity_y ** 2))

    ts = np.array(player_df1["ts"])
    sn = (ts[2] - ts[1]) / 2000
    speed = distance / sn
    data = {"ts": ts,
            "speed": speed,
            "velocity_x": velocity_xm,
            "velocity_y": velocity_ym
            }

    return data

def plot_relative_speed(player_id: int, df: pd.DataFrame):
    # Initialise the subplot function using number of rows and columns
    figure, axis = plt.subplots(2, 5, figsize=(25, 10))
    figure.subplots_adjust(wspace=0.25, hspace=0.4)

    # Combine all the operations and display

    player_df1 = df[df["player_id"] == player_id]
    pd.to_datetime(player_df1['ts'], unit='ms')

    for j in range(10):
        if j < 5:
            distance = []
            player_df2 = df[df["player_id"] == j]
            pd.to_datetime(player_df2['ts'], unit='ms')
            x1 = np.array(player_df1["x"])
            y1 = np.array(player_df1["y"])
            x2 = np.array(player_df2["x"])
            y2 = np.array(player_df2["y"])
            distance.append(0)
            velocity_xm = []
            velocity_ym = []
            velocity_xm.append(0)
            velocity_ym.append(0)
            for i in range(len(x1) - 1):
                velocity_x = (x1[i] - x1[i + 1]) - (x2[i] - x2[i + 1])
                velocity_y = (y1[i] - y1[i + 1]) - (y2[i] - y2[i + 1])
                velocity_xm.append(velocity_x)
                velocity_ym.append(velocity_y)
                distance.append(sqrt(velocity_x ** 2 + velocity_y ** 2))
            ts = np.array(pd.to_datetime(player_df1['ts'], unit='ms'))
            ts = np.array(player_df1["ts"])
            sn = (ts[2] - ts[1]) / 2000
            speed = distance / sn
            ts = np.array(pd.to_datetime(player_df1['ts'], unit='ms'))

            axis[0, j].plot(ts, speed)
            axis[0, j].set_title('Player {}`s relative speed to Player {}'.format(player_id, j))
            axis[0, j].set_xlabel('Time Stamp in ms')
            axis[0, j].set_ylabel('Speed in m/s')
            axis[0, j].tick_params(axis='x', labelrotation=60)
        else:
            distance = []
            player_df2 = df[df["player_id"] == j]
            pd.to_datetime(player_df2['ts'], unit='ms')
            x1 = np.array(player_df1["x"])
            y1 = np.array(player_df1["y"])
            x2 = np.array(player_df2["x"])
            y2 = np.array(player_df2["y"])
            distance.append(0)
            velocity_xm = []
            velocity_ym = []
            velocity_xm.append(0)
            velocity_ym.append(0)
            for i in range(len(x1) - 1):
                velocity_x = (x1[i] - x1[i + 1]) - (x2[i] - x2[i + 1])
                velocity_y = (y1[i] - y1[i + 1]) - (y2[i] - y2[i + 1])
                velocity_xm.append(velocity_x)
                velocity_ym.append(velocity_y)
                distance.append(sqrt(velocity_x ** 2 + velocity_y ** 2))

            ts = np.array(player_df1["ts"])
            sn = (ts[2] - ts[1]) / 2000
            ts = np.array(pd.to_datetime(player_df1['ts'], unit='ms'))
            speed = distance / sn
            # print(speed)
            axis[1, j - 5].plot(ts, speed)
            axis[1, j - 5].set_title('Player {}`s relative speed to Player {}'.format(player_id, j))
            axis[1, j - 5].set_xlabel('Time Stamp in ms')
            axis[1, j - 5].set_ylabel('Speed in m/s')
            axis[1, j - 5].tick_params(axis='x', labelrotation=60)
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)

    return send_file(bytes_image,
        attachment_filename='plot.png',
        mimetype='image/png')

def plot_momentan_speed(player_id: int, df: pd.DataFrame):

    distance = []
    player_df = df[df["player_id"] == player_id]
    pd.to_datetime(player_df['ts'], unit='ms')
    x = np.array(player_df["x"])
    y = np.array(player_df["y"])
    distance.append(0)
    for i in range(len(x) - 1):
        distance.append(sqrt((x[i] - x[i + 1]) ** 2 + (y[i] - y[i + 1]) ** 2))
    pd.to_datetime(player_df['ts'], unit='ms')
    ts = np.array(player_df["ts"])
    sn = (ts[2] - ts[1]) / 2000
    speed = distance / sn
    ts=np.array(pd.to_datetime(player_df['ts'], unit='ms'))
    fig = plt.figure()
    fig.set_size_inches(7.5, 8)
    plt.plot(ts, speed
             )  # plotting by columns

    plt.xlabel('Time Stamp')
    plt.ylabel('Speed in m\s')

    plt.xticks(rotation=60)
    plt.title("Player {} Average Speed".format(player_id))

    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return send_file(bytes_image,
        attachment_filename='plot.png',
        mimetype='image/png')

def plot_player_speed_change(player_id: int, df: pd.DataFrame):
    distance=[]
    player_df1 = df[df["player_id"] ==player_id]
    pd.to_datetime(player_df1['ts'], unit='ms')

    x1=np.array(player_df1["x"])
    y1=np.array(player_df1["y"])

    distance.append(0)
    velocity_xm=[]
    velocity_ym=[]
    velocity_xm.append(0)
    velocity_ym.append(0)
    for i in range(len(x1)-1):
        velocity_x=(x1[i]-x1[i+1])
        velocity_y=(y1[i]-y1[i+1])
        velocity_xm.append(velocity_x)
        velocity_ym.append(velocity_y)
        distance.append(sqrt(velocity_x**2+velocity_y**2))

    ts=np.array(player_df1["ts"])
    sn=(ts[2]-ts[1])/2000
    speed=distance/sn
    acceleration=np.insert(np.diff(speed),0, 0)
    acceleration_x=np.insert(np.diff(velocity_xm),0, 0)
    acceleration_y=np.insert(np.diff(velocity_ym),0, 0)
    sn=(ts[2]-ts[1])/2000
    ts=np.array(pd.to_datetime(player_df1['ts'], unit='ms'))
    data = {"ts": ts,
      "acceleration": acceleration,
        "acceleration_x": acceleration_x,
        "acceleration_y": acceleration_y

    }

    figure, axis = plt.subplots(3,figsize=(10,20))
    figure.subplots_adjust( wspace=0.25,hspace=0.4)
    axis[0].plot(ts,acceleration)
    axis[0].set_title('Player {}`s Acceleration'.format(player_id))
    axis[0].set_xlabel('Time Stamp in ms')
    axis[0].set_ylabel('Speed in m/s')
    axis[1].plot(ts,acceleration_x)
    axis[1].set_title('Player {}`s Horizontal Speed Change'.format(player_id))
    axis[1].set_xlabel('Time Stamp in ms')
    axis[1].set_ylabel('Speed in m/s')
    axis[2].plot(ts,acceleration_y)
    axis[2].set_title('Player {}`s Vertical Speed Change'.format(player_id))
    axis[2].set_xlabel('Time Stamp')
    axis[2].set_ylabel('Speed in m/s')

    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return send_file(bytes_image,
        attachment_filename='plot.png',
        mimetype='image/png')
