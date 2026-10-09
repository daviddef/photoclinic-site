# Photo Clinic website

The source of https://photoclinic.org, kept here so the site is versioned with the app. It is a static site served by GitHub Pages from the public repo `daviddef/photoclinic-site`.

- Edit `_gen/build.py` (all the page text and layout), then run `python3 _gen/build.py` to regenerate the `.html` files and `style.css`.
- `img/` holds the screenshots (made from a private copy of the app with sample data).
- To publish: copy this folder into a clone of `daviddef/photoclinic-site` (keep its `CNAME`) and push to `main`.
