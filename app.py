from flask import Flask, render_template, request
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/capture', methods=['POST'])
def capture():
    image_data = request.form['image']
    image_data = image_data.replace("data:image/png;base64,", "")
    image_data = base64.b64decode(image_data)

    # Save the image to a file (optional)
    with open('captured_image.png', 'wb') as f:
        f.write(image_data)

    # Get the coordinates of the click
    x = request.form['x']
    y = request.form['y']

    return f'Clicked at ({x}, {y})'
 
if __name__ == '__main__':
    app.run(debug=True)
