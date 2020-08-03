# Notes

## Links

- https://docs.python.org/3/

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

Get type of variable:

```
type(word)
```

Get character of string:

```
word = "hej"
word[0] # h
word[2] # j
word[-1] # j
word[:2] # he
```

Get length of string:

```
len('hej') # 3
```

Get help in repl:

```bash
python3
help(str)
```
