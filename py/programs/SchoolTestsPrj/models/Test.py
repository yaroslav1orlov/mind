class Test:
    def __init__(self, date, subject, title, grade):
        self.date = date
        self.subject = subject
        self.title = title
        self.grade = grade

    def __str__(self):
        return f"Test: {self.title} in {self.subject}, date: {self.date}, grade: {self.grade}"
