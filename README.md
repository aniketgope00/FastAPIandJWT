# FastAPIandJWT


### Setting Up Repo
```
uv init
uv venv myenv
# for powershell
myenv/Scripts/activate
```

check running containers with: ```docker ps```
run postgres image as ```docker run --name postgres-db -e POSTGRES_USER=user -e POSTGRES_PASSWORD=password -p 5432:5432 -d postgres```


install and build: ```uv pip install -r requirements.txt; uv sync --active```

run app: ```fastapi dev main.py```
login to postgres:<br>
```
MYSYS_NO_PATHCONV=1 docker exec -it <postgres_container_id> /bin/bash
psql -U <username> -d <db_name> # here username:user, dbname:postgres
#list tables
\dt
#see table schema
\d "<tablename>"
```
