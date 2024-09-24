# Start with a base image for Kafka
FROM bitnami/kafka:latest

# Switch to root user to install dependencies
USER root

# Install dependencies for Kafdrop
RUN apt-get update && \
    apt-get install -y wget openjdk-17-jre-headless --fix-missing && \
    apt-get clean

# Download and set up Kafdrop
RUN wget https://github.com/obsidiandynamics/kafdrop/releases/download/3.29.0/kafdrop-3.29.0.jar -O /kafdrop.jar

# Expose Kafka and Kafdrop ports
EXPOSE 9092 9000

# Environment variables for Kafka
ENV KAFKA_BROKER_ID=1
ENV KAFKA_LISTENERS=PLAINTEXT://:9092
ENV KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092
ENV KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181
ENV ALLOW_PLAINTEXT_LISTENER=yes

# Create the start script inside the Dockerfile with root permissions
RUN echo "#!/bin/bash\n\
# Start ZooKeeper\n\
/opt/bitnami/zookeeper/bin/zkServer.sh start &\n\
# Wait for ZooKeeper to start\n\
sleep 10\n\
# Start Kafka\n\
/opt/bitnami/kafka/bin/kafka-server-start.sh /opt/bitnami/kafka/config/server.properties &\n\
# Wait for Kafka to start\n\
sleep 20\n\
# Start Kafdrop\n\
java -jar /kafdrop.jar --kafka.brokerConnect=localhost:9092 --server.port=9000\n\
# Keep container running\n\
tail -f /dev/null\n" > /start-services.sh && \
chmod +x /start-services.sh

# Switch back to the default user
USER 1001

# Start Kafka and Kafdrop
CMD ["/bin/bash", "/start-services.sh"]
