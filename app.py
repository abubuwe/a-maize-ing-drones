from flask import Flask, render_template
import os, random, io, base64
import numpy as np
from controller import predict_image

from PIL import Image

BASE_SRC = "static/dataset/"

# Returns a the filepath to a random image
def random_image_src():
    random_folder = os.path.join(BASE_SRC, random.choice(os.listdir(BASE_SRC)))
    random_image = os.path.join(random_folder, random.choice(os.listdir(random_folder)))
    return random_image

app = Flask(__name__)
app.debug = True
classes = ['broadleaf', 'grass', 'soil', 'soybean'] 

@app.route('/')
@app.route('/index')
def show_index():
        full_filename = random_image_src()

        (full_filename)

        img = Image.open(full_filename)

        pr, a = predict_image(full_filename)

        pr = list(map(abs, pr))
        preds = np.random.choice(range(4), p = [x/sum(pr) for x in pr])

        # Convert plot to PNG image
        data = io.BytesIO()
        img.save(data, "JPEG")
        encoded_img_data = base64.b64encode(data.getvalue())

        print(preds, a)

        return render_template("index.html", user_image = encoded_img_data.decode('utf-8'), pred = classes[int(preds)], actual = classes[int(a)])

if __name__ == "__main__":
    app.run(debug=True)