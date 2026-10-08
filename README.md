# Django CI/CD Demo

A small 3-page Django site (Home, About the Project, Contact) with CI/CD on GitHub Actions:

```
GitHub → Build → Testing → Docker Build → Docker Hub → Starting the container and verifying it
```

## Structure

```
.
├── .github/workflows/ci-cd.yml   # pipeline GitHub Actions
├── config/                       # configuring a Django project
├── pages/                        # an app with pages, templates, and quizzes
│   ├── templates/pages/
│   ├── static/pages/style.css
│   └── tests.py
├── Dockerfile
├── .dockerignore
├── requirements.txt
└── manage.py
```

## Pipeline (`.github/workflows/ci-cd.yml`)

Runs on every push to `main` (and manually via *Run workflow*):

| Job | What does it do?                                                                                                                     |
|---|--------------------------------------------------------------------------------------------------------------------------------------|
| **Build & Test** | Check out the code -> Install Python 3.12 and dependencies -> `manage.py check` -> `manage.py test`                                  |
| **Docker Build & Push** | Only if the tests pass: builds the image according to the `Dockerfile` and pushes it to Docker Hub with the tags `latest` and `<sha commit>`|
| **Run container & check site** | pulls the image from Docker Hub, starts the container, and checks `/`, `/about/`, `/contact/`, `/health/`, and the static files      |

Only Build & Test are performed on the pull request.

## Secrets are required on GitHub

*Settings → Secrets and variables → Actions → New repository secret*:

- `DOCKERHUB_USERNAME` — your Docker Hub username (all lowercase)
- `DOCKERHUB_TOKEN` — Access Token from Docker Hub (*Account settings → Personal access tokens*, Read & Write permissions)

## Local launch

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py test
python manage.py runserver
```

## Running an image from Docker Hub

```bash
docker pull <DOCKERHUB_USERNAME>/django-cicd-demo:latest
docker run -d --name django-app -p 8000:8000 <DOCKERHUB_USERNAME>/django-cicd-demo:latest
curl http://localhost:8000/health/   # {"status": "ok"}
```

Сайт: http://localhost:8000
