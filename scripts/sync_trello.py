"""Export approved Trello projects to the public site without exposing private notes."""

import json
import os
import urllib.parse
import urllib.request
from pathlib import Path

BOARD_ID = "69a1b1f30ef01b6f565f195e"
PUBLIC_LIST = "69a1b1f30ef01b6f565f1954"
OUTPUT = Path(__file__).resolve().parents[1] / "data" / "collaborations.json"


def trello(endpoint, key, token):
    query = urllib.parse.urlencode({"key": key, "token": token})
    separator = "&" if "?" in endpoint else "?"
    request = urllib.request.Request(f"https://api.trello.com/1/{endpoint}{separator}{query}")
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.load(response)


def fields(description):
    result = {}
    for line in description.splitlines():
        if ":" in line and not line.startswith("#"):
            key, value = line.split(":", 1)
            result[key.strip().casefold()] = value.strip()
    return result


def public_url(value):
    url = urllib.parse.urlparse(value)
    return value if url.scheme == "https" and url.hostname and not url.username and not url.password else ""


def export(cards):
    projects = []
    for card in cards:
        if card.get("closed") or card.get("idList") != PUBLIC_LIST:
            continue
        data = fields(card.get("desc", ""))
        if data.get("accord de publication obtenu auprès des artistes", "").casefold() != "oui":
            continue
        title = data.get("titre public", "")
        artists = data.get("artistes", "")
        summary_fr = data.get("résumé fr", "")
        summary_en = data.get("summary en", "")
        if not all((title, artists, summary_fr, summary_en)):
            continue
        bpm = data.get("bpm", "")
        if bpm and (not bpm.isdigit() or not 40 <= int(bpm) <= 300):
            bpm = ""
        projects.append({
            "title": title[:140],
            "artists": artists[:200],
            "genre": data.get("genre", "")[:80],
            "bpm": bpm,
            "summaryFr": summary_fr[:600],
            "summaryEn": summary_en[:600],
            "image": public_url(data.get("visuel public (url https autorisée)", "")),
            "listenUrl": public_url(data.get("lien d'écoute public (url https)", "")),
        })
    return projects


def main():
    key = os.environ["TRELLO_API_KEY"]
    token = os.environ["TRELLO_TOKEN"]
    cards = trello(f"boards/{BOARD_ID}/cards?fields=idList,closed,desc,name", key, token)
    result = export(cards)
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Exported {len(result)} approved projects")


if __name__ == "__main__":
    main()
