Instructions
Save the Dockerfile: Copy the above Dockerfile content into a file named Dockerfile.

Build the Docker Image: Run the following command in the directory containing the Dockerfile:

bash
Copy code
docker build -t kafka-kafdrop .
Run the Docker Container: Start the container with:

bash
Copy code
docker_ex_kafka_gui % docker run -p 9092:9092 -p 9001:9000 kafka-kafdrop

This setup will automatically create and run a script to start ZooKeeper, Kafka, and Kafdrop. Kafka will be accessible on port 9092, and the Kafdrop GUI will be accessible on port 9000. This allows you to connect your TigerGraph CDC directly to Kafka and manage it through the Kafdrop web interface. Let me know if you have any further questions or need additional modifications!


DOCKER COMPOSE:
docker-compose up
