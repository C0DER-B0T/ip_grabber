# 🌐 IP Grabber & GeoLocator Tool

A Flask-based application that captures visitors' IP addresses and geolocation data using either browser geolocation (if permitted) or IP-based lookup. Also includes a sneaky HTML trick to **embed invisible tracking links over images**.

---

## 📦 Features

- 🌍 **IP Tracking**: Fetches and logs user's IP and related location info (city, region, ISP).
- 📌 **Browser Geolocation**: Uses browser GPS for more accurate coordinates (if user allows).
- 🗺 **Reverse Geocoding**: Converts coordinates into a readable location using OpenStreetMap.
- 🖼 **Image with Invisible Link**: A stealthy HTML `Image.html` that places an invisible `<a>` link over any image.
- 📝 **Logging**: All data is saved to `ip_log.txt` with proper UTC timestamps.
- 📁 **Standalone Assets**:
  - `ip_grabber.py`: Flask server
  - `Image.html`: Embeds tracker over image
  - `your_image.jpg`: Can be any image for camouflage
  - `ip_log.txt`: Stores all tracking logs

---

## 🔍 How the Invisible Link Works

The `Image.html` file creates a transparent clickable layer over an image:

```html
<div class="image-container">
  <img src="your-image.jpg" alt="Descriptive text" />
  <a href="http://<your-ip>:5000/track" target="_blank">Invisible Link</a>
</div>
```

- The `<a>` tag stretches to cover the full image.
- The link silently redirects to `/track` route, triggering the logging mechanism.
- Useful for stealthy demonstrations or educational awareness.

> ⚠️ **Disclaimer**: For ethical and educational use only. Never track users without informed consent.

---

## ⚙️ Setup Instructions

1. Install dependencies:

```bash
pip install flask requests
```

2. Run the Flask app:

```bash
python ip_grabber.py
```

3. Serve the `Image.html` file on any static file host or embed in your webpage.

---

## 🧪 Example Log Output (ip_log.txt)

```json
2025-04-26 10:22:11 UTC {"ip": "111.222.3.44", "method": "ip-api", "country": "India", "region": "Delhi", "city": "New Delhi", "zip": "110001", "isp": "Airtel"}
```

Or using GPS:

```json
2025-04-26 10:23:11 UTC {"ip": "111.222.3.44", "method": "browser-geolocation", "coords": {"lat": 28.6139, "lon": 77.2090}, "location": "New Delhi, India"}
```

---

## 📁 Files Description

| File           | Description                                   |
|----------------|-----------------------------------------------|
| `ip_grabber.py`| Flask app to track and log IP/geolocation     |
| `Image.html`   | Image overlay with invisible tracking link     |
| `your_image.jpg` | Used as a disguise for invisible tracking   |
| `ip_log.txt`   | Output log file for all geolocation records    |

---

## ⚠️ Ethical Use Notice

This tool is for **learning and awareness only**. Respect privacy and comply with local data protection regulations. Do not deploy this without user knowledge and consent.

---

## 🤝 Contributing

Feel free to fork, improve, or suggest enhancements.

---

Need this exported as a `README.md` file or want GitHub Actions/Badge setup as well?
