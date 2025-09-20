what we are doing is:
1. Django project and DRF setup
2. Create Models
3. Dockerize application using Elastic
4. Make connection between DB - Elactic
5. Indexing
6. How to apply Searching



https://www.mockaroo.com/


docker build -t core:latest . 

docker compose up -d


documents.py:

docker exec -it django /bin/bash 

root@d413ac0ace7b:/app# python manage.py search_index --rebuild


Now i see products that index with elasticsearch:
http://localhost:9200/products/_search


UI:
https://autocomplete.trevoreyre.com/#/