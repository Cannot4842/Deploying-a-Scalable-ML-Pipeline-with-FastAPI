# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
Model Type: RandomForestClassifier
Framework: Scikit-learn
Purpose: Predict whether an individual's salary is greater than 50K based on census data.
Version: 1.0
Input Data: Various demographic and socio-economic features.
Output: Binary classification - '>50K' or '<=50K'
## Intended Use
This model is designed for educational purposes and to explore the influence of various demographic factors on salary prediction. It is intended for use by data scientists, researchers, and students to understand model training, evaluation, and deployment in machine learning workflows. This model should not be used for real-world decision-making without further validation and testing.
## Training Data
Source: Census dataset
Total Samples: 26,048
Features: Workclass, education, marital status, occupation, relationship, race, sex, native country, and others.
Target Variable: Salary (greater than 50K or not)
## Evaluation Data
Source: Census dataset
Total Samples: 6,513
Purpose: To evaluate the performance of the model.
## Metrics
The model was evaluated using precision, recall, and F1-score. Below are the performance metrics on the test dataset:

Overall Metrics:
Precision: 0.7419
Recall: 0.6384
F1-Score: 0.6863
Performance on Categorical Slices:
Workclass
Workclass: ?, Count: 389
Precision: 0.6538 | Recall: 0.4048 | F1: 0.5000
Workclass: Federal-gov, Count: 191
Precision: 0.7971 | Recall: 0.7857 | F1: 0.7914
Workclass: Local-gov, Count: 387
Precision: 0.7576 | Recall: 0.6818 | F1: 0.7177
Workclass: Private, Count: 4,578
Precision: 0.7376 | Recall: 0.6404 | F1: 0.6856
Workclass: Self-emp-inc, Count: 212
Precision: 0.7807 | Recall: 0.7542 | F1: 0.7672
Workclass: Self-emp-not-inc, Count: 498
Precision: 0.7064 | Recall: 0.4904 | F1: 0.5789
Workclass: State-gov, Count: 254
Precision: 0.7424 | Recall: 0.6712 | F1: 0.7050
Workclass: Without-pay, Count: 4
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
Education
Education: 10th, Count: 183
Precision: 0.4000 | Recall: 0.1667 | F1: 0.2353
Education: 11th, Count: 225
Precision: 1.0000 | Recall: 0.2727 | F1: 0.4286
Education: 12th, Count: 98
Precision: 1.0000 | Recall: 0.4000 | F1: 0.5714
Education: 1st-4th, Count: 23
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
Education: 5th-6th, Count: 62
Precision: 1.0000 | Recall: 0.5000 | F1: 0.6667
Education: 7th-8th, Count: 141
Precision: 0.0000 | Recall: 0.0000 | F1: 0.0000
Education: 9th, Count: 115
Precision: 1.0000 | Recall: 0.3333 | F1: 0.5000
Education: Assoc-acdm, Count: 198
Precision: 0.7000 | Recall: 0.5957 | F1: 0.6437
Education: Assoc-voc, Count: 273
Precision: 0.6471 | Recall: 0.5238 | F1: 0.5789
Education: Bachelors, Count: 1,053
Precision: 0.7523 | Recall: 0.7289 | F1: 0.7404
Education: Doctorate, Count: 77
Precision: 0.8644 | Recall: 0.8947 | F1: 0.8793
Education: HS-grad, Count: 2,085
Precision: 0.6594 | Recall: 0.4377 | F1: 0.5261
Education: Masters, Count: 369
Precision: 0.8271 | Recall: 0.8551 | F1: 0.8409
Education: Preschool, Count: 10
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
Education: Prof-school, Count: 116
Precision: 0.8182 | Recall: 0.9643 | F1: 0.8852
Education: Some-college, Count: 1,485
Precision: 0.6857 | Recall: 0.5199 | F1: 0.5914
Marital Status
Marital-status: Divorced, Count: 920
Precision: 0.7600 | Recall: 0.3689 | F1: 0.4967
Marital-status: Married-AF-spouse, Count: 4
Precision: 1.0000 | Recall: 0.0000 | F1: 0.0000
Marital-status: Married-civ-spouse, Count: 2,950
Precision: 0.7346 | Recall: 0.6900 | F1: 0.7116
Marital-status: Married-spouse-absent, Count: 96
Precision: 1.0000 | Recall: 0.2500 | F1: 0.4000
Marital-status: Never-married, Count: 2,126
Precision: 0.8302 | Recall: 0.4272 | F1: 0.5641
Marital-status: Separated, Count: 209
Precision: 1.0000 | Recall: 0.4211 | F1: 0.5926
Marital-status: Widowed, Count: 208
Precision: 1.0000 | Recall: 0.1579 | F1: 0.2727
Occupation
Occupation: ?, Count: 389
Precision: 0.6538 | Recall: 0.4048 | F1: 0.5000
Occupation: Adm-clerical, Count: 726
Precision: 0.6338 | Recall: 0.4688 | F1: 0.5389
Occupation: Armed-Forces, Count: 3
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
Occupation: Craft-repair, Count: 821
Precision: 0.6567 | Recall: 0.4862 | F1: 0.5587
Occupation: Exec-managerial, Count: 838
Precision: 0.7952 | Recall: 0.7531 | F1: 0.7736
Occupation: Farming-fishing, Count: 193
Precision: 0.5455 | Recall: 0.2143 | F1: 0.3077
Occupation: Handlers-cleaners, Count: 273
Precision: 0.5714 | Recall: 0.3333 | F1: 0.4211
Occupation: Machine-op-inspct, Count: 378
Precision: 0.5938 | Recall: 0.4043 | F1: 0.4810
Occupation: Other-service, Count: 667
Precision: 1.0000 | Recall: 0.1923 | F1: 0.3226

## Ethical Considerations
When developing and deploying this model, several ethical considerations should be taken into account:

Bias and Fairness: The model is trained on historical data, which may contain inherent biases. For instance, certain groups may be underrepresented or overrepresented in the data, leading to biased predictions. It is important to assess the model for any such biases and take corrective measures to ensure fairness.
Privacy: The model uses personal demographic and socio-economic information, which are sensitive data. Ensure that any data handling complies with relevant privacy laws and regulations to protect individuals' privacy.
Transparency: Users of the model should be informed about how the model works, the data it was trained on, and its limitations. This transparency is crucial for building trust and ensuring the model is used appropriately.
Impact of Errors: Incorrect predictions can have significant impacts, especially if the model is used in a decision-making context. Careful consideration should be given to the potential consequences of false positives and false negatives.
## Caveats and Recommendations
While this model provides useful insights, there are several caveats and recommendations to consider:

Generalization: The model is trained on a specific dataset and may not generalize well to other datasets or populations. It is recommended to retrain or fine-tune the model with relevant data when applying it to a new context.
Feature Importance: Understanding which features are most influential in the model's predictions can help in interpreting the results and identifying potential biases. Feature importance should be analyzed and monitored regularly.
Continuous Monitoring: The model's performance should be continuously monitored to detect any degradation over time. Regular updates and maintenance are recommended to ensure sustained performance.
Complementary Use: This model should be used as a complementary tool rather than a standalone decision-maker. Human oversight and domain expertise are crucial to interpret the results correctly and make informed decisions.
Ethical Usage: Ensure that the model is used ethically and responsibly, avoiding any applications that may cause harm or reinforce unfair biases.

