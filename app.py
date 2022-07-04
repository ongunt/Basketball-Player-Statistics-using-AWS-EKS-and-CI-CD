

from flask import Flask


from controllers import StatisticsController



app = Flask(__name__)
import preloaded
preloaded.init()

app.register_blueprint(StatisticsController)

app.run(host='0.0.0.0', port=80, debug=True)
