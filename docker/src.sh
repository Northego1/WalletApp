cd app

export $(grep -v '^#' .env | xargs)


gunicorn main:app --workers $APP_GUNICORN_WORKERS --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000