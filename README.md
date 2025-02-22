# Project Setup Instructions

This document outlines the steps to set up and run the project.

## 1. Install Dependencies

First, install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

# 2. Running the Flask Application and Tester

To run the Flask application and the device tester, follow these steps:

1.  **Identify the COM Port:**
    * Open your device manager to find the COM port associated with your device.
2.  **Start the Flask Application:**
    * Run the Flask application:
        ```bash
        python app.py
        ```
3.  **Run the Device Tester:**
    * Open your device manager to find the COM port associated with your device.
    * Replace `<COM?>` with the actual COM port number you identified.
    * Execute the device tester using `ampy`:
        ```bash
        ampy --port <COM?> run tester.py
        ```
## 3. Sending Data to Ubidots

To send data to Ubidots, ensure you have completed the following:

1.  **Ubidots Setup:**
    * Create an account on Ubidots.
    * Set up your variables and devices in your Ubidots account.
2.  **Token Configuration:**
    * Open the `SendToUbidots.py` file.
    * Replace the placeholder with your valid SSID, password, and Ubidots API token.
3.  **Identify the COM Port:**
    * Open your device manager to find the COM port associated with your device.
4.  **Run the Ubidots Script:**
    * Replace `<COM?>` with the actual COM port number you identified.
    * Execute the script using `ampy`:
        ```bash
        ampy --port <COM?> run SendToUbidots.py
        ```

