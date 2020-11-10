# Flask Template

## Development notes

### Install virtualenv

```
pip install virtualenv
```

### Create virtualenv

```
virtualenv .venv
```

### Activate virtualenv

```
. .venv/bin/activate
```

### Install dependencies

```
pip install -r requirements.txt
```

### Init database

```
python init_db.py
```

### Run Flask application

```
python run.py

* Serving Flask app "app.app" (lazy loading)
* Environment: production
  WARNING: This is a development server. Do not use it in a production deployment.
  Use a production WSGI server instead.
* Debug mode: on
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: 213-963-766
```

### Get list of users
```
curl http://127.0.0.1:5000/users 
{
  "users": [
    {
      "email": "user1@gmail.com", 
      "first_name": "User", 
      "id": 1, 
      "last_name": "One"
    },
    ...
  ]
}
```

### Sent post request to create a user:

```
curl -X POST http://127.0.0.1:5000/users -d '{"first_name":"User","last_name":"Two","email":"user2@gmail.com"}' -H "Content-Type: application/json"
{
  "email": "user2@gmail.com", 
  "first_name": "User", 
  "id": 2, 
  "last_name": "Two"
}
```
