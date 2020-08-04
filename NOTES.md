# Notes

## Links

- https://docs.python.org/3/

## Tips

- The nargs (number of arguments) option to argparse allows you to validate the number of arguments from the user. The asterisk ('*') means zero or more, whereas '+' means one or more.
- If you define an argument using type=argparse.FileType('rt'), argparse will validate that the user has provided a readable text file and will make the value available in your code as an open file handle.
- You can read and write from the standard in/out file handles by using sys.stdin and sys.stdout.

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

Read a file (reads the entire file into memory):

```
fh = open(text)
text = fh.read()
fh.close()
```

Read a file (without reading the entire file into memory):

```
fh = open(text)
for line in fh:
	print(line.upper())
fh.close()
```

Handle text that might be a file of a string:

```
if os.path.isfile(args.text):
	args.text = open(args.text)
else:
	args.text = io.StringIO(args.text + '\n')
```

Handle output to file if specified else to print:

```
out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout
```
