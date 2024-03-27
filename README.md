
# HL-LHC Detector Test Data Visualization

This web application is built using the Dash framework to visualize test data conducted on detector modules for the High-Luminosity Large Hadron Collider (HL-LHC) project. It provides three main features:

1. **Data Visualization**: Display visualizations of tests performed on detector modules which are planned to be used for the HL-LHC project. The visualizations include a variety of different experiments conducted on the silicon strip detectors like: IV Test, Strobe Delay, Noise as a function of channel, etc... 

2. **Comparison of Test Data**: Compare data from different tests or detector modules within a single run. Users can easily compare various parameters and metrics to analyze the performance and characteristics of the detector module. Only certain tests are compared with each other such as the VT50, gain and intrinsic noise of the system, all as a function of channel.

3. **Automatic Directory Scanning**: The website automatically scans a specified directory where new test runs are completed and uploaded. Once new data is detected, it is incorporated into the website, allowing users to access the latest test results without manual intervention.

## Motivation

- **Repository**: This web page hopes to serve as a central repository for all data that is collected from the runs conducted on the modules. All to be served on this local webpage. Giving the UoB particle physics team a place to easily access the data. 
  
- **Data Comparison**: This feature serves the important process of identifying any 
  
- **Automatic Updates**: The web application continuously scans a designated directory for new test data. Once new data is available, it is automatically incorporated into the website, ensuring that users always have access to the latest test results.

## Usage

To use the web application:

1. Clone this repository to your local machine.
   
2. Install the required dependencies by running:
   
   - uproot 
   - Flask
   - dash
   - pickle 
   - 
3. For it to run successfully on the local PC, all that is needed to be changed to the code is the directory of 


