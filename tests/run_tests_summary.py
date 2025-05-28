import subprocess
import re

def run_custom_tests():
    print("\n📋 Running Student Model Evaluation...\n")

    # Run pytest on your tests folder quietly
    result = subprocess.run(
        ["pytest", "--tb=short", "--disable-warnings", "-q", "tests/"],
        capture_output=True,
        text=True,
    )
    output = result.stdout + result.stderr  # capture both stdout and stderr

    # Extract test results using regex
    test_results = {}
    pattern = re.compile(r"tests/.+::(\w+)\s+(PASSED|FAILED)")

    for match in pattern.finditer(output):
        test_name = match.group(1)
        status = match.group(2)
        test_results[test_name] = status

    # Test points mapping
    test_points = {
        "test_file_exists": 20,
        "test_required_imports": 20,
        "test_model_definition_present": 20,
        "test_data_processing_steps_present": 20,
        "test_prediction_attempt_present": 20,
    }

    points_earned = 0
    total_points = sum(test_points.values())

    print("\n🎓 Grade Report")
    print("Result\tTest\tPoints\tEarned\tDetails")
    print("Graded Student Model Tests")

    for test_name, points in test_points.items():
        status = test_results.get(test_name, "NOT RUN")
        if status == "PASSED":
            points_earned += points
            result_str = "✅ PASS"
            earned_points = points
        elif status == "FAILED":
            result_str = "❌ FAIL"
            earned_points = 0
        else:
            result_str = "❓ NOT RUN"
            earned_points = 0

        print(f"{result_str}\t{test_name}\t{points}\t{earned_points}\t")

    score = int((points_earned / total_points) * 100) if total_points > 0 else 0

    # Choose emoji based on performance
    if score == 100:
        emoji = "🎉"
    elif score >= 80:
        emoji = "👍"
    elif score >= 60:
        emoji = "😐"
    else:
        emoji = "💥"

    print(f"Subtotal\t{total_points}\t{points_earned}")
    print(f"TOTAL\t{total_points}\t{points_earned}")
    print(f"\n📝 Final Score: {score}/100 {emoji}")
    print("\n🛠️  Details:\n")
    print(output)


if __name__ == "__main__":
    run_custom_tests()
