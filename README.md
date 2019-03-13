# Youtube Comments Word Counter

> Counts words for you, so you don't have to.

### Info

Creates a lot of `savedata*.dat` files; use those for recovery, or delete them, see if I care.

The one you do want to save is results_<video_key>.dat - it's a json dump of the unadulterated words object.

### Requirements

There needs to be a key in `$API_KEY`.  Here's how to get one: [https://developers.google.com/youtube/v3/getting-started]

I store mine in a file called `secrets` (see [secrets.example](secrets.example) ) and `source` it.

Also, there's a `requirements.txt` file to `pip install -r` after you've `python -m venv venv` -ed and `source venv/bin/activate` -ed.

### How To Run It

1. Set `$API_KEY` and edit `main.py` to change `video_id`

2. Run the script to download the comments

    `python main.py`

3. Clean up the mess it made

    `rm savedata*.dat`

4. Run the random walker

    `python walker.py results_<video_id>.dat <start_word>`

### Example

video id: [EoiyJXsNerI](https://www.youtube.com/watch?v=EoiyJXsNerI)

```
there appear to montreal this turns out such little bit problem solved by hinging off things especially more joke i ironic slogan let jody that fans
```

```
no doubt that living costs them drugs rock
```

```
see ours have captions
```

```
the roadblocks for these huge upset i digress asides 1if youre happy as you’re talking faster in things it might recall her her at issue with illegal pressure regardless life for far less worried over 200 canadian to toss him call bs everything he stole his politics atm
```
