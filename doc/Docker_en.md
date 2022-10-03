# Running a project on Docker

**Goal**: Run backend with Docker

## Preparatory stage

*Prerequisites: Windows 10 x64 Update 20H1 (Build 19041) or later*

1. Update Windows to the specified version.
2. Install [Docker Desktop for Windows](https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe) and
   restart your computer
3. After reboot, you need to download and install the
   kernel [Linux](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi)
4. Start or Reload Docker Desktop

## Start compose and load sample data

- Clone project:

```shell
# clone project
git clone --branch develop git@github.com:slijirqqq/ASSSOIService.git
cd ASSSOIService
```

- Start docker compose:

```shell
# create shared docker network on Linux system
docker network create assoi >/dev/null 2>&1
# create shared docker network on Windows system
docker network create assoi
# start everything up
docker compose up -d
# wait init app of docker compose
docker compose logs -f --tail=100 init
# load initial data
docker compose run --rm api python manage.py init_full_data
```

- Shut down and remove all data:

```shell
docker compose down -v
```

![img.png](static/images/img.png)
