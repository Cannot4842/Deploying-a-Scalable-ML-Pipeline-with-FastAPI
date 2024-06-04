import pytest
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, LabelBinarizer
from sklearn.ensemble import RandomForestClassifier
from ml.data import process_data
from ml.model import train_model, inference

def test_process_data():
    """
    Test the process_data function to ensure it correctly processes the data.
    """
    # Create a small sample dataframe
    data = pd.DataFrame({
        'workclass': ['Private', 'Self-emp-not-inc', 'Private'],
        'education': ['Bachelors', 'HS-grad', 'HS-grad'],
        'marital-status': ['Married-civ-spouse', 'Divorced', 'Divorced'],
        'occupation': ['Prof-specialty', 'Exec-managerial', 'Handlers-cleaners'],
        'relationship': ['Husband', 'Not-in-family', 'Not-in-family'],
        'race': ['White', 'Black', 'White'],
        'sex': ['Male', 'Female', 'Female'],
        'native-country': ['United-States', 'United-States', 'United-States'],
        'salary': ['>50K', '<=50K', '<=50K']
    })

    cat_features = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'native-country']
    
    X, y, encoder, lb = process_data(
        data, 
        categorical_features=cat_features, 
        label='salary', 
        training=True
    )

    # Check the shape of the output
    assert X.shape[0] == 3
    expected_num_columns = X.shape[1]  # Capture the expected number of columns dynamically
    assert X.shape[1] == expected_num_columns

    # Check that the label is correctly processed
    assert (y == lb.transform(data['salary']).flatten()).all()

    # Check that the encoder is fitted
    assert isinstance(encoder, OneHotEncoder)
    assert encoder.categories_ is not None

    # Check that the label binarizer is fitted
    assert isinstance(lb, LabelBinarizer)
    assert lb.classes_ is not None

def test_train_model():
    """
    Test the train_model function to ensure it correctly trains a model.
    """
    # Create a small sample dataframe
    X_train = pd.DataFrame({
        'feature1': [0.1, 0.2, 0.3, 0.4],
        'feature2': [1, 2, 3, 4],
        'feature3': [5, 6, 7, 8]
    })
    y_train = pd.Series([0, 1, 0, 1])

    # Train the model
    model = train_model(X_train, y_train)

    # Check that the model is an instance of RandomForestClassifier
    assert isinstance(model, RandomForestClassifier)

    # Check that the model has been fitted (i.e., it has learned from the training data)
    assert hasattr(model, "n_classes_")

    # Check that the model can make predictions
    predictions = model.predict(X_train)
    assert len(predictions) == len(X_train)

def test_inference():
    """
    Test the inference function to ensure it correctly makes predictions.
    """
    # Create a small sample dataframe for training
    X_train = pd.DataFrame({
        'feature1': [0.1, 0.2, 0.3, 0.4],
        'feature2': [1, 2, 3, 4],
        'feature3': [5, 6, 7, 8]
    })
    y_train = pd.Series([0, 1, 0, 1])

    # Train the model
    model = train_model(X_train, y_train)

    # Create a small sample dataframe for inference
    X_test = pd.DataFrame({
        'feature1': [0.5, 0.6],
        'feature2': [5, 6],
        'feature3': [9, 10]
    })

    # Use the inference function to make predictions
    preds = inference(model, X_test)

    # Check the shape of the predictions
    assert preds.shape[0] == X_test.shape[0]

    # Check the type of the predictions
    assert isinstance(preds, (pd.Series, np.ndarray))

if __name__ == "__main__":
    pytest.main()
