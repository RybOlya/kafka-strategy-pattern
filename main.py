from data_processor import DataProcessor
from output_strategy import ConsoleOutputStrategy, KafkaOutputStrategy

def choose_output_strategy():
    choice = input("Choose output strategy (1 for Console, 2 for Kafka): ")
    if choice == "1":
        return ConsoleOutputStrategy()
    elif choice == "2":
        bootstrap_servers = 'localhost:9092'
        topic = 'parking_violations'
        return KafkaOutputStrategy(bootstrap_servers, topic)
    else:
        print("Invalid choice. Using Console Output Strategy.")
        return ConsoleOutputStrategy()

def main():
    output_strategy = choose_output_strategy()
    start_index = int(input("Enter start index: "))
    end_index = int(input("Enter end index: "))
    data_processor = DataProcessor(output_strategy)
    file_path = '/home/orybe/test/doc/lab4/Parking_Violations_Issued.csv'
    data_processor.process_data(file_path, start_index, end_index)

if __name__ == "__main__":
    main()
