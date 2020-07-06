from flask import Flask, jsonify, request, send_file, send_from_directory
from flask_cors import CORS
from utils import download_video, info_video
import config

app = Flask(__name__, static_url_path='', static_folder='public')

if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")

    # Use built files on production
    @app.errorhandler(404)
    def catch_all(err):
        return send_file("./public/index.html")

else:
    app.config.from_object("config.DevelopmentConfig")

CORS(app, resources={r'/api/*': {'origins': '*'}})

# API route for downloading Youtube video
@app.route('/api/download/', defaults={'video_id': None}, methods=['GET'])
@app.route('/api/download/<video_id>/', methods=['GET'])
def download(video_id):
    if video_id is not None:
        streams = download_video(video_id)

        # If function returned dict with key "error"
        if "error" in streams:
            return jsonify(streams), 400
        else:
            return jsonify(streams)
    else:
        error = {
            "error": "Missing video_id parameter"
        }
        return jsonify(error)

# API route for retrieving info on Youtube video
@app.route('/api/info/', defaults={'video_id': None}, methods=['GET'])
@app.route('/api/info/<video_id>/', methods=['GET'])
def info(video_id):
    if video_id is not None:
        info = info_video(video_id)
        if "error" in info:
            return jsonify(info), 400
        else:
            return jsonify(info)
    else:
        error = {
            "error": "Missing video_id parameter"
        }
        return jsonify(error), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0')
