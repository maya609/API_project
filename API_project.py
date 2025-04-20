from flask import Flask, request, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)
API_TOKEN = "supersecrettoken123"

# Capital city to timezone mapping
capital_timezones = {
    "Washington": "America/New_York",
    "London": "Europe/London",
    "Tokyo": "Asia/Tokyo",
    "Paris": "Europe/Paris",
    "New Delhi": "Asia/Kolkata",
    "Canberra": "Australia/Sydney",
    "Ottawa": "America/Toronto",
    "Beijing": "Asia/Shanghai"
}

def token_required(f):
    def decorator(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]
            if token == API_TOKEN:
                return f(*args, **kwargs)
        return jsonify({"error": "Unauthorized"}), 401
    decorator.__name__ = f.__name__
    return decorator

@app.route('/api/time', methods=['GET'])
@token_required
def get_local_time():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "Missing city parameter"}), 400

    timezone_name = capital_timezones.get(city)
    if not timezone_name:
        return jsonify({"error": f"{city} not found in database"}), 404

    tz = pytz.timezone(timezone_name)
    now = datetime.now(tz)
    offset = now.strftime('%z')
    offset_formatted = f"UTC{'+' if int(offset) >= 0 else ''}{int(offset)//100}"

    return jsonify({
        "city": city,
        "local_time": now.strftime("%Y-%m-%d %H:%M:%S"),
        "utc_offset": offset_formatted
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
