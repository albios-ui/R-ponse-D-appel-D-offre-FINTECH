# IA - Predict Trajectory

[DAT Data - ****TFL Liability Insurance Improvement****](https://www.notion.so/DAT-Data-TFL-Liability-Insurance-Improvement-04141439b7924ea38962a18b40129946?pvs=21)

Responsable : **Gaël Sorin**

---

Ce document fournit une présentation de notre solution d'intelligence artificielle (IA) pour la prédiction de trajectoires. L'objectif de l'IA est de prendre en entrée des données liées au véhicule et de prédire la trajectoire à suivre afin d'éviter les accidents. Cette IA sera intégrée aux véhicules de la TFL (Transport For London) et permettra au véhicule de réagir en cas d’obstacle afin d’éviter de blesser des personnes ou alors de causer des dommages matériels. En analysant les données de trajectoire réelles et prévues, notre IA peut contribuer à l'identification des modèles et des facteurs qui influencent les accidents de la route.

Ce fichier de documentation décrit les principales étapes du processus, notamment le prétraitement des données, la définition du modèle, l'entraînement, l'évaluation, le réglage et l'amélioration, ainsi que le déploiement du modèle dans un système réel.

1. Prétraitement des données :
Avant d'entraîner notre modèle, il est essentiel de prétraiter les données pour les mettre dans un format approprié. Les étapes de prétraitement peuvent inclure :
    - Normalisation des valeurs : mise à l'échelle des données pour qu'elles se situent dans une plage spécifique, ce qui facilite l'apprentissage du modèle.
    - Nettoyage des données erronées ou aberrantes : identification et suppression des données incohérentes ou incorrectes qui pourraient affecter les performances du modèle.
    - Séparation des données : division des données en ensembles distincts, tels que l'ensemble d'entraînement et l'ensemble de test, pour évaluer le modèle de manière indépendante.
2. Définition du modèle :
Dans notre solution, nous utiliserons soit un réseau de neurones convolutionnels (CNN) soit un réseau de neurones récurrents (RNN) pour prédire la trajectoire. Le modèle prendra en entrée les données disponibles, telles que la vitesse du véhicule, la vitesse de rotation des roues, l'angle du volant, les données GPS et les informations du détecteur d'obstacles. L'objectif est d'apprendre à faire correspondre ces entrées aux sorties correspondantes, c'est-à-dire les trajectoires réelles.
3. Entraînement du modèle :
L'entraînement du modèle consiste à ajuster les poids et les paramètres du réseau de neurones en utilisant les données d'entraînement prétraitées. Le processus d'entraînement vise à minimiser l'erreur de prédiction entre les trajectoires prédites et les trajectoires réelles. Pour cela, nous utilisons des techniques d'apprentissage supervisées, où nous fournissons à notre modèle à la fois les données d'entrée (caractéristiques) et les sorties attendues (trajectoires réelles). Ainsi, le modèle peut apprendre à associer les caractéristiques aux sorties correspondantes.
4. Évaluation du modèle :
Une fois que le modèle est entraîné, nous évaluons sa performance en utilisant les données de test qui n'ont pas été vues lors de l'entraînement. L'évaluation nous permet de mesurer la précision des prédictions du modèle et de déterminer s'il est capable de prédire efficacement les trajectoires pour éviter les accidents. Différentes mesures d'évaluation, telles que la précision, le rappel et la F-mesure, peuvent être utilisées pour évaluer la performance du modèle.
5. Réglage et amélioration :
Si les performances du modèle ne sont pas satisfaisantes, il est possible de procéder à des ajustements et des améliorations. Cela peut inclure le réglage des hyperparamètres du modèle, tels que le taux d'apprentissage, la taille du réseau ou d'autres paramètres spécifiques au modèle utilisé. Il est également possible d'ajouter de nouvelles fonctionnalités pertinentes ou de modifier le prétraitement des données pour améliorer les résultats.
6. Déploiement :
Une fois que nous sommes satisfaits des performances du modèle, nous pouvons le déployer dans un système réel pour effectuer des prédictions en temps réel. Le déploiement peut nécessiter l'intégration du modèle dans une infrastructure informatique existante, l'adaptation des interfaces de communication et la configuration des ressources nécessaires. Il est important de surveiller régulièrement les performances du modèle déployé et de mettre en place des mécanismes de rétroaction pour maintenir et améliorer la qualité des prédictions.

Conclusion :
Ce fichier de documentation a présenté les principales étapes de notre solution d'IA pour la prédiction de trajectoires. En suivant ces étapes, nous pouvons prétraiter les données, définir un modèle approprié, l'entraîner en utilisant des données d'entraînement, évaluer ses performances, l'ajuster si nécessaire et enfin le déployer dans un système réel. En continuant à améliorer notre modèle et en recueillant des données supplémentaires, nous pouvons renforcer sa précision et sa capacité à éviter les accidents sur la route.