from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsYOLOv3() # This line specifies the model type
detector.setModelPath(os.path.join(execution_path, "yolov3.pt")) # This line sets the path to the model file
detector.loadModel()

detections = detector.detectObjectsFromImage(
    input_image=os.path.join(execution_path, "img.jpeg"),
    output_image_path=os.path.join(execution_path, "imagenew.jpeg")
)

for eachObject in detections:
    print(eachObject["name"], " : ", eachObject["percentage_probability"])