class FileHandler:
    def __init__(self, file_name):
        self.file = open(file_name)

    def get_file_lines(self):
        return [x.strip() for x in self.file.readlines()]

    def get_file_lines_no_strip(self):
        return self.file.readlines()