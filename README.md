# Streaming EEG Data OSC Receiver, MUSE

This project sets up a Python server to receive and log brainwave data streamed via Open Sound Control (OSC) protocol used by [**MUSE**](https://choosemuse.com/) (need to purchase [**Mind Monitor**](https://apps.apple.com/us/app/mind-monitor/id988527143) App on your ios device). The data is captured from a brain-sensing headset and stored in a structured CSV file for further analysis.

## Requirements
Install the required Python libraries:
```
pip install -r requirements.txt
```
## Usage
1. wear the muse headset, turn it on:
    * setup Mind Monitor, follow instructions to pair headset with device.
    * enable streaming from the interactive tab at the bottom.
    * take note of the **address ip** and **port** used.

2 Run the OSC Server:
```
python3 listen.py <address_ip> <port>
```

## Data Structure recieved
The following columns are streamed to stream_data.csv and the streamed data needs to be organized by addressing the columns below:

* TimeStamp: Time of data reception.
* Delta_TP9, Delta_AF7, Delta_AF8, Delta_TP10
* Theta_TP9, Theta_AF7, Theta_AF8, Theta_TP10
* Alpha_TP9, Alpha_AF7, Alpha_AF8, Alpha_TP10
* Beta_TP9, Beta_AF7, Beta_AF8, Beta_TP10
* Gamma_TP9, Gamma_AF7, Gamma_AF8, Gamma_TP10
* RAW_TP9, RAW_AF7, RAW_AF8, RAW_TP10
* AUX_RIGHT, AUX_LEFT
* Accelerometer_X, Accelerometer_Y, Accelerometer_Z
* Gyro_X, Gyro_Y, Gyro_Z
* HeadBandOn, HSI_TP9, HSI_AF7, HSI_AF8, HSI_TP10
* Battery, Elements

## TODOS

1. organize streamed data
2. figure out whats next (interpret the data)