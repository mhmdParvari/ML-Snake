# Machine Learning Snake
Machine learning implementation of the snake game
  
![c](https://github.com/mhmdParvari/Assignment-6/assets/103634638/7450a490-78b4-45e8-9543-dbf41f534aff)

## Contents
* [Overview](#overview)  
* [Prerequisites](#prerequisites)  
* [Quick run](#quick-run)  
* [Deep dive](#deep-dive)  
  * [Data generation](#data-generation)
  * [Dataset features](#dataset-features)
  * [Model and test](#model-and-test)

## Overview
Creating a snake game using Python and **Arcade** library in which the snake goes for the apple by itself (without user involvement).  
In the meantime data is being collected and later used to construct an Artificial Neural Network model with the help of **TensorFlow** package.  
Then the trained model will be used to guide the snake to its food.

## Prerequisites
This project is written in Python language, so first of all you need to have python installed. (My Python version was 3.8.10)

There are several libraries you also need to have installed. Run the following command line to install the required libraries all at once.
```
pip install -r requirements.txt
```
The above line will install **NumPy, Arcade, Pandas and TensorFlow** on your machine, all of which necessary to run the project.

## Quick run
If you are already familiar with the project and don't want to go through an in-depth analysis, run the following commands in your terminal:  

1. To collect data and create the dataset:
   ```
   python TrainSnake.py
   ```
   *Note 1: Make sure to press `Esc` button to quit the program. Any other method of quiting will result in not creating the dataset.*
   
   *Note 2: The default configuration of this program will create 2 data samples per second.*

2. To build the ANN model:
   ```
   python modelConstruction.py
   ```

3. To observe the result:
   ```
   python TestSnake.py
   ```

## Deep dive

### Data generation
So the rule-based game (`AutomatedSnake.py`) makes the snake move toward the apple on its own. The `TrainSnake.py` is basically the rule-based game but
it collects the feature information over time. So firstly, you must run this file to create the dataset. It will generate 1 data sample
per 0.5 seconds. So forexample if you let it run for 2 minutes, there will be 240 samples in the dataset (which is more than enough).  
Pay attention that for quitting, you must press `Esc`. Otherwise the dataset will not be saved on your computer.

### Dataset features
The data obtained from the previous step will look like this:

<div align="center">
  
| x_diff | y_diff | directions
| ------ | ------ | ---
| 160    | 90     | 2
| 15     | 90     | 2
| 0      | -35    | 1
| -180   | -140   | 0

</div>

There are 2 features:  
The difference between snake's position and apple's position on x and y axis.  

The label is the direction in which the snake is going. Since it can only go to four directions, there are 4 numbers. (0 to 3)
  
![output](https://github.com/mhmdParvari/Assignment-6/assets/103634638/0bd05f7c-51fb-44d5-bad0-cdaeacc93eb1)

The snake will prioritize x axis. Meaning that most of the time it first moves toward the apple on x axis and when their x coordinates are equal (x_diff = 0), 
then it will move through the y axis.

### Model and test
Now with the dataset being available you can run `modeConstruction.py` to build the neural network model.  
To check the validation accuracy of the model you can take a look at `details.ipynb`.  
At the final step run `TestSnake.py` to test the snake's performance.
