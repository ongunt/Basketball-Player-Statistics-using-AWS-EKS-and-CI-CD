from flask import Flask, request, jsonify
from flask.logging import create_logger
import logging
# import joblib
import pandas as pd
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import io
from sklearn.preprocessing import StandardScaler
from flask import Flask, request, jsonify
from flask.logging import create_logger
from flask import Flask, send_file, make_response
from math import sqrt


app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)



@app.route('/api/v1/player_speed/<int:player_id>/', methods=['GET'])

def plot_momentan_speed(player_id):
    df = pd.read_csv("positions (1).csv", delimiter=',')
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
@app.route('/api/v1/distance/<int:player_id>/', methods=['GET'])
def distance(player_id):

    df = pd.read_csv("positions (1).csv", delimiter=',')
    distance=0
    player_df = df[df["player_id"] ==player_id]
    pd.to_datetime(player_df['ts'], unit='ms')
    x=np.array(player_df["x"])
    y=np.array(player_df["y"])
    for i in range(len(x)-1):
        distance=distance+sqrt((x[i]-x[i+1])**2+(y[i]-y[i+1])**2)
    ts=np.array(player_df["ts"])
    sn=(ts[-1]-ts[1])/2000
    speed=distance/sn
    return "Distance covered by the player "+str(player_id)+": "+str(distance)+"meters in "+str(sn)+"Average speed of the player " + str(player_id) + ": " + str(speed)+"m/s"
@app.route('/relative_speed/<int:player_id>/', methods=['GET'])
def plot_relative_speed(player_id):
    # Initialise the subplot function using number of rows and columns
    figure, axis = plt.subplots(2, 5, figsize=(25, 10))
    figure.subplots_adjust(wspace=0.25, hspace=0.4)

    # Combine all the operations and display
    df = pd.read_csv("positions (1).csv", delimiter=',')
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


@app.route("/predict_speed/<int:player_id>/", methods=['GET'])
# def predict():
#     # Logging the input payload
#     json_payload = request.json
#     LOG.info(f"JSON payload: \n{json_payload}")
#     inference_payload = pd.DataFrame(json_payload)
#     LOG.info(f"Inference payload DataFrame: \n{inference_payload}")
#     # scale the input
#     scaled_payload = scale(inference_payload)
#     # get an output prediction from the pretrained model, clf
#     prediction = list(clf.predict(scaled_payload))
#     # TO DO:  Log the output prediction value
#     return jsonify({'prediction': prediction})
def predict(player_id):
    # Logging the input payload
    clf = joblib.load("forecaster_player {}.joblib".format(player_id))



    # get an output prediction from the pretrained model, clf
    prediction = list(clf.predict(steps=100))
    # TO DO:  Log the output prediction value

    plt.plot(prediction
             )  # plotting by columns
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return send_file(bytes_image,
        attachment_filename='plot.png',
        mimetype='image/png')


if __name__ == "__main__":
    # load pretrained model as clf
    app.run(host='0.0.0.0', port=5050, debug=True)  # specify port=80
