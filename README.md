# **Realtime face-distance detector**
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

This project helps you to find the distance between a face and a normal webcam.Also, it changes the text-size on other screen in-response to the distance.
### How to run?
- Install the required python packages
```sh 
pip install -r requirements.txt
```
- run the file 
```sh 
python main.py
```
- if your pc has multiple camera's you can switch them by changing the index of Video Capture
```py
cap = cv2.VideoCapture(index)
# changed the index here (default set to =0)
```
