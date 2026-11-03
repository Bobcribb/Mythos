#!/usr/bin/env python3
"""Generate one MYTHOS image using OpenAI Images API; write assets and gallery."""
import base64, json, os, pathlib, urllib.request, urllib.error, time
from datetime import datetime, timezone
root=pathlib.Path(__file__).resolve().parents[1]
items=[
("delphes-apollon","Delphes — sanctuaire et temple d'Apollon","Phocide","IVe siècle av. J.-C."),
("nemee-zeus","Némée — temple de Zeus","Argolide","vers 330 av. J.-C."),
("corinthe-apollon","Corinthe — temple d'Apollon","Corinthie","vers 540 av. J.-C."),
("messene-asklepieion","Messène — Asclépieion","Messénie","IIIe siècle av. J.-C."),
("sounion-poseidon","Sounion — temple de Poséidon","Attique","vers 440 av. J.-C."),
("brauron-artemis","Brauron — sanctuaire d'Artémis","Attique","Ve siècle av. J.-C."),
("dodone-theatre","Dodone — théâtre et sanctuaire de Zeus","Épire","IIIe siècle av. J.-C."),
("bassae-apollon","Bassae — temple d'Apollon Épicourios","Arcadie","vers 420–400 av. J.-C."),
("mycenes-citadelle","Mycènes — porte des Lionnes et citadelle","Argolide","XIIIe siècle av. J.-C."),
("olympie-zeus","Olympie — temple de Zeus","Élide","Ve siècle av. J.-C."),
("epidaure-asclepios","Épidaure — sanctuaire d'Asclépios","Argolide","IVe siècle av. J.-C."),
("epidaure-theatre","Épidaure — théâtre et panorama","Argolide","IVe siècle av. J.-C."),
("tirynthe-citadelle","Tirynthe — palais fortifié mycénien","Argolide","XIIIe siècle av. J.-C."),
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
("priene-agora","Priène — agora","Ionie antique","IVe siècle av. J.-C."),
("samos-heraion","Samos — Héraion et temple de Rhoikos","Samos","vers 570–560 av. J.-C.")
]
# Institutional sources for documented chronology and archaeological context.
# These references do not certify AI-generated details (elevations, polychromy, layout).
references = {
    "delphes-apollon": "https://whc.unesco.org/en/list/393/",
    "nemee-zeus": "https://nemeacenter.berkeley.edu/ancient-nemea/temple-zeus",
    "corinthe-apollon": "https://www.ascsa.edu.gr/excavations/ancient-corinth/about-the-excavations-1",
    "sounion-poseidon": "https://perseus-aa.github.io/items/aa_373.html",
    "bassae-apollon": "https://whc.unesco.org/en/list/392/",
    "mycenes-citadelle": "https://whc.unesco.org/en/list/941/",
    "olympie-zeus": "https://whc.unesco.org/en/list/517/",
    "epidaure-asclepios": "https://whc.unesco.org/en/list/491/",
    "epidaure-theatre": "https://whc.unesco.org/en/list/491/",
    "tirynthe-citadelle": "https://whc.unesco.org/en/list/941/",
    "samos-heraion": "https://whc.unesco.org/en/list/595/",
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
# A monument-level image and an independent panoramic image for each site.
# Never overwrite an existing image or repeat a published slug.
available=[]
for base_slug,site_title,region,period in items:
    for view_kind in ("monument", "panorama"):
        shot_slug=base_slug if view_kind=="monument" else base_slug+"-panorama"
        if shot_slug not in used:
            available.append((shot_slug,base_slug,site_title,region,period,view_kind))
if not available:
    print("All configured sites and panoramas generated; no duplicates.")
    raise SystemExit(0)
slug,base_slug,site_title,region,period,view_kind=available[0]
view_label="Plan large panoramique" if view_kind=="panorama" else "Vue architecturale"
title=(site_title+" — plan large du site") if view_kind=="panorama" else site_title
view_prompt=(
    "EXTREME WIDE ESTABLISHING PANORAMIC SHOT from a plausible elevated natural viewpoint: "
    "show the ancient monument within its full sanctuary or town context, multiple buildings "
    "and terraces only when archaeologically plausible, the local relief, access routes, "
    "and distant landscape. Give the surroundings substantial space, not a close-up of a single façade. "
    "Do not portray conjectural neighboring monuments as certainties. "
    if view_kind=="panorama" else
    "MEDIUM-WIDE ARCHITECTURAL VIEW from a believable visitor viewpoint, emphasizing the "
    "principal monument, its columns or walls and immediate architectural context, with clear depth. "
)
prompt=(f"Photorealistic archaeological 3D-rendered reconstruction of {site_title}, {region}, around {period}. "
    +view_prompt+
    "Single continuous landscape composition in 3:2 format, natural Mediterranean lighting, realistic materials, "
    "historically informed conservative proportions and archaeological restraint. "
    "NO 2.5D diagram, NO axonometric map, NO flat illustration, NO infographic. "
    "No website menu, interface, labels, logos, embedded captions, ornamental frame or fantasy architecture. "
    "An interpretive view, not a metrically exact survey; uncertain reconstruction details must remain restrained."
)
payload={"model":"gpt-image-2","prompt":prompt,"size":"1536x1024","quality":"medium","output_format":"webp","output_compression":85,"n":1}
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
existing.append({"slug":slug,"title":title,"region":region,"period":period,"view_kind":view_kind,"view_label":view_label,"src":"/Mythos/assets/reconstitutions-3d/"+dest.name,"certainty":"Reconstitution interprétative : élévations et couleurs à vérifier","created_at":datetime.now(timezone.utc).date().isoformat(),"source_url":references.get(base_slug),"certainty_level":"Moyen pour la topographie, faible pour les élévations restituées"})
manifest_path.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
from render_reconstitution_gallery import write_gallery
write_gallery(root,existing)
# Link from the existing documented atlas only after an image is generated.
atlas = root / "reconstitutions-3d.html"
if atlas.exists():
    html = atlas.read_text(encoding="utf-8")
    gallery_url = "/Mythos/reconstitutions-photorealistes.html"
    anchor = '</section>\\n<nav class="r3d-subnav"'
    if gallery_url not in html and anchor in html:
        link = '<p><a href="' + gallery_url + '">Voir les reconstitutions photoréalistes effectivement publiées →</a></p>'
        html = html.replace(anchor, link + anchor, 1)
        atlas.write_text(html, encoding="utf-8")

print("Generated",dest)
