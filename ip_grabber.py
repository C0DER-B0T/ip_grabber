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
    app.run(host='0.0.0.0', port=5000)