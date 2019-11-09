# ChangeTheFuture
This is a simple web game to play in group: it is known an event, try to change the past action in order to it never existed.

# Build and run the Server
One click deploy:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/nicolalandro/ChangeTheFuture)

or manually:
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

# Knowledge and Framework
## Languages
* HTML
* JavaScript
* CSS
* Python
## Libraries
* [Django](https://docs.djangoproject.com/en/2.2/intro/tutorial01/)
* [GraphQL](https://graphql.org/) and [Graphene](https://github.com/graphql-python/graphene-django)
* [vue.js](https://vuejs.org/)
* [vue-cli](https://cli.vuejs.org/guide/)
* [Bulma](https://bulma.io/) and [Buefy](https://buefy.org/)
* [Material Design Icon](https://cdn.materialdesignicons.com/3.5.95/)