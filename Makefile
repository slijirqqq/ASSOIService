test:
        docker-compose run --rm api python manage.py test

lint:
        docker-compose run --rm api pylint account/ app_core/ ASSOI/ assoi_manage/ geo/