

Dans l'objectif de doter une Banque d'un système performant de gestion des activités, il vous est demandé de mettre en oeuvre une API de gestion des clients et des comptes.

Un client est caratérisé par un nom, un prénom, une date de naissance, une profession, une nationnalité, un numéro de pièce d'identité.

Un compte est caractérisé par un numéro de compte (généré à la création  sous le format 'code_banque-annee-mois-random_id_between_1_and_1000000'), la date de création, le nom de l'agence, le nom de l'agent, le solde initial, la date de dernière opération.

On suppose qu'un client peut disposer d'un compte et qu'un compte possède nécessairement un client qui en est le titulaire. 

Cette API doit fournir les fonctionnalités suivantes :
- [ ] Créer un client
- [ ] Modifier un client
- [ ] Supprimer logiquement un client (sans le supprimer réellement de la base)
- [ ] Afficher les détails d'un client dont l'identifiant est fourni en paramètre de route
- [ ] Afficher la liste des clients (la pagination sera fournie comme paramètre de requête)
- [ ] Créer un compte
- [ ] Modifier un compte
- [ ] Supprimer logiquement un compte
- [ ] Afficher les détails d'un compte
- [ ] Lister les comptes (avec une pagination)

En vue de sécuriser l'API, on décide de créer une route pour l'authentification basique (avec username, et password) et qui retourne lorsque l'utilisateur est authentifiée le token pour l'authentification des autres routes/ressources. 

Vous aurez à utiliser le framework FastAPI de Python ainsi que la base de données SQLite.
La mise en application des bonnes pratiques sera prise en compte dans la notation.
# Fast-API-Python-
