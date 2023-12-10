# Health-Care-Application
Capstone project using Random Forest classifier we have build a disease prediction, Flask for front end , Putty and AWS for Backend.
# Health Prediction Models Deployment

## Overview

This repository contains machine learning models for predicting health conditions such as breast cancer, diabetes, heart disease, liver disease, and chronic kidney disease. The models have been implemented using the scikit-learn library in Python and deployed using Flask on an Amazon EC2 instance.

## Table of Contents

1. [Datasets](#datasets)
2. [Machine Learning Models](#machine-learning-models)
3. [Flask Web Application](#flask-web-application)
4. [Requirements](#requirements)
5. [Usage](#usage)
6. [Making Predictions](#making-predictions)
7. [Web Application Screens](#web-application-screens)
8. [References](#references)

## Datasets

The `data` folder contains the datasets used for training and testing the machine learning models. Each dataset corresponds to a specific health condition.

## Machine Learning Models

The `models` folder contains the trained machine learning models in the form of pickle files (`*.pkl`). There is one model for each health condition: breast cancer (`cancer_model.pkl`), diabetes (`diabetes_model.pkl`), heart disease (`heart_model.pkl`), liver disease (`liver_model.pkl`), and chronic kidney disease (`kidney_model.pkl`).

## Flask Web Application

The `app` folder contains the Flask web application for deploying and interacting with the machine learning models. The web application allows users to input relevant health features and receive predictions for the respective health conditions.

## Requirements

The `requirements.txt` file lists all the necessary Python packages and dependencies required to run the application. You can install these dependencies using the command `pip install -r requirements.txt`.

## Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/health-prediction.git
