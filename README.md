# ChangeTheFuture
This is a simple web game to play in group: it is known an event, try to change the past action in order to it never existed.

# Build and run the Server
One click deploy:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/nicolalandro/ChangeTheFuture)

or run manually after the clone:
```bash
cd front_end
nmp install

cd ..
pip install -r requirements
cd back_end
./manage.py build_vue
./manage.py collectstatic
./manage.py runserver
```

# Developers

## Knowledge and Framework
### Languages
* HTML
* JavaScript
* CSS
* Python
### Libraries
* [Django](https://docs.djangoproject.com/en/2.2/intro/tutorial01/)
* [GraphQL](https://graphql.org/) and [Graphene](https://github.com/graphql-python/graphene-django)
* [vue.js](https://vuejs.org/)
* [vue-cli](https://cli.vuejs.org/guide/)
* [Bulma](https://bulma.io/) and [Buefy](https://buefy.org/)
* [Material Design Icon](https://cdn.materialdesignicons.com/3.5.95/)
* [axios](https://github.com/axios/axios)

## Develop back-end
Install dependecies:
```bash
pip install -r requirements
```
Configure database:
```bash
cd back_end

./manage.py migrate
./manage.py createsuperuser
```
Compile the frontend and copy into statics:
```bash
cd front_end
nmp install

cd ..
cd back_end
./manage.py build_vue
./manage.py collectstatic
```
Run server:
```bash
cd back_end
./manage.py runserver
```

## Develop front-end
Install dependecies:
```bash
cd front_end
nmp install
```

Run server with back-end, and real time changes.
```bash
# shell 1
cd back_end
./manage.py runserver 0.0.0.0:8000

# shell 2
cd front_end
npm run serve
```