#!/usr/bin/env python3
"""Import a trusted image URL and update a MYTHOS photorealistic gallery."""
import json, os, pathlib, urllib.request, urllib.parse
from PIL import Image
from io import BytesIO
root=pathlib.Path(__file__).resolve().parents[1]
url=os.environ["IMAGE_URL"]
site=os.environ["SITE_NAME"].strip()
slug=os.environ["SITE_SLUG"].strip()
if not url.startswith("https://"): raise SystemExit("HTTPS required")
if not slug or any(c not in "abcdefghijklmnopqrstuvwxyz0123456789-" for c in slug): raise SystemExit("Invalid slug")
request=urllib.request.Request(url,headers={"User-Agent":"MYTHOS-publisher/1.0"})
with urllib.request.urlopen(request,timeout=45) as response:
    if response.headers.get("Content-Length") and int(response.headers["Content-Length"])>20000000: raise SystemExit("File too large")
    data=response.read(20000001)
if len(data)>20000000: raise SystemExit("File too large")
im=Image.open(BytesIO(data)); im.verify()
im=Image.open(BytesIO(data)).convert("RGB")
if im.width<600 or im.height<350: raise SystemExit("Resolution too small")
folder=root/"assets"/"reconstitutions-3d"; folder.mkdir(parents=True,exist_ok=True)
dest=folder/(slug+".webp")
im.save(dest,"WEBP",quality=85,method=5)
manifest=folder/"photorealistes.json"
items=json.loads(manifest.read_text(encoding="utf-8")) if manifest.exists() else []
previous=next((i for i in items if i.get("slug")==slug),{})
entry=dict(previous)
entry.update({"slug":slug,"title":site,"src":"/Mythos/assets/reconstitutions-3d/"+dest.name})
entry.pop("note",None)
source_url=os.getenv("SOURCE_URL","").strip()
if source_url:
    if not source_url.startswith("https://"): raise SystemExit("La source institutionnelle doit être une URL HTTPS")
    entry["source_url"]=source_url
items=[i for i in items if i["slug"]!=slug]+[entry]
manifest.write_text(json.dumps(items,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
from render_reconstitution_gallery import write_gallery
write_gallery(root,items)
print(dest)
