# Real-Time Object Detection for Advanced Driver Assistance Systems Using YOLOv3

This repository contains a report and code related to the implementation of real-time object detection techniques using YOLOv3 for Advanced Driver Assistance Systems (ADAS).

#### Tasks Covered:
- Video processing with FFmpeg for format conversion
- Video display and frame extraction using OpenCV
- Object detection and labeling from video frames
- Integration with YOLOv3 for real-time object detection using `darknet`

![YOLOV3e](./rep/images/Figure%202.png)


## Report

The report `Real-Time Object Detection for Advanced Driver Assistance Systems that Uses YOLOv3`  explores the performance of YOLOv3 on driving videos from the BDD100K dataset and discusses its implications for enhancing road safety in autonomous vehicles.

- `Report.pdf`: LATEX built report.

## Code

The code for object detection using YOLOv3 is available in two formats:

- `YOLO.ipynb`: Jupyter Notebook implementation.
- `yolo.py`: Python script version of the same code.

## Additional Resources

- **Datasets**: The BDD100K dataset was used for training and evaluation.
- **Dependencies**: Ensure you have Python, OpenCV, FFmpeg, and `darknet` installed.
- **Multi Object Traking Lables**: Download `mot_lables.csv` from [Kaggle Dataset](https://www.kaggle.com/datasets/robikscube/driving-video-with-object-tracking/data?select=bdd100k_videos_train_00) and place it in `src\data\`

Feel free to explore and modify the provided code for your specific use case or research purposes.

For any questions or feedback, please contact:
- Roman Guerra: rguerra6@cougarnet.uh.edu
   - GitHub: [RomanGuerra](https://github.com/RomanGuerra)