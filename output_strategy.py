from abc import ABC, abstractmethod
from confluent_kafka import Producer
import json

class OutputStrategy(ABC):
    @abstractmethod
    def output(self, data):
        pass

class ConsoleOutputStrategy(OutputStrategy):
    def output(self, data):
        print("Console Output:")
        for item in data:
            print(item)

class KafkaOutputStrategy(OutputStrategy):
    def __init__(self, bootstrap_servers, topic):
        self.bootstrap_servers = bootstrap_servers
        self.topic = topic
        self.producer = None

    def output(self, data):
        producer_config = {'bootstrap.servers': self.bootstrap_servers}
        self.producer = Producer(producer_config)

        try:
            for item in data:
                self.producer.produce(self.topic, json.dumps(item))
            self.producer.flush()
            print("Data successfully sent to Kafka")
        except Exception as e:
            print(f"Failed to send data to Kafka: {e}")
        finally:
            if self.producer is not None:
                self.producer.flush()
                self.producer = None  