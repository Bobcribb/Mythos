#!/usr/bin/env python3
"""Generate one MYTHOS image using OpenAI Images API; write assets and gallery."""
import base64, json, os, pathlib, urllib.request, urllib.error, time
from datetime import datetime, timezone
root=pathlib.Path(__file__).resolve().parents[1]
items=[
("athenes-acropole","Athènes — Acropole classique","Attique","Ve siècle av. J.-C."),
("eleusis-telesterion","Éleusis — Télestérion","Attique","Ve–IVe siècle av. J.-C."),
("delos-sanctuaire","Délos — sanctuaire d'Apollon","Cyclades","IIIe–IIe siècle av. J.-C."),
("knossos-palais","Cnossos — palais minoen","Crète","vers 1450 av. J.-C."),
("phaistos-palais","Phaistos — palais minoen","Crète","IIe millénaire av. J.-C."),
("vergina-palais","Aigai — palais macédonien","Macédoine","IVe siècle av. J.-C."),
("philippes-forum","Philippes — forum","Macédoine","IIe siècle apr. J.-C."),
("samothrace-sanctuaire","Samothrace — sanctuaire des Grands Dieux","Égée du Nord","IIIe siècle av. J.-C."),
("thermos-apollon","Thermos — temple d'Apollon","Étolie","VIIe–VIe siècle av. J.-C."),
("argos-theatre","Argos — théâtre","Argolide","IIIe siècle av. J.-C."),
("olynthe-quartier","Olynthe — quartier résidentiel","Chalcidique","IVe siècle av. J.-C."),
("priene-agora","Priène — agora","Ionie antique","IVe siècle av. J.-C.")
]
# Institutional sources for documented chronology and archaeological context.
# These references do not certify AI-generated details (elevations, polychromy, layout).
references = {
    "athenes-acropole": "https://whc.unesco.org/en/list/404/",
    "delos-sanctuaire": "https://whc.unesco.org/en/list/530/",
    "knossos-palais": "https://whc.unesco.org/en/list/1733/",
    "phaistos-palais": "https://whc.unesco.org/en/list/1733/",
    "vergina-palais": "https://whc.unesco.org/en/list/780/",
    "philippes-forum": "https://whc.unesco.org/en/list/1517/",
    "samothrace-sanctuaire": "https://www.samothrace.emory.edu/excavations/",
}
manifest_path=root/"assets/reconstitutions-3d/photorealistes.json"
manifest_path.parent.mkdir(parents=True,exist_ok=True)
existing=json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else []
used={i["slug"] for i in existing}
available=[item for item in items if item[0] not in used]
if not available:
    print("All configured sites generated; no duplicates.")
    raise SystemExit(0)
slug,title,region,period=available[0]
prompt=(f"Photorealistic archaeological 3D-rendered reconstruction of {title}, {region}, around {period}. "
"One coherent immersive wide architectural view, natural Mediterranean light, realistic stone, landscape and building proportions, "
"historically informed reconstruction with conservative architectural assumptions, no modern buildings. "
"No website menu, no interface, no labels, no logos, no captions, no infographic panels, no fantasy architecture. "
"This is an interpretive artistic reconstruction, not a metrically exact survey.")
payload={"model":"gpt-image-1","prompt":prompt,"size":"1536x1024","quality":"medium","output_format":"webp","output_compression":85,"n":1}
req=urllib.request.Request("https://api.openai.com/v1/images/generations",data=json.dumps(payload).encode(),headers={"Authorization":"Bearer "+os.environ["OPENAI_API_KEY"],"Content-Type":"application/json"},method="POST")
# Diagnose rate limiting versus billing/quota errors without displaying credentials.
result = None
for attempt in range(3):
    try:
        with urllib.request.urlopen(req,timeout=240) as response:
            result=json.load(response)
        break
    except urllib.error.HTTPError as exc:
        try:
            details=json.loads(exc.read().decode("utf-8")).get("error",{})
        except (ValueError, UnicodeDecodeError):
            details={}
        code=str(details.get("code") or details.get("type") or "unknown")
        message=str(details.get("message") or "")[:350].replace("\\n"," ")
        print(f"OpenAI image API HTTP {exc.code}: {code}: {message}",flush=True)
        # A depleted billing balance is not a transient rate limit.
        if exc.code == 429 and code in ("rate_limit_exceeded","rate_limit_error","requests_rate_limit_exceeded") and attempt < 2:
            time.sleep(20 * (attempt + 1))
            continue
        raise SystemExit("API image generation not completed; no image or gallery was published.")
if result is None:
    raise SystemExit("Generation unavailable; nothing published.")
raw=base64.b64decode(result["data"][0]["b64_json"])
dest=root/"assets/reconstitutions-3d"/(slug+".webp")
dest.write_bytes(raw)
existing.append({"slug":slug,"title":title,"region":region,"period":period,"src":"/assets/reconstitutions-3d/"+dest.name,"certainty":"Reconstitution interprétative : élévations et couleurs à vérifier","created_at":datetime.now(timezone.utc).date().isoformat(),"source_url":references.get(slug),"certainty_level":"Moyen pour la topographie, faible pour les élévations restituées"})
manifest_path.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
from html import escape
cards="".join('<article><img loading="lazy" src="'+escape(x["src"])+'" alt="'+escape(x["title"])+'"><h2>'+escape(x["title"])+'</h2><p>'+escape(x["region"])+' · '+escape(x["period"])+'</p><p>'+escape(x.get("certainty_level", "Certitude non réévaluée"))+'</p><p>'+escape(x["certainty"])+'</p>'+('<p><a target="_blank" rel="noopener noreferrer" href="'+escape(x["source_url"])+'">Source institutionnelle</a></p>' if x.get("source_url") else '<p>Référence institutionnelle à compléter</p>')+'</article>' for x in existing)
page='<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>MYTHOS — Reconstitutions photoréalistes</title><style>body{background:#0c0e10;color:#eee0c1;margin:0;font-family:Georgia,serif}header{text-align:center;padding:3rem 1rem;border-bottom:1px solid #aa8744}h1,h2{color:#dfba71}main{max-width:1250px;margin:auto;padding:2rem 1rem;display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:1.4rem}article{padding:1rem;border:1px solid #9b7b40;background:#17191b}img{width:100%;height:auto}a{color:#dfba71}</style></head><body><header><h1>MYTHOS — Reconstitutions 3D photoréalistes</h1><p>Illustrations interprétatives, non modèles interactifs ni relevés métriques</p><a href="/reconstitutions-3d.html">Consulter les notices scientifiques</a></header><main>'+cards+'</main></body></html>'
(root/"reconstitutions-photorealistes.html").write_text(page,encoding="utf-8")
print("Generated",dest)
