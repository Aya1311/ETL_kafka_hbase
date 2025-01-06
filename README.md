# ETL Kafka-HBase

Ce projet est un pipeline ETL (Extract, Transform, Load) qui intègre des flux de données en temps réel à partir de Kafka et les stocke dans une base de données HBase. Ce pipeline consomme des articles d'actualité à partir de l'API NewsAPI, les publie sur un sujet Kafka, puis les consomme et les stocke dans HBase.

## Fonctionnalités
- Extraction des articles d'actualité à partir de NewsAPI.
- Transformation des articles pour correspondre à un schéma précis.
- Publication des articles transformés sur un sujet Kafka.
- Consommation des articles depuis Kafka et stockage dans HBase.

## Architecture

Le pipeline est constitué de trois principaux composants :

1. **Kafka Producer** :
   - Utilise l'API NewsAPI pour récupérer des articles.
   - Transforme les articles au format JSON.
   - Envoie les articles transformés à un sujet Kafka (e.g., `topic_aya`).

2. **Kafka Consumer** :
   - Lit les messages (articles) depuis le sujet Kafka.
   - Transforme les données et les stocke dans HBase.

3. **HBase Storage** :
   - Stocke les données d’articles dans une table (e.g., `table_aya`) avec une famille de colonnes (e.g., `cf1:data`).

## Fichiers principaux

- **kafka_news_producer.py** : Ce script publie des articles d'actualité dans Kafka.
- **Kafka_news_consumer.py** : Ce script consomme les articles depuis Kafka et les stocke dans HBase.
- **hbase_consumer.py** : Une variante du consumer qui peut également stocker les données dans HDFS.
- **secret.txt** : Contient des clés secrètes pour l’API (veillez à ne pas partager publiquement ce fichier).

## Prérequis

- **Kafka** : Installé et configuré sur votre machine.
- **HBase** : Installé et configuré.
- **Python** : Avec les bibliothèques suivantes installées :
  - `kafka-python`
  - `happybase`
  - `newsapi-python`
  - `rich`
- **HDFS** (optionnel) : Pour le stockage supplémentaire.

## Installation

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/Aya1311/ETL_kafka_hbase.git
   ```
2. Installez les dépendances Python :
   ```bash
   pip install kafka-python happybase newsapi-python rich
   ```
3. Configurez les fichiers nécessaires :
   - Remplissez les clés dans `secret.txt`.
   
## Utilisation

### 1. Lancer Kafka et HBase
Assurez-vous que Kafka et HBase sont déjà démarrés sur votre machine.

### 2. Exécuter le Producer
Lancez le producer pour récupérer les articles et les publier sur Kafka :
```bash
python kafka_news_producer.py
```

### 3. Exécuter le Consumer
Lancez le consumer pour lire les messages de Kafka et les stocker dans HBase :
```bash
python Kafka_news_consumer.py
```

### 4. Vérifier HBase
Vérifiez que les données sont correctement stockées dans HBase :
```bash
hbase shell
scan 'table_aya'
```

## Structure des Données

Chaque article est stocké sous la forme d'une ligne dans HBase, avec les colonnes suivantes :
- **cf1:data** : Contient les informations de l'article au format JSON.

## Avertissements

- Si vous utilisez un environnement de production, configurez des paramètres de sécurité pour Kafka et HBase.
### Auteur
Projet réalisé par Aya Laadaili dans le cadre d'une architecture ETL pour stockage de flux temps réel.


