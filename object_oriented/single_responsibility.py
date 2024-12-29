# Exercise 7 - Single Responsibility
class DataGenerator:
    def generate_data(self):
        return {"sales": 1000, "profit": 200}

class DataFormatter:
    def format_as_json(self, data):
        import json
        return json.dumps(data)

class FileSaver:
    def save_to_file(self, content, filename):
        with open(filename, "w") as file:
            file.write(content)

class Report:
    def __init__(self):
        self.data_generator = DataGenerator()
        self.data_formatter = DataFormatter()
        self.file_saver = FileSaver()

    def create_report(self, filename):
        data = self.data_generator.generate_data()
        formatted_data = self.data_formatter.format_as_json(data)
        self.file_saver.save_to_file(formatted_data, filename)

if __name__ == '__main__':

    report = Report()
    report.create_report("report.json")
