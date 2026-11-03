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
from html import escape
# Scientific captions are kept in HTML below the photographs, never embedded into the image.
# These summaries refer to the monuments; they do not certify the generated visual details.
site_comments={
"delphes-apollon":"Le temple dorique d’Apollon appartient au sanctuaire panhellénique de Delphes. Le plan et la reconstruction au IVe siècle sont documentés ; les statues, couleurs et édifices voisins ne sont pas restitués avec certitude.",
"nemee-zeus":"Le temple de Zeus, reconstruit au IVe siècle av. J.-C., présente une colonnade dorique extérieure et des ordres intérieurs distincts. La topographie et les décors de la scène restent interprétatifs.",
"corinthe-apollon":"Le temple archaïque d’Apollon, daté du VIe siècle av. J.-C., conserve des colonnes monolithes doriques. L’apparence complète du toit et des couleurs est proposée à titre illustratif.",
"messene-asklepieion":"L’Asclépiéion de Messène associait culte, vie civique et monuments publics. Son plan hellénistique est documenté, mais les couvertures et les aménagements restitués demeurent hypothétiques.",
"sounion-poseidon":"Le temple dorique de Poséidon domine le cap Sounion. Le plan est connu ; la polychromie, l’élévation intégrale et les détails paysagers de la scène sont interprétatifs.",
"brauron-artemis":"Le sanctuaire d’Artémis à Brauron comprenait un temple et des portiques dont la chronologie et les états construits demandent prudence. Les éléments non attestés sont présentés comme hypothèses.",
"dodone-theatre":"Dodone associait le sanctuaire oraculaire de Zeus à un ensemble monumental développé en plusieurs phases. Le théâtre et les reliefs sont documentés, les détails de restitution demeurent hypothétiques.",
"bassae-apollon":"Le temple d’Apollon Épikourios présente un péristyle dorique et une organisation intérieure exceptionnelle. La toiture, la lumière intérieure et les couleurs reconstruites restent incertaines.",
"mycenes-citadelle":"La citadelle mycénienne est célèbre pour ses murailles cyclopéennes et la Porte des Lionnes. Les parties hautes du palais et les décors proposés n’ont pas la précision d’un relevé archéologique.",
"olympie-zeus":"Le sanctuaire d’Olympie comprenait le grand temple dorique de Zeus. L’architecture fondamentale est documentée ; l’ensemble des peintures et équipements restitués n’est pas assuré.",
"epidaure-asclepios":"Le sanctuaire d’Asclépios à Épidaure se développa autour de monuments de guérison, de culte et de représentation. Leur topographie générale est connue mais plusieurs élévations sont restituées.",
"epidaure-theatre":"Le théâtre d’Épidaure possède des vestiges exceptionnellement lisibles. Les gradins et l’implantation sont documentés, contrairement aux couleurs et détails de l’environnement ancien.",
"tirynthe-citadelle":"À Tirynthe, les remparts cyclopéens et certains dispositifs du palais mycénien sont attestés. Les toitures, étages et peintures proposés constituent des hypothèses.",
"athenes-acropole":"L’Acropole classique résulte de plusieurs programmes architecturaux du Ve siècle av. J.-C. Les bâtiments et la topographie de l’Attique ne sont pas une restitution métrique dans cette image.",
}
def render_card(x):
    site_slug=x["slug"].removesuffix("-panorama")
    commentary=escape(site_comments.get(site_slug,
        "Reconstitution visuelle interprétative fondée sur la documentation générale du site. La topographie de détail, les décors, les teintes et les personnages ne sont pas garantis."))
    source=x.get("source_url")
    source_html=('<p><a target="_blank" rel="noopener noreferrer" href="'+escape(source,quote=True)+'">Source institutionnelle ou scientifique ↗</a></p>' if source else '<p>Référence institutionnelle spécifique à compléter avant validation scientifique.</p>')
    label=escape(x.get("view_label","Vue architecturale"))
    return ('<article class="mythos-image"><figure><img loading="lazy" decoding="async" src="'+escape(x["src"],quote=True)+'" alt="'+escape(x["title"],quote=True)+'">'
       '<figcaption><strong>'+escape(x["title"])+'</strong><span>'+label+' · '+escape(x["region"])+' · '+escape(x["period"])+'</span></figcaption></figure>'
       '<details><summary>Notice scientifique, sources et certitude</summary>'
       '<p>'+commentary+'</p><p><strong>Certitude :</strong> '+escape(x.get("certainty_level","Topographie à contrôler ; détails de restitution hypothétiques"))+'</p>'
       '<p><strong>Limites :</strong> restitution interprétative non métrique ; aucun détail généré n’est validé par la seule citation de la source.</p>'
       +source_html+'</details></article>')
cards="\n".join(render_card(x) for x in existing)
page=('''<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>MYTHOS — Reconstitutions photoréalistes</title>
<style>
:root{color-scheme:dark}*{box-sizing:border-box}
body{background:#0c0e10;color:#eee0c1;margin:0;font:17px/1.6 Georgia,serif}
header{text-align:center;padding:3rem 1rem;border-bottom:1px solid #9b7b40}
header p{max-width:850px;margin:1rem auto;color:#cdbd9d}
h1{font-size:clamp(2rem,4vw,3.4rem);line-height:1.15;margin:.2rem;color:#dfba71}
a{color:#dfba71}main{max-width:1390px;margin:auto;padding:2rem 1rem 4rem;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,510px),1fr));gap:1.6rem}
article{border:1px solid #9b7b40;background:#17191b;overflow:hidden}
figure{margin:0}img{display:block;width:100%;height:auto}
figcaption{padding:1rem 1.2rem;display:grid;gap:.3rem}
figcaption strong{color:#e9c581;font-size:1.35rem;font-weight:normal}
figcaption span{font-size:.95rem;color:#cfc2a5}
details{padding:.9rem 1.2rem;border-top:1px solid #61512e}
summary{color:#e7c689;cursor:pointer}details p{margin:.7rem 0}
</style></head><body>
<header><h1>MYTHOS — Reconstitutions 3D photoréalistes</h1>
<p>Vues monumentales et plans larges des sites antiques grecs. Les légendes, notices et sources sont séparées des images. Reconstitutions numériques interprétatives, sans prétention de précision métrique.</p>
<a href="/Mythos/reconstitutions-3d.html">Consulter les notices archéologiques détaillées →</a></header><main>'''
+cards+'</main></body></html>')
(root/"reconstitutions-photorealistes.html").write_text(page,encoding="utf-8")
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
