FROM eclipse-mosquitto:2
COPY mosquitto.conf /mosquitto/config/mosquitto.conf
COPY passwd /mosquitto/config/passwd
COPY certs/ /mosquitto/certs/
EXPOSE 8883
