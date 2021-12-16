import cv2
from keras.models import load_model

MODEL_PATH = r"C:\Users\abzku\Desktop\Project_DiabeticRetinopathy\project_diabetic\CPG-105\src\static\modelsave.h5"
PREDICTIONS = ['Normal', 'Mild', 'Moderate', 'Severe', 'Proliferate DR']
sigmaX = 10


def predict(imagePath: str):
    # PREPROCCESSED IMAGE
    image = cv2.imread(imagePath)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.addWeighted(image, 4, cv2.GaussianBlur(image, (0, 0), sigmaX), -4, 128)
    pre_image = imagePath.split(".")
    pre_image = pre_image[0] + "__pre." + pre_image[1]
    cv2.imwrite(pre_image, image)

    # OUTPUT OF MODEL
    model = load_model(MODEL_PATH, compile=True)
    img = cv2.imread(imagePath)
    img = cv2.resize(img, (128, 128), interpolation=cv2.INTER_AREA)
    img = img.reshape(1, 128, 128, 3)  # This Step needs to be done !! Reshaping was not perfect..
    prediction = model.predict(img)
    prediction = prediction.tolist()
    return PREDICTIONS[prediction[0].index(1.0)]
