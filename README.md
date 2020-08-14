# fontdue-python-demo

Install

```shell
$ pipenv install
```

Run

```
$ pipenv run flask run
```

The app should start at [http://localhost:5000](http://localhost:5000)


# Deploying to Now.sh

The `FONTDUE_URL` environment variable must point to a Fontdue endpoint.

``` shell
now secrets add fontdue-url "https://example.fontdue.com"
now --prod
```
