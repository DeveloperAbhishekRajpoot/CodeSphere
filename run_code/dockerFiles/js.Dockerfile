# Use official Node.js image
FROM node:latest
WORKDIR /app
COPY script.js /app/
CMD ["node", "script.js"]
