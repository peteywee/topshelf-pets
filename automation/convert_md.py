#!/usr/bin/env python3
import os, sys, pathlib
try:
    import markdown
except ImportError:
    print("Install dependency first: pip install markdown", file=sys.stderr); sys.exit(1)

SRC = pathlib.Path("content/blogs")
DST = pathlib.Path("site/blogs")
DST.mkdir(parents=True, exist_ok=True)

for name in os.listdir(SRC):
    if name.endswith(".md"):
        md = (SRC/name).read_text(encoding="utf-8")
        body = markdown.markdown(md, extensions=["fenced_code","tables"])
        html = f'<!doctype html><meta charset="utf-8"><link rel="stylesheet" href="/styles.css"><div class="container card">{body}</div>'
        (DST/name.replace(".md",".html")).write_text(html, encoding="utf-8")
        print("Converted", name)
print("Done.")
