# School API IV

By the end of this assignment you will have a fully serviceable CRUD API with user authentication capabilities that will allow School staff to easily manage students and scholastic equipment.

## Student Model

In this assignment we will write the following Django Serializers that will return the following example response for a single Student instance:

- StudentSerializer

```json
{
  "name": "John W. Watson",
  "student_email": "thisIsAnEmail@school.com",
  "locker_number": 13
}
```

- StudentAllSerializer

```json
{
  "name": "John W. Watson",
  "student_email": "thisIsAnEmail@school.com",
  "personal_email": "thisIsAnEmail@gmail.com",
  "locker_number": 13,
  "locker_combination": "12-33-44",
  "good_student": true
}
```

## Running Tests

Replace the `test.py` file inside your app with the `test.py` file already attached to this repository.

Now you can run the test suite by typing the following

```bash
  python manage.py test
```

- `.` means a test passed
- `E` means an unhandled error populated on a test
- `F` means a test completely failed to run

## Running with Docker Compose

This project runs as two containers, **Django** (`server/`) and **PostgreSQL** (`db/`), started together with Docker Compose. Run every command below from the root of this repository (where `docker-compose.yml` lives).

```bash
# build the images and start both containers in the background
docker compose up -d --build

# open a shell inside the Django container
docker compose exec backend bash
```

Django commands must run **inside** the `backend` container, because `settings.py` reaches the database through the host name `db`:

```bash
# DOCKER CONTAINER TERMINAL
python manage.py migrate
python manage.py test
```

The API is served at [http://localhost:8000](http://localhost:8000). Useful commands:

| Command | What it does |
| ------- | ------------ |
| `docker compose ps` | Lists the containers and their status |
| `docker compose logs -f backend` | Follows Django's output |
| `docker compose down` | Stops and removes the containers (the database volume is kept) |
| `docker compose down -v` | Same, but also **deletes** the database volume |

> Whenever you `pip install` a new package, run `pip freeze > requirements.txt` inside `server/` (with your virtual environment active) and then `docker compose up -d --build` so the image gets the new package.
