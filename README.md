# OBJECT_DETECTOR
Object Detection System using ImageAI and YOLOv3. A Python project for real-time and static image analysis, capable of identifying and localizing over 80 common objects (e.g., people, cars).
This project takes an input image and outputs a new image with bounding boxes drawn around detected objects, along with their names and probability percentages.

🚀 Getting Started
Prerequisites
To run this project, you need Python 3.x and a few dependencies.

Python: Ensure you have Python installed.

Virtual Environment (Recommended): Use a virtual environment to manage dependencies:

Bash

# Create the environment
python -m venv .venv

# Activate the environment (on Windows PowerShell)
.\.venv\Scripts\Activate
Installation
Once your virtual environment is active, install the necessary libraries:

Bash

pip install imageai==2.1.6
pip install tensorflow==2.4.0
pip install numpy
Model Files
This project requires the pre-trained YOLOv3 model file (yolov3.pt).

Download the model: Get the YOLOv3 model file. (Note: You may need to search for the exact model file required by ImageAI 2.1.6, which is typically a .pt or .h5 file, and place it in your project root directory.)

File Naming: Ensure the downloaded model file is named yolov3.pt (or whatever name you use in your script).

🛠 Usage
Project Structure
Your project directory should look something like this:

object_detector/
├── .venv/                   # Python virtual environment
├── your_script.py           # The main execution script
├── img.jpeg                 # Input image file
├── yolov3.pt                # The pre-trained model file
└── README.md
Running the Detector
Execute your main Python script from the terminal:

Bash

python your_script.py
Output
The script will perform the following actions:

Load the yolov3.pt model.

Detect objects in the input image img.jpeg.

Save the results to a new image file named imagenew.jpeg.

Print the detected objects and their probabilities to the console.

Console Output Example:

name: car, percentage_probability: 98.75
name: person, percentage_probability: 92.11
⚙️ Customization
You can easily change the input and output files by modifying lines 11 and 12 of your_script.py:

Python

# Change the input file name:
input_image_os_path.join(execution_path, "your_new_input.jpg"),

# Change the output file name:
output_image_path_os_path.join(execution_path, "output_results.jpg")
🤝 Contributing
If you have suggestions or improvements, feel free to fork the repository and create a pull request!

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

📄 License
Distributed under the MIT License. See LICENSE for more information.

Built with Python and ImageAI.
