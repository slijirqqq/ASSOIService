# ASSOI service

![img.png](doc/static/images/kstu.png)

> Backend api to store information on employees and students of the university's ASSOI department

> [CHANGELOG](CHANGELOG.md)

# Getting started

- [Running a project on a local machine](doc/Docker_en.md)

- The interface will be available at localhost:
    - [http://localhost:8000/](http://localhost:8000/) — main UI (frontend)
    - [http://localhost:8000/api/](http://localhost:8000/api/) — backend prefix
    - [http://localhost:8000/api/doc/](http://localhost:8000/api/doc/) - api doc
    - [http://localhost:8000/admin/](http://localhost:8000/admin/) — admin panel

- Sample users:

    - `superassoi@assoi.com:superassoi` — admin user (only admin role)

    - `assoigod@assoi.com:FehKNot7` — user with all roles

    - `<role name>@assoi.com:FehKNot7` (pts@assoi.com, sts@assoi.com, etc.) — users with specific role
- Default roles:

    - `sts`: *Teaching support staff* - УВП
    - `pts`: *Professor teaching staff* - ППС
    - `aspirant`: *Aspirant* - Аспирант
    - `student`: *Student* - Студент

# Contributing

## Running tests

Run all tests:

```shell
docker-compose run --rm api python manage.py test
```

or

```shell
make test
```

Preserve database (will not require migrations to apply on subsequent calls):

```shell
docker-compose run --rm api python manage.py test --keepdb
```

## Linters

To run linters using make:

```shell
make lint
```

Plain:

```shell
docker-compose run --rm api pylint account/ geo/ app_core/ ASSOI/ ASSOI_manage/ academic/ authentication/ version/ api_doc/

```

# APPs

- [account](account/README.md)
- [app_core](app_core/README.md)
- [geo](geo/README.md)
- [ASSOI_manage](ASSOI_manage/README.md)
- [academic](academic/README.md)
- [authentication](authentication/README.md)
- [api_doc](api_doc/README.md)
- [version](version/README.md)