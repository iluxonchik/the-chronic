# The Chronic

The Chronic is a tool that combines/permutes words from a dictionary to generate passwords that are a composition/permutation of dictionary words. I could not find anything that would be simple and straighforward to use,
so I wrote my own tool.

It's a useful program for penentration testing when you're bruteforcing passwords. It's based on the fact that many people use a combination of dictionary words as their passwords. You provide it with a file containing
a list of words, one per line. The tool will output the combinations of those words.

# Requirements

* `Python 3.x`

# Usage

```
usage: thechronic.py [-h] [--min MIN] [--max MAX] [-n NUM_WORDS] [-b]
                     [files [files ...]]

Generate passwords by combining words from provided files(s)

positional arguments:
  files                 File(s) to load the words from.

optional arguments:
  -h, --help            show this help message and exit
  --min MIN             Minimum output word length.
  --max MAX             Maximum output word length.
  -n NUM_WORDS, --num_words NUM_WORDS
                        Number of words to combine.
  -b, --no_build_up     Don't build up number of word combinations. This means
                        that if you provide the value 3 for the '-n' argument,
                        only words which are a combination of 3 words will be
                        genrated, otherwise all words from combination of 1 to
                        3 words will be.

```

# Examples

Let's say you have a `words.txt` file with the following content:

```
still
dre
day
```

Running `python thechronic.py words.txt - n 3` will produce the following (all possilbe combinations from `1` up to `3`
with the words in `words.txt`):

```
still
dre
day
stillstill
stilldre
stillday
drestill
dredre
dreday
daystill
daydre
dayday
stillstillstill
stillstilldre
stillstillday
stilldrestill
stilldredre
stilldreday
stilldaystill
stilldaydre
stilldayday
drestillstill
drestilldre
drestillday
dredrestill
dredredre
dredreday
dredaystill
dredaydre
dredayday
daystillstill
daystilldre
daystillday
daydrestill
daydredre
daydreday
daydaystill
daydaydre
daydayday
```

Running `python thechronic.py words.txt - n 3 -b` will produce all possible combinations consisting of `3` words only:

```
stillstillstill
stillstilldre
stillstillday
stilldrestill
stilldredre
stilldreday
stilldaystill
stilldaydre
stilldayday
drestillstill
drestilldre
drestillday
dredrestill
dredredre
dredreday
dredaystill
dredaydre
dredayday
daystillstill
daystilldre
daystillday
daydrestill
daydredre
daydreday
daydaystill
daydaydre
daydayday
```
Running `python thechronic.py words.txt - n 3 -min 7 -b` will produce all possible combinations consisting of `3` words only wich have a length of `7` characters or more:

```
stillstill
stilldre
stillday
drestill
daystill
stillstillstill
stillstilldre
stillstillday
stilldrestill
stilldredre
stilldreday
stilldaystill
stilldaydre
stilldayday
drestillstill
drestilldre
drestillday
dredrestill
dredredre
dredreday
dredaystill
dredaydre
dredayday
daystillstill
daystilldre
daystillday
daydrestill
daydredre
daydreday
daydaystill
daydaydre
daydayday
```
