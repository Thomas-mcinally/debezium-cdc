# debezium-cdc
## Run docker containers
    `docker-compose up`

## Configure debezium to stream updates from company table
    `curl -i -X POST localhost:8083/connectors/ --data "@debezium.json" -H "Content-Type: application/json" -H "Accept:application/json"`

## Tail outputs in kafka topic
    `docker run --tty --network postgres_debezium_cdc_default confluentinc/cp-kafkacat kafkacat -b kafka:9092 -C -t pre.public.company`

- The files `example_output_1_create.json` and `example_output_2_update.json` illustrate what the kafka messages look like when write a new entry to the company table and then subsequently update this entry

## Setup sink connector
curl -X PUT http://localhost:8083/connectors/sink-jdbc-mysql-01/config \
     -H "Content-Type: application/json" -d '{
    "connector.class"                    : "io.confluent.connect.jdbc.JdbcSinkConnector",
    "connection.url"                     : "jdbc:mysql://mysql:3306/demo",
    "topics"                             : "test01",
    "key.converter"                      : "org.apache.kafka.connect.storage.StringConverter",
    "value.converter"                    : "io.confluent.connect.avro.AvroConverter",
    "value.converter.schema.registry.url": "http://schema-registry:8081",
    "connection.user"                    : "connect_user",
    "connection.password"                : "asgard",
    "auto.create"                        : true,
    "auto.evolve"                        : true,
    "insert.mode"                        : "insert",
    "pk.mode"                            : "record_key",
    "pk.fields"                          : "MESSAGE_KEY"
}'
