import logging, time, random
from flask import Flask, jsonify

app = Flask(__name__)

# configure root logger
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s %(message)s')
handler.setFormatter(formatter)
root = logging.getLogger()
root.setLevel(logging.INFO)
root.addHandler(handler)

@app.route("/")
def home():
    app.logger.info("home endpoint hit")
    return jsonify(message="Hello — EFK demo!")

@app.route("/work")
def work():
    ms = random.randint(50, 300)
    app.logger.info("work endpoint start - sleeping %dms", ms)
    time.sleep(ms / 1000.0)
    app.logger.info("work endpoint end")
    return jsonify(status="done", slept_ms=ms)

@app.route("/error")
def error():
    try:
        1 / 0
    except Exception as e:
        app.logger.exception("simulated exception")
        return jsonify(error=str(e)), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

