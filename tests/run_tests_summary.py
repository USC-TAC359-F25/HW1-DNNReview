import subprocess

def run_custom_tests():
    print("\n📋 Running Student Model Evaluation...\n")

    # Run pytest on your tests folder quietly
    result = subprocess.run(
        ["pytest", "--tb=short", "--disable-warnings", "-q", "tests/"],
        capture_output=True,
        text=True,
    )

    output = result.stdout + result.stderr  # capture both stdout and stderr
    passed = output.count("✓")
    failed = output.count("F")
    total = passed + failed

    score = max(int((passed / max(total, 1)) * 100), 0)

    # Choose emoji based on performance
    if score == 5:
        emoji = "🎉"
    elif score >= 4:
        emoji = "👍"
    elif score >= 3:
        emoji = "😐"
    else:
        emoji = "💥"

    print("\n🎓 Grade Report")
    print("Result\tTest\tPoints\tEarned\tDetails")
    print("Graded Student Model Tests")

    # Map tests to points roughly (adjust as you want)
    test_points = {
        "test_file_exists": 1,
        "test_required_imports": 1,
        "test_model_definition_present": 1,
        "test_data_processing_steps_present": 1,
        "test_prediction_attempt_present": 1,
    }

    # Calculate points earned per test (basic approximation)
    points_earned = 0
    for test_name, points in test_points.items():
        if test_name in output:
            if f"✓ {test_name}" in output:
                points_earned += points
                status = "✅ PASS"
            elif f"F {test_name}" in output:
                status = "❌ FAIL"
            else:
                status = "❓ UNKNOWN"
            print(f"{status}\t{test_name}\t{points}\t{points if status=='✅ PASS' else 0}\t")

    print(f"Subtotal\t{sum(test_points.values())}\t{points_earned}")
    print(f"TOTAL\t{sum(test_points.values())}\t{points_earned}")
    print(f"\n📝 Final Score: {score}/100 {emoji}")
    print("\n🛠️  Details:\n")
    print(output)


if __name__ == "__main__":
    run_custom_tests()
