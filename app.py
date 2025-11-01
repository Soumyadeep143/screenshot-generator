from flask import Flask, render_template, request, send_from_directory
import requests
import os
import time

app = Flask(__name__)

# API key for ScreenshotBase
API_KEY = os.getenv("SCREENSHOTBASE_API_KEY", "scr_live_DEC7oNEupl5DlQ6fYKI4bF2sVanBZbinRZio8GAY")
SCREENSHOTBASE_BASE_ENDPOINT = "https://api.screenshotbase.com/v1/take"

# Ensure 'static' folder exists for saving screenshots
os.makedirs('static', exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def home():
    screenshot_url = None
    error_message = None

    if request.method == 'POST':
        target_url = request.form.get('url')
        format_ = request.form.get('format', 'png')
        full_page = request.form.get('full_page') == 'on'
        viewport_width = request.form.get('viewport_width', '1280')
        viewport_height = request.form.get('viewport_height', '720')

        if not target_url:
            error_message = "Please enter a valid URL."
            return render_template('index.html', screenshot=None, error=error_message)

        params = {
            "url": target_url,
            "format": format_,
            "full_page": int(full_page),
            "viewport_width": viewport_width,
            "viewport_height": viewport_height
        }
        headers = {"apikey": API_KEY}

        try:
            response = requests.get(SCREENSHOTBASE_BASE_ENDPOINT, params=params, headers=headers, timeout=30)
            response.raise_for_status()

            # Create a unique filename based on timestamp
            timestamp = int(time.time())
            image_extension = format_ if format_ != 'jpeg' else 'jpg'
            image_filename = f'screenshot_{timestamp}.{image_extension}'
            image_path = os.path.join('static', image_filename)

            # Save screenshot to static folder
            with open(image_path, 'wb') as f:
                f.write(response.content)

            screenshot_url = image_filename

        except requests.exceptions.RequestException as e:
            error_message = f"Error capturing screenshot: {e}"

    return render_template('index.html', screenshot=screenshot_url, error=error_message)

@app.route('/static/<filename>')
def serve_screenshot(filename):
    """Serve saved screenshots directly from the static folder."""
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(debug=True)
