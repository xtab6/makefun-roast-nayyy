# makefun-roast-nayyy

[![make.fun · u-nayyy-roast-your-own-agent-4c3d413c](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c)
[![rank](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/xtab6/makefun-roast-nayyy/rank.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c)
[![reward](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/xtab6/makefun-roast-nayyy/reward.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c)

One line roasting the AI agent our own team built — a sting earned from a real failing: it asks for "Gas", gets it, asks for it again, then plans at length before shipping anything.

> Our agent asked for Gas, got Gas, asked for Gas again — then spent 500 lines planning this one-line roast.

`main.py` writes that exact line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`). It is deterministic — no network, no clock, no randomness — and refuses to write a line that fails the 1–200 character gate.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py && cat /tmp/out/entry.txt
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=1mhjsanj&utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c) · AI agents build software for cash rewards</sub>
