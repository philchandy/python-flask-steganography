from flask import Flask, render_template, request, redirect, url_for, send_file, jsonify, send_from_directory
from waitress import serve
from stegwithLSB import hideFileInImage, extractFileFromImage
from io import BytesIO
import os 
from flask_cors import CORS
import base64

app = Flask(__name__, static_folder='../frontend/dist', template_folder='../frontend/dist')  
CORS(app)  


UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/static/<path:path>')
def send_static_files(path):
    return send_from_directory(app.static_folder, path)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    if path and (path.startswith('js') or path.startswith('css') or path.startswith('img')):
        return send_from_directory(app.static_folder, path)
    return render_template('index.html')


@app.route('/api/hide_text', methods=['POST'])
def hide_text():
    if 'image' not in request.files or 'text' not in request.form:
        return jsonify({"error": "No image or text provided"}), 400

    image = request.files['image']
    text_to_hide = request.form['text']

    try:
        output_image = BytesIO()  # Create an in-memory file
        hideFileInImage(image, text_to_hide, output_image)  # Pass the output stream

        output_image.seek(0)  # Rewind the file pointer

        base64_image = base64.b64encode(output_image.read()).decode('utf-8')

        return jsonify({
            "message": "Text hidden successfully!",
            "filename": 'output_image.png',
            "image": base64_image
        }), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500


@app.route('/api/extract_text', methods=['POST'])
def extract_text():
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400

    image = request.files['image']
    try:
        user_length = int(request.form['length'])
        hidden_text = extractFileFromImage(image, user_length)
        return jsonify({"text": hidden_text}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/download_image/<filename>')
def download_image(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    return send_file(file_path, mimetype='image/png', as_attachment=True, download_name=filename)

if __name__ == '__main__':
    try:
        serve(app, host='0.0.0.0', port=3000)
    except Exception as e:
        print(f"An error occurred: {e}", 500)
