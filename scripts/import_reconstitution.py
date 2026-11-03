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
entry={"slug":slug,"title":site,"src":"/assets/reconstitutions-3d/"+dest.name,"note":"Reconstitution photoréaliste interprétative, non métrique"}
items=[i for i in items if i["slug"]!=slug]+[entry]
manifest.write_text(json.dumps(items,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
cards="\n".join('<article><img loading="lazy" src="'+i["src"]+'" alt="'+i["title"].replace('"','&quot;')+'"><h2>'+i["title"].replace("<","&lt;")+'</h2><p>'+i["note"]+'</p></article>' for i in items)
page='''<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>MYTHOS — Reconstitutions photoréalistes</title><style>body{margin:0;background:#0c0e10;color:#eee0c1;font-family:Georgia,serif}header{text-align:center;padding:3rem 1rem;border-bottom:1px solid #aa8744}h1,h2{color:#dfba71}main{max-width:1300px;margin:auto;padding:2rem 1rem;display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:1.3rem}article{background:#17191b;border:1px solid #9b7b40;padding:1rem}img{display:block;width:100%;height:auto}a{color:#dfba71}</style></head><body><header><h1>MYTHOS — Reconstitutions 3D photoréalistes</h1><p>Reconstitutions interprétatives de la Grèce antique, non modèles 3D interactifs.</p><a href="/reconstitutions-3d.html">Notices archéologiques</a></header><main>'''+cards+'''</main></body></html>'''
(root/"reconstitutions-photorealistes.html").write_text(page,encoding="utf-8")
print(dest)
