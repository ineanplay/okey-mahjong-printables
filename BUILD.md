# Build the print packs

Original text lives in `data/translations.json`. The PDF layout lives in `scripts/build_pdfs.py`. Use Python 3 and install `requirements.txt`; then run:

```sh
python -m pip install -r requirements.txt
python scripts/build_pdfs.py --font /path/to/latin.ttf --bold-font /path/to/latin-bold.ttf --cjk-font /path/to/chinese.ttf --cjk-bold-font /path/to/chinese-bold.ttf
```

The Latin fonts must include German and Turkish characters. The Chinese font must include simplified Chinese and Latin characters; a TrueType `.ttc` collection is supported with `--cjk-index`. Fonts are embedded in the generated PDF but are not supplied in this source repository. Use fonts whose embedding terms permit your use. Inspect all pages after changing translations or fonts.

Original content and forms: [CC BY 4.0](LICENSE.md). Generator code: [MIT](LICENSE-CODE). Third-party material and trademarks retain their own rights. [Contribute corrections or translations](CONTRIBUTING.md).
