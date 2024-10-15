# Odoo Docker

This repository contains the Dockerfile and docker-compose.yml to run Odoo 17.0 with PostgreSQL 15.0.

## Usage

First, clone the repository:

```bash
git clone https://github.com/aerabi/odoo-docker.git
```

Update the `db_password.txt` file with the desired password for the PostgreSQL database, e.g.:

```bash
echo "mysecretpassword" > db_password.txt
```

Then, run the following command to start Odoo:

```bash
docker compose up
```
