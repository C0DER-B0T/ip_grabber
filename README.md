🌐 IP Grabber & GeoLocator

A Flask-based tool to capture and log visitors' IP addresses and geolocation data using both browser geolocation (GPS) and IP-based lookup. It stores results in a log file for easy tracking and analysis.

🚀 Features

📍 Get accurate geolocation using browser-based GPS (if allowed)

🌐 Fallback to IP-based location using ip-api.com

📦 Reverse geocoding with OpenStreetMap's Nominatim

🧠 Logs detailed location data including IP, city, region, country, ZIP, ISP

📝 Stores all logs in ip_log.txt with UTC timestamps

🧪 Minimal, script-based deployment (no frontend frameworks)

📂 Project Structure

ip_grabber.py         # Main Flask app
ip_log.txt            # Output log file (auto-created)

⚙️ Requirements

Python 3.6+

Flask

Requests

Install with:

pip install flask requests

🧪 Usage

Run the server:

python ip_grabber.py

Access the tracker page:

Visit: http://localhost:5000/track

View logs:

All captured data is saved in ip_log.txt in JSON format with timestamps.

📄 Example Log Output

2025-04-25 18:23:45 UTC {"ip": "123.45.67.89", "method": "ip-api", "country": "USA", "region": "California", "city": "Los Angeles", "zip": "90001", "isp": "Comcast"}

Or when browser geolocation is available:

2025-04-25 18:25:01 UTC {"ip": "123.45.67.89", "method": "browser-geolocation", "coords": {"lat": 34.0522, "lon": -118.2437, "accuracy": 20}, "location": "Los Angeles, California, USA"}

⚠️ Disclaimer

This project is intended for educational and ethical purposes only. Do not use this script without clear consent from users. Always follow privacy and data protection laws.

📬 Contact

For issues, suggestions, or contributions, feel free to open an issue or pull request.

