## TP1 : Docker & Docker Compose

Réalisé par: Oussama Khouya

### Exercice 1 - Découverte de Docker

```
# 1. Vérifiez que Docker Desktop est installé et démarré
# Cette commande affiche la version client et serveur Docker si Docker fonctionne correctement
docker version

# 2. Exécutez votre premier conteneur avec l’image hello-world
# Cette commande télécharge l’image hello-world si nécessaire et la lance pour afficher un message de vérification
docker run hello-world

# 3. Téléchargez l’image nginx:alpine sans la lancer
# 'docker pull' récupère l’image depuis Docker Hub sans la lancer
docker pull nginx:alpine

# 4. Listez toutes les images présentes sur votre système
# Affiche toutes les images Docker présentes localement
docker images

# 5. Lancez un conteneur nginx en arrière-plan sur le port 8080
# '-d' lance en mode détaché (arrière-plan), '-p' fait le mapping des ports hôte:conteneur, '--name' donne un nom au conteneur
docker run -d -p 8080:80 --name mon-nginx nginx

# 6. Vérifiez que le serveur web est accessible dans le navigateur
# Ouvrez dans votre navigateur : http://localhost:8080

# 7. Affichez les logs du conteneur nginx
# Cette commande affiche les logs générés par le serveur nginx en cours d’exécution
docker logs mon-nginx

# 8. Listez tous les conteneurs (en cours et arrêtés)
# 'docker ps -a' affiche tous les conteneurs, actifs ou non
docker ps -a

# 9. Arrêtez et supprimez le conteneur nginx
docker stop mon-nginx    # Arrête le conteneur nommé mon-nginx
docker rm mon-nginx      # Supprime ce conteneur

# 10. Nettoyez les images inutilisées pour libérer de l’espace disque
docker image prune -a

```
