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

The `FONTDUE_URL` environment variable must point to a Fontdue endpoint.

``` shell
now secrets add fontdue-url "https://example.fontdue.com"
now --prod
```
