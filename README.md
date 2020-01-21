# fontdue-python-demo

Install

```shell
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

Run

```
$ flask run
```

The app should start at [http://localhost:5000](http://localhost:5000)


# Deploying to Now.sh

The `GRAPHQL_URL` environment variable must point to a Fontdue graphql endpoint.

``` shell
now secrets add graphql-url "https://example.fontdue.com/graphql"
now --prod
```
