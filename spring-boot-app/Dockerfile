# Use OpenJDK image
FROM openjdk:11-jre-slim

# Copy the JAR file into the image
COPY ./target/spring-boot-app-0.0.1-SNAPSHOT.jar /app.jar

# Run the application
CMD ["java", "-jar", "/app.jar"]
