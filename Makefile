test:
        docker-compose run --rm api python manage.py test

lint:
        docker-compose run --rm api pylint account/ geo/ app_core/ ASSOI/ ASSOI_manage/ academic/ authentication/