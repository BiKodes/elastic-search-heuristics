# elastic-search-heuristics
Search Index enabled programs

The motordelears project implements the use of multiple elastic clusters at the same time.
However, this connections are constructed lazily when requested for the first time.

The Django Querysets used to populate the index in all programs are paginanted uses
the the database driver's default setting

#Populate
To create and populate the Elasticsearch index and mapping use the search_index command:

```$./manage.py search_index --rebuild``` 

** However if your model have huge amount of data, its preferred to use parallel indexing. To do that, you can pass –parallel flag while reindexing or populating. **

Elastic search instances are created on querysets for searcherbility.

Search results will be cached. Subsequent calls to execute or trying to iterate over an already executed Search objectwill not trigger additional requests being sent to Elasticsearch.


