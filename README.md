# Handwritten-Digit-Predictor

This predictor system starts by collecting data from the user. Next comes the training phase, after which the trained model is deployed to a website to evaluate its performance.

##Data Collection & Preprocessing: 
I collect the sketch data in a 280 X 280 pixel format and downsample it to 28 X 28 pixels. The sketched area is assigned a value of 1, while the background area is assigned 0. All outputs are converted into a 1D array(1+784) format and stored in a CSV file.

##Model Training:
During the training phase, I primarily perform Principal Component Analysis (PCA) to reduce the number of columns (features). This yields similar model performance with significantly less computational overhead. Afterward, I use a K-Nearest Neighbors (KNN) model to train the predictor, setting the value of K=5 to achieve higher accuracy.

##Deployment:
Finally, I export the trained model using the pickle format to deploy it onto the website.



