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
