````markdown
# Django + DRF + Elasticsearch + Docker

## 📌 Overview
This project demonstrates how to:
1. Setup Django + Django REST Framework (DRF)
2. Create Models
3. Dockerize Django application with Elasticsearch
4. Connect Database ↔ Elasticsearch
5. Index data into Elasticsearch
6. Apply Full-text Search with REST API + UI Autocomplete

---

## ⚙️ Setup

### 1. Build Docker Image
```bash
docker build -t core:latest .
````

### 2. Start Services

```bash
docker compose up -d
```

This will start:

* **Django** on `http://localhost:8000`
* **Elasticsearch** on `http://localhost:9200`

---

## 📂 Important Files

### `documents.py`
documents.py is used to define which Django model fields should be indexed in Elasticsearch so they can be searched efficiently

---

### Run Elasticsearch Index Rebuild

```bash
docker exec -it django /bin/bash
python manage.py search_index --rebuild
```

✅ Now you can see indexed products at:

```
http://localhost:9200/products/_search
```

---

## 🔎 API Endpoint

**Search API**:

```
GET /api/products/?search=iphone
```

Response:

```json
{
  "status": true,
  "message": "Products fetched successfully.",
  "data": [
    {
      "id": 1,
      "product_name": "iPhone 15",
      "product_brand": "Apple",
      "product_price": "1000"
    }
  ]
}
```

---

## 🎨 UI Autocomplete

We use **trevoreyre/autocomplete-js** for instant search.

Open browser:

```
http://localhost:8000
```

---

## 🌐 Useful Links

* [Mockaroo - Fake Data Generator](https://www.mockaroo.com/)
* [Autocomplete.js Demo](https://autocomplete.trevoreyre.com/#/)

---
