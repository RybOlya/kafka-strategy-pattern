# Strategy pattern
```bash
docker pull apache/kafka:3.7.0
```
```bash
docker run -p 9092:9092 apache/kafka:3.7.0
```
```bash
docker exec -it <container-name> /bin/bash
```

## To create topic
```bash
/opt/kafka/bin/kafka-topics.sh --create --topic parking_violations --bootstrap-server localhost:9092
```
## To view written data
```bash
/opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic parking_violations --from-beginning
```