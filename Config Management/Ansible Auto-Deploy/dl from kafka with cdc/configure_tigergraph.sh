#!/bin/bash

# Set variables
TG_HOST="http://YOUR_TG_HOST:9000"
TG_TOKEN="YOUR_TG_TOKEN"

# Enable V2 data loading
curl -X PUT -H "Authorization: Bearer $TG_TOKEN" -H "Content-Type: application/json" -d '{"dataLoadingV2": true}' "$TG_HOST/graph/settings"

# Create Kafka data source
curl -X POST -H "Authorization: Bearer $TG_TOKEN" -H "Content-Type: application/json" -d '{
  "name": "kafka_source",
  "brokerURL": "YOUR_KAFKA_BROKER_URL",
  "topic": "my_topic",
  "format": "json",
  "kafkaConfig": {
    "group.id": "tg_consumer_group",
    "enable.auto.commit": "false",
    "auto.offset.reset": "earliest"
  }
}' "$TG_HOST/restpp/datasource"

# Create a loading job
curl -X POST -H "Authorization: Bearer $TG_TOKEN" -H "Content-Type: application/json" -d '{
  "job": "CREATE LOADING JOB load_from_kafka FOR GRAPH my_graph { 
              DEFINE FILENAME kafka_data = \"kafka://kafka_source\"; 
              LOAD kafka_data TO VERTEX Person VALUES ($\"person_id\", $\"name\", $\"age\") 
              USING SEPARATOR=\",\", HEADER=\"true\", EOL=\"LF\"; 
              LOAD kafka_data TO EDGE Knows VALUES ($\"person_id\", $\"friend_id\") 
              USING SEPARATOR=\",\", HEADER=\"true\", EOL=\"LF\"; 
           }"
}' "$TG_HOST/ddl"

# Configure CDC to send data back to Kafka
curl -X POST -H "Authorization: Bearer $TG_TOKEN" -H "Content-Type: application/json" -d '{
  "graph": "my_graph",
  "config": {
    "kafka": {
      "brokerURL": "YOUR_KAFKA_BROKER_URL",
      "topic": "processed_data_topic"
    }
  }
}' "$TG_HOST/restpp/datasource/cdc"

echo "TigerGraph configuration completed."
