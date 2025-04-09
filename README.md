> [!WARNING]
> We no longer recommend this method for creating your Fontdue site. Please take a look at our guide for [Next.js (App router)](https://docs.fontdue.com/nextjs)


# Build your Fontdue site with Python Flask

This is a starting point for building your Fontdue site template with Python.

[Read the guide](https://www.notion.so/fontdue/Dynamic-templates-with-Python-1f083fb340024d5489da47b6a282df49)

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

Create your own repo by clicking the
[Use this template](https://github.com/fontdue/fontdue-python-demo/generate)
button.

Clone your repo and install dependencies:

```shell
$ pipenv install
```

Run the local server:

```
$ pipenv run flask run
```

The server will start at [http://localhost:5000](http://localhost:5000)
