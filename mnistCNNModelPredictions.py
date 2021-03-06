# Importing the Keras libraries and packages
import numpy as np
from tensorflow.keras.models import load_model
model = load_model('models/mnist-CNN.h5')

from PIL import Image
import numpy as np

for index in range(10):
    img = Image.open('./data/' + str(index) + '.png').convert("L")
    img = img.resize((28,28))
    im2arr = np.array(img)
    im2arr = im2arr.reshape(1,28,28,1)
    # Predicting the Test set results
    y_pred = np.argmax(model.predict(im2arr), axis=-1)
    print(y_pred)
