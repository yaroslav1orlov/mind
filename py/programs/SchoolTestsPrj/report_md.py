import json

# Чтение данных из файла JSON
with open('/repos/mind/py/programs/SchoolTestsPrj/grades.json', 'r') as file:
    tests = json.load(file)

# Создание Markdown строки для отчета
report_md = "# Test Grades Report\n\n"
report_md += "| Date       | Subject     | Title          | Grade |\n"
report_md += "|------------|-------------|----------------|-------|\n"

for test in tests:
    report_md += f"| {test['date']} | {test['subject']} | {test['title']} | {test['grade']} |\n"

# Вывод Markdown отчета
print(report_md)

# Saving the report to a Markdown file
with open('test_grades_report.md', 'w') as md_file:
    md_file.write(report_md)

print("Markdown file successfully created and saved as 'test_grades_report.md'.")
