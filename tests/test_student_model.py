import os
import ast
import pytest

def test_file_exists():
    """Check that the student_model.py file exists."""
    assert os.path.exists("src/student_model.py"), "student_model.py not found in src folder. Rename your python file to 'student_model.py'"

def test_required_imports():
    """Check for required library imports."""
    with open("src/student_model.py", "r") as f:
        tree = ast.parse(f.read())

    import_modules = {node.names[0].name for node in tree.body if isinstance(node, ast.Import)}
    from_modules = {node.module for node in tree.body if isinstance(node, ast.ImportFrom)}

    required_imports = {"pandas", "tensorflow", "keras", "numpy", "matplotlib.pyplot", "sklearn.metrics"}
    found_imports = import_modules.union(from_modules)

    for module in required_imports:
        assert any(module in imp for imp in found_imports), f"Missing import: {module}"

def test_model_definition_present():
    """Check that model is defined and structured properly."""
    with open("src/student_model.py", "r") as f:
        content = f.read()

    assert "Sequential()" in content, "Model not using Sequential API"
    assert "Dense(" in content, "Model does not include Dense layers"
    assert "model.compile" in content, "Model is not compiled"
    assert "model.fit" in content, "Model is not trained"

def test_data_processing_steps_present():
    """Check that the expected preprocessing steps are in the script."""
    with open("src/student_model.py", "r") as f:
        content = f.read()

    assert "pickup_datetime" in content, "pickup_datetime feature not used"
    assert "distance" in content, "distance feature missing or incorrect in DataFrame"
    assert 'fare_amount' in content, "fare_amount column missing or incorrect in DataFrame" 
    assert ".drop(" in content, "drop() not used to remove unnecessary columns"

def test_prediction_attempt_present():
    """Check that the script attempts to make a prediction."""
    with open("src/student_model.py", "r") as f:
        content = f.read()

    assert "model.predict" in content, "Model is not used to make a prediction"

def run_custom_tests():
    import subprocess

    print("\n📋 Running Student Model Evaluation...\n")
    result = subprocess.run(["pytest", "--tb=short", "--disable-warnings", "-q", "tests/"], capture_output=True, text=True)

    output = result.stdout
    passed = output.count("✓")
    failed = output.count("F")
    total = passed + failed

    score = max(int((passed / max(total, 1)) * 100), 0)

    # Choose emoji based on performance
    if score == 100:
        emoji = "🎉"
    elif score >= 80:
        emoji = "👍"
    elif score >= 60:
        emoji = "😐"
    else:
        emoji = "💥"

    print("📊 Test Summary:")
    print(f"✅ Passed: {passed} / {total}")
    print(f"📝 Final Score: {score}/100 {emoji}")
    print("\n🛠️  Details:\n")
    print(output)

if __name__ == "__main__":
    run_custom_tests()
