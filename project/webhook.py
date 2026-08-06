from flask import Flask, request, jsonify

from utils.helpers import (
    log_info,
    log_error
)

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():

    try:

        data = request.json

        log_info(data)

        return jsonify({
            "success": True
        })

    except Exception as e:

        log_error(str(e))

        return jsonify({
            "success": False
        }), 500

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )
