## TP1 : Docker & Docker Compose

Réalisé par: Oussama Khouya

### Exercice 1 - Découverte de Docker
1. Vérifiez que Docker Desktop est bien installé et démarré.![img.png](snapshots/img.png)
2. Exécutez votre premier conteneur avec l’image hello-world.![img_1.png](snapshots/img_1.png)
3. Téléchargez l’image nginx:alpine sans la lancer.! ![img_5.png](snapshots/img_5.png)
4. Listez toutes les images présentes sur votre système.![img_6.png](snapshots/img_6.png)
5. Lancez un conteneur nginx en arrière-plan sur le port 8080. ![img_3.png](snapshots/img_3.png)
6. Vérifiez que le serveur web est accessible dans votre navigateur.![img_2.png](snapshots/img_2.png)
7. Affichez les logs du conteneur nginx.![img_7.png](snapshots/img_7.png)
8. Listez tous les conteneurs (en cours et arrêtés).![img_8.png](snapshots/img_8.png)
9. Arrêtez et supprimez le conteneur nginx.![img_9.png](snapshots/img_9.png)
10. Nettoyez les images inutilisées.![img_10.png](snapshots/img_10.png)




### Exercice 2 - Manipulation avancée des conteneurs

1. Lancez un conteneur Ubuntu en mode interactif.![img_17.png](snapshots/img_17.png)
2. Dans ce conteneur, installez curl et vim.![img_11.png](snapshots/img_11.png)
3. Créez un fichier test.txt avec du contenu.![img_18.png](snapshots/img_18.png)
4. Sortez du conteneur sans l’arrêter (Ctrl+P puis Ctrl+Q).
5. Copiez le fichier test.txt du conteneur vers votre machine.![img_19.png](snapshots/img_19.png)
6. Modifiez le fichier sur votre machine et recopiez-le dans le conteneur.![img_20.png](snapshots/img_20.png) ![img_22.png](snapshots/img_22.png)
7. Reconnectez-vous au conteneur et vérifiez les modifications.![img_23.png](snapshots/img_23.png)
8. Créez une nouvelle image à partir de ce conteneur modifié.
```
docker commit heuristic_poitras heuristic_poitras2
```
9. Lancez un nouveau conteneur basé sur votre image personnalisée.!![img_16.png](snapshots/img_16.png)
10. Testez que vos modifications sont bien présentes.![img_15.png](snapshots/img_15.png)
11. Bonus : Explorez les statistiques en temps réel des conteneurs!
```
docker stats
```
![img_12.png](snapshots/img_12.png)
### Exercice 3 - Création d’une application web Node.js
### Exercice 4 - Stack complète avec Docker Compose
