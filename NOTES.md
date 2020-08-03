# Notes

## Tools

Run tests:

```
pytest -xv test.py
```

Run lint:

```
pylint hello.py
```

## Tricks

Make executable:

```
chmod +x hello.py
```

Add to PATH:

```
mkdir ~/bin
cp 01_hello/hello.py ~/bin
PATH=~/bin:$PATH
```
