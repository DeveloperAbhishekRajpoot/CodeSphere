# Use official GCC image
FROM gcc:latest
WORKDIR /app
COPY run.c /app/
RUN gcc run.c -o run
CMD ["./run"]
