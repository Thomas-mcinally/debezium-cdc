# debezium-cdc
- Debezium is a set of Kafka-Connect source and sink connectors that make it easy to stream database mutations from a database to kafka and/or from kafka into a db

## Run docker containers
    `docker-compose up`

## Setup source connector
    `curl -i -X POST localhost:8083/connectors/ --data "@source.json" -H "Content-Type: application/json" -H "Accept:application/json"`

## Tail outputs in kafka topic
    `docker run --tty --network postgres_debezium_cdc_default confluentinc/cp-kafkacat kafkacat -b kafka:9092 -C -t pre.public.company`

- The files `example_output_1_create.json` and `example_output_2_update.json` illustrate what the kafka messages look like when write a new entry to the company table and then subsequently update this entry

## Setup sink connector
    `curl -i -X POST http://localhost:8083/connectors/ --data "@sink.json" -H "Content-Type: application/json" -H "Accept:application/json"`
