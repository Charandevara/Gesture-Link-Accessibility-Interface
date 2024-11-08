

## Installation

To install GLAI and its associated features, follow these steps:

1. Clone the repository to your local machine: 
2. Navigate to the project directory:
   ```
   cd glai
   ```

3. Install the required Python modules for each feature using pip. Ensure that you navigate to the appropriate subdirectory containing the feature you want to use, and install the dependencies accordingly. For example:
   ```
   cd gesture_control
   pip install -r requirements.txt
   ```
   Repeat this step for each feature directory (e.g., multimedia_control, digital_canvas, LED_control, etc.) to install the necessary modules specific to each feature.

4. Ensure that the paths in each Python file are configured correctly based on the required location of the Python files. Update the paths as necessary to reflect the file structure of your project.

5. For features like CRUZZ multimedia control, ensure that your system setup allows for hand detection and recognition of specific hand gestures required for controlling multimedia functions.

6. For the digital canvas feature, ensure that the hand gestures for drawing and stopping drawing are properly implemented. Two-finger touch should stop drawing, while single-finger movement should initiate drawing.

7. LED control feature requires an Arduino Uno and LEDs hardware kit. Check the PIN numbers and ensure they are connected based on the COM pin value specified in the code.

8. Voice commands integration should be configured and tested according to the specific commands and functionalities you want to implement.

9. Virtual keyboard and virtual mouse features should have a similar mechanism using hand fingers. Ensure that the hand gestures for keyboard input and mouse control are implemented correctly.

10. Follow the configuration guide in each feature directory to customize GLAI based on your specific requirements and hardware setup.

---

By following these steps, users can install and configure GLAI and its associated features according to their requirements and hardware setup. Ensure that each feature is configured properly and the necessary dependencies are installed to enable seamless integration and functionality.
