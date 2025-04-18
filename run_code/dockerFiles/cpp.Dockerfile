FROM gcc:latest

WORKDIR /app

COPY run_code.cpp /app/run_code.cpp

RUN g++ run_code.cpp -o run_code

CMD ["./run_code"]
