import logging

class StudentProcessor:
    def __init__(self):
        self.students = []
        self.logger = logging.getLogger('StudentProcessor')
        self.logger.setLevel(logging.INFO)
        console_handler = logging.StreamHandler()
        console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(console_formatter)
        self.logger.addHandler(console_handler)

    def add_student(self, student):
        self.students.append(student)
        self.logger.info(f"Student {student} added.")

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            self.logger.info(f"Student {student} removed.")
        else:
            self.logger.warning(f"Student {student} not found in the list.")

    def process_students(self):
        self.logger.info("Processing students:")
        for student in self.students:
            self.logger.info(f"Processing student: {student}")

processor = StudentProcessor()
processor.add_student("Akutagawa")
processor.add_student("Blade")
processor.add_student("Himeko")
processor.remove_student("Diluc")
processor.remove_student("Eve")
processor.process_students()
