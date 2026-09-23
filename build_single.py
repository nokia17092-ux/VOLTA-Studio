#!/usr/bin/env python3
"""Inline ./assets/*.ogg into index.html -> one self-contained volta-studio.html"""
import base64, json, os, re, sys
here = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(here, "index.html"), encoding="utf-8").read()
adir = os.path.join(here, "assets")
files = sorted(f for f in os.listdir(adir) if f.endswith(".ogg"))
blob = {f: "data:audio/ogg;base64," + base64.b64encode(open(os.path.join(adir, f), "rb").read()).decode() for f in files}
decl = re.compile(r"// In this source layout.*?\n// build_single\.py.*?\nconst ASSET_DATA = new Proxy.*?/\*ASSET_DATA_END\*/", re.S)
out = decl.sub(lambda m: "const ASSET_DATA = " + json.dumps(blob, ensure_ascii=False, separators=(",", ":")) + ";", src, count=1)
dst = sys.argv[1] if len(sys.argv) > 1 else os.path.join(here, "volta-studio.html")
open(dst, "w", encoding="utf-8").write(out)
print("written", dst, len(out), "bytes")
