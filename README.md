# elastic-search-heuristics
Search Index enabled programs

The motordelears project implements the use of multiple elastic clusters at the same time.
However, this connections are constructed lazily when requested for the first time.


The bookmemoiz program implements the use of a single elastic cluster.

## Table of contents

* [About](#about)

* [Acknowledgements](#acknowledgements)

* [Software Architecture](#software-architecture)

* [Pattern Used](#features)

* [Tech Stack](#tech-stack)

* [Local Development](#local-development)

* [Running Tests](#running-tests)

* [Demo](#demo)

* [Lessons Learned](#lessons-learned)

* [Feedback](#feedback)

* [License](#license)

### Software Design

The following designs are applied in the program:

    - Modular architecture
    - Separation of concerns
    - SOLID Principles(However, this is applied superficially)
    - 12 Factor app()

### Architecture

#### 1. Application Layer

The project specific logic has been cementrized in this very repository. Al the API level interactivity comes outrightly from this backend-api.

### Requirements

The project requirements are specified in the ```requirements.txt```

You can run your elastic search inside a container as per the following commands:

```docker pull docker.elastic.co/elasticsearch elasticsearch:7.3.0```

```docker run -p 9200:9200 -e "discovery type=single-node" -e "xpack.security.enabled=false" docker.elastic.co/elasticsearch/elasticsearch:7.3.0```

NOTE: The project implements Elastic search version 8 but the provided above requires no authentication as suitabele for testing.

Elasticsearch documents are defined in a ```search_indexes``` app.

The basic units of information in the project are expressed in a ubiquitous internet data interchange format(JavaScript Object Notation). This units are indexed or assigned to a type inside an index.

In the ```bookmemoiz``` project all the respective models(Author, Publisher, Tag, Book) have been flatterned into a single ```BookDocument``` which holds all the required information.

All environments should have different indexes i.e for testing, staging and prodcution environments.

Access to the documents location should be done through a pythonic file path.

The projects use the default shards and replica provisions.

### Syncing Django’s database with Elasticsearch indexes

The project uses django-elasticsearch-dsl library for keeping  index(es) fresh. It makes use of signals, so whenever the model(s) is changed, the correspondent index(es) is updated.

The following commands come in play when running full sync between Django’s database and Elasticsearch:

    1. Create Elasticsearch indexes with:

        ```./manage.py search_index --create -f```

    2. Sync the data with:

        ```./manage.py search_index --populate -f```

The project utilizes the fluid Django signals to keep indexes fresh(updated).

## Lessons Learned



## License

[MIT](https://choosealicense.com/licenses/mit/)