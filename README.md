# Python - Week 3

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
