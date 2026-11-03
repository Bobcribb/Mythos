#!/usr/bin/env python3
"""Shared MYTHOS photorealistic gallery renderer: keeps captions, sources and scholarship across scheduled generations and imports."""
from html import escape
from pathlib import Path

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
    title = escape(x.get("title", "Monument antique"))
    src = escape(x["src"], quote=True)
    region = escape(x.get("region", ""))
    period = escape(x.get("period", ""))
    view = escape(x.get("view_label", "Vue architecturale"))
    caption = escape(x.get("caption", "Reconstitution numérique photoréaliste interprétative."))
    base_slug = x["slug"].removesuffix("-panorama")
    commentary = escape(x.get("commentary") or site_comments.get(base_slug,
        "Reconstitution visuelle interprétative fondée sur la documentation du site. La topographie de détail et les décors sont susceptibles de correction."))
    limits = escape(x.get("limits", "Élévations, couleurs et bâtiments secondaires restent hypothétiques : les sources ne valident pas à elles seules les détails de cette image."))
    certainty = x.get("certainty_notes")
    if isinstance(certainty, dict):
        confidence = ("<p><strong>Certitude élevée :</strong> " + escape(certainty.get("eleve","")) + "</p>"
                    + "<p><strong>Certitude moyenne :</strong> " + escape(certainty.get("moyen","")) + "</p>"
                    + "<p><strong>Certitude faible :</strong> " + escape(certainty.get("faible","")) + "</p>")
    else:
        confidence = "<p><strong>Degré de certitude :</strong> " + escape(x.get("certainty_level", "Hypothétique pour les détails de restitution.")) + "</p>"
    sources = list(x.get("institutional_sources") or [])
    if x.get("source_url") and not any(s.get("url")==x["source_url"] for s in sources):
        sources.insert(0, {"url":x["source_url"],"name":"Source institutionnelle"})
    source_links = " · ".join(
        '<a href="'+escape(s["url"],quote=True)+'" target="_blank" rel="noopener noreferrer">'+escape(s.get("name","Source institutionnelle"))+'</a>'
        for s in sources if s.get("url","").startswith("https://")
    )
    source_html = '<p><strong>Sources :</strong> '+source_links+'</p>' if source_links else '<p>Source institutionnelle spécifique à compléter.</p>'
    panoramic = ' panorama' if x.get("view_kind")=="panorama" or x["slug"].endswith("-panorama") else ''
    return ('<article class="mythos-image'+panoramic+'"><figure><a href="'+src+'" target="_blank" rel="noopener noreferrer">'
        '<img loading="lazy" decoding="async" src="'+src+'" alt="'+title+' — reconstitution 3D photoréaliste interprétative"></a>'
        '<figcaption><strong>'+title+'</strong><span>'+view+' · '+region+' · '+period+'</span>'
        '<p><strong>Légende.</strong> '+caption+'</p></figcaption></figure>'
        '<section class="science"><h3>Commentaire archéologique</h3><p>'+commentary+'</p>'
        +confidence+'<p><strong>Limites :</strong> '+limits+'</p>'+source_html
        +'<p class="disclaimer">Illustration numérique contemporaine ; les institutions citées ne valident pas cette image.</p>'
        '</section></article>')

def write_gallery(root, items):
    root=Path(root)
    cards="\n".join(render_card(x) for x in sorted(items,
        key=lambda x:(x.get("created_at",""),x.get("view_kind")=="panorama"),reverse=True))
    page = '''<!doctype html><html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>MYTHOS — Reconstitutions 3D photoréalistes</title>
<style>
:root{color-scheme:dark}*{box-sizing:border-box}
body{background:#0c0e10;color:#eee0c1;margin:0;font:17px/1.6 Georgia,serif}
header{text-align:center;padding:3rem 1rem;border-bottom:1px solid #9b7b40}
header p{max-width:850px;margin:1rem auto;color:#cdbd9d}
h1{font-size:clamp(2rem,4vw,3.4rem);line-height:1.15;margin:.2rem;color:#dfba71}
a{color:#dfba71}
main{max-width:1450px;margin:auto;padding:2rem 1rem 4rem;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,510px),1fr));gap:1.6rem}
article{border:1px solid #9b7b40;background:#17191b;overflow:hidden}
article.panorama{grid-column:1/-1}
figure{margin:0}figure>a{display:block}img{display:block;width:100%;height:auto}
figcaption{padding:1rem 1.3rem;display:grid;gap:.3rem}
figcaption strong{color:#e9c581;font-size:1.35rem;font-weight:normal}
figcaption span{font-size:.95rem;color:#cfc2a5}
figcaption p{margin:.4rem 0 0}
.science{padding:.4rem 1.3rem 1.2rem;border-top:1px solid #61512e}
.science h3{font-size:1.15rem;color:#e7c689;font-weight:normal;margin:.8rem 0}
.science p{margin:.6rem 0}
.disclaimer{color:#bcae96;font-size:.83rem}
</style></head><body><header><h1>MYTHOS — Reconstitutions 3D photoréalistes</h1>
<p>Monuments et panoramas archéologiques. Légendes, commentaires scientifiques, sources et degrés de certitude sont présentés sous chaque image, sans inscription dans le visuel.</p>
<a href="/Mythos/reconstitutions-3d.html">Consulter les notices archéologiques détaillées</a></header><main>'''
    page+=cards+"</main></body></html>"
    (root/"reconstitutions-photorealistes.html").write_text(page,encoding="utf-8")
