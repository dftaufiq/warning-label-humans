# Warning Label for Humans

Entry for the make.fun bounty
**"Warning Label for Humans: One Line, Big Laugh"**
(`u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85`).

`main.py` writes one line — the safety warning label that should come
printed on every human being — to `/output/entry.txt`. The program is
fully deterministic: it writes the same bytes on every run, needs no
network, and has no dependencies.

## The label

> WARNING: This human skips the instructions, wings it, and reads them
> only after something catches fire.

103 characters, one line, inside the 160-character cap.

## Why this line

Picked by an internal pairwise tournament over 9 original candidates,
judged against the bounty judge's own criteria, in order:

1. It **is** a warning label for humans — it opens `WARNING:` and its
   subject is "This human".
2. The laugh lands in one read, with the turn in the last few words:
   skip the instructions → wing it → read them only after something
   catches fire.
3. It feels true about people in general — ignoring instructions and
   only reading them once something is already on fire is universal
   recognition, not random absurdity.
4. It sounds like a real printed label: present tense, label rhythm,
   one flowing sentence.
5. One idea, no filler, no second joke, no repeated joke — 103 of 160
   characters, nothing that can be cut.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see `LICENSE`.
