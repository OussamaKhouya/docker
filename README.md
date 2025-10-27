## TP1 : Docker & Docker Compose

Réalisé par: Oussama Khouya

### Exercice 1 - Découverte de Docker
1. Vérifiez que Docker Desktop est bien installé et démarré.

![img.png](snapshots/img.png)
2. Exécutez votre premier conteneur avec l’image hello-world.!

![img_1.png](snapshots/img_1.png)
3. Téléchargez l’image nginx:alpine sans la lancer.! 

![img_5.png](snapshots/img_5.png)
4. Listez toutes les images présentes sur votre système.

![img_6.png](snapshots/img_6.png)
5. Lancez un conteneur nginx en arrière-plan sur le port 8080. 

![img_3.png](snapshots/img_3.png)
6. Vérifiez que le serveur web est accessible dans votre navigateur.

![img_2.png](snapshots/img_2.png)
7. Affichez les logs du conteneur nginx.

![img_7.png](snapshots/img_7.png)
8. Listez tous les conteneurs (en cours et arrêtés).

![img_8.png](snapshots/img_8.png)
9. Arrêtez et supprimez le conteneur nginx.

![img_9.png](snapshots/img_9.png)
10. Nettoyez les images inutilisées.

![img_10.png](snapshots/img_10.png)




### Exercice 2 - Manipulation avancée des conteneurs

1. Lancez un conteneur Ubuntu en mode interactif.

![img_17.png](snapshots/img_17.png)
2. Dans ce conteneur, installez curl et vim.

![img_11.png](snapshots/img_11.png)
3. Créez un fichier test.txt avec du contenu.

![img_18.png](snapshots/img_18.png)
4. Sortez du conteneur sans l’arrêter (Ctrl+P puis Ctrl+Q).
5. Copiez le fichier test.txt du conteneur vers votre machine.!

[img_19.png](snapshots/img_19.png)
6. Modifiez le fichier sur votre machine et recopiez-le dans le conteneur.

![img_20.png](snapshots/img_20.png)

![img_22.png](snapshots/img_22.png)
7. Reconnectez-vous au conteneur et vérifiez les modifications.

![img_23.png](snapshots/img_23.png)
8. Créez une nouvelle image à partir de ce conteneur modifié.
```
docker commit heuristic_poitras heuristic_poitras2
```
9. Lancez un nouveau conteneur basé sur votre image personnalisée.

![img_16.png](snapshots/img_16.png)
10. Testez que vos modifications sont bien présentes.

![img_15.png](snapshots/img_15.png)
11. Bonus : Explorez les statistiques en temps réel des conteneurs!
```
docker stats
```
![img_12.png](snapshots/img_12.png)
### Exercice 3 - Création d’une application web Node.js

1. Créez un dossier node-app pour votre projet.
````bash
mkdir node-app
cd node-app
touch package.json server.js Dockerfile .dockerignore
````
2. Créez les fichiers suivants :
   * package.json : Configuration npm avec Express 
   * server.js : Serveur web simple avec plusieurs routes 
   * Dockerfile : Instructions de containerisation 
   * .dockerignore : Exclusions pour l’image
````bash
touch package.json server.js Dockerfile .dockerignore
````
```
# Image de base
FROM node:18-alpine

# Répertoire de travail
WORKDIR /usr/src/app

# Copie package.json et installation des dépendances
COPY package.json ./
RUN npm install

# Copie du reste des fichiers
COPY . .

# Expose le port 3000
EXPOSE 3000

# Commande de lancement
CMD ["node", "server.js"]
```
```
{
  "name": "node-app",
  "version": "1.0.0",
  "main": "server.js",
  "dependencies": {
    "express": "^4.18.2"
  }
}
```
```
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Bienvenue sur la page d\'accueil !');
});

app.get('/api/health', (req, res) => {
  res.json({ status: 'OK' });
});

app.get('/api/info', (req, res) => {
  res.json({ environment: process.env.NODE_ENV || 'dev', nodeVersion: process.version });
});

app.get('/api/time', (req, res) => {
  res.json({ time: new Date().toISOString() });
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Serveur démarré sur le port ${PORT}`);
});
```
3. Construisez l’image Docker avec le tag node-app:1.0.
````bash
docker build -t node-app:1.0 .
````
4. Lancez le conteneur sur le port 3000.
````bash
docker run -d -p 3000:3000 --name node-app node-app:1.0
````
5. Testez toutes les routes de votre application.

![image_10.png](image_10.png)

![image_11.png](image_11.png)

![image_13.png](image_13.png)

![image_15.png](image_15.png)
6. Optimisez le Dockerfile pour réduire la taille de l’image.
```
FROM node:18-alpine AS build
WORKDIR /usr/src/app
COPY package.json ./
RUN npm install --production
COPY . .

FROM node:18-alpine
WORKDIR /usr/src/app
COPY --from=build /usr/src/app ./
EXPOSE 3000
CMD ["node", "server.js"]
```

7. Reconstruisez avec le tag node-app:1.1.
```
docker build -t node-app:1.1 .
```
![img_3.png](img_3.png)
8. Comparez les tailles des deux images.

![img_4.png](img_4.png)
9. Ajoutez un health check à votre Dockerfile.
````dockerfile
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

````
10. Testez le health check avec docker inspect.

![img_5.png](img_5.png)

![img_6.png](img_6.png)
### Exercice 4 - Stack complète avec Docker Compose
