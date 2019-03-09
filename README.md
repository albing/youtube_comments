# Youtube Comments Word Counter

> Counts words for you, so you don't have to.

### Info

Creates a lot of `savedata*.dat` files; use those for recovery, or delete them, see if I care.

The one you do want to save is results.dat - it's a json dump of the unadulterated words dict.

### Requirements

There needs to be a key in `$API_KEY`.  Here's how to get one: [https://developers.google.com/youtube/v3/getting-started]

I store mine in a file called `secrets` (see [secrets.example](secrets.example) ) and `source` it.

Also, there's a `requirements.txt` file to `pip install -r` after you've `python -m venv venv` -ed and `source venv/bin/activate` -ed.

### Example

video id: [EoiyJXsNerI](https://www.youtube.com/watch?v=EoiyJXsNerI)

```
trudeau                                 11
for                                     13
the                                     32
of                                      24
and                                     27
to                                      21
i                                       18
he                                      14
is                                      17
a                                       22
that                                    15
```
