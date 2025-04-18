FROM openjdk:17

WORKDIR /app

COPY RunCode.java /app/RunCode.java

RUN javac RunCode.java

CMD ["java", "RunCode"]
