import pytest
import sys
from _pytest.config import ExitCode

def run_tests():
    # Run pytest on the test file or current directory (assuming tests are in the same directory)
    # Capture results without pytest exiting the process
    result = pytest.main(["-q", "--tb=short"])
    return result

def print_summary(result_code):
    # Mapping exit code to emoji summary
    if result_code == ExitCode.OK:
        # All tests passed
        print("🎉 All tests passed! Great job! 🚀🎈")
    elif result_code == ExitCode.TESTS_FAILED:
        print("❌ Some tests failed. Keep trying! 💪😅")
    elif result_code == ExitCode.INTERRUPTED:
        print("⏸️ Tests were interrupted. Try running again! 🔄")
    else:
        print("⚠️ Some unexpected error occurred during testing. 🤔")

if __name__ == "__main__":
    print("Running your test suite... 🧪🔍")
    result_code = run_tests()
    print_summary(result_code)
