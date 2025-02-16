import json
import os

# Report Data
report_data = {
    "Flake8": "",
    "Pylint": "",
    "SonarQube": "",
}

# Save Report in Workspace
report_path = os.path.join(os.getcwd(), "code_quality_report.txt")
with open(report_path, "w") as report_file:
    json.dump(report_data, report_file, indent=4)

print(f"Code quality report generated at: {report_path}")