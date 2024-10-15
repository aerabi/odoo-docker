# How the Project was Created

This project is a base Docker Compose setup for Odoo 17.0 with PostgreSQL 15.0. The Dockerfile is based on the official Odoo Docker image, and the `docker-compose.yml` file is a simple setup to run Odoo with PostgreSQL.

In Addition, we have created an addon, that we'll walk you through in the next section.

# Creating an Addon

The `addons` directory contains a simple Odoo addon.
To load it after creation, you have to enable the developer mode in Odoo:

- [http://localhost/web?debug=assets,tests](http://localhost/web?debug=assets,tests)

Then, go to the Apps menu and click on `Update Apps List`.

