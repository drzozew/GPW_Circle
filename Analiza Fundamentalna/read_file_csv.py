import csv


class Read_file():

    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        with open(self.file_name) as f:
            reader = csv.reader(f)
            header_row = next(reader)
            return header_row

    def print_file(self, header_row):
        for index, column_header in enumerate(header_row):
            print(index, column_header)
