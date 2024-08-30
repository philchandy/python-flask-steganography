from flask import Flask, render_template, request, redirect, url_for, send_file
from waitress import serve
from stegwithLSB import hideFileInImage, extractFileFromImage
from io import BytesIO
import os 

app = Flask(__name__)

# Define the upload folder path
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/hide_text', methods=['POST'])
def hide_text():
    if 'image' not in request.files or 'text' not in request.form:
        return "No image or text provided", 400
    
    image = request.files['image']
    text_to_hide = request.form['text']

    try:
        output_image = BytesIO()  # Create an in-memory file
        hideFileInImage(image, text_to_hide, output_image)  # Pass the output stream

        output_image.seek(0)  # Rewind the file pointer

        # Save the output image to the temporary folder
        output_image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'output_image.png')
        with open(output_image_path, 'wb') as f:
            f.write(output_image.read())

        # redirect to download page
        return redirect(url_for('download_page', filename='output_image.png'))

    except Exception as e:
        return f"An error occurred: {e}", 500

# Route to handle extracting text from image
@app.route('/extract_text', methods=['POST'])
def extract_text():
    if 'image' not in request.files:
        return "No image provided", 400
    
    image = request.files['image']
    try:
        user_length = int(request.form['length'])
        hidden_text = extractFileFromImage(image, user_length)
        return render_template('extracted_text.html', text=hidden_text)
    except Exception as e:
        return f"An error occurred: {e}", 500

@app.route('/download/<filename>')
def download_page(filename):
    return render_template('download.html', filename=filename)

@app.route('/download_image/<filename>')
def download_image(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    return send_file(file_path, mimetype='image/png', as_attachment=True, download_name=filename)

if __name__ == '__main__':
    try:
        serve(app, host='0.0.0.0', port=3000)
        
    except Exception as e:
        print(f"An error occurred: {e}", 500)
    