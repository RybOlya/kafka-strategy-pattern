class DataProcessor:
    def __init__(self, output_strategy):
        self.output_strategy = output_strategy

    def process_data(self, file_path, start_index=None, end_index=None):
        data = self.read_data_from_file(file_path, start_index, end_index)
        self.output_strategy.output(data)

    def read_data_from_file(self, file_path, start_index=None, end_index=None):
        data = []
        with open(file_path, 'r') as file:
            if start_index is not None:
                for _ in range(start_index):
                    next(file)
            if end_index is not None:
                for _ in range(start_index, end_index):
                    line = file.readline().strip()
                    if not line:
                        break
                    data.append(line)
            else:
                for line in file:
                    data.append(line.strip())
        return data

