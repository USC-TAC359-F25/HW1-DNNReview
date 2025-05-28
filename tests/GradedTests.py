import pandas as pd
import numpy as np
import importlib.util
import os

# Load the student's script dynamically (assume script is named student_model.py)
def load_student_module():
    spec = importlib.util.spec_from_file_location("student_model", "student_model.py")
    student_model = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(student_model)
    return student_model

def test_file_exists():
    assert os.path.exists("student_model.py"), "student_model.py not found."

def test_dataframe_processed_correctly():
    student = load_student_module()
    assert hasattr(student, 'df'), "DataFrame 'df' is missing"
    assert 'distance' in student.df.columns, "'distance' column missing in DataFrame"
    assert 'fare_amount' in student.df.columns, "'fare_amount' column missing in DataFrame"
    assert student.df.shape[1] == 5, f"Expected 5 columns after processing, found {student.df.shape[1]}"

def test_model_architecture():
    student = load_student_module()
    model = student.model
    assert model is not None, "Model is not defined"
    assert len(model.layers) == 3, "Model should have 3 layers (2 hidden + 1 output)"
    assert model.input_shape[1] == 4, "Model input should have 4 features"

def test_prediction_shape():
    student = load_student_module()
    pred = student.model.predict(np.array([[2, 4, 15.33, 3.2]]))
    assert pred.shape == (1, 1), f"Expected prediction shape (1, 1), got {pred.shape}"

def test_r2_score_computation():
    student = load_student_module()
    r2 = student.r2_score
    assert isinstance(r2, float), "R2 score should be a float"
    assert 0 <= r2 <= 1, f"R2 score should be between 0 and 1, got {r2}"
