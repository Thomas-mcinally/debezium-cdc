# debezium-cdc
- curl -i -X POST localhost:8083/connectors/ --data "@debezium.json" -H "Content-Type: application/json" -H "Accept:application/json"
- docker run --tty --network postgres_debezium_cdc_default confluentinc/cp-kafkacat kafkacat -b kafka:9092 -C -s key=s -s value=avro -r http://schema-registry:8081 -t postgres.public.student