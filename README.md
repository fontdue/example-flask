# fontdue-python-demo

This is a Flask demo project for a web app consuming data from the Fontdue GraphQL API.

[Learn about GraphQL queries →](https://graphql.org/learn/queries/)

Explore the GraphQL API via [GraphiQL →](https://www.electronjs.org/apps/graphiql) \
Enter your Fontdue site's graphql endpoint, e.g. https://example-type.fontdue.com/graphql and click "Docs"

---

### Running this demo project

Install python & virtualenv

```shell
brew install python3
pip3 install virtualenv
```

Clone this repo and install dependencies

```shell
virtualenv -p python3 venv
source venv/bin/activate
pip3 install -r requirements.txt
```

Run

```
flask run
```

The app should start at [http://localhost:5000](http://localhost:5000)


### Deploying to Now.sh

The `FONTDUE_URL` environment variable must point to a Fontdue endpoint.

``` shell
now secrets add fontdue-url "https://example.fontdue.com"
now --prod
```
