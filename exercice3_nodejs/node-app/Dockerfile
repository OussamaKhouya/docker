FROM node:18-alpine AS build
WORKDIR /usr/src/app
COPY package.json ./
RUN npm install --production
COPY . .

FROM node:18-alpine
WORKDIR /usr/src/app

# Install curl for healthcheck
RUN apk add --no-cache curl

COPY --from=build /usr/src/app ./

EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s CMD curl -f http://localhost:3000/api/health || exit 1

CMD ["node", "server.js"]
