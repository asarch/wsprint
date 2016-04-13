# wsprint
WeasyPrint front-end with own CSS style written in Python

## Dependencies

In Debian-based distros, install them:

```shell
apt-get install python-dev libffi-dev libxslt1-dev zlib1g-dev
```

## Preparing the virtual environment

Create it:

```
$ virtualenv --verbose --no-site-packages alpha
```

Activate the enviroment:

```
$ cd alpha && . bin/activate
```

Install WeasyPrint and the Jinja2 template system:

```
(alpha)$ pip --verbose install jinja2 weasyprint
```

## Render the documents

To render a document:

```
(alpha)$ ./wsprint.py document.html
```

To render a document from URL:

```
(alpha)$ ./wsprint.py --url "https://en.wikipedia.org/w/index.php?title=Python_%28programming_language%29&printable=yes"
```
