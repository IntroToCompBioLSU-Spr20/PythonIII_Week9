# Python - Week 3

## While loops

- Sometimes we want to do something repetitively, but we don't know ahead of time how many times we need to repeat it (as in a `for` loop.
- In these cases, we can use a `while` loop. A `while` loop will continue to do something until a certain condition is no longer satisfied.

```
num = 0
while num < 10:
    print(num)
    num += 1
```

- WARNING - You need to make sure to update variables such that the condition will eventually be satisified. If you don't, you could create an infinite loop!

## Dictionaries

- Dictionaries are incredibly useful for storing pairs of things - known as "keys" and "values"
- They don't store these pairs in a particular order, like lists do, but they make looking up values from keys much faster.
- The keys and values can each be different types of variables
- To create a new dictionary, you can use this syntax:
    - `myDict = {"keyOne":"valueOne", "keyTwo":"valueTwo"}`
- To look at the methods available for dictionaries, try this:
    - `dir(myDict)`
- You can access a value, as long as you know its key, either of these ways:
    - `myDict.get("keyOne")`
    - `myDict["keyOne"]`
- You can change a value using its key, this way:
    - `myDict["keyOne"] = <NEW_VALUE>`
- You can add a new key/value pair using the update method:
    - `myDict.update({<NEW_KEY:NEW_VALUE})`


## Importing libraries and drawing random numbers

- Sometimes it will be helpful to use functionality that's not part of the core python functionality.
- Thankfully, python has a built-in way to import new functions that other people have written to extend the core functions
- Once you know the name of a library, you can use the `import` command to load it (if it's already been installed).
- One library that we're going to use today is called `random`.
- Once it's loaded, you'll need to precede any of its functions with `random.` in order to use them.
- Try this:
    - `import random`
    - `random.random()` - Do this a few times
    - `random.uniform(0,1)` - Do this a few times
    - `random.uniform(0,5)` - Do this a few times
    - `random.choice([5,6,7,8])` - Do this a few times
    - `firstList`
    - `random.shuffle(firstList)`
    - `firstList`
    - `random.shuffle(firstList)`
    - `firstList`
    - `random.shuffle(firstList)`
    - `firstList`

## Reading from files

- To read or write from a file, you'll first need to define the file name
    - e.g., `inFileName = "FileToRead.txt"`
- However, this is just a string variable with the file name. We need to create an object that can actually read the contents of a file.
- Python has a built-in function to create a file object - `open(<FILENAME>,<MODE>)`
- The `<FILENAME>` argument is just a string with the file's name (or path to the file)
- The `<MODE>` argument tells Python whether we are reading from a file (`r`), writing to a file (`w`), or appending to a file (`a`).
- To open up a new File object to read file contents, use syntax like this:
    - `inFile = open(inFileName,'r')`
- There are several useful methods associated with file objects, but one of the most commonly used is `readline()`. This method will read lines one-by-one from the file. Note that the end of line character (\n) is retained when the line is read in.
    - `firstLine = inFile.readline()`
- Files opened for reading can be used in a `for` loop, as follows, to go through all the lines in the file:

```
        for line in file:
            print("Length of line is: %d" % (len(line)))
```

- Note that `line` is just a variable name we've chosen to hold each line as we iterate through the file. You can use any variable name you choose, as with any other `for` loop.


## Writing to Files

- Writing to a file is very similar to reading from a file. First, you define an output file name
    - `outFileName = "FileToWrite.txt"`
- To create a file object to use for writing, we'll again use the `open()` function, but we'll specify `'w'` for the `<MODE>`.
    - `outFile = open(outFileName,'w')`
- To write to the file line-by-line, we can use the `.write()` method.
    - `outFile.write("This is a new sentence.\n")`
    - Note that the `write()` method does NOT, by default, add a new line character to strings. If we want to end a line, we have to explicitly include `\n`.


## Command-line Arguments
  
- As with bash scripts, Python scripts can also take advantage of command-line arguments.
- To easily deal with command-line arguments, we're going to take advantage of some functions in the `sys` library. So we'll need to start by importing that library:
    - `import sys`
- Any command-line arguments we pass to a script can then be accessed using the `sys.argv` variable.
    - `print(sys.argv[2])`
    - Which argument is printed when you run the line above? Does that make sense with the 0-based indexing in Python?
- We can also loop through all command-line arguments:
        for arg in sys.argv:
            print(arg)
- These abilities are very useful in a variety of contexts, but particularly when a set of filenames are provided as command-line arguments and you want to iteratively process each file.

