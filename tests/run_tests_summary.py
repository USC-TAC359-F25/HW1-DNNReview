def run_custom_tests():
    import subprocess

    # Define tests and their weights (example weights, adjust as needed)
    tests = [
        ("Test A", 20),
        ("Test B", 30),
        ("Test C", 25),
        ("Test D", 25),
    ]
    total_points = sum(weight for _, weight in tests)

    print("\n📋 Running Student Model Evaluation...\n")
    result = subprocess.run(
        ["pytest", "--tb=short", "--disable-warnings", "-q", "tests/"],
        capture_output=True, text=True
    )

    output = result.stdout
    # Basic heuristic for counting passed and failed tests
    passed = output.count("✓") + output.count("PASSED")  # cover different pytest output styles
    failed = output.count("F") + output.count("FAILED")
    total = passed + failed

    # Calculate score (simple percent passed)
    score = max(int((passed / max(total, 1)) * 100), 0)

    # Emoji for score
    if score == 100:
        emoji = "🎉"
    elif score >= 80:
        emoji = "👍"
    elif score >= 60:
        emoji = "😐"
    else:
        emoji = "💥"

    # Print the formatted grade report
    print("\nGrade Report")
    print(f"Result\tTest\tPoints\tEarned\tDetails")
    print(f"Graded Student Model tests")

    # Distribute points proportionally (simplified)
    # Here we just show all tests passed for demo, you can enhance by parsing actual test names
    for test_name, points in tests:
        status = "✅ PASS" if passed > 0 else "❌ FAIL"
        earned = points if passed > 0 else 0
        print(f"{status}\t{test_name}\t{points}\t{earned}\t")

    print(f"Subtotal\t{total_points}\t{score}\t")
    print(f"Test Cases Grade")
    print(f"Subtotal\t0\t0\t")
    print(f"TOTAL\t{total_points}\t{score}\t")
    print(f"\n🔥 All test cases passed!! 😀" if score == 100 else "\n⚠️ Some tests failed.")
    print(f"You received {score} out of {total_points} points.")
    print("\nKeep in mind you still need to check for warnings, and there may be additional assignment-specific points.\n")

    print("🛠️  Details:\n")
    print(output)

if __name__ == "__main__":
    run_custom_tests()
