# OKEY & Mahjong Printables

Free, reusable forms for a real game night: agree the rules, record OKEY scores, track Mahjong points, plan seating and keep an external-care log. No account or purchase is needed. Download the PDF and print only the pages you need.

## Download / 下载 / İndir / Herunterladen

| Language | Five-page A4 pack | Instructions |
|---|---|---|
| English | [PDF](output/pdf/game-night-pack-en.pdf) | [English](docs/en.md) |
| 简体中文 | [PDF](output/pdf/game-night-pack-zh.pdf) | [简体中文](docs/zh.md) |
| Türkçe | [PDF](output/pdf/game-night-pack-tr.pdf) | [Türkçe](docs/tr.md) |
| Deutsch | [PDF](output/pdf/game-night-pack-de.pdf) | [Deutsch](docs/de.md) |

Use actual size for A4 or fit-to-page for US Letter. The PDFs are static handwriting sheets, not interactive forms. No commercial annual Mahjong card or third-party scoring chart is included.

## What's inside

1. Table agreement: named rules, tile selection, opening, claims, scoring and end conditions.
2. OKEY score record: four players, starting values, signed changes for 12 hands, final totals.
3. Mahjong points ledger: four players plus an optional shared pool, with a point-conservation example.
4. Seating and session log: eight entries for the host's own seat/table plan; no automatic pairing or dealer rule.
5. Everyday care record: external checks, observations, action and next inspection under the model manual.

Choose the score direction before play. These forms record your agreed rules; they do not calculate legal hands or impose one universal scoring system. Keep personal and service records private.

## Learn and care

- [OKEY beginner pack](https://github.com/ineanplay/okey-guide/tree/main/community)
- [Mahjong beginner pack](https://github.com/ineanplay/mahjong-guide/tree/main/community)
- [Everyday care guide](https://github.com/ineanplay/automatic-mahjong-table-knowledge/tree/main/community)

## Edit and rebuild

Original text lives in `data/translations.json`. The PDF layout lives in `scripts/build_pdfs.py`. Use Python 3 and install `requirements.txt`; then run:

```sh
python -m pip install -r requirements.txt
python scripts/build_pdfs.py --font /path/to/latin.ttf --bold-font /path/to/latin-bold.ttf --cjk-font /path/to/chinese.ttf
```

The Latin fonts must include German and Turkish characters. The Chinese font must include simplified Chinese and Latin characters; a TrueType `.ttc` collection is supported with `--cjk-index`. Fonts are embedded in the generated PDF but are not supplied in this source repository. Use fonts whose embedding terms permit your use. Inspect all pages after changing translations or fonts.

Original content and forms: [CC BY 4.0](LICENSE.md). Generator code: [MIT](LICENSE-CODE). Third-party material and trademarks retain their own rights. [Contribute corrections or translations](CONTRIBUTING.md).

---

## About INEAN PLAY

INEAN PLAY focuses on automatic OKEY tables, automatic Mahjong tables and compatible accessories, providing products and practical support for homes, clubs, cafés and game rooms. We maintain free community resources to help enthusiasts learn, organize games and care for their equipment. Corrections, translations and improvements are welcome.

This project provides printable score sheets and session records for players, teachers and clubs.

### Products and quotations

- [Standard OKEY table](https://ineanplay.com/products/inean-otokey)
- [Folding OKEY table](https://ineanplay.com/products/inean-otokey-f)
- [Standard Mahjong table](https://ineanplay.com/products/inean-automatic-mahjong-table-standard)
- [Folding Mahjong table](https://ineanplay.com/products/inean-automatic-mahjong-table-folding)

[Official website](https://ineanplay.com/) · [Request a quote](https://ineanplay.com/pages/contact) · [Support and manuals](https://ineanplay.com/pages/support)

[service@ineanplay.com](mailto:service@ineanplay.com) · [WhatsApp +86 173 7839 0199](https://wa.me/8617378390199)

[Facebook](https://www.facebook.com/profile.php?id=61585370578775) · [Instagram](https://www.instagram.com/ineanplay/) · [TikTok](https://www.tiktok.com/@ineanplay) · [YouTube](https://www.youtube.com/@ineanplay)
