# fontdue-python-demo

This is a Flask demo project for a web app consuming data from the Fontdue GraphQL API.

[Learn about GraphQL queries →](https://graphql.org/learn/queries/)

Explore the GraphQL API via [GraphiQL →](https://www.electronjs.org/apps/graphiql) \
Enter your Fontdue site's graphql endpoint, e.g. https://example-type.fontdue.com/graphql and click "Docs"

---

### Installing

Make sure you have python3 & pipenv installed, e.g.

``` shell
python3 --version
pipenv --version
```

If you don't, install them:

```shell
brew install python3
pip3 install pipenv
```

Clone this template project by clicking the
[Use this template](https://github.com/fontdue/fontdue-python-demo/generate)
button.

Clone your repo, then install dependencies:

```shell
$ pipenv install
```

Run the local server:

```
$ pipenv run flask run
```

The server will start at [http://localhost:5000](http://localhost:5000)


### Deploying to Vercel

Set up your project with [Vercel](https://vercel.com/signup)
(choose the GitHub integration).

The `FONTDUE_URL` environment variable must point to a Fontdue endpoint.
