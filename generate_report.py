import json
import os
import subprocess

# Function to run a shell command and capture output
def run_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout if result.returncode == 0 else result.stderr
    except Exception as e:
        return str(e)

# Collect tool outputs
report_data = {
    "Flake8": run_command("flake8 --exit-zero ."),
    "Pylint": run_command("pylint *.py"),
    "SonarQube": run_command("sonar-scanner"),
}

# Save report in the workspace
report_path = os.path.join(os.getcwd(), "code_quality_report.txt")
with open(report_path, "w") as report_file:
    json.dump(report_data, report_file, indent=4)

print(f"Code quality report generated at: {report_path}")
