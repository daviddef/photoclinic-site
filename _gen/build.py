import html, pathlib
OUT = pathlib.Path(__file__).resolve().parent.parent
DL = "https://github.com/daviddef/photoclinic-releases/releases/latest/download/PhotoClinic-arm64.dmg"   # a fixed-name copy of the newest dmg: the click starts the download
NAV = [("story.html", "Our story"), ("tools.html", "All tools"), ("guides.html", "Guides"), ("copy-icloud-drive-to-external-drive-mac.html", "Copy from the cloud"), ("fix-takeout.html", "Google Takeout"), ("monitor.html", "Monitor"), ("problems.html", "Find problems"), ("tidy.html", "Duplicates &amp; tidy"), ("old-libraries.html", "Old libraries"), ("apple-photos.html", "Apple Photos"), ("safety.html", "Safety")]

CSS = """:root{--bg:#fbfaff;--card:#fff;--ink:#1b1830;--mute:#5f5b78;--line:#e3e0f2;--soft:#f1eefe;--acc:#5b3df5;--acc2:#e23fa0;--ok:#15803d}
@media (prefers-color-scheme:dark){:root{--bg:#14121f;--card:#1e1b2e;--ink:#f3f1ff;--mute:#a9a5c4;--line:#322e4a;--soft:#25213a;--acc:#8b74ff;--acc2:#ff6fbd;--ok:#4ade80}}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.6 -apple-system,system-ui,"Segoe UI",sans-serif}
a{color:var(--acc)}
main{max-width:920px;margin:0 auto;padding:0 20px 60px}
nav{position:sticky;top:0;z-index:5;background:color-mix(in srgb,var(--bg) 92%,transparent);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
nav div{max-width:920px;margin:0 auto;padding:10px 20px;display:flex;gap:6px 18px;flex-wrap:wrap;align-items:center;font-size:15px}
nav b{margin-right:auto;font-size:17px}
nav a{text-decoration:none;color:var(--ink);font-weight:600}
nav a:hover,nav a[aria-current]{color:var(--acc)}
h1{font-size:clamp(32px,6vw,48px);line-height:1.12;margin:0 0 14px}
h1 span{background:linear-gradient(90deg,var(--acc),var(--acc2));-webkit-background-clip:text;background-clip:text;color:transparent}
h2{font-size:26px;line-height:1.2;margin:48px 0 6px}
h3{font-size:18px;margin:0 0 4px}
.lead{font-size:20px;color:var(--mute);margin:0 0 24px}
.sub{color:var(--mute);margin:0 0 16px}
.crumb{font-size:14px;margin:28px 0 0}
.kicker{color:var(--acc);font-weight:800;font-size:13px;letter-spacing:.08em;text-transform:uppercase;margin:0 0 6px}
.btn{display:inline-block;padding:14px 28px;border-radius:999px;background:linear-gradient(90deg,var(--acc),var(--acc2));color:#fff;font-weight:800;font-size:18px;text-decoration:none}
.btn:focus-visible,a:focus-visible,summary:focus-visible{outline:3px solid var(--ink);outline-offset:3px}
.note{color:var(--mute);font-size:14px;margin-top:12px}
.hero{display:grid;grid-template-columns:1fr 1.1fr;gap:32px;align-items:center;padding:48px 0 16px}
.phead.one{grid-template-columns:1fr;max-width:720px}.phead{padding:12px 0 8px;display:grid;grid-template-columns:1fr 1.1fr;gap:32px;align-items:center}
.shot{width:100%;height:auto;display:block;border-radius:18px;border:1px solid var(--line);box-shadow:0 10px 30px rgba(60,40,140,.18)}
figure{margin:0}
figcaption{color:var(--mute);font-size:13.5px;margin-top:8px;text-align:center}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(270px,1fr));gap:14px;margin-top:16px}
.card{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:18px 20px;display:flex;flex-direction:column;gap:6px}
.card p{margin:0;color:var(--mute);font-size:15.5px}
.card a.more{margin-top:auto;padding-top:8px;font-weight:700;text-decoration:none}
.card i{font-style:normal;font-size:28px;line-height:1}
.pair{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px;margin-top:16px}
.pair .card{border-radius:16px}
.td{border-top:1px solid var(--line);padding:22px 0}.td h3{margin:0 0 4px}.td .what{margin:0 0 10px;color:var(--mute)}.td dl{margin:0}.td dt{font-weight:700;font-size:13px;color:var(--mute);text-transform:uppercase;letter-spacing:.04em;margin-top:12px}.td dd{margin:2px 0 0}.td.phead{align-items:start}.td figure{position:sticky;top:70px}.td .stl{margin:14px 0 4px}.td.phead{display:grid}.jump{font-size:17px;line-height:2}@media (max-width:760px){.td figure{position:static}}
ul.ticks{list-style:none;padding:0;margin:8px 0 0}
ul.ticks li{padding:8px 0 8px 28px;position:relative;border-bottom:1px solid var(--line)}
ul.ticks li:last-child{border:0}
ul.ticks li::before{content:"\\2713";position:absolute;left:4px;color:var(--ok);font-weight:900}
ul.ticks b{font-weight:700}
ul.bad li::before{content:"\\2715";color:var(--acc2)}
.steps{display:grid;gap:12px;padding:0;list-style:none;counter-reset:s;margin:16px 0 0}
.steps li{counter-increment:s;background:var(--card);border:1px solid var(--line);border-radius:16px;padding:14px 18px 14px 62px;position:relative}
.steps li::before{content:counter(s);position:absolute;left:18px;top:12px;width:32px;height:32px;border-radius:50%;background:var(--acc);color:#fff;font-weight:800;display:grid;place-items:center}
.states{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:10px;margin:14px 0}
.states div{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:10px 14px;font-size:15px}
.states b{display:block}
.callout{background:var(--soft);border:1px solid var(--line);border-radius:16px;padding:16px 18px;margin-top:20px;font-size:15.5px}
details{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:12px 16px;margin:10px 0}
summary{cursor:pointer;font-weight:700}
details p{margin:8px 0 0;color:var(--mute)}
.badge{display:inline-block;vertical-align:middle;font-size:12px;font-weight:800;padding:2px 10px;border-radius:999px;background:var(--acc);color:#fff;margin-left:8px;letter-spacing:.04em}
.relhead{display:flex;justify-content:space-between;align-items:baseline;gap:12px;flex-wrap:wrap}
.reldate{color:var(--mute);font-size:14px}
.rel{border-top:1px solid var(--line);margin-top:32px;padding-top:4px}
.feats{margin-top:8px}.feat{border-top:1px solid var(--line);padding:22px 0 18px}.feat h3{font-size:22px;line-height:1.25;margin:0 0 8px}.feat p{margin:0 0 8px;font-size:17px}.feat ul{margin:6px 0 8px 0;padding-left:22px}.feat li{margin:4px 0}.feat .more{font-weight:700;text-decoration:none}.toc{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0 6px}.toc a{background:var(--soft);border:1px solid var(--line);border-radius:999px;padding:6px 14px;font-size:14.5px;text-decoration:none;font-weight:600;color:var(--ink)}.toc a:hover{border-color:var(--acc);color:var(--acc)}.faq h3{font-size:18px;margin:18px 0 4px}
.cta{text-align:center;margin-top:56px;padding:32px 20px;background:var(--soft);border:1px solid var(--line);border-radius:22px}
.cta h2{margin-top:0}
.next{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;margin-top:40px;font-weight:700}
.next a{text-decoration:none}
footer{margin-top:48px;color:var(--mute);font-size:14px;text-align:center}.gcstats{font-size:13px;opacity:.85}
@media (max-width:760px){.hero,.phead{grid-template-columns:1fr}.hero figure,.phead figure{max-width:560px;margin:0 auto}}
"""

def nav(cur):
    items = "".join('<a href="%s"%s>%s</a>' % (h, ' aria-current="page"' if h == cur else "", t) for h, t in NAV)
    return '<nav><div><b><a href="index.html" style="text-decoration:none;color:inherit">Photo Clinic</a></b>%s</div></nav>' % items

SITE = "https://photoclinic.org/"
JSONLD = '''<script type="application/ld+json">{"@context":"https://schema.org","@type":"SoftwareApplication","name":"Photo Clinic","applicationCategory":"MultimediaApplication","operatingSystem":"macOS","description":"A free Mac app that restores the dates, places and captions in a Google Takeout, copies iCloud Drive and Google Drive to your own drive, finds duplicates and damaged photos, shows which photos are not in Apple Photos yet, rescues old iPhoto and Aperture libraries, and explains what Apple Photos and iCloud are doing.","featureList":["Restore dates, places and captions from Google Takeout","Copy iCloud Drive to an external drive, slowly and safely, and fill the gaps in an earlier copy","Download a Google Drive folder, or Takeout files from an email, to your Mac","Find exact duplicates and look-alike photos","Find damaged or unreadable photos and rescue the good ones","Show which photos are not in Apple Photos yet","Send photos to Apple Photos in careful batches","Check Apple Photos and iCloud sync, and explain the errors","Rescue photos from old iPhoto and Aperture libraries","Convert old videos to MP4"],"url":"https://photoclinic.org/","downloadUrl":"https://github.com/daviddef/photoclinic-releases/releases/latest/download/PhotoClinic-arm64.dmg","offers":{"@type":"Offer","price":"0","priceCurrency":"USD"},"license":"https://opensource.org/licenses/MIT"}</script>'''


EXTRA = {
"google-takeout-dates-wrong.html": """<h2>How to see what date a photo really has</h2>
<ul class="ticks">
<li><b>In Finder</b>, select the photo and press Cmd+I. <b>Created</b> and <b>Modified</b> are the file's own dates, which are often the day you downloaded it. Under <b>More Info</b>, <b>Content Created</b> is the date stored inside the picture. If it is missing, the picture has no date inside.</li>
<li><b>In Apple Photos</b>, select a photo and press Cmd+I to see the date Photos is using, and choose <b>Image &gt; Adjust Date and Time</b> to change it for a few photos by hand.</li>
</ul>
<h2>The strange dates and what each means</h2>
<ul class="ticks">
<li><b>The day you downloaded or unzipped them.</b> The picture has no date inside, so the app used the file's own date.</li>
<li><b>1 January 1970.</b> A date of zero in the Unix clock. A tool wrote an empty date.</li>
<li><b>1 January 2001.</b> A date of zero in Apple's own clock. The same problem on a Mac.</li>
<li><b>Hours out, or a day out.</b> A time in UTC was read as local time, or the other way round. See <a href="photo-dates-and-time-zones-explained.html">photo dates and time zones explained</a>.</li>
<li><b>Videos wrong but photos right.</b> Videos store their date in UTC, photos usually in local time, so a tool that treats both alike gets one of them wrong.</li>
</ul>
<h2>Can I fix it by hand?</h2>
<p>For a handful of photos, yes: Photos' <b>Adjust Date and Time</b>. For thousands, no. A free command-line program called ExifTool can read the <code>.json</code> files and write the dates, but it needs careful setup, handles file names that were cut short poorly, and does nothing for time zones unless you tell it. That gap is what Photo Clinic fills. It reads the date from the JSON, writes local time with the right offset into a <b>copy</b>, and shows you a before-and-after for real photos first.</p>""",

"google-takeout-json-files.html": """<h2>What is inside one of them</h2>
<p>Open a <code>.json</code> file in any text editor and you will see plain text. The parts that matter:</p>
<ul class="ticks">
<li><b>photoTakenTime</b>: when the photo was taken, as a number of seconds since 1970 (UTC), with a readable version beside it.</li>
<li><b>creationTime</b>: when it was uploaded to Google, which is not the same thing.</li>
<li><b>geoData</b>: the place, as latitude, longitude and altitude. A value of 0, 0 means &ldquo;no place&rdquo;.</li>
<li><b>description</b>: the caption you wrote.</li>
<li><b>people</b>: the names of people you labelled in the photo.</li>
<li><b>favorited</b>: whether you starred it.</li>
<li><b>url</b> and <b>title</b>: the photo's Google Photos link and its original file name.</li>
</ul>
<h2>How a photo and its file find each other</h2>
<p>The usual pattern is <code>photo.jpg</code> and <code>photo.jpg.json</code> (in newer exports, <code>photo.jpg.supplemental-metadata.json</code>). The exceptions are what make this hard: names over a certain length are shortened, copies get <code>(1)</code> added in a different place, and edited copies named <code>photo-edited.jpg</code> share the original's JSON. Every album folder also holds its own <code>metadata.json</code>, which describes the album, not a photo.</p>
<h2>Can I delete them?</h2>
<p>Only after the information is inside the photos. The files are small, so keeping them costs nothing, and they are the only record of your places and captions. If you want to be sure, keep the original Takeout zip files as well.</p>""",

"find-duplicate-photos-mac.html": """<h2>What about the Duplicates album in Apple Photos?</h2>
<p>Recent versions of Photos have a <b>Duplicates</b> album that finds copies inside your Photos library and offers to merge them. It is worth using for that. It cannot help with duplicates in folders outside Photos, with copies spread across drives, or with a Takeout you have not imported yet, and it works only on what is already in the library.</p>
<h2>Things that look like duplicates but are not</h2>
<ul class="ticks">
<li><b>RAW and JPEG pairs</b> from a camera share a name. The RAW is the original data and the JPEG is the picture made from it.</li>
<li><b>A Live Photo</b> is a still and a short video with the same name.</li>
<li><b>Burst photos</b> are a run of near-identical frames. You may only want to remove some.</li>
<li><b>An original and its edit</b>, such as <code>photo.jpg</code> and <code>photo-edited.jpg</code>.</li>
</ul>
<h2>A safe way to clear duplicates</h2>
<ol class="steps"><li><b>Find them</b> without changing anything, and read the list.</li><li><b>Move them aside</b> into a spare folder, not the Trash. Nothing is deleted.</li><li><b>Check again</b> that nothing was left behind, and look through your library for a week or two.</li><li><b>Delete the spare folder</b> yourself when you are sure.</li></ol>
<p>For the longer explanation of how duplicates are told apart, read <a href="how-to-tell-if-photos-are-duplicates.html">how to tell if two photos are really duplicates</a>.</p>""",

"move-google-photos-to-apple-photos.html": """<h2>Before you start</h2>
<ul class="ticks">
<li><b>Check your space.</b> A Takeout is a copy, so you need room for the zip files, the unzipped photos and the fixed copy, until you delete the extras. Photos also needs room in its library, and for the files it makes while importing.</li>
<li><b>Know what Google kept.</b> If your Google Photos is set to <b>Storage saver</b> (the old &ldquo;High quality&rdquo;), the photos were compressed when they were uploaded. A Takeout can only give you what Google kept.</li>
<li><b>Export only Google Photos.</b> On the Takeout page, deselect everything else, and choose a zip size that suits your internet connection.</li>
<li><b>Download promptly.</b> The links expire, and each archive can only be downloaded a few times. See <a href="whats-in-a-google-takeout-and-how-to-check-it.html">what is in a Google Takeout and how to check it</a>.</li>
</ul>
<h2>How long it takes</h2>
<p>The upload to iCloud is usually the slowest part. As a guide, 100 GB over a 20 megabit-per-second upload connection is about 11 hours of continuous uploading, and a large library takes days. Photos may also pause on low power or a poor connection. That is normal; see <a href="icloud-photos-stuck-syncing.html">is iCloud Photos slow, or stuck?</a></p>
<h2>How to check it worked</h2>
<ol class="steps"><li>Compare the number of photos and videos in Photos with what Google Photos showed.</li><li>Open a few photos from different years and check the date, place and caption in the Info panel.</li><li>Check an album or two. Folders can become albums.</li><li>Only then, and only if you are sure, think about removing anything from Google.</li></ol>""",

"icloud-photos-stuck-syncing.html": """<h2>How long should it take?</h2>
<p>Upload speed is the limit, and home connections upload far more slowly than they download. A quick sum: 100 GB is 800,000 megabits. At 20 megabits per second that is 40,000 seconds, about 11 hours, if nothing else uses the connection and the Mac stays awake. At 5 megabits per second it is about 44 hours. Photos also uploads in the background and slows down when the Mac is busy, on battery, in Low Power Mode, or on a connection marked as limited.</p>
<h2>Things that pause syncing without telling you</h2>
<ul class="ticks">
<li><b>Low Power Mode</b> on a laptop, and Low Data Mode on the network.</li>
<li><b>The Mac asleep or on battery.</b> Syncing runs best when plugged in and awake.</li>
<li><b>Full iCloud storage.</b> Uploads stop when your plan is full.</li>
<li><b>&ldquo;Pause for a day&rdquo;</b> in Photos' iCloud settings.</li>
<li><b>A signed-out Apple Account</b>, or one that needs you to sign in again.</li>
<li><b>One file it cannot upload</b>, such as a damaged picture, which can hold things up.</li>
</ul>
<h2>Reading the numbers</h2>
<p>In Photos, the status line at the bottom of the Library view shows how many items remain to upload. If that number goes down over hours, even slowly, the sync is working. If it stays the same for a day with the Mac awake and online, something is stopping it. Photo Clinic's <b>Sync meter</b> draws this as a chart, and separates the number of photos waiting from the internal records the sync engine keeps, which can grow without anything being wrong.</p>""",

"find-damaged-photos-mac.html": """<h2>How photos get damaged</h2>
<ul class="ticks">
<li><b>A download or copy that stopped part-way</b>, leaving a file that exists but ends early.</li>
<li><b>A drive that is failing</b>, or was disconnected while it was being written to.</li>
<li><b>A full disk</b> during a copy or import.</li>
<li><b>A zip file that did not finish downloading.</b></li>
<li><b>Old media</b> that has simply degraded.</li>
</ul>
<h2>Checking one photo by hand</h2>
<p>Press the space bar on a photo in Finder to open Quick Look, or open it in Preview. A picture that is cut short usually shows a grey or smeared bottom part, or will not open at all. For a zip file, Terminal can test it: <code>unzip -t file.zip</code> reads every file in it and reports any that are bad. That is fine for one file, and slow for hundreds, which is where a tool helps.</p>
<h2>What to do with a damaged file</h2>
<ul class="ticks">
<li><b>Look for another copy.</b> A backup, your phone, a second drive, or Google Photos may have a good one. Photo Clinic lists a good copy elsewhere when it finds one.</li>
<li><b>Do not delete the damaged file</b> until you have found a replacement. Parts of it can sometimes still be recovered.</li>
<li><b>Download a damaged zip again.</b> The rest of your Takeout can still be fixed in the meantime.</li>
</ul>""",

"apple-photos.html": """<h2>Before you send a big library</h2>
<ul class="ticks">
<li><b>Check space</b> on the drive that holds your Photos library and on your Mac.</li>
<li><b>Find out what Photos already has</b>, so you do not import the same pictures twice. See <a href="photos-not-in-apple-photos.html">which photos are not in Apple Photos yet</a>.</li>
<li><b>Fix dates first.</b> Photos files pictures by the date inside them, and changing dates afterwards is slow.</li>
<li><b>Put albums in folders.</b> A folder of pictures can become an album in Photos.</li>
<li><b>Try a small test</b> of about 20 photos and look at them in Photos.</li>
</ul>
<h2>If something goes wrong</h2>
<p>Photos has no undo for imports, so the safest plan is to send in batches and watch. If an import shows &ldquo;Cannot Import&rdquo; or asks about duplicates, read <a href="apple-photos-cannot-import-and-duplicate-messages.html">what those messages mean</a>. If iCloud falls behind, wait for it to catch up before sending more.</p>""",
}


def page(fname, title, desc, body, cur=None, ld=""):
    if fname in EXTRA:
        body = body.replace('<div class="cta">', EXTRA[fname] + '<div class="cta">', 1)
    t = "Photo Clinic: free Mac app for Google Takeout, iCloud Drive and Apple Photos" if fname == "index.html" else "%s - Photo Clinic" % title
    doc = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%s</title>
<meta name="description" content="%s">
<link rel="canonical" href="%s">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Photo Clinic">
<meta property="og:title" content="%s">
<meta property="og:description" content="%s">
<meta property="og:url" content="%s">
<meta property="og:image" content="https://photoclinic.org/img/home.jpg">
<meta name="twitter:card" content="summary_large_image">
%s
<link rel="stylesheet" href="style.css">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4156851882993001" crossorigin="anonymous"></script>
<script data-goatcounter="https://photoclinic.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>
</head>
<body>
%s
<main>
%s
<footer>
<p>Photo Clinic is free to use, under the MIT licence. It is an independent project and is not affiliated with Google or Apple. Google, Google Photos, Apple, iCloud, iPhone and macOS are trademarks of their owners.</p>
<p><a href="%s">Download</a> &middot; <a href="guides.html">Guides</a> &middot; <a href="about.html">About</a> &middot; <a href="contact.html">Contact</a> &middot; <a href="editorial-policy.html">How we write</a> &middot; <a href="versions.html">Release notes</a> &middot; <a href="safety.html">Safety</a> &middot; <a href="privacy.html">Privacy</a></p>
<p class="gcstats" id="gcstats" hidden></p>
<script>
(function(){try{var r=new XMLHttpRequest();r.addEventListener("load",function(){try{var j=JSON.parse(this.responseText),e=document.getElementById("gcstats");
if(e&&j&&j.count!==undefined){e.textContent="Visitors: "+j.count_unique+" \u00b7 Page views: "+j.count+" (counted by GoatCounter)";e.hidden=false}}catch(x){}});
r.open("GET","https://photoclinic.goatcounter.com/counter/TOTAL.json");r.send()}catch(x){}})();
</script>
</footer>
</main>
</body>
</html>
""" % (html.escape(t), html.escape(desc), SITE + ("" if fname == "index.html" else fname), html.escape(t), html.escape(desc), SITE + ("" if fname == "index.html" else fname), (JSONLD if fname == "index.html" else "") + ld, nav(cur), body, DL)
    (OUT / fname).write_text(doc, encoding="utf-8")


import struct as _struct
def imgdim(fname):
    """CSS size of a screenshot: its pixel size, halved-and-a-bit for the 1.5x ones."""
    try:
        d = (OUT / "img" / fname).read_bytes(); i = 2
        while i < len(d):
            m = d[i + 1]
            if m in (0xC0, 0xC2):
                h, w = _struct.unpack(">HH", d[i + 5:i + 9]); return (round(w / 1.5), round(h / 1.5)) if w > 1000 else (w, h)
            i += 2 + _struct.unpack(">H", d[i + 2:i + 4])[0]
    except Exception:
        pass
    return (800, 732)

def figure(img, alt, cap, lazy=True, cls="shot"):
    w, h = imgdim(img)
    return '<figure><img class="%s" src="img/%s" width="%d" height="%d"%s alt="%s"><figcaption>%s</figcaption></figure>' % (cls, img, w, h, ' loading="lazy"' if lazy else "", alt, cap)

def head(kicker, h1, lead, img=None, alt="", cap=""):
    fig = figure(img, alt, cap, lazy=False) if img else ""
    return '<p class="crumb"><a href="index.html">&larr; Photo Clinic</a></p><div class="phead%s"><div><p class="kicker">%s</p><h1>%s</h1><p class="lead">%s</p><a class="btn" href="%s">Download for Mac</a></div>%s</div>' % ("" if img else " one", kicker, h1, lead, DL, fig)

def ticks(items, cls=""):
    return '<ul class="ticks %s">%s</ul>' % (cls, "".join("<li>%s</li>" % i for i in items))

def cards(items, cls="pair"):
    return '<div class="%s">%s</div>' % (cls, "".join('<div class="card"><h3>%s</h3><p>%s</p></div>' % (a, b) for a, b in items))

def nextlinks(prev, nxt):
    p = '<a href="%s">&larr; %s</a>' % prev if prev else "<span></span>"
    n = '<a href="%s">%s &rarr;</a>' % nxt if nxt else "<span></span>"
    return '<div class="next">%s%s</div>' % (p, n)

def cta():
    return '<div class="cta"><h2>Look at your library for free</h2><p class="sub">Download it, point it at your photos, and read the preview. That costs nothing and changes nothing.</p><a class="btn" href="%s">Download for Mac</a><p class="note">Free &middot; Apple silicon Macs &middot; signed and checked by Apple</p></div>' % DL

# ---------------------------------------------------------------- home
home = """<section class="hero">
<div>
<p class="kicker">A free Mac app, from people who got stuck</p>
<h1>Photos is hard. <span>Leaving Google Photos is harder.</span></h1>
<p class="lead">We tried to move a big photo library. Dates came out wrong, places went missing, duplicates piled up, and Apple Photos stalled without saying why. So we worked out what was going on, and built the tool we wished we had. It is free.</p>
<a class="btn" href="%s">Download for Mac</a>
<p class="note">Free &middot; 66&nbsp;MB &middot; Apple silicon Macs &middot; signed and checked by Apple &middot; your photos never leave your Mac</p>
</div>
<figure><img class="shot" src="img/home.jpg" width="1185" height="1515" alt="The Photo Clinic home screen: what do you have, then six jobs"><figcaption>The home screen: start here, or pick a job.</figcaption></figure>
</section>

<h2 id="what-it-does">What Photo Clinic does</h2>
<p class="sub">One free Mac app, in plain words. Every job starts with a preview that changes nothing. Pick what you need:</p>
<div class="toc">
<a href="#fix-google-takeout">Fix Google Takeout</a><a href="#copy-icloud-drive">Copy iCloud Drive</a><a href="#google-drive">Google Drive</a><a href="#not-in-photos">Not in Photos yet</a><a href="#duplicates">Duplicates</a><a href="#damaged">Damaged photos</a><a href="#organise">Organise</a><a href="#scan">One scan</a><a href="#send-to-photos">Apple Photos</a><a href="#watch">Watch iCloud</a><a href="#old-libraries">Old libraries</a><a href="#videos">Old videos</a><a href="#safe">Safe and private</a>
</div>
<div class="feats">

<section class="feat" id="fix-google-takeout">
<h3>Fix Google Takeout photos: put back the real dates, places and captions</h3>
<p>When you export from Google Photos, the dates, places and captions come out in separate <code>.json</code> files and the photos themselves arrive bare, often showing the day you downloaded them. Photo Clinic reads those files and writes everything back into the pictures, across as many zip files as Google gave you.</p>
<ul><li>Dates in the right local time, places, captions, people and favourites.</li><li>Live Photos paired again, hidden videos taken out of Motion Photos, edited copies matched to their originals.</li><li>Photos with no date get one worked out from the file name, the folder or the photos next to them, and each guess is labelled.</li></ul>
<a class="more" href="fix-takeout.html">How the Takeout fix works &rarr;</a></section>

<section class="feat" id="copy-icloud-drive">
<h3>Copy iCloud Drive to an external drive, even when the files are only in iCloud</h3>
<p>Big iCloud Drive folders do not copy well in Finder: files that are not downloaded fail, and you cannot tell what is missing. Photo Clinic copies slowly and carefully, one file at a time. It asks iCloud to send each file, copies it, checks it, then frees the space on your Mac again.</p>
<ul><li><b>Carries on where it stopped</b> after a restart, a sleep or a closed lid.</li><li><b>Compares with an earlier copy</b> and shows exactly which files are missing or cut short, folder by folder, then copies only those gaps.</li><li>Shows the speed, the time left, and every file as it goes, with a link to the copied file.</li><li>Groups any problems by cause, in plain words, with what to do about each.</li></ul>
<a class="more" href="copy-icloud-drive-to-external-drive-mac.html">How to copy iCloud Drive to an external drive &rarr;</a></section>

<section class="feat" id="google-drive">
<h3>Download a Google Drive folder, or your Takeout files from an email, to your Mac</h3>
<p>Sign in with your own Google account, choose your own folders, and Photo Clinic copies them to the drive you choose. It can only read your Drive, never change it, and it carries on after any stop. Got an email with &ldquo;View 1 of 43 in Drive&rdquo; links? Paste the email and Photo Clinic finds every link, puts them in order and downloads them with a checklist.</p>
<ul><li>Several files at once, with the speed and time left for each part.</li><li>Files that share a name in Drive are all kept.</li><li>Takeout links that must be opened in the browser are tracked for you: each finished file is moved into your folder and ticked off.</li></ul>
<a class="more" href="download-google-drive-folder-mac.html">How to download from Google Drive &rarr;</a></section>

<section class="feat" id="not-in-photos">
<h3>See which photos are not in Apple Photos yet, before you import</h3>
<p>Dragging a huge folder into Photos wastes hours when most of it is already there. Photo Clinic compares your folder with your Photos library, including pictures that live only in iCloud, and tells you what is already in, what is a different version, and what is really missing.</p>
<ul><li>Side-by-side pictures of your file and the one in Photos, with links to both.</li><li>Copies only the missing ones into a new folder, named after the album that suits them best.</li><li>Can move the ones Photos already has out of the way. Nothing is deleted.</li></ul>
<a class="more" href="photos-not-in-apple-photos.html">Find photos that are not in Apple Photos &rarr;</a></section>

<section class="feat" id="duplicates">
<h3>Find and clear duplicate photos, safely</h3>
<p>Exact copies are found by their content, not their name, and moved into a spare folder, never deleted. Look-alikes (the same picture at another size or lightly edited) are shown side by side with a suggested keeper, and the same picture saved in more than one format is found too.</p>
<ul><li>You can see both pictures, tick the one you prefer, and check again afterwards to be sure it worked.</li><li>Everything can be undone from Past runs.</li></ul>
<a class="more" href="find-duplicate-photos-mac.html">How to find duplicate photos on a Mac &rarr;</a></section>

<section class="feat" id="damaged">
<h3>Find damaged or unreadable photos, and rescue the good ones</h3>
<p>Photos that stopped short, empty files, and zips that did not finish downloading are found before they cause trouble, with the reason for each. If a drive is failing, Photo Clinic copies what still reads, gently, skips the stuck files and tries them last.</p>
<a class="more" href="find-damaged-photos-mac.html">How to find damaged photos &rarr;</a></section>

<section class="feat" id="organise">
<h3>Organise a messy pile of folders, zips and old libraries into one dated library</h3>
<p>Point Photo Clinic at a drive full of Takeout zips, loose folders and old libraries. It works out what each part is, copies everything into one library filed by year and month, keeps one copy of each picture and leaves your originals alone.</p>
<a class="more" href="organise-photos-by-date-mac.html">Organise photos by date &rarr;</a></section>

<section class="feat" id="scan">
<h3>Check everything in one scan and get a plan</h3>
<p>One button reads your folders and your library and gives a health score out of 100, then a plan: what would be fixed, what is duplicated, what is damaged, which videos will not play. Each line has <b>Show me</b> and <b>Do it now</b>, and you can check again to be sure it is done.</p>
<a class="more" href="tools.html#check">The Check tab &rarr;</a></section>

<section class="feat" id="send-to-photos">
<h3>Send photos to Apple Photos in careful batches</h3>
<p>Photos has no undo for imports and can choke on a big one. Photo Clinic sends your library oldest first in batches, keeps Live Photos together, turns folders into albums, and waits for iCloud to keep up before the next batch.</p>
<a class="more" href="apple-photos.html">Moving into Apple Photos &rarr;</a></section>

<section class="feat" id="watch">
<h3>Watch Apple Photos and iCloud: is it syncing, or stuck?</h3>
<p>A reading of how your library is doing every 15 minutes, a live meter of upload speed and what is waiting, and the hidden Photos and iCloud messages explained in plain words with steps to try. Apple's own status is one click away.</p>
<a class="more" href="monitor.html">Monitor Photos and iCloud &rarr;</a> &middot; <a class="more" href="icloud-photos-stuck-syncing.html">Is iCloud Photos stuck? &rarr;</a></section>

<section class="feat" id="old-libraries">
<h3>Rescue photos from an old iPhoto or Aperture library</h3>
<p>The library's own records are read, so albums, events, keywords and ratings come out with the pictures, even from an old or failing drive.</p>
<a class="more" href="old-libraries.html">Old libraries &rarr;</a></section>

<section class="feat" id="videos">
<h3>Make old videos play: convert AVI, MPG, WMV, MTS and 3GP to MP4</h3>
<p>Old camera and phone formats do not play everywhere or import into Photos. Photo Clinic converts them to MP4, without re-encoding when it can, and keeps your original or moves it aside, as you choose.</p>
<a class="more" href="tools.html#videos">The Videos tool &rarr;</a></section>

<section class="feat" id="safe">
<h3>Safe by design: preview first, copy not move, nothing leaves your Mac</h3>
<p>Every job starts as a preview that changes nothing. Files are copied, not moved, and nothing is deleted without you typing a confirmation. Your photos are never uploaded; the only network use is the Google and iCloud copying you ask for and checking for a new version.</p>
<a class="more" href="safety.html">How we keep your photos safe &rarr;</a></section>
</div>

<h2>Free, and open</h2>
<p class="sub">Photo Clinic is free under the MIT licence, for Macs with Apple silicon, signed and checked by Apple.</p>
<p><a href="tools.html"><b>See every tool, one line each &rarr;</b></a></p>

<h2>What went wrong for us</h2>
<p class="sub">It is probably what is going wrong for you too.</p>
<div class="cards" style="grid-template-columns:repeat(auto-fit,minmax(min(100%%,380px),1fr))">
<div class="card"><i>&#128196;</i><h3>The photos come out, the story does not</h3><p>Google keeps the dates, places and captions in separate files. The photos arrive bare, and many show the day you downloaded them.</p><a class="more" href="fix-takeout.html">How we fix that &rarr;</a></div>
<div class="card"><i>&#128101;</i><h3>Duplicates multiply</h3><p>Edited copies, album copies, the same picture at two sizes. It is hard to tell what is safe to remove.</p><a class="more" href="tidy.html">How we sort them &rarr;</a></div>
<div class="card"><i>&#127822;</i><h3>Apple Photos will not tell you what it is doing</h3><p>Imports have no undo. iCloud can take days to catch up, and the reasons are buried in logs nobody reads.</p><a class="more" href="problems.html">What we read for you &rarr;</a></div>
<div class="card"><i>&#128190;</i><h3>Old libraries and tired drives</h3><p>Old iPhoto and Aperture libraries, and drives that stall halfway through a copy.</p><a class="more" href="old-libraries.html">How we get them out &rarr;</a></div>
</div>
<p><a href="story.html"><b>Read what we learned, in plain words &rarr;</b></a></p>

<h2>Questions we hear</h2>
<ul class="ticks">
<li><a href="how-to-fix-google-takeout-metadata-mac.html">How do I fix Google Takeout metadata on a Mac?</a></li>
<li><a href="google-takeout-dates-wrong.html">Why do my Google Takeout photos show the wrong date?</a></li>
<li><a href="google-takeout-json-files.html">What are all those .json files in my Takeout?</a></li>
<li><a href="move-google-photos-to-apple-photos.html">How do I move from Google Photos to Apple Photos?</a></li>
<li><a href="icloud-photos-stuck-syncing.html">Is iCloud Photos slow, or stuck?</a></li>
<li><a href="find-duplicate-photos-mac.html">How do I find and remove duplicate photos on a Mac?</a></li>
<li><a href="copy-icloud-drive-to-external-drive-mac.html">How do I copy iCloud Drive to an external drive on a Mac?</a></li>
<li><a href="download-google-drive-folder-mac.html">How do I download a Google Drive folder, or my Takeout files from an email?</a></li>
<li><a href="photos-not-in-apple-photos.html">How do I find which photos are not in Apple Photos yet?</a></li>
<li><a href="find-damaged-photos-mac.html">How do I find damaged or unreadable photos?</a></li>
</ul>

<h2>How it works</h2>
<ol class="steps">
<li><b>Tell it what you have.</b> Drop in your Google Takeout zips, a folder, an old library, or point it at your Photos library.</li>
<li><b>Read the preview.</b> It shows what would change. Nothing is touched yet.</li>
<li><b>Press go.</b> Your photos are copied, fixed and tidied into a new folder. Your originals stay as they were.</li>
</ol>
<div class="callout"><b>Our promise.</b> Preview first. Copy, do not move. Undo where we can. Nothing is uploaded. You can read how in <a href="safety.html">Safety</a>.</div>
%s""" % (DL, cta())
FAQ_HOME = [
 ("Is Photo Clinic free?", "Yes. Photo Clinic is free for Macs with Apple silicon, under the MIT licence."),
 ("Does Photo Clinic upload my photos?", "No. Your photos never leave your Mac. The only network use is checking for a new version and the Google Drive or iCloud copying you ask for."),
 ("Can Photo Clinic copy iCloud Drive to an external drive?", "Yes. It copies one file at a time, asks iCloud to send files that are only in the cloud, checks each copy, frees the space again, and carries on after any stop. It can also compare with an earlier copy and fill in only the gaps."),
 ("How do I fix wrong dates in a Google Takeout?", "Photo Clinic reads the .json files Google leaves beside each photo and writes the real date, place and caption back into a copy of the photo. It starts as a preview that changes nothing."),
 ("Can it show which photos are not in Apple Photos yet?", "Yes. It compares a folder with your Photos library, including pictures that exist only in iCloud, and shows what is already in Photos, what is a different version and what is missing."),
]
LD_FAQ = '<script type="application/ld+json">' + __import__("json").dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a_}} for q, a_ in FAQ_HOME]}) + '</script>'
page("index.html", "Photo Clinic", "A free Mac app that fixes Google Takeout photos, copies iCloud Drive and Google Drive to your drive, finds duplicates and shows what is not in Apple Photos yet.", home, ld=LD_FAQ)

# ---------------------------------------------------------------- story
b = head("Our story", "Photos is hard. Leaving Google Photos is harder.", "We struggled with it, a lot. This page is what we learned the hard way, so you can skip the struggle.")
b += """<h2>1. The photos come out, but their story does not</h2>
<p>When you take your photos out of Google, you get the pictures, and beside each one a small file with the date, the place and the caption. Google calls them JSON files. Most programs ignore them. So the photos arrive with no place, no caption, and often the wrong date: the day you downloaded them.</p>
<p><b>What we do:</b> Photo Clinic reads those little files and writes the dates, places, captions, people and favourites back into the photos themselves, across as many zip files as Google gave you.</p>

<h2>2. Dates are harder than they look</h2>
<p>Google stores times in a universal clock (UTC). Your photo was taken in your local time, so a straight copy is wrong by hours, and sometimes lands on the wrong day. And some photos have no date at all.</p>
<p><b>What we do:</b> We write local time with the right offset, using the photo's place or your Mac's time zone. For photos with no date we work it out from the file name, the photos next to it or the folder name. Every guess is labelled as a guess, with how sure we are, and a guess never replaces a real date.</p>

<h2>3. One photo turns into many</h2>
<p>Edited copies sit beside the originals. Albums become folders full of extra copies. Live Photos arrive as a picture plus a separate video. Motion Photos hide a video inside the picture. Hundreds of little files and numbered names get in the way.</p>
<p><b>What we do:</b> We pair Live Photos back up, match edits to originals (you choose to keep both, the edit, or the original), keep one copy of each photo and write the album names out so nothing is lost, and pull the hidden video out of Motion Photos.</p>

<h2>4. Duplicates come in two kinds</h2>
<p><b>Exact copies</b> are the same file twice. Those are easy to spot and safe to remove. <b>Look-alikes</b> are the same picture saved at another size, or re-saved. Those need a decision: which one is the keeper?</p>
<p><b>What we do:</b> Exact copies are found by their content, not their name. For look-alikes we show them side by side and suggest a keeper using rules you control (a favourite, an edit, more pixels, a bigger file, more information inside). Nothing is deleted without a preview. And when you have two places to check, such as a source and the copy you made of it, <b>Compare two places</b> shows what is the same and lets you clear the identical files from one side, after checking each one byte for byte.</p>

<h2>5. Apple Photos does not tell you what it is doing</h2>
<p>An import into Photos cannot be undone. Sending a huge library all at once can fill your Mac and confuse iCloud. And when iCloud stalls, the reason is buried in system logs that nobody reads.</p>
<p><b>What we do:</b> We send your library in careful batches and wait for iCloud to keep up. We take a reading of how your library is doing every 15 minutes and show the trend. We read the hidden messages and explain them in plain words. And we are honest about it: Apple does not document most of these messages, so each explanation says how sure we are and where it came from.</p>

<h2>6. Old libraries and tired drives</h2>
<p>Photos from an old iPhoto or Aperture library are locked inside a folder only that program understood. And old drives stall: a copy gets stuck on one bad file and never finishes.</p>
<p><b>What we do:</b> We read the old library's own records, so your albums, events, keywords and ratings come out with the photos. When a drive stops answering, we skip the stuck files after a short wait, carry on, list what we skipped, and try those last next time. There is a gentle mode for a drive that is struggling.</p>

<h2>What we would tell a friend</h2>
%s
<div class="callout"><b>We are not perfect, and we say so.</b> Some of what Photo Clinic tells you about Apple's messages is our best reading, not Apple's word. When that is the case, it says so. If something is wrong, <a href="mailto:thestocksoup@gmail.com">tell us</a>.</div>
%s%s""" % (
 ticks(["<b>Back up first.</b> Keep your original Google Takeout until everything is checked in Photos.", "<b>Preview before you press go.</b> Always.", "<b>Copy, do not move.</b> You can always throw the copy away. You cannot un-delete.", "<b>Try 20 photos first</b> before sending thousands into Apple Photos.", "<b>Give iCloud days, not minutes.</b> Slow is not the same as stuck.", "<b>Do not trust a duplicate finder that deletes on its own.</b> Look at the keeper it picked.", "<b>If a drive hangs, stop.</b> Do not keep hammering it. Reconnect it, then run the copy again."]),
 cta(), nextlinks(None, ("tools.html", "All tools")))
page("story.html", "Our story", "Why we built Photo Clinic: what we learned moving a big photo library out of Google Photos and into Apple Photos.", b, "story.html")

# ---------------------------------------------------------------- tools
def tool(name, text, link=None):
    return (name, text + (' <a href="%s">More</a>' % link if link else ""))

# ---------------------------------------------------------------- all tools (detailed)
def td(tid, name, summary, rows, img=None, alt="", cap="", steps=None):
    """One tool, in detail: what it is for, then a few labelled rows, optional steps and a screenshot."""
    dl = "".join("<dt>%s</dt><dd>%s</dd>" % (k, v) for k, v in rows)
    st = ("<p class=\"stl\"><b>How to use it</b></p><ol class=\"steps\">%s</ol>" % "".join("<li>%s</li>" % x for x in steps)) if steps else ""
    text = '<div><h3 id="%s">%s</h3><p class="what">%s</p><dl>%s</dl>%s</div>' % (tid, name, summary, dl, st)
    if img:
        return '<div class="td phead">%s%s</div>' % (text, figure(img, alt, cap))
    return '<div class="td">%s</div>' % text

NO = "No. It only reads."
b = head("All tools", "Every tool, in plain words", "Photo Clinic is a set of small tools. The <b>Workflow</b> tab runs the common ones in order, and the <b>Tools</b> tab has each one on its own. You do not need all of them. Here is each one: what it is for, what it does, whether it can change your files, and how to use it. Not sure where to begin? Open the <b>Workflow</b> tab, or <b>Start here</b> on the Home tab.", "tools.jpg", "The Tools screen with the tools as coloured tiles", "The Tools tab")
b += """<div class="callout"><b>Every tool that changes files works the same way.</b> It starts with a <b>Preview</b> button that changes nothing. When you like what you see, the button becomes <b>Do it for real</b>, and it goes back to Preview if you change any setting. Every job ends in one short card: a headline, a before-and-after strip, where it went, how to undo it (or a plain note that it cannot be undone), and a <b>Details</b> button that opens the choices, the folders and a list of <b>every file</b> with where it came from and what happened to it. Tools that only look say so.</div>
<h2>A preview explains every choice</h2>
<div class="phead" style="padding-top:0"><div><p class="sub">After you press <b>Preview</b>, every option shows what it did to your files, right under it, so you see exactly what each switch does and how many files it touches.</p>
<ul class="ticks"><li><b>A count and an example.</b> &ldquo;4 folders: 16 files go into 2017/2017-07 Summer in Lisbon &hellip;&rdquo;, or &ldquo;1 folder: Japan 2025 (1) &rarr; Japan 2025&rdquo;.</li><li><b>Options you left off say what they would do.</b> &ldquo;Would affect 2 folders: Takeout wrapper folders&rdquo;, with a button to turn it on and preview again.</li><li><b>Show them.</b> One click filters the list of every file to just the files that option touched.</li><li><b>Slow questions are asked, not forced.</b> Counting exact copies in different folders means reading every file, so it waits for you to press <b>Count it</b>.</li><li><b>Warnings that name the consequence.</b> If 43 pictures have no date and the file date is today, it says they would be filed under today, and offers <i>_undated</i> instead.</li><li><b>A before-and-after strip</b> for the whole job: files kept, deleted, changed, how much is copied, what is renamed, and what Undo does.</li></ul></div>
<figure><img class="shot" src="img/move-impact.jpg" width="1188" height="1941" loading="lazy" alt="The Move options after a preview, each with a count and an example under it"><figcaption>Move, after a preview: every option reports its effect</figcaption></figure></div>
<h2>Jump to a tab</h2>
<p class="jump"><a href="#home">Home</a> &middot; <a href="#fix">Fix</a> &middot; <a href="#tidy">Tidy</a> &middot; <a href="#move">Move</a> &middot; <a href="#check">Check</a> &middot; <a href="#cloud">Copy from the cloud</a> &middot; <a href="#rescue">Rescue</a> &middot; <a href="#tools">Tools</a></p>
"""
b += '<h2 id="home">Home</h2><p class="sub">Pick a job, or let Photo Clinic look at what you have and suggest one.</p>'
b += td("start-here", "Start here", "For when you are not sure where to begin.", [
 ("What it does", "You choose what you have: a Google Takeout (zip files or folder), a folder of photos, a Photos library, or an old iPhoto or Aperture library. Photo Clinic works out which it is, looks inside, says what is wrong with it in plain words, and builds a plan with the steps in order. Each step has a button for the tool that does it."),
 ("Use it when", "You have a pile of photos and no idea which tool to use, or you want one recommended path."),
 ("Changes your files?", NO + " The plan only opens the other tools, and each of those starts with a preview."),
 ("You get", "A short plan with the steps in order, and your progress is remembered if you come back.")],
 "tab-start.jpg", "The top of Home: what do you have, with a Look at it button for each source", "Home: choose what you have, then Look at it",
 ["Open <b>Start here</b> on Home.", "Press <b>Choose&hellip;</b> and pick a folder, a Takeout zip or a Photos library (or drop it on the box at the top).", "Press <b>Look at it</b> and read what was found.", "Press <b>Make my plan</b> and follow the steps."])
b += '<h2 id="fix">Fix</h2><p class="sub">Put the real dates, places and captions back on photos that came out of Google Photos.</p>'
b += td("fix-my-photos", "Fix my photos", "For a Google Takeout. Google keeps the date, place and caption in a separate <code>.json</code> file and leaves the photo bare. This writes them back.", [
 ("What it does", "Matches every photo to its <code>.json</code> file (even across zips and numbered or cut-off names) and writes the real date, location, caption, people and favourites into the photo. It writes dates in local time with the right offset, pairs Live Photos with their video, keeps album names, skips exact copies, handles Google's edited copies, and rebuilds missing dates from file names and folder names, labelled as guesses. Five styles from <b>Safest</b> to <b>I like risk</b> set every option for you."),
 ("Use it when", "Your photos show the day you downloaded them, or are missing places and captions."),
 ("Changes your files?", "By default it makes fixed <b>copies</b> in Where to save and leaves your Takeout alone. Only choosing <b>Fix in place</b> writes into your own files, and it says so in capitals."),
 ("You get", "A result card with a before-and-after <b>storyboard</b> of a few of your real photos (what the date, place and caption change from and to), the counts, and a list of every file. A preview shows the same, with nothing changed.")],
 "easy-fix.jpg", "The Fix my photos screen with quick jobs and options", "The Fix screen: pick a style, press Preview",
 ["Add your Takeout zip files or folders under <b>File Sources / Locations</b>, and choose <b>Where to save</b>.", "Choose a style with the button at the top (<b>Balanced</b> is the default). Not sure what to tick? Press <b>Help me choose</b> and read its advice.", "Press <b>Preview</b> and look at the storyboard and the list.", "Press <b>Do it for real</b>. Keep your Takeout until you have checked the result."])
b += '<h2 id="tidy">Tidy</h2><p class="sub">Clear leftovers, make old videos play, and find the same picture saved twice.</p>'
b += td("tidy-leftovers", "Tidy up leftovers", "For the clutter a copy or a Takeout leaves behind.", [
 ("What it does", "Five steps, always in the safe order: <b>1</b> give files with no extension a proper one; <b>2</b> delete Google's extra <code>.json</code> files (off until you tick it); <b>3</b> delete junk and cache files (system leftovers, Picasa.ini, iPod thumbnail caches, temporary files, empty files); <b>4</b> tidy names (remove <i>(1)</i> and <i>copy</i>, extra spaces, and put a folder with a date in its name under that year); <b>5</b> delete empty folders, so the last step catches the ones the others leave."),
 ("Use it when", "You have finished fixing or merging and want the folders clean."),
 ("Changes your files?", "<b>Yes.</b> It deletes, renames and merges. That is why it starts as a preview, lists every change, and says that removed and renamed items cannot be put back from Photo Clinic."),
 ("You get", "A card with one fact per step and a list of every change, which you can filter by step.")],
 "tab-tidy.jpg", "The Tidy up screen with its five steps", "Tidy up: five steps, in a safe order",
 ["Choose the folder under <b>File Sources / Locations</b>.", "Tick the steps you want (the defaults are cautious).", "Press <b>Preview</b> and read the list of changes.", "Press <b>Do it for real</b>."])
b += td("smart-folder-consolidation", "Smart folder consolidation", "Finds folders that are really the same folder with slightly different names and merges them.", [
 ("What it does", "Spots groups such as <i>Japan 2025</i>, <i>delete-Japan 2025</i> and <i>Japan 2025-old</i>, shows each group, and merges the ones you tick into one folder. Identical files are kept once; different files with the same name are both kept."),
 ("Changes your files?", "Yes, it moves files. It starts as a preview. Merged folders are gone from their old places and this cannot be undone from Photo Clinic.")])
b += td("videos", "Videos that will not play", "Turns old video formats into MP4 that plays everywhere, including in Apple Photos.", [
 ("What it does", "Converts <code>.avi</code>, <code>.mpg</code>, <code>.mpeg</code>, <code>.wmv</code>, <code>.3gp</code>, <code>.flv</code>, <code>.mkv</code>, <code>.mts</code>, <code>.m2ts</code> and <code>.vob</code> (and <code>.mov</code> if you tick it). It re-wraps without re-encoding when it can, so nothing is lost, and re-encodes only when it must. Each result is checked before the old file is touched. Live Photo videos are left alone unless you say otherwise. A preview estimates the size afterwards by test-encoding a few samples."),
 ("Changes your files?", "It makes new MP4s. <b>What to do with the old video</b> is your choice: move it to an <code>_original_videos</code> folder (the default), keep it, or delete it (the card tells you which, and that deleting cannot be undone)."),
 ("You get", "A card with how many were converted, how, the space saved, and a list of every video and what happened.")],
 "tab-videos.jpg", "The Videos that will not play screen", "Choose which video types to convert")
b += td("look-alikes", "Find look-alike photos", "The same picture saved twice, or at another size, or lightly edited.", [
 ("What it does", "Compares how pictures <b>look</b>, not what they are called, and shows each group side by side with a suggested keeper. The keeper is chosen by rules you control: a favourite wins, an edited version wins, more pixels, a bigger file, more information inside, in an album, a real photo over a screenshot, and bursts are kept by default. You can tick or untick any photo."),
 ("Changes your files?", "Only when you press <b>Set aside the ticked photos</b>. They are moved, not deleted, into a <code>_similar_set_aside</code> folder with their folder structure. <b>Undo</b> in Past runs moves them back."),
 ("You get", "A card with groups, extra copies and the space you could free, and the list to review.")],
 "look-alikes.jpg", "The look-alike photos result with Keep and Set aside choices", "Each group has a suggested keeper; you decide")
b += '<h2 id="move">Move</h2><p class="sub">Combine folders, sort them into neat folders, copy an old library out, or send photos to Apple Photos.</p>'
b += td("combine-arrange", "Combine and arrange folders", "For a folder full of folders.", [
 ("What it does", "<b>Combines:</b> folders with the same name merge at any depth; identical files are kept once; two different files with the same name are both kept (or one wins, as you choose). <b>Arranges</b> (tick <i>Arrange them by date and event too</i>): files are filed by the date each picture was taken. The default is a folder per year with a folder per month inside it (<code>2025/2025-04</code>); year only, year, month and day, or one folder per month are one click away. A folder with a real name, like <i>Japan 2025</i>, stays together as an event, with the date first (<code>2025-04 Japan</code>) and filed in its year. <i>Japan 2025</i> and <i>2025 Japan</i> become one folder."),
 ("Changes your files?", "By default it <b>copies</b> into Where to save. Tick <i>Move instead of copy</i> to empty the source folders instead. <b>Undo this run</b> in Past runs removes copies or moves files back (extra identical copies that you chose to delete cannot come back)."),
 ("You get", "A before-and-after strip, a count and example under <b>every option</b> (including the ones you left off), and a list of <b>every file</b>: where it came from, where it goes, and why (for example, dated from the picture or from its folder). Click a path to see it in Finder. See <a href=\"organise-photos-by-date-mac.html\">how to sort photos into folders by date</a>.")],
 "move-options.jpg", "The Move screen with the arrange options", "Choose the layout, and what happens to named folders",
 ["Add the folders under <b>File Sources / Locations</b> and a new folder under <b>Where to save</b>.", "Open <b>Move</b>, choose <b>A folder</b>, and tick <b>Arrange them by date and event too</b> if you want it.", "Press <b>Preview</b> and look through the list.", "Press <b>Do it for real</b>."])
b += td("old-library-in-move", "Old libraries (iPhoto, Aperture, old Photos)", "Add the old library and Move does the rest.", [
 ("What it does", "Move recognises an old library and says so. It reads the library's own database, so albums, keywords, people, ratings, titles, places and edited versions come with the pictures, and it copies them into clean folders: by album, year, year then month, year, month and day, one folder per month, or keeping the library's own folders. It skips exact and probable copies, and can skip pictures you already have in your current library. <b>Copy gently</b> goes slowly with a rest after every file, for a struggling drive."),
 ("Changes your files?", "The old library is only ever read. The copies are made in Where to save, and <b>Undo</b> removes exactly what the run made. After a good copy you can choose <b>Clear the copied originals</b>, to the Trash or deleted for good (you type DELETE), for the files whose copy is verified."),
 ("You get", "A card with what was found (pictures, edits, videos, albums, keywords, people), what would be copied into how many folders, and a list of every file. See <a href=\"old-libraries.html\">Old libraries</a>.")],
 "old-library.jpg", "Move reading an old library: what was found and what would be copied", "An old library, previewed in Move")
b += td("apple-photos", "Send to Apple Photos", "Sends a finished library into the Photos app in careful batches.", [
 ("What it does", "Sends oldest first in batches of about 2 to 50 GB so the timeline fills in order, keeps a Live Photo's picture and video together, turns album folders into Photos albums, and waits between batches for iCloud to keep up (until each batch has uploaded, until there is room, until you press Continue, or not at all). Files Photos cannot import are listed and left out."),
 ("Changes your files?", "It does not change your files. It <b>adds to your Photos library</b>, and Photos has no undo for imports, so start with <b>Preview</b>, then <b>Send a small test (20 photos)</b> and look at it in Photos."),
 ("You get", "A card with how many were sent, in how many batches, how many were already there, and any that cannot be imported. See <a href=\"apple-photos.html\">Apple Photos</a>.")],
 "tab-applephotos.jpg", "The Send to Apple Photos screen", "Batch size, waiting and a small test",
 ["Choose your finished library under <b>File Sources / Locations</b>.", "Open <b>Move</b> and choose <b>Apple Photos</b>.", "Press <b>Preview</b> to see the batches.", "Press <b>Send a small test</b>, check it in Photos, then <b>Do it for real</b>."])
b += '<h2 id="check">Check</h2><p class="sub">Is my library healthy? Is it really in iCloud? What is it doing?</p>'
b += td("check-my-photos", "Check my photos", "One scan for your folders, and your Photos library too if you tick Include my Photos library. It ends in a plan you can do in one go.", [
 ("What it does", "Gives a <b>health score out of 100</b> and a plain list of what is wrong, each with a button to the tool that fixes it: wasted space and duplicates, messy folders, empty or wrongly named files, old-format videos, files only in iCloud Drive, photos with no date or the wrong date, and more. With your Photos library included it also checks upload progress, the system logs and your Mac's free space and battery. <b>Look harder</b> reads far more files. <b>Check again later by itself</b> repeats it while the app is open."),
 ("Changes your files?", NO + " Fixing what it finds is done in the other tools, each with its own preview."),
 ("You get", "A verdict, a score history so you can see whether the library is getting tidier, and findings you can act on.")],
 "scan-plan.jpg", "Your plan: one row per job with its count, a tick box, Open and Do this one", "Scan everything ends in a plan: tick what you want and do it in one go",
 ["Choose your folders (and tick <b>Include my Photos library</b> if you want it checked).", "Press <b>Scan everything</b>.", "Read <b>Your plan</b>: each row has its count, a tick box, <b>Open</b> and <b>Do this one</b>.", "Press <b>Do the ticked ones</b> to run them in order, or do one job at a time."])
b += td("health-over-time", "Health over time", "A reading every 15 minutes, so you can see whether Photos is syncing, stuck or erroring.", [
 ("What it does", "Takes a reading of your Photos library (its database, the system log and the sync engine) every 15 minutes while Photo Clinic is open, or when it is closed if you switch that on, and draws the trend. It tells <b>syncing</b>, <b>stuck</b> and <b>erroring</b> apart, which is hard to see from the outside on a big iCloud library."),
 ("Changes your files?", NO + " It reads a copy of the database."),
 ("You get", "A state in plain words, a trend chart, and a note if the readings stop.")],
 "tab-health.jpg", "The Health over time screen", "Readings, and whether to keep taking them")
b += td("is-it-in-icloud", "Is it in iCloud?", "Counts what has uploaded, how fast, and whether it looks stuck.", [
 ("What it does", "Reads a copy of your Photos library's database to count what has reached iCloud, the speed, and the time left. It can also check that the photos in a folder you chose have <b>arrived in Photos</b>, by file name and size. <b>Make a migration receipt</b> saves a record of what arrived. Apple does not document this database, so treat the numbers as a strong hint and confirm in Photos and on iCloud.com."),
 ("Changes your files?", NO + " <b>Keep it syncing while I am away</b> opens the Keep sync running tool."),
 ("You get", "A plain answer, a progress figure and a receipt you can keep.")],
 "tool-icloud.jpg", "The Is it in iCloud? tool", "Is it all uploaded?")
b += '<h2 id="cloud">Copy from the cloud</h2><p class="sub">Copy iCloud Drive, a Google Drive folder, or your Takeout files from an email to a drive you choose.</p>'
b += td("copy-icloud-drive", "Copy iCloud Drive", "A slow, careful copy of iCloud Drive folders to your own drive.", [
 ("What it does", "Copies the folders you tick, one file at a time. Files that are only in iCloud are brought down, copied, checked, and taken off your Mac again. You can compare with an earlier copy and copy only the gaps. It shows the speed, an honest time left, and a line for every file."),
 ("Changes your files?", NO + " iCloud is only read. The copy goes into a folder called iCloud Drive inside Where to save. An optional green Finder tag can be added to each original once its copy is checked."),
 ("You get", "A folder-by-folder view of what is copied and what is missing, a list of the gaps, and any problems grouped by cause with what to do. See <a href=\"copy-icloud-drive-to-external-drive-mac.html\">Copy iCloud Drive to an external drive</a>.")])
b += td("copy-google-drive", "Copy a Google Drive folder", "Download your own Google Drive folders to your drive.", [
 ("What it does", "You sign in with your own Google account on Google's page (read-only), browse My Drive or Shared with me, and copy the folders you choose. It carries on where it stopped, keeps files that share a name, and checks at the end that everything arrived."),
 ("Changes your files?", NO + " It can only read your Drive."),
 ("You get", "A summary with sizes, speed and time left while it runs, and a clear reason for anything Google refused. See <a href=\"download-google-drive-folder-mac.html\">Download a Google Drive folder</a>.")])
b += td("links-from-an-email", "Links from an email", "Paste an email with &ldquo;View 1 of 43 in Drive&rdquo; links or Takeout download links.", [
 ("What it does", "Finds every link, puts them in order, and makes a checklist. Google Drive links download here, several at a time. Takeout links that must be opened in the browser are tracked: finished files are moved from Downloads into your folder and ticked off."),
 ("Changes your files?", "It moves only complete, readable Takeout zips out of Downloads, and only when you have started the watch."),
 ("You get", "A runsheet with the state, size and speed of every part, and a button to use the finished zips as your Takeout source.")])
b += td("not-in-photos-yet", "What is not in Photos yet?", "Compares a folder with your Photos library.", [
 ("What it does", "Matches by content and by Photos' own records (original name and exact size, so pictures that live only in iCloud count). Shows what is already in, what is a different version and what is missing, side by side with thumbnails, and suggests the best album."),
 ("Changes your files?", "It only reads, until you choose to copy the missing ones into a new folder, or to move the ones Photos already has into <code>_already_in_Photos</code>. Nothing is deleted."),
 ("You get", "Four counts, a list with pictures and links, and the buttons for what to do next. See <a href=\"photos-not-in-apple-photos.html\">Find photos that are not in Apple Photos</a>.")])
b += '<h2 id="rescue">Rescue</h2><p class="sub">Photos that are hard to get at: an old library, or a failing drive.</p>'
b += td("rescue-old-library", "Rescue an old library", "Opens Move with your old library chosen (see Move above).", [
 ("Good to know", "If a drive keeps stalling, files it will not answer on for 90 seconds are skipped and listed, the copy carries on with the rest, and they are tried last next time. <b>Keep trying</b> goes back to just those files. If your Mac has crashed during a long copy, tick <b>Copy gently</b>. The old library is never changed."),
 ("Changes your files?", "Not the library. The copies go to Where to save and can be undone.")],
 "tab-rescue.jpg", "The Rescue tab", "Rescue: an old library, or a failing drive")
b += td("find-damaged-files", "Find damaged files", "Finds pictures and videos that will not open.", [
 ("What it does", "Checks every photo and video you chose and lists the ones that are cut short, empty, filled with zeros or will not open, and any that make the drive stop answering (if the drive stalls the scan stops and says so, instead of freezing). The quick check looks at the file; <b>Check thoroughly</b> reads each file to the end and tries to open it, which is much slower and finds damage in the middle. <b>Copy the good files</b> copies only the healthy ones, one at a time and gently, to a safe place."),
 ("Changes your files?", "Finding is read-only. Copying makes copies. The option to <b>remove each file from the original place once its copy is verified</b> is off unless you tick it. You can also tag the damaged files in Finder, and remove the tag later."),
 ("You get", "A list of damaged files with the reason, and a place to copy the good ones.")],
 "tool-damaged.jpg", "The Find damaged files tool", "Find, then copy only the good files")
b += '<h2 id="tools">Tools</h2><p class="sub">Small tools that each do one job. They open over the page, and most only read.</p>'
b += td("compare-two-places", "Compare two places", "How alike are two folders or libraries?", [
 ("What it does", "Takes two places (folders, Photos libraries, old libraries or Takeout zips), for example a source and the copy you made, and shows what is identical, the same file filed in a different folder, files with the same name that differ, the same picture at a different size, and what only one side has. From there you can <b>copy what only one place has</b> into a folder, and <b>clear the identical files from one side</b>: tag them in Finder so you can review, set them aside in a folder, move them to the Trash, or delete them for good (you type DELETE)."),
 ("Changes your files?", "Comparing is read-only. Every file is compared byte for byte with its twin just before it is removed, and only removed if the twin is still there. The other side is never touched, and it will not clear an Apple Photos library (do that inside Photos)."),
 ("You get", "A card with the percentage alike and the counts, and a list of every file as a spreadsheet.")],
 "compare.jpg", "The Compare two places result with the clear identical files panel", "Choose a side, choose how, press Remove",
 ["Add the two places under <b>File Sources / Locations</b>.", "Open <b>Tools</b>, then <b>Compare two places</b>, and press the button.", "Read the card. To clear the identical files, choose a side and how, then <b>Remove&hellip;</b>."])
b += td("count-my-photos", "Count my photos", "How many photos and videos you have, how big, and where.", [
 ("What it does", "Counts photos and videos in the folders you chose (and your Photos library if you include it), with size, by file type and by folder."),
 ("Changes your files?", NO)])
b += td("disk-space", "Disk space", "Where is my disk space going?", [
 ("What it does", "For when <b>Optimise Mac Storage</b> is on but the library is not shrinking. Shows what takes the space and how much Photos could still free. It can take a minute or two on a big library."),
 ("Changes your files?", NO)],
 "tool-space.jpg", "The Disk space tool", "Check my space")
b += td("look-up-a-photo", "Look up a photo", "Turns an id in a log message into the real photo.", [
 ("What it does", "Paste a long Photos id from a log (or part of one), or part of a file name. It shows the real file name, date and albums."),
 ("Changes your files?", NO)],
 "tool-lookup.jpg", "The Look up a photo tool", "Paste an id or part of a name")
b += td("broken-thumbnails", "Broken thumbnails", "Finds the grey or black squares in Photos.", [
 ("What it does", "Finds photos whose small preview picture is missing, empty or the wrong size, and can copy the affected photos to a folder so you can re-import them."),
 ("Changes your files?", "It only reads your Photos library and never changes it.")],
 "tool-thumbs.jpg", "The Broken thumbnails tool", "Find broken thumbnails")
b += td("sync-meter", "Sync meter", "How fast Photos is talking to iCloud right now.", [
 ("What it does", "Reads the network use of the Photos and iCloud background processes and the library's own upload count, and shows how the queue is moving. It also has <b>Is iCloud's queue moving?</b> and a button to <b>restart the iCloud Photos service</b> if it is stuck."),
 ("Changes your files?", "No. Restarting the service restarts a macOS helper, not your photos.")])
b += td("icloud-drive-busy-files", "iCloud Drive busy files", "Which file is iCloud Drive stuck on?", [
 ("What it does", "iCloud Drive errors in the log never say which file. This lists the files that changed in the last 30 minutes in iCloud Drive, Desktop and Documents (a file that keeps changing, such as a database, a browser profile or a project folder, is the usual cause) and any items still waiting to download. It looks only at names and dates, never inside files."),
 ("Changes your files?", NO)],
 "tool-busyfiles.jpg", "The iCloud Drive busy files tool", "Find the busy files")
b += td("keep-sync-running", "Keep sync running", "For when nobody is at the Mac, such as a holiday.", [
 ("What it does", "Every 10 minutes it checks whether iCloud is stuck (the sync backlog not shrinking for an hour while the engine keeps growing, or a service pinned at 90% CPU) and restarts only that service, gently, at most once every 2 hours. It leaves things alone while iCloud is throttling, and gives up and tells you after 3 restarts that did not help. <b>Check before I leave</b> tells you whether it is ready."),
 ("Changes your files?", "No. It is off by default, and nothing leaves your Mac.")],
 "tool-keepsync.jpg", "The Keep sync running tool", "Turn it on, or check before you leave")
b += td("apple-system-status", "Apple system status", "Is Apple having a problem?", [
 ("What it does", "Many iCloud and Photos errors in the log are on Apple's side, and nothing on your Mac will fix them. This asks Apple's public status page whether anything is not green. It sends nothing about you or your photos, and only runs when you press the button."),
 ("Changes your files?", NO)],
 "tool-applestatus.jpg", "The Apple system status tool", "Check Apple's status")
b += td("read-the-log", "Read the log", "Photos and iCloud errors, in plain words.", [
 ("What it does", "Reads recent Photos, iCloud and Photo Clinic messages that you never see in Console and explains each in plain language with fixes, coloured <i>expected</i>, <i>worth watching</i> or <i>needs attention</i>. Look back from 1 hour to 7 days, switch between <b>Plain words</b> and <b>Technical</b>, paste log text from elsewhere, or have it check again by itself while the app is open."),
 ("Changes your files?", NO + " Nothing is uploaded unless you switch on the optional sharing of unrecognised lines (see <a href=\"privacy.html\">Privacy</a>).")],
 "tool-log.jpg", "The Read the log tool", "Choose how far back to look")
b += td("live-watch", "Live watch", "The messages as they happen.", [
 ("What it does", "Streams the Photos and iCloud messages as they happen and explains each one in plain language. They appear in the side panel, so you can keep it open while you work and filter or group them."),
 ("Changes your files?", NO)],
 "tool-live.jpg", "The Live watch tool", "Start watching")
b += td("fix-guides", "Fix guides and Known problems", "Checklists and a reference list.", [
 ("Fix guides", "Pick what you are seeing. Each guide is an ordered checklist: some steps are buttons in Photo Clinic, some you do in Photos or Finder, some are a Terminal command you can copy. Your ticks are remembered on this Mac."),
 ("Known problems", "A built-in reference list of known Photos, iCloud and macOS problems, each with a badge for how serious it would be. It is <b>not</b> a report about your library: to see what is wrong with yours, use Check my photos."),
 ("Changes your files?", NO)],
 "tool-guides.jpg", "The Fix guides tool", "Pick what you are seeing")
b += """<div class="callout"><b>Always safe to try.</b> Everything starts as a preview. Tools that only look say so. Tools that can remove files ask first, show you the count, and say whether the files go to a folder, the Trash or are gone for good. Keep a backup anyway.</div>
%s%s""" % (cta(), nextlinks(("story.html", "Our story"), ("fix-takeout.html", "Google Takeout")))
page("tools.html", "All tools", "Every Photo Clinic tool in plain words: fix, tidy, move, check and rescue.", b, "tools.html")

# ---------------------------------------------------------------- fix takeout
b = head("Google Takeout metadata fixer for Mac", "Fix your Google Takeout metadata and give every photo its story back", "Photo Clinic is a free Google Takeout metadata fixer for Mac. Google keeps the dates, places and captions in separate files and leaves the photos themselves bare. Photo Clinic reads those files and writes everything back.", "easy-fix.jpg", "The Fix my photos screen with quick jobs and options", "Fix my photos: choose a style, then look at your files")
b += """<h2>What goes wrong in a Takeout</h2>
%s
<h2>What Photo Clinic puts right</h2>
%s
<h2>Dates and places, even when Google has none</h2>
%s
<h2>Choose how careful to be</h2>
<p class="sub">Five styles set every option for you: <b>Safest</b>, <b>Balanced</b> (the recommended mix), <b>Fastest</b>, <b>Thorough</b> and <b>I like risk</b>. Only want one job? The quick jobs do just the JSON fix, just dates, just places, or fix in place.</p>
<div class="phead" style="padding-top:0"><div>%s</div><figure><img class="shot" src="img/styles.jpg" width="960" height="1440" loading="lazy" alt="A table comparing what the five styles turn on and off"><figcaption>All five styles side by side</figcaption></figure></div>
<h2>See it before it happens</h2>
%s
<p class="sub">The result is one card: what happened, how many files, where they went, and a list of <b>every file</b> with where it came from and where it went. Each path opens in Finder.</p>
<figure><img class="shot" src="img/fix-result.jpg" width="1182" height="1719" loading="lazy" alt="The result card of a preview: headline, facts, before and after storyboard and the list of every file"><figcaption>A preview of a Takeout fix: nothing has changed yet, and it says so</figcaption></figure>
<p class="sub">After a preview, <b>every option says what it did or would do</b>, with a count and an example, even the ones you left off. Press <b>Show the 26</b> to open the exact files behind that number.</p>
<figure><img class="shot" src="img/fix-impact.jpg" width="1188" height="2490" loading="lazy" alt="The Fix options after a preview, each with a count and an example under it"><figcaption>Fix, after a preview: every option reports its effect</figcaption></figure>
<figure><img class="shot" src="img/show-them.jpg" width="1182" height="416" loading="lazy" alt="The window that opens from Show the 26, listing each file with the date written"><figcaption>Show the 26: the exact files behind the count</figcaption></figure>
<div class="callout"><b>Good to know.</b> Some old video formats (AVI, MKV, WMV, MPG, MTS) and BMP files cannot hold this kind of information, so those only get their file date fixed. Other files in your Takeout, such as PDFs, are copied beside the photos so your copy is complete.</div>
%s%s""" % (
 ticks(["Every photo shows the day you <b>downloaded</b> it, not the day you took it.", "Locations and captions are missing from the pictures.", "Live Photos arrive split into a picture and a separate video.", "Google's <code>-edited</code> copies sit next to the originals.", "Albums become folders full of duplicate copies.", "Hundreds of <code>.json</code> files clutter the folders, and names get cut off or numbered <code>(1)</code>."], "bad"),
 cards([("Dates, places, captions", "Restored from Google's own files: dates, locations, captions, people and favourites, across many zips and batches."), ("Time zones done properly", "Google stores times in UTC. Photo Clinic writes local time with the right offset, using the photo's location or this Mac's time zone."), ("Live Photos back together", "The picture and its video are paired again so Apple Photos treats them as one."), ("Edited copies matched", "Choose to keep both, keep the edit or keep the original."), ("Albums kept", "One copy of each photo is kept, and the albums are written out as keywords and a list so nothing is lost."), ("Motion Photos", "The video hidden inside a Google Motion Photo is pulled out and saved as a normal MP4.")]),
 ticks(["<b>Missing dates rebuilt</b> from the file name (<code>IMG_20190704_&hellip;</code>, <code>PXL_&hellip;</code>, screenshots), neighbouring photo numbers, the folder name and the file's own time. Each guess has a confidence you can review.", "<b>Places filled in</b> from nearby photos or a GPX track, or guessed from a folder name like <code>Johannesburg</code>. Guesses are labelled as guesses and never replace a real location.", "<b>Place names written in</b> (city, region, country) from an offline list of about 144,000 towns and cities. No internet needed.", "<b>Wrong dates flagged</b>, such as future dates or a year that disagrees with the folder."]),
 ticks(["Every style starts as a <b>preview</b>. Nothing changes until you press <b>Do it for real</b>.", "Compare all five in one table, and save your own settings as a favourite with the star."]),
 ticks(["A <b>pre-flight check</b> tells you what is in your Takeout before anything runs.", "A <b>before-and-after storyboard</b> shows a few of your real photos with what changes in the date, place and caption.", "Your originals are <b>copied, not touched</b>.", "<b>Start here</b> can do all of this for you: it looks at what you have and builds the plan."]),
 cta(), nextlinks(("tools.html", "All tools"), ("monitor.html", "Monitor your Photos library")))
page("fix-takeout.html", "Google Takeout metadata fixer for Mac", "A free Google Takeout metadata fixer for Mac: restore the real dates, places, captions, Live Photos and albums that Google leaves out of your exported photos.", b, "fix-takeout.html")

# ---------------------------------------------------------------- monitor
b = head("Monitor", "Is Photos syncing, or is it stuck?", "A big iCloud library can take days or weeks to sync, and from the outside it is hard to tell working from stuck. Photo Clinic keeps watch, shows the trend, and tells you in plain words.", "photos-health.jpg", "The Photos Health screen with a plain verdict, library counts and trend", "Photos Health (sample data)")
b += """<h2>A plain verdict</h2>
<p class="sub">One word and one sentence on what to do. It only reads; it never writes to your library.</p>
<div class="states">
<div><b>Healthy</b>Nothing is wrong and nothing is happening.</div>
<div><b>Downloading</b>Catching up with iCloud. Normal.</div>
<div><b>Merging</b>Albums and edits being merged. Normal; Apple needs days.</div>
<div><b>Waiting on sync</b>Photo analysis is waiting for iCloud.</div>
<div><b>Errors</b>iCloud is returning errors.</div>
<div><b>Stuck</b>Only when every sign agrees (see below).</div>
</div>
<h2>What it records</h2>
%s
<h2>It never guesses</h2>
%s
<h2>Also on watch</h2>
%s
<h2>When it runs</h2>
%s
<div class="callout"><b>One permission.</b> To read the Photos database, macOS needs you to give Photo Clinic <b>Full Disk Access</b> once. If it is missing, Photo Clinic says so, names the program and opens the settings page for you.</div>
%s%s""" % (
 cards([("Your library", "Photos and videos (visible, hidden, deleted), albums and how many have been analysed."), ("iCloud's sync backlog", "The size of the queue iCloud works through. It should shrink over time."), ("Errors", "iCloud error counts, and how busy the sync process is."), ("Trends", "A chart for each number, the change over 24 hours, and a warning if the backlog has not moved for hours.")]),
 ticks(["Anything it cannot measure is shown as <b>unknown</b>, not as good or bad.", "A steady heartbeat in the logs is <b>not</b> treated as progress or as a stall.", "<b>Stuck</b> needs all three: the merge has run for hours, the backlog has not moved, and the sync process is busy. Then it tells you to leave the library alone and keep the evidence."]),
 cards([("Live watch", "Messages from Photos and iCloud as they happen, with the real file name, date and albums instead of a long id. You can filter by how serious they are."), ("Keep sync running", "For a holiday. Every 10 minutes it checks whether iCloud is truly stuck, and restarts only that service, gently, at most once every two hours. After three tries that did not help it stops and tells you."), ("Apple system status", "Checks Apple's own status page, so you know if the problem is on Apple's side before you change anything."), ("Status bar and side panel", "Shows the job that is running, how far it has got and how long is left, and keeps the last results one click away.")]),
 ticks(["<b>While Photo Clinic is open</b>, it takes a reading every 15 minutes. You can leave it in the background.", "<b>A separate background job</b> is optional, so readings continue while the app is closed.", "A <b>full dashboard page</b> adds a gap check against iCloud.com, a by-year breakdown and your own to-do list."]),
 cta(), nextlinks(("fix-takeout.html", "Google Takeout"), ("problems.html", "Find what is not right")))
page("monitor.html", "Monitor", "Photos Health records how your Apple Photos and iCloud library is doing every 15 minutes, with live messages, Apple's status and a gentle keep-alive.", b, "monitor.html")

# ---------------------------------------------------------------- problems
b = head("Find problems", "Photos and iCloud fail quietly", "Photo Clinic reads what they will not tell you and explains it in plain words, with fixes to try. It only looks. It changes nothing.", "tools.jpg", "The Tools screen with the monitoring and finding tools", "The tools that read and explain")
b += """<h2>One tap for the big picture</h2>
<p class="sub"><b>Check my photos</b> gives one verdict (healthy, needs attention or problem) from four checks:</p>
%s
<h2>Is it all in iCloud?</h2>
%s
<h2>Reads the messages you never see</h2>
%s
<h2>Fixes, in order</h2>
%s
<div class="callout"><b>Honest about its limits.</b> Apple does not document the Photos database or most of its messages, and they change between macOS versions. So upload counts are a strong hint, not a guarantee, and many explanations are our best reading. Each one says how sure we are and where it came from. Give Apple's servers days, not minutes, before deciding something is permanently stuck.</div>
%s%s""" % (
 cards([("Your library files", "Empty, wrongly named and duplicate files, older formats and look-alike folders."), ("Photos upload progress", "Whether Photos is progressing or stuck, with time left."), ("Photos and iCloud logs", "Problems in the system logs, explained with fixes."), ("This Mac", "Free space, battery, power mode and heat.")]),
 ticks(["<b>Is it all uploaded?</b> Counts what is in Photos and what has reached iCloud, works out your speed and time left, and says so if nothing has moved for about 45 minutes.", "<b>Which photos have not uploaded?</b> Lists each one with its size, date and the likely reason: an empty file, a wrong extension, an unusual type, a huge file or a missing original.", "<b>Did my albums and Live Photos arrive?</b> Compares what you sent with what Photos holds.", "<b>Sync meter.</b> Shows how fast Photos talks to iCloud, and whether iCloud's own queue is shrinking or going round in circles.", "<b>iCloud Drive busy files.</b> Shows which file iCloud Drive keeps working on.", "<b>Where is my disk space going?</b> For when Optimise Mac Storage is on but the library is not shrinking."]),
 ticks(["<b>Read the log.</b> Recent Photos, iCloud and crash messages, grouped and explained: a full disk, a full iCloud plan, a dropped network, a sign-in problem, a damaged library, files Photos refused to import and more.", "<b>Live watch.</b> Streams the messages as they happen, and shows the real file name, date and albums of the photo a message is about, not a long id.", "<b>Look up a photo</b> from an id in a log, or part of a file name.", "<b>Broken thumbnails.</b> Finds photos whose previews are missing or empty.", "<b>Migration receipt.</b> A page you can share: what was done, how complete the metadata is, and what arrived in Photos and iCloud."]),
 cards([("More than 300 known messages", "A built-in catalogue of Photos, iCloud and macOS messages, each with the likely causes and fixes to try, safest first. It also knows many harmless message families and hides them so they do not bury the real problems. Most entries are our best reading, marked with how sure we are."), ("17 fix guides", "Step-by-step checklists: iCloud stuck or paused, &ldquo;Unable to Upload&rdquo;, ghost files, a library that will not open, copy error -36, a slow or hot Mac, shared albums and more. Each step says who does it: Photo Clinic, you, or a Terminal command you can copy."), ("Set it up for me", "Where a problem has a matching tool, one button switches to it and sets the options. It always leaves Preview on, never presses Start, and has an undo."), ("Help us explain more (optional)", "If you choose, Photo Clinic can share messages it does not recognise, cleaned of anything personal, so we can explain them for everyone. It is off until you turn it on. See Privacy.")]),
 cta(), nextlinks(("monitor.html", "Monitor"), ("tidy.html", "Duplicates and tidy-up")))
page("problems.html", "Find problems", "Photo Clinic reads the hidden Photos and iCloud messages, explains problems in plain words and gives fixes to try.", b, "problems.html")

# ---------------------------------------------------------------- tidy
b = head("Duplicates and tidy-up", "Get the whole library in order", "Remove copies, review look-alikes, compare two places and clean up. Nothing is deleted without a preview and a way back.", "look-alikes.jpg", "The Find look-alike photos screen with its matching and keeper rules", "Find look-alike photos: you choose the keeper rules")
b += """<h2>Two kinds of duplicate, two tools</h2>
%s
<h2>Compare two places, then clear what is the same</h2>
<p class="sub">Give it two folders or libraries, for example a source and the copy you made of it. It shows how alike they are, then lets you clear the identical files from one side.</p>
<div class="phead" style="padding-top:0"><div>%s</div><figure><img class="shot" src="img/compare.jpg" width="1230" height="1118" loading="lazy" alt="The Compare two places result with the clear identical files panel"><figcaption>Choose a side, choose how, press Remove</figcaption></figure></div>
<h2>Clean up</h2>
%s
<h2>Health score for your photos</h2>
<p class="sub">A score out of 100 with a plain list of what is wrong, and a button to the tool that fixes it. It keeps a history so you can see whether your library is getting tidier.</p>
%s
<div class="callout"><b>You stay in control.</b> Every one of these starts as a preview, copies by default, can be stopped, and can be undone from Past runs where a run can be undone. Tools that can remove files tell you whether they go to a folder, the Trash, or are deleted for good.</div>
%s%s""" % (
 cards([("Find look-alike photos", "One source, no target. Finds the same picture saved twice, or at another size, and suggests a keeper using rules you choose: favourite, edited, more pixels, bigger file, more information, in an album. Bursts are kept by default. Never deleted automatically."), ("Compare two places", "Two sources, side by side: what is identical, what is the same file in another folder, same name but different, same picture at a different size, and what only one side has.")]),
 ticks(["<b>Set aside in a folder</b> (the safest), <b>move to the Trash</b>, or <b>delete for good</b> (you type DELETE).", "Only files that are the <b>same in both places</b>. Every file is compared byte for byte with its twin just before it is removed, and is only removed if the twin is still there.", "The other side is <b>never touched</b>, and it will not clear an Apple Photos library (do that inside Photos).", "A list of everything removed is saved."]),
 cards([("Tidy up leftovers", "Clears empty files, wrongly named and temporary files, leftover folders and odd names."), ("Videos won't play", "Turns old video formats into MP4. Each conversion is verified before the original is replaced."), ("Blurry and screenshots", "Spots blurry pictures and screenshots so your keeper rules can prefer the sharp one."), ("Count my photos", "How many photos and videos, how big, and what is in your folders by type and by folder.")]),
 ticks(["Duplicate files, and the same file saved in several formats.", "Empty (0-byte) files, wrongly named files, temporary and leftover files.", "Look-alike folders, such as <code>Japan 2025</code> and <code>delete-Japan 2025</code>.", "Old video formats, and files only in iCloud Drive that are not on this disk.", "Photos with no date, and an estimate of the space you could win back."]),
 cta(), nextlinks(("problems.html", "Find problems"), ("old-libraries.html", "Old libraries")))
page("tidy.html", "Duplicates and tidy-up", "Find duplicates and look-alike photos, compare two places and clear what is identical, and tidy up your photo library.", b, "tidy.html")

# ---------------------------------------------------------------- old libraries
b = head("Old libraries", "Get your photos out of an old library", "An old iPhoto or Aperture library hides your photos in folders only that program understood. Photo Clinic reads its records and brings your photos out with their albums, keywords and ratings. It also copes when the drive is failing.", "old-library.jpg", "Move my photos reading an old library: what was found and what would be copied", "Preview of an old library in Move my photos")
b += """<h2>Just add it to Move my photos</h2>
<p class="sub">Add the old library under <b>File Sources / Locations</b>. Move says <i>This is an old library</i>, reads its database, and offers the same choices as for any folder: arrange by album, year, month or day, skip duplicates, copy gently. Preview first, then Do it for real.</p>
%s
<h2>When the drive is failing</h2>
<p class="sub">A drive that has started to fail can get stuck on a single file and never finish. We learned to plan for it.</p>
%s
<h2>When you have copied it all</h2>
<p class="sub">The old library is not changed by a copy. When you are happy, you can clear the originals you have safely copied, so only what is left to do remains.</p>
%s
<div class="callout"><b>Check before you clear anything.</b> Look at the copy first. Try the Trash option before deleting for good. If the drive is a backup of something you cannot replace, keep it until you are sure.</div>
%s%s""" % (
 ticks(["Reads <b>iPhoto, Aperture and older Photos libraries</b>, including <code>.migratedphotolibrary</code>, and tells you which kind it found.", "Copies your original pictures into folders named for your <b>albums and events</b>, or by year, or by month.", "Writes <b>keywords, ratings, titles, captions, dates and places</b> into the copies. For Photos libraries the edited versions are kept beside the originals; for iPhoto and Aperture libraries only the originals are read for now.", "Skips what is trashed or missing, and skips exact duplicates inside the library.", "Preview first: it shows the folders it would make and how many files, before it copies anything.", "Running it again <b>picks up where it stopped</b>: files already copied are skipped."]),
 ticks(["<b>Skips stuck files.</b> If the drive does not answer for 90 seconds, the files it stuck on are listed as skipped and the copy carries on.", "<b>Tries them last next time.</b> A rerun tries those files at the end, for a short time each, so they cannot hold up the others.", "<b>Keep trying.</b> One button after a copy retries just the files that failed.", "<b>Copy gently.</b> A slower copy that rests after every file, for a drive, cable or hub that is struggling.", "<b>Find damaged files</b> spots photos and videos that are cut short, empty or will not open, and can copy only the good ones.", "A saved list names every file that could not be copied, and why."]),
 ticks(["<b>Clear the copied originals</b> first shows how many are safely copied and how big they are, and moves nothing.", "It only touches an original whose copy is in your folder and about the same size. Files the drive stuck on are left alone.", "Choose <b>Move to the Trash</b> (you can put them back) or <b>Delete for good</b> (you type DELETE).", "If the drive stops answering part-way, it stops, and nothing is lost.", "<b>Compare two places</b> can double-check the copy against the library first."]),
 cta(), nextlinks(("tidy.html", "Duplicates and tidy-up"), ("apple-photos.html", "Apple Photos")))
page("old-libraries.html", "Old libraries", "Get photos, albums, keywords and ratings out of an old iPhoto or Aperture library, even from a failing drive.", b, "old-libraries.html")

# ---------------------------------------------------------------- apple photos
b = head("Apple Photos", "Send it slowly, safely", "Importing a huge library all at once can fill your Mac and confuse iCloud. Photo Clinic sends it in careful batches and waits for iCloud to keep up.")
b += """<h2>How it sends</h2>
%s
<h2>Waiting for iCloud</h2>
<p class="sub">Between batches it waits so Photos can upload. You choose how:</p>
%s
<h2>Before you start</h2>
%s
<div class="callout"><b>Photos has no undo for imports</b>, and Photo Clinic cannot take photos back out of Photos. That is why it starts with a preview and a small test. Keep your finished library and your Takeout until you have checked everything in Photos and iCloud.</div>
%s%s""" % (
 ticks(["<b>Batches of about 2 to 50&nbsp;GB</b>, oldest first, so your timeline fills in order.", "A Live Photo's picture and video always travel together.", "Folders that are albums become Photos albums.", "Photos skips what it already has, so running it again never duplicates.", "Files Photos cannot import (such as AVI, MKV, WMV) are listed and left out. Convert them first with Videos won't play."]),
 cards([("Until it reaches iCloud", "The default. Reads the Photos database to see each batch uploaded, and can make batches smaller or bigger depending on how iCloud keeps up."), ("Until there is room", "Waits until your Mac has the free space you choose."), ("Pause for me", "Stops between batches and waits for you to press Continue."), ("Do not wait", "Sends the next batch straight away.")]),
 ticks(["In Photos, turn on <b>iCloud Photos</b> and choose <b>Optimize Mac Storage</b>.", "<b>Preview</b> first, then <b>send a small test of 20 photos</b> and look at it in Photos.", "Leave Photos open and the Mac awake. Keep sync running can look after it while you are away.", "Short of space? Build the library on an <b>external drive</b>.", "The first time, macOS asks if Photo Clinic may control Photos. Allow it."]),
 cta(), nextlinks(("old-libraries.html", "Old libraries"), ("safety.html", "Safe and private")))
page("apple-photos.html", "Apple Photos", "How Photo Clinic sends a large library to Apple Photos in careful batches and waits for iCloud.", b, "apple-photos.html")

# ---------------------------------------------------------------- safety
b = head("Safe and private", "Built so you can trust it with your only copy", "Your photos are the one thing you cannot get back, so everything here is built around not hurting them.")
b += """<h2>Safe</h2>
%s
<h2>Everything is written down</h2>
<p class="sub">Every run is kept in <b>Past runs</b> (in the Activity tab of the right-hand pane) with a report and a log. You can search it, open the folder, and undo a run that copied or moved files.</p>
<figure><img class="shot" src="img/past-runs.jpg" width="1185" height="1350" loading="lazy" alt="The Past runs list with filters and one row per run"><figcaption>Past runs: what happened, where it went, and a way back</figcaption></figure>
<h2>Private</h2>
%s
<h2>Permissions it asks for</h2>
%s
<div class="callout"><b>Please still back up your photos first.</b> Photo Clinic can move or delete files if you ask it to. It is provided as is, with no warranty. Keep your original Takeout until you have checked the result in Photos and iCloud.</div>
<h2 id="app-store">Why is it not in the Mac App Store?</h2>
<p class="sub">Because the App Store would make it do less. Apps there must run inside Apple's <b>sandbox</b>, which walls an app off from the rest of your Mac. Photo Clinic's whole job is to reach across that wall:</p>
%s
<p>That is why Photo Clinic is downloaded from here instead. It is still <b>signed with a registered Apple developer ID and checked (notarised) by Apple</b>, so macOS opens it without scary warnings. Being outside the App Store also keeps it free and simple to update.</p>
<div class="callout"><b>Could that change?</b> A cut-down App Store version, with fewer checks and no Photos monitoring, is possible if enough people ask. For now we would rather do the whole job well.</div>
<h2>Questions</h2>
<details><summary>Why is it not in the Mac App Store?</summary><p>The App Store requires apps to run in a sandbox, and Photo Clinic needs to read your Photos library, any folder you pick and the system log. <a href="#app-store">Read the full answer</a>.</p></details>
<details><summary>Is it really free?</summary><p>Yes. It is free to use, under the MIT licence. There is no account and no subscription.</p></details>
<details><summary>Which Macs does it run on?</summary><p>Apple silicon Macs today. It needs no extra software. An Intel version is not available yet.</p></details>
<details><summary>Does it work on Windows or iPhone?</summary><p>Not yet. Photo Clinic is a Mac app, and the Apple Photos checks only make sense on a Mac.</p></details>
<details><summary>Will it change my Google Takeout files?</summary><p>No. By default it copies your photos to a new folder and fixes the copies.</p></details>
<details><summary>Can it break my Apple Photos library?</summary><p>The checks only read a copy of the database. The one way it adds to Photos is the send step, which uses Photos' own import and starts with a preview and a 20-photo test.</p></details>
<details><summary>Does it work with iCloud Photos switched on?</summary><p>Yes, that is what the Monitor and Find problems tools are for.</p></details>
<details><summary>What if Google changes Takeout?</summary><p>It may need an update. Photo Clinic checks for updates and tells you when one is ready.</p></details>
%s%s""" % (
 ticks(["<b>Preview first, always.</b> Every run starts as a preview showing exactly what would change.", "<b>Copy by default.</b> Your originals stay where they are unless you choose otherwise.", "<b>Stop and undo.</b> Stop any job, and put everything back from a copy or move run with one click.", "<b>Reports and logs</b> of every run, and a one-tap diagnostic summary if you need help.", "<b>Faulty drives handled.</b> If a drive stops answering, Photo Clinic skips the stuck files after a short wait, carries on, lists what it skipped, and tries them last next time. A gentle mode copies more slowly.", "<b>Removing files is always your choice.</b> Tools that can remove files show the count and size first, and say whether the files go to a folder, the Trash, or are deleted for good (that needs the word DELETE typed). When two places are compared, each file is checked byte for byte against its twin first, and the other side is never touched."]),
 ticks(["It runs on your Mac. <b>No account, and your photos are never uploaded.</b> Nothing else leaves your Mac unless you switch on the optional sharing of unrecognised log lines (see Privacy).", "The app can only be reached from your own computer.", "Checks read a <b>copy</b> of Photos' database, never the original. Sending photos to Photos goes through Photos' own import."]),
 ticks(["<b>Full Disk Access</b> to read the Photos database for the checks and the monitor.", "<b>Photos control</b> if you use the send-to-Photos step.", "macOS asks the first time, and the app explains what to do if it is missing."]),
 ticks(["It reads the <b>Photos library and its database</b>, which belong to another app, to count uploads and check sync.", "It reads <b>any folder you choose</b>, including whole drives and Takeout zips.", "It reads the <b>system log</b> to explain Photos and iCloud problems.", "It <b>controls Photos</b> to import in batches.", "It runs helper programs (ExifTool and ffmpeg) to read and write photo details and convert video."]),
 cta(), nextlinks(("apple-photos.html", "Move to Apple Photos"), None))
page("safety.html", "Safe and private", "How Photo Clinic keeps your photos safe: preview first, copies by default, undo, and nothing leaves your Mac.", b, "safety.html")


# ---------------------------------------------------------------- answers (one page per question people search for)
def answer(fname, title, h1, lead, body, desc, others):
    links = "".join('<li><a href="%s">%s</a></li>' % (f, t) for f, t in ANSWERS if f != fname)
    b = head("Answers", h1, lead) + body + '<h2>More answers</h2><ul class="ticks">%s</ul>' % links + cta() + nextlinks(("story.html", "Our story"), ("tools.html", "All tools"))
    page(fname, title, desc, b, None)

ANSWERS = [
 ("google-takeout-dates-wrong.html", "Google Takeout photos show the wrong date"),
 ("how-to-fix-google-takeout-metadata-mac.html", "How to fix Google Takeout metadata on a Mac"),
 ("google-takeout-json-files.html", "What are the .json files in a Google Takeout?"),
 ("move-google-photos-to-apple-photos.html", "How to move from Google Photos to Apple Photos"),
 ("icloud-photos-stuck-syncing.html", "iCloud Photos stuck syncing on a Mac: slow or stuck?"),
 ("find-duplicate-photos-mac.html", "How to find and remove duplicate photos on a Mac"),
 ("organise-photos-by-date-mac.html", "How to sort photos into folders by date on a Mac"),
]

answer("google-takeout-dates-wrong.html", "Google Takeout photos show the wrong date", "Why do my Google Takeout photos show the wrong date?",
 "Short answer: Google stores the real date in a separate file, not in the photo. When you open the photo, your Mac shows the day you downloaded it.",
 """<h2>What is going on</h2>
<p>When Google Photos exports your library, each photo comes with a small <code>.json</code> file beside it. The real date and time the photo was taken, the place and the caption are in that file. The photo itself often has none of them. So Finder, Apple Photos and other programs fall back to the date the file was created: the day you downloaded it.</p>
<h2>Why time zones make it worse</h2>
<p>Google stores times in a universal clock (UTC). Your photo was taken in your local time. If the two are mixed up, a photo can be hours out, and sometimes lands on the wrong day.</p>
<h2>What fixes it</h2>
%s
<h2>What if a photo has no date at all?</h2>
<p>Some photos have no usable date. Photo Clinic rebuilds one from the file name (such as <code>IMG_20190704_...</code>), neighbouring photos or the folder name, and labels it as a guess with how sure it is. A guess never replaces a real date.</p>
<div class="callout"><b>Always copy first.</b> Photo Clinic makes the fixed copies in a new folder and leaves your Takeout alone. Keep the Takeout until you have checked the result.</div>""" % ticks(["Read the date, place and caption from each photo's <code>.json</code> file.", "Write them into the photo itself, so every program sees them.", "Write local time with the right offset, not raw UTC.", "Do this across all the zip files Google gave you, in one go.", "Preview first: see what would change before anything does."]),
 "Why Google Takeout photos show the wrong date, and how to put the real dates back on a Mac.", None)

answer("how-to-fix-google-takeout-metadata-mac.html", "How to fix Google Takeout metadata on a Mac", "How do I fix Google Takeout metadata on a Mac?",
 "Short answer: the real dates, places and captions are in the .json files beside your photos. Fixing the metadata means writing them back into the photos. You can do that by script or with an app.",
 """<h2>What needs fixing</h2>
%s
<h2>Two ways to do it</h2>
<div class="pair">
<div class="card"><h3>With a script or command-line tool</h3><p>Free scripts and open-source tools exist. They can work well if you are happy using Terminal, installing the tools they need, and reading their notes. Check that the one you pick handles long and numbered file names, edited copies, Live Photos and time zones, and that it works on a copy, not your only set of photos.</p></div>
<div class="card"><h3>With an app (Photo Clinic)</h3><p>Photo Clinic is a free Mac app with a preview, so you see what would change before anything does. It copies your photos to a new folder and fixes the copies. It also pairs Live Photos, matches edits, flags wrong dates and can rebuild missing ones. No Terminal needed.</p></div>
</div>
<h2>The steps, whichever you choose</h2>
<ol class="steps">
<li><b>Keep your Takeout.</b> Download every zip file. Do not delete the Takeout until you have checked the result.</li>
<li><b>Work on a copy.</b> Never fix your only copy.</li>
<li><b>Preview first.</b> Look at what would change for a few real photos.</li>
<li><b>Fix the dates, places and captions.</b> Write local time, not raw UTC.</li>
<li><b>Check a sample.</b> Open some fixed photos in Photos or Finder and look at the date and place.</li>
<li><b>Then tidy.</b> Remove duplicates and edited copies you do not want, and move into Apple Photos in batches.</li>
</ol>
<p>The full list of what Photo Clinic does is on the <a href="fix-takeout.html">Google Takeout page</a>.</p>
<div class="callout"><b>Some files cannot hold this information.</b> Old video formats (AVI, MKV, WMV, MPG, MTS) and BMP images cannot store dates and places inside the file, so those only get their file date fixed, whichever tool you use.</div>""" % ticks(["Photos show the day you downloaded them, not the day they were taken.", "Locations and captions are not inside the pictures.", "Times are stored in UTC, so they can be hours out.", "Live Photos arrive as a picture and a separate video.", "Edited copies and album copies sit beside the originals.", "Hundreds of <code>.json</code> files clutter the folders."]),
 "How to fix Google Takeout metadata on a Mac: what needs fixing, the two ways to do it (script or app) and the steps to follow.", None)

answer("google-takeout-json-files.html", "What are the .json files in a Google Takeout?", "What are all those .json files in my Google Takeout?",
 "Short answer: they hold your photos' dates, places, captions and more. Do not delete them until the information is written into the photos.",
 """<h2>What they are</h2>
<p>For each photo or video, Google adds a file with the same name and a <code>.json</code> ending. It holds what Google knows about that photo: when it was taken, where, the caption you wrote, who is in it, and whether it was a favourite. The pictures themselves are often exported without that information inside them.</p>
<h2>Why they are a problem</h2>
%s
<h2>What to do with them</h2>
<p>Do not just delete them. If you do, the dates, places and captions are gone for good. First write the information into the photos. Then the <code>.json</code> files have done their job.</p>
%s
<div class="callout"><b>Good to know.</b> Some old video formats (AVI, MKV, WMV, MPG, MTS) and BMP files cannot hold this kind of information, so those only get their file date fixed.</div>""" % (
 ticks(["Most programs ignore them, so your places and captions seem to vanish.", "There are hundreds or thousands of them, mixed in with your photos.", "Long names get cut off and duplicates get numbered <code>(1)</code>, so a photo and its file can end up with different names.", "Edited copies, Live Photos and album copies add more of them."]),
 ticks(["Photo Clinic matches each photo with its <code>.json</code> file, even when the names were cut or numbered.", "It writes the dates, places, captions, people and favourites into the photos.", "It pairs Live Photos back up and matches edited copies to originals.", "It keeps your Takeout untouched and puts the result in a new folder."])),
 "What the .json files in a Google Takeout are, why they matter, and how to put their information back into your photos.", None)

answer("move-google-photos-to-apple-photos.html", "How to move from Google Photos to Apple Photos", "How do I move my photos from Google Photos to Apple Photos?",
 "Short answer: export a Takeout, fix the dates and places, then send the photos to Apple Photos in small batches and let iCloud catch up. Keep your Takeout until you have checked everything.",
 """<h2>The steps, in order</h2>
<ol class="steps">
<li><b>Export a Google Takeout.</b> Choose Google Photos, and download every zip file. Do not unzip them yet.</li>
<li><b>Put the dates, places and captions back.</b> The photos come out without them. Photo Clinic reads Google's <code>.json</code> files and writes everything into copies of your photos. See <a href="fix-takeout.html">Google Takeout</a>.</li>
<li><b>Tidy and remove duplicates.</b> Edited copies, album copies and look-alikes pile up. See <a href="tidy.html">Duplicates and tidy-up</a>.</li>
<li><b>Send a small test first.</b> Import about 20 photos into Apple Photos and look at them. Photos has no undo for imports.</li>
<li><b>Send the rest in batches.</b> Oldest first, waiting for iCloud to upload between batches. See <a href="apple-photos.html">Apple Photos</a>.</li>
<li><b>Watch it finish.</b> A big library can take days. <a href="monitor.html">Monitor</a> shows whether it is syncing or stuck.</li>
</ol>
<h2>Things that catch people out</h2>
%s
<div class="callout"><b>Do not delete anything from Google yet.</b> Keep your Takeout and your Google library until you have checked Apple Photos and iCloud.</div>""" % ticks(["Photos show the download date, not the date taken, unless you fix them first.", "Live Photos arrive as two files and need pairing.", "Importing everything at once can fill your Mac and confuse iCloud.", "Videos in older formats (AVI, MKV, WMV) cannot be imported until converted.", "iCloud is slow to catch up on a big library. Days are normal."]),
 "A step-by-step plan to move from Google Photos to Apple Photos on a Mac without losing dates, places or albums.", None)

answer("icloud-photos-stuck-syncing.html", "iCloud Photos stuck syncing on a Mac: slow or stuck?", "iCloud Photos seems stuck syncing on my Mac. Is it slow or stuck?",
 "Short answer: a big library can take days or weeks to sync, so slow is normal. Look for signs that it is not moving at all, and check Apple's own status first.",
 """<h2>Check the easy things first</h2>
%s
<h2>Slow or stuck?</h2>
<p>From the outside they look the same. What tells them apart is whether the numbers move over hours. Photo Clinic takes a reading of your library every 15 minutes and shows the trend: the size of iCloud's sync queue should shrink over time. It only calls a library <b>stuck</b> when every sign agrees: the merge has run for hours, the queue has not moved, and the sync process is busy.</p>
<h2>What not to do</h2>
%s
<h2>Where to look next</h2>
<p>Photo Clinic reads the hidden Photos and iCloud messages and explains them in plain words. It also has step-by-step fix guides, such as "iCloud Photos is stuck, paused or never finishes". Many of the explanations are our best reading, because Apple does not document them, and each one says how sure we are. See <a href="problems.html">Find problems</a>.</p>""" % (
 ticks(["Is Apple having a problem? Check Apple's system status page. Photo Clinic can check it for you.", "Is the Mac plugged in and awake? Low Power Mode pauses background syncing.", "Is there free space on the Mac, and room in your iCloud plan?", "Is Photos open, and is iCloud Photos turned on?", "Give it days, not minutes, before deciding anything is permanently stuck."]),
 ticks(["Do not repair the library just because it is slow. Repairing is for real damage.", "Do not keep restarting services. It can make things worse.", "Do not delete anything to make it go faster.", "If it really is stuck, keep the evidence and leave the library alone while you check."])),
 "How to tell whether iCloud Photos is slow or really stuck on a Mac, what to check, and what not to do.", None)

answer("find-duplicate-photos-mac.html", "How to find and remove duplicate photos on a Mac", "How do I find and remove duplicate photos on a Mac?",
 "Short answer: there are two kinds. Exact copies are safe to remove. Look-alikes need you to choose which one to keep.",
 """<h2>Two kinds of duplicate</h2>
<p><b>Exact copies</b> are the same file twice, byte for byte. A program can find them by their content, whatever they are called. <b>Look-alikes</b> are the same picture saved at another size, or re-saved or edited. Those are a judgement call, because one of them is usually better.</p>
<h2>How to choose the keeper</h2>
%s
<h2>Comparing two places</h2>
<p>If you copied a folder or library and want to clear what is now in both, <a href="tidy.html">Compare two places</a> shows what is identical, then lets you clear those files from one side. It compares each file byte for byte with its twin first, and you choose whether they go to a folder, the Trash, or are deleted for good. The other side is never touched.</p>
<div class="callout"><b>Be wary of anything that deletes duplicates on its own.</b> Always look at the keeper it chose. Photo Clinic shows look-alikes side by side with a suggested keeper and never deletes them automatically.</div>""" % ticks(["A favourite (5 stars) beats one that is not.", "An edited version beats an untouched one.", "More pixels (higher resolution) wins.", "A bigger file wins, because it is less compressed.", "More information inside (date, location, caption, keywords) wins.", "You can reorder or switch off any rule, and bursts are kept by default."]),
 "How to find and remove duplicate photos on a Mac: exact copies, look-alikes, and how to choose which one to keep.", None)

answer("organise-photos-by-date-mac.html", "How to sort photos into folders by date on a Mac", "How do I sort a messy pile of photo folders into neat folders by date?",
 "Short answer: merge the folders, then file every picture by the date it was taken, and keep named folders such as <i>Japan 2025</i> together as events. Photo Clinic does all three in one preview-first step.",
 """<h2>The problem</h2>
<p>Years of backups, imports and downloads leave you with folders inside folders: the same trip in three places, <code>Japan 2025</code> next to <code>japan 2025 (1)</code>, loose pictures with no folder at all, and old library folders full of one-picture folders named by the second they were taken. Sorting that by hand takes days.</p>
<h2>What you end up with</h2>
%s
<h2>The steps</h2>
<ol class="steps">
<li><b>Add your folders</b> under <b>File Sources / Locations</b>, and choose a new, empty folder under <b>Where to save</b>. (Or leave the save folder empty to arrange in place.)</li>
<li>Open the <b>Move</b> tab, choose <b>A folder</b>, and tick <b>Arrange them by date and event too</b>.</li>
<li>Pick the layout you like. The default is a folder for the year with a folder for each month inside it (<code>2025/2025-04</code>); year only, year, month and day, or one folder per month are one click away.</li>
<li>Press <b>Preview</b>. You get a list of <b>every file</b>: where it came from and where it would go. Search it, filter it, click a path to see it in Finder.</li>
<li>Happy? Press <b>Do it for real</b>. <b>Undo this run</b> in Past runs removes the copies or moves the files back.</li>
</ol>
<div style="height:18px"></div>
<figure><img class="shot" src="img/move-options.jpg" width="1188" height="1367" loading="lazy" alt="The Move screen with the Arrange options: layout, events, names, dates"><figcaption>The choices, with an example of what they do</figcaption></figure>
<p>After <b>Preview</b>, each option reports what it did: how many folders it made, which events it found, how each picture was dated, what it renamed, and what the options you left off would do. <b>Show them</b> filters the list to those files.</p>
<figure><img class="shot" src="img/move-impact.jpg" width="1188" height="1941" loading="lazy" alt="Every option shows a count and an example after a preview"><figcaption>Every option explains itself, on or off</figcaption></figure>
<figure><img class="shot" src="img/move-result.jpg" width="1182" height="504" loading="lazy" alt="A preview of the arrange: every file, where it came from and where it goes"><figcaption>The preview lists every file before anything moves</figcaption></figure>
<h2>How it decides the date</h2>
%s
<div class="callout"><b>Nothing is deleted, and nothing is guessed.</b> A picture with no date at all can go in an <code>_undated</code> folder instead of getting a made-up one. Copy is the default, so your originals stay where they are until you are happy.</div>""" % (
 ticks(["<b>Loose pictures</b> go in a folder for their year, month or day, as you choose.", "<b>Folders with a real name</b> (<i>Japan 2025</i>, <i>Mia's birthday</i>) stay together as events, with the date first and filed in their year: <code>2025/2025-04 Japan</code>.", "<b><i>Japan 2025</i> and <i>2025 Japan</i></b> become one folder, and so do <i>Trip</i> and <i>trip (1)</i>.", "<b>Identical files are kept once.</b> Two different files with the same name are both kept.", "Old Photos library folders named by the second (<code>20191013-071453</code>) dissolve, and the pictures go by their date."]),
 ticks(["The date the picture was <b>taken</b>, read from the picture itself.", "If there is none, a date in the <b>file name</b> (such as <code>IMG_20190704</code>).", "Then the date in Google's <b>info file</b>, then the dates in the <b>folders</b> it was in.", "Only if you choose, the <b>file's own date</b>. Otherwise it goes in <code>_undated</code>."])),
 "How to sort a messy pile of photo folders into neat folders by year, month or event on a Mac, with a preview and undo.", None)


# ---------------------------------------------------------------- versions
REL = "https://github.com/daviddef/photoclinic-releases/releases/tag/"
def release(ver, date, tag, note, items, latest=False):
    badge = ' <span class="badge">Latest</span>' if latest else ""
    return '<section class="rel" id="v%s"><div class="relhead"><h2>%s%s</h2><span class="reldate">%s</span></div><p class="sub">%s</p>%s<p><a href="https://github.com/daviddef/photoclinic-releases/releases/download/%s/PhotoClinic-%s-arm64.dmg">Download %s</a></p></section>' % (ver, ver, badge, date, note, items, tag, ver, ver)

b = head("Versions", "What is new in each version", "Every release, newest first. The app tells you when an update is ready, so you never have to check.")
b += release("1.0.123", "7 November 2026", "v1.0.123", "The Photos step stops with a plain message when the Mac's disk is full.", ticks([
  "<b>A full startup disk is caught before Photos refuses everything.</b> When Photos has no room to copy files in, it refuses whole batches with Unknown error. The step now stops at the start if free space is below Keep at least this many GB free, whatever the wait setting, and says how much is free and what to do.",
  "<b>A batch Photos refuses on a nearly full disk is explained.</b> The message now names the full disk instead of a general list of causes."]), latest=True)
b += release("1.0.122", "7 November 2026", "v1.0.122", "The Photos import checks an old list by itself, and Unzip stays off when there is nothing to unzip.", ticks([
  "<b>An old Photos import list is checked once, automatically.</b> A list written by an older version counted files Photos had refused as sent, so a run could say 0 files left. Photo Clinic now checks such a list against Photos once, sends the missing files again and notes it in the result. After that the list is trusted and no check is needed.",
  "<b>First check what Photos really has switches itself off</b> after it has run, so it no longer stays ticked on every run.",
  "<b>Unzip Takeout starts switched off when your folders hold no zip files</b>, including when fixing in place."]), latest=False)
b += release("1.0.121", "7 November 2026", "v1.0.121", "The Fix step no longer hunts for exact copies when it is only fixing in place.", ticks([
  "<b>No more Finding exact duplicates during a metadata fix.</b> The workflow Fix step used a hidden Remove exact copies setting from the Fix tool, which fingerprinted every file on the drive before it started. It now does that only when it is making copies; Remove duplicates is its own step."]), latest=False)
b += release("1.0.120", "8 November 2026", "v1.0.120", "Later steps follow a renamed source folder, and the Photos import keeps its list after a rename.", ticks([
  "<b>A workflow keeps going after the source folder is renamed.</b> If Unzip finished and your prefix renamed the folder, the next step looked for the old name and stopped with Not a folder or zip file. The later steps now follow the rename.",
  "<b>The Photos import keeps its list of sent files when the folder is renamed.</b> The list inside the folder kept the old name, so after a rename every file looked new and was sent again. The list is now matched to the folder's current name, including by the First check what Photos really has setting.",
  "<b>A few refused files no longer stop the import.</b> Photos refuses files it already has. Those are now noted as refused and listed, and the run stops only when nearly the whole batch is refused."]), latest=False)
b += release("1.0.119", "7 November 2026", "v1.0.119", "Importing into Photos only remembers what Photos really took.", ticks([
  "<b>Files Photos refuses are no longer remembered as imported.</b> Before, every file sent to Photos was written to the list of finished files, even when Photos showed a Cannot Import box. That list now holds only the files Photos confirmed, so running again tries the rest.",
  "<b>A batch that mostly fails stops the run.</b> If Photos does not add half or more of a batch, Photo Clinic stops with a plain message and the list of files, instead of working through thousands more.",
  "<b>Network drives are copied to your Mac first.</b> When the folder you are importing sits on a network drive, each batch is copied to a temporary folder on your Mac and imported from there, because Photos reads a network share badly. The copy waits for a drive that stops answering and carries on.",
  "<b>First check what Photos really has.</b> A new setting on the Copy to your Photos library step compares the files Photo Clinic says it sent with Photos' own records and forgets the ones Photos does not have, so they are sent again. The old list is kept beside it."]), latest=False)
b += release("1.0.118", "7 November 2026", "v1.0.118", "Monitor panels display properly again, and Mac awake can be switched on from the Activity panel.", ticks([
  "<b>Monitor panels open properly again.</b> Since 1.0.115 the Sync meter, Live watch and Mac awake panels opened as an empty strip with only a sliver visible, because of a styling mistake made when the new status panels were added. They now open in full.",
  "<b>Mac awake is a switch in the Activity panel.</b> The chip used to be a label that did nothing when clicked. It now turns the setting on and off, and says ready when it will hold the Mac awake while a job runs."]), latest=False)
b += release("1.0.117", "7 November 2026", "v1.0.117", "Photos imports that no longer time out, files Photos skips are reported, and clearer upload numbers.", ticks([
  "<b>Importing into Photos no longer gives up after two minutes.</b> A big batch could make Photos take longer than AppleScript's two-minute limit, and the step stopped with \u201cAppleEvent timed out (-1712)\u201d. Each batch now waits up to three hours, and if Photos is still busy the message says so and what to do next.",
  "<b>Files Photos did not add are listed.</b> Photos skips a file it already has, such as a duplicate burst photo, and shows a \u201cCannot import\u201d box. The report now says how many files Photos did not add and names them, with the full list saved beside the run.",
  "<b>Clearer sync numbers.</b> The Sync meter used to say \u201cNearly done\u201d when the upload queue was short, even with thousands of photos not yet in iCloud. It now shows both numbers and explains that Photos queues a few at a time.",
  "<b>Look only explains how to run for real.</b> At Look only the note now links to Make copies and Change in place, and the three levels no longer fold away."]), latest=False)
b += release("1.0.116", "6 November 2026", "v1.0.116", "Unzip waits for a network drive that drops and carries on.", ticks([
  "<b>A dropped network drive no longer stops Unzip.</b> If the drive times out, disconnects or unmounts, Unzip now says so in its status, waits for it to come back and carries on where it stopped. Files already unpacked are skipped, and the final report notes how many times it waited.",
  "<b>No half-written files.</b> Each file is written under a temporary name and renamed once it is whole, so a dropped connection cannot leave a truncated file behind. A zip is still deleted only after every file in it is unpacked and checked."]), latest=False)
b += release("1.0.115", "6 November 2026", "v1.0.115", "Look at a step's settings while it runs, and clearer Unzip progress.", ticks([
  "<b>Settings can be viewed while a job runs.</b> The gear on a step used to be greyed out during a run. It now opens the settings read-only, with a note that they are locked until the job finishes, so you can check what a running step is using.",
  "<b>Clear Unzip progress.</b> While zips are unpacked, the step showed the bytes done as a count of files, such as 22,105,291 of 176,620,082,439 files. It now shows the bar and a plain message: which zip, and how many GB of the total are done.",
  "<b>Click a status pill for a small panel.</b> Disk, Library health, Load and Needs attention now open a small panel like the monitor rings, with the reading, how old it is, and the checks you can run from there (check disk health, scan everything, and so on), plus a link to the full page.",
  "<b>iCloud joins the Sync meter.</b> The separate iCloud pill is gone. The Sync meter's panel now shows the live count waiting to upload, the last full check and how old it is, a Check iCloud and Photos button and a link to open it.",
  "<b>Unrecognised log lines get a pill.</b> A new pill shows how many log lines Photo Clinic could not explain are waiting. Its panel lists them, can send them now, and links to the full list and the sharing settings."]), latest=False)
b += release("1.0.114", "6 November 2026", "v1.0.114", "Choose where Unzip unpacks, one checkbox for a new folder next to your photos, and a quiet start-up fix.", ticks([
  "<b>Unpack into, in the step's settings.</b> Unzip now has a clear choice: automatic, my target folder, or the same folder as the zips. Choosing the same folder as the zips works at every level, so you are no longer sent to switch level.",
  "<b>A preview needs no target.</b> Previewing Unzip before you have chosen where to save no longer stops with a problem.",
  "<b>One checkbox for a new folder.</b> New folder next to my source is now a single checkbox that saves a copy next to your originals now and each time you choose new photos, replacing the separate button and Always box.",
  "<b>A clear choice for renaming the source folder.</b> Under Choose your source, pick what happens when a step finishes cleanly: leave the name alone, rename it automatically with the steps done (FIX_TIDY_), or add a prefix of your own, such as READY - . A prefix is never added twice and replaces a steps-done mark.",
  "<b>See where Unzip will save.</b> Under Unpack into, the step's settings now show the folder the zips will be unpacked into, based on what you chose.",
  "<b>Clearing the target unticks the box.</b> Removing the target now also unticks New folder next to my source, so it does not come back by itself. With several sources, one new folder is made next to the first, named Photo Clinic - fixed.",
  "<b>Start-up fix.</b> Photo Clinic no longer throws a hidden error on start when a source is already chosen, which could skip the check for an old library."]), latest=False)
b += release("1.0.113", "6 November 2026", "v1.0.113", "After Unzip, the rest of the workflow works on the unpacked folders.", ticks([
  "<b>Unzip hands over to the next steps.</b> Once Unzip has unpacked your zips, Organize, Fix, Remove duplicates, Tidy and Videos work on the unpacked folders: the target when you make copies, or the folder beside the zips when you change in place. Before, a copy run would read the zips again and write a second copy beside the unpacked one.",
  "<b>Clearer wording.</b> The target shortcut now reads New folder next to my photos, with a note that it is a copy and your originals stay as they are. Unzip says Same folder as the zips when changing in place.",
  "<b>Your originals stay safe.</b> Working on the unpacked copy in your target never touches the zips, unless you ticked Delete the zip files. The folder name is not marked in this case, so the target keeps its name for the next step."]), latest=False)
b += release("1.0.112", "6 November 2026", "v1.0.112", "A new Unzip Takeout step: unpack Takeout zips into your target or beside the zips, and optionally delete them once checked.", ticks([
  "<b>Unzip Takeout, at every level.</b> A new step at the start of the Workflow unpacks your Takeout zips, keeping the folders inside them. Changing in place, it unpacks beside the zips so the parts merge into one folder. Making copies, it unpacks into your target.",
  "<b>Delete the zips, safely (optional).</b> Off by default and needs you to type DELETE. A zip is deleted only after every file in it is unpacked at its full size and its checksums have passed. A zip that could not be fully unpacked is kept.",
  "<b>Careful by design.</b> A preview lists the zips, files and size and checks there is room, and changes nothing. A stopped run carries on later, and a different file with the same name is kept beside the first, never overwritten.",
  "<b>Marks.</b> With Mark the folder name on, a clean in-place unpack adds UNZIP_ to the front of the source folder name."]), latest=False)
b += release("1.0.111", "5 November 2026", "v1.0.111", "Mark a source folder with the steps done to it, and each step shows its own last run.", ticks([
  "<b>Mark the source folder (optional).</b> Tick it under Choose your source. When a step that changes your folder in place finishes with no problems, its name gets a mark at the front: FIX_, then FIX_TIDY_. A step already in the name is never added again, so it does not stack. Your run history follows the new name, so last-run lines and Run again keep working.",
  "<b>Already done, and when.</b> Choose a folder that carries a mark and the source step says which steps were done and how long ago.",
  "<b>Last run on the right step.</b> Tidy your photos was being shown under Remove duplicates, so Tidy showed nothing. Each step now shows its own last run.",
  "<b>A link to the report or log.</b> When a run has no saved report, its last-run line now links to its log instead of showing no link."]), latest=False)
b += release("1.0.110", "5 November 2026", "v1.0.110", "A clearer status ribbon, monitor panels, a plain-English delete warning and live detail while folders are scanned.", ticks([
  "<b>Monitor panels.</b> Click a ring in the ribbon to open a small panel: what it is doing, the issues found so far (Live watch) or the upload queue (Sync meter), a button to turn it on or off, and one to open the full details. The rings carry a count badge as things are found.",
  "<b>A clearer ribbon.</b> Readings say what they measure and how old they are, for example iCloud nothing waiting to upload, read 27 days ago. It shows how much of your Photos library could be freed, and the running workflow with its progress. The page now leaves room at the bottom so the ribbon never covers the last step.",
  "<b>A plain-English delete warning.</b> Before steps that delete files in place, Photo Clinic lists exactly what will be deleted, what will also change and what is left alone, based on the steps and settings you chose, with your last preview result when there is one.",
  "<b>Steps not in this run collapse.</b> While a workflow runs, the steps that are not part of it shrink to one greyed line, so the running step stands out.",
  "<b>Live detail while scanning folders.</b> The folder scan shows files found so far, folders read, files a second and the folder it is in, and Stop now works during a long scan of a big or slow drive."]), latest=False)
b += release("1.0.109", "5 November 2026", "v1.0.109", "A status ribbon along the bottom, with the three monitors in it.", ticks([
  "<b>A status ribbon</b> runs along the bottom of the window: the running job with its progress, free disk space, Library and iCloud readings, Photo Clinic's own load, and how many things need a look. Click any part to open its detail. A refresh button updates the readings.",
  "<b>The monitor rings moved into the ribbon.</b> Sync meter, Live watch and Mac awake sit at its left end, pulsing green while running. Click one to turn that monitor on or off."]), latest=False)
b += release("1.0.108", "5 November 2026", "v1.0.108", "Three monitor rings in the header, Preview all steps, and when each step last ran.", ticks([
  "<b>Monitor rings in the header.</b> Three small rings show whether the Sync meter, Live watch and Mac awake are running. A running one pulses green; Mac awake shows a steady ring when it is ready to hold the Mac awake during a job. Click a ring to turn that monitor on or off.",
  "<b>Preview all steps.</b> When the Workflow is set to copies or in place, a Preview all steps button sits beside Run all steps, so you can see what everything would do without changing your level.",
  "<b>When each step last ran.</b> Each step in the Workflow shows, for your current source, how long ago it last ran or was previewed, how it finished, and a link to the report."]), latest=False)
b += release("1.0.107", "5 November 2026", "v1.0.107", "Past runs show up again.", ticks([
  "<b>Past runs load as soon as the app opens.</b> In 1.0.105 and 1.0.106 the list under Activity could show Nothing here yet until you opened it another way. Your history was never lost; it now loads at start and whenever Activity opens.",
  "<b>The search box in Activity</b> now shows its hint properly."]), latest=False)
b += release("1.0.106", "5 November 2026", "v1.0.106", "The header and the source strip stay put while you scroll.", ticks([
  "<b>A frozen header.</b> The tabs stay at the top of the window as you scroll, and the heading reads the same on Workflow and Home: Pick a source, destination and Workflow to get going.",
  "<b>A frozen source strip.</b> File Sources / Locations and Where to save stay under the header, with a soft blurred band behind both so nothing slides under them."]), latest=False)
b += release("1.0.105", "5 November 2026", "v1.0.105", "A tidier layout: tabs in the header, one slim source and destination strip, Past runs beside Activity, and a grouped Check everything.", ticks([
  "<b>Tabs in the header.</b> Workflow, Home, Tools and Health sit in the header bar, so the page starts higher. On a narrow window they show icons only.",
  "<b>One slim strip for source and destination.</b> Under the tabs, <b>File Sources / Locations</b> and <b>Where to save</b> are two halves. Click one to open it, click again to close it. With a source chosen it starts closed, and a Photos library on its own now shows as a source.",
  "<b>Past runs live under Activity</b> in the right-hand pane, as plain cards with a filter bar and a ⋯ menu for the reports folder, clearing old previews and diagnostic info. The reports folder shows its size.",
  "<b>Check everything</b> has its button at the top of Your steps, and the steps are grouped under Your files, Photos and iCloud, This Mac and The result. Steps that need a source say <b>Needs a source defined</b> until you choose one.",
  "<b>Quick jobs are gone</b> from the Fix screen. The Workflow does the same job in order.",
  "<b>Stop works while duplicates are compared,</b> and Remove duplicates shows live detail: sizes, a quick look, then a full comparison by files and gigabytes."]), latest=False)
b += release("1.0.104", "5 November 2026", "v1.0.104", "Stop now works while duplicates are being compared.", ticks([
  "<b>Stop is quick during Remove duplicates.</b> Stopping while files are compared in full used to wait for the current file or stage to finish. It now responds within a second or two, and nothing is deleted if you stop before the comparison ends."]))
b += release("1.0.103", "5 November 2026", "v1.0.103", "Check everything, an Activity tab, clearer charts, and live detail while duplicates are removed.", ticks([
  "<b>Check everything.</b> A read-only Workflow that checks your sources, your Photos library, iCloud sync, the logs and this Mac, runs the checks side by side, and ends with a verdict. Check my sources stays greyed out until you choose a source.",
  "<b>Activity in the right pane.</b> It sits beside Summary, opens by itself when a job starts, holds the monitors, and shows a pulsing tick on every finished step.",
  "<b>Remove duplicates shows its progress.</b> Sizes checked, a quick look, then a full comparison by files and gigabytes, with the exact copies found and the space to free updating as it goes.",
  "<b>Photos Health.</b> Clear trend charts with scales, lows, highs and a definition for each measure. Readings carry on if the library is not found for a moment, and a reading that is out of date says so. Things that need attention disappear after 24 hours.",
  "<b>iCloud.</b> The Summary shows how many photos are waiting for iCloud, and the library size card shows that your originals are confirmed in iCloud.",
  "<b>Stop preview.</b> While a preview runs the button says Stop preview, so you always know which mode is running. Ten more log messages are now explained instead of flagged."]))
b += release("1.0.100", "4 November 2026", "v1.0.100", "A Workflow that follows your style, with steps you can reorder, new Remove duplicates and Videos steps, and live status all the way through.", ticks([
  "<b>Settings follow your style.</b> Pick Safest, Balanced, Fastest, Thorough or I like risk and every step's options follow it. Deleting Google's info files is preferred, and only happens once Fix has run first.",
  "<b>Remove duplicates.</b> A separate step that removes exact duplicates only, keeping the copy in the Photos from year folder.",
  "<b>Videos that will not play</b> is a single tick in the Workflow. Deleting the originals is only for I like risk, and asks you to type DELETE.",
  "<b>Reorder the steps</b> by dragging them or with the arrows, within sensible limits. Organize my Photos is always step 2 when ticked, and the target is hidden when no step needs one.",
  "<b>Open tool</b> opens the exact tool with the exact options the step uses. Preview, Run and Open tool sit at the top of each step, with the options underneath.",
  "<b>Monitors in the Workflow.</b> The Sync meter, Live watch and Mac awake start with the copy and show in the Workflow window, with a live message, counts and a still working heartbeat. The right-hand pane starts collapsed."]))
b += release("1.0.93", "28 October 2026", "v1.0.93", "A Summary pane, one place to start your monitors, favourites for every tool, and Organize my Photos that handles old libraries.", ticks([
  "<b>A Summary pane.</b> The right-hand pane shows what needs attention, the status of your Photos library, iCloud and Apple, this Mac's disk, and Photo Clinic's own CPU and memory. One button starts all the monitors, and the Mac is kept awake while a job runs.",
  "<b>A favourite star on every tool.</b> Save just that tool's settings, and run it again from One-Click. Styles now set Tidy, Videos, Move and Copy too, and never switch on anything destructive.",
  "<b>Organize my Photos.</b> Move my photos is now Organize my Photos, and it works on one source. A picture with no date is dated by the earliest of its folder name (May 2002, 2002-05, 02-05-2002) and its file dates, and the dating list says why each date won. Old libraries, even ones named .photoslibrary, are recognised and read from their own database.",
  "<b>Pause and queue.</b> Start another job while one runs and it waits its turn. Finished jobs say so, and a copy at 100% no longer looks as if it is still going.",
  "<b>Disk health on one page</b>, an Activity tab with a find box that matches every word, a light and dark theme toggle, and fixes to Fix in place, which no longer asks for a destination."]))
b += release("1.0.83", "27 October 2026", "v1.0.83", "A clearer copy progress card, with progress on every folder.", ticks([
  "<b>Progress on every folder.</b> While a copy runs, each folder in the tree shows how far its part has got and what is left, for example 2.19% with the files and gigabytes still to do.",
  "<b>A tidier card.</b> Files, data, speed and time left are at the top, with percentages, then one heading that says what is copied and where it goes. The file in hand and its bar sit beside Stop.",
  "<b>Two decimals.</b> Percentages show two decimal places, so a long copy visibly moves, and the Activity list is taller."]))
b += release("1.0.82", "27 October 2026", "v1.0.82", "A simpler app: five tabs, one click jobs, one progress card, a faster iCloud copy and a whole-Mac disk check.", ticks([
  "<b>Five tabs.</b> Home, Jobs, Health, Files and Activity. Fix, Tidy and Move and copy sit in one Jobs bar. Moving and copying is one flow: where from (folders, iCloud Drive or Google Drive, an old library), where to, and how.",
  "<b>One click.</b> Organise everything, Fix a Takeout, Tidy a folder, and your own saved favourites. Each one opens a preview first, and Organise no longer needs the long scan.",
  "<b>One progress card.</b> Every running job shows the same card: what it is copying from and to, the file in hand with its own bar, and tiles for files, data, speed, time left and problems. Go to this job takes you back to it.",
  "<b>Faster iCloud copy.</b> A new Speed setting asks iCloud for the next files while one is copied, and freeing space no longer makes the copy wait. The file in hand shows iCloud's own progress, the same figure Finder shows.",
  "<b>Disk space.</b> One tool for the whole Mac: it finds what takes space (Chrome's temporary copies, Xcode, iCloud leftovers, caches, simulators), clears only what you confirm, and can watch what is filling the disk.",
  "<b>Clearer pages.</b> One Help screen, long descriptions folded behind More, path links, Past runs laid out like results, and even button spacing. While a job runs, buttons that would start another are dimmed.",
  "<b>Fixes.</b> Google Drive compare finds a copy made into a same-named folder, a file that does not fit yet is put back while others copy, and a copy no longer shows another job's old summary."]), latest=False)
b += release("1.0.77", "26 October 2026", "v1.0.77", "A clearer Copy page, a smarter Google Drive compare, and a copy that no longer waits on one big file.", ticks([
  "<b>Google Drive finds an earlier copy.</b> If you already copied a Drive folder with another tool, straight into a folder of the same name, the compare now finds it, so it no longer reports everything as missing. Copying the gaps goes to the same place.",
  "<b>A copy that keeps going.</b> A file that does not fit in the free space yet is put back, and the files that do fit are copied first. Freed space lets it return to the big ones.",
  "<b>Clearer Copy page.</b> The summary is one row of cards at the top, the duplicate folder-by-folder list is gone, each source shows only its own results, and the source tabs look like tabs.",
  "<b>Loading you can see.</b> Spinners and a plain sentence while iCloud Drive or Google Drive folders are read, and a Try again button if Photo Clinic does not answer.",
  "<b>Fixes.</b> The Stop button on a copy responds, and the list no longer flashes while folder sizes are counted."]), latest=False)
b += release("1.0.76", "26 October 2026", "v1.0.76", "Copy from iCloud Drive and Google Drive, photos not in Apple Photos yet, and a whole-Mac disk space check.", ticks([
  "<b>Copy from the cloud.</b> Copy iCloud Drive or Google Drive folders to your Mac slowly and safely, one file at a time, resuming where it stopped. You sign in to your own accounts and choose your own folders, with a folder tree showing sizes and the space needed. Nothing in the cloud is changed or deleted.",
  "<b>Compare with what is already copied.</b> For iCloud Drive and Google Drive, see which files are missing or cut short, folder by folder, and copy only the gaps.",
  "<b>Live copy status.</b> The file in hand with its size, how much has arrived and its speed, and the progress of the whole copy, refreshed every second. Problems can be listed while the copy runs, grouped by cause with what to do about each.",
  "<b>Google Takeout email links.</b> Paste the links from a Takeout email and Photo Clinic downloads them in order, and collects the parts in your Downloads folder.",
  "<b>What is not in Photos yet?</b> Check a folder against your Photos library by content and by Photos' own records, see thumbnails of both sides, and copy only what the library lacks. Items Photos already has can be moved aside, never deleted.",
  "<b>Disk space, whole Mac.</b> Sizes the usual space hogs (Chrome's temporary copies, Xcode files, iCloud leftovers, caches, simulators), sorts them into safe to clear and yours to decide, clears only what you confirm, and can watch what is filling the disk right now. It never quits an app for you.",
  "<b>Fixes.</b> The Stop button on a copy works again, the Activity log no longer jumps while a copy runs, and duplicates scans list every group instead of the first 150."]), latest=False)
b += release("1.0.61", "26 October 2026", "v1.0.61", "One plan for a whole drive, a side rail that stays with you, and a clearer look inside every file.", ticks([
  "<b>Organise everything into one place.</b> When you choose several things, or a drive full of mixed folders, libraries and zips, the plan can copy what you tick into one folder, filed by year and month, with exact copies kept once. It only copies: your originals are never changed. Photos libraries are left alone, and folders that do not look like photos start unticked.",
  "<b>A side rail on every screen.</b> What you are working on and where it saves stay beside every page, each source with what Photo Clinic found it to be and a Remove button. Your last choice comes back when you reopen the app, and Activity sits underneath, newest first. Both sections collapse.",
  "<b>One tidy plan.</b> Scan everything is now one card, grouped by the part of the plan each result belongs to (Fix my photos, Duplicates and formats, Tidy up, Old videos, Look-alikes, Damaged files, Other files). Each group says how many things need a look, and every row has Show me, Show details and Do it now.",
  "<b>Damaged files and other files.</b> The scan now looks for damaged or unreadable files in folders, reports zip files that could not be read, and counts files that are not photos or videos. Those inside zips are copied into an Other files folder.",
  "<b>Copies you can see.</b> The list of what Fix would do shows a picture of both copies of every exact copy, bigger on a click, with sizes and the one kept outlined in green. Tick Keep this one instead to swap them. Pictures inside zips show too.",
  "<b>Look inside any file.</b> A Metadata button shows EXIF, IPTC, XMP, video tags, the files beside a picture (Google .json, .xmp) and macOS extended attributes, even for files inside zips.",
  "<b>Where reports are saved.</b> Choose the folder for your reports (for example on an external drive), with an offer to move what is there. If the drive is not connected, Photo Clinic says so and uses the default instead of creating a folder in the wrong place.",
  "<b>Better recognition.</b> A folder of zip files is recognised as Takeout, or as photos when there are no Google info files, even without Takeout in the names. Counts no longer include the exact copies that are left out.",
  "<b>Optional AI explanation.</b> Off by default. If you turn it on and save your own key, you can ask for a plain explanation of one log message at a time, after seeing exactly what will be sent.",
  "<b>Smaller things.</b> Check now sits beside Home; adding a folder always opens a menu; dropping onto an existing source asks whether to add or replace; permission problems in the log say which app was refused what, with a button to the right setting."]), latest=False)
b += release("1.0.53", "25 October 2026", "v1.0.53", "Permission help, an optional AI explanation, and a clearer sync backlog.", ticks([
  "<b>Permission problems say where they happen.</b> A log message that means macOS refused something names the app, what was refused and the path, with a button to the right privacy setting.",
  "<b>Optional AI explanation, off by default.</b> Turn it on and save your own key, and you can ask for a plain explanation of one message at a time. You see exactly what will be sent first, your user name and home folder are removed, and nothing is sent unless you ask.",
  "<b>Sync backlog.</b> When the backlog is shrinking, it shows how many items an hour are cleared and a rough finish time, marked as an estimate. The queues have plain names.",
  "<b>Clearer folder problems.</b> If the folder you chose cannot be written to, the message names it and says how to fix it."]))
b += release("1.0.52", "25 October 2026", "v1.0.52", "Clearer log messages, a sync meter that moves, and plainer set-aside and plan rows.", ticks([
  "<b>Sync meter fixed.</b> On current macOS it always showed 0 B/s because it could not read the system&rsquo;s network figures. It now shows real traffic, and the wording no longer contradicts itself when nothing is waiting.",
  "<b>Log messages made clear.</b> Whole multi-line messages are kept and copied. Messages from unrelated parts of macOS are counted, not shown. Harmless ones say <b>Harmless</b>, not <b>Must resolve</b>. The chart legend names the area (iCloud sync, Network, Database&hellip;), and its line is now a trend that can fall.",
  "<b>What to do, with buttons.</b> Steps can restart the Photos widget or reset privacy, and show a tick when Full Disk Access or Automation is already on. Permission errors say which app was refused what, with a button to the right setting.",
  "<b>Plan and set-aside.</b> A plan job that has run turns into a green tick with <b>Open</b> and <b>Do again</b>. Set-aside rows say exactly where each file goes (from &rarr; to), with an (i) that explains it.",
  "<b>Scan.</b> Choosing the recommended settings no longer fails the whole scan.",
  "<b>More known problems.</b> Eight new entries for Photos and iCloud messages, mostly harmless background noise."]))
b += release("1.0.50", "18 October 2026", "v1.0.50", "Two small fixes to the confirmation windows and the plan.", ticks([
  "<b>Readable confirmations.</b> The note under <b>Do this for real?</b> and similar notes in other windows were squashed into a narrow column and ran over the buttons. They now sit in a normal full-width box.",
  "<b>Plan wording.</b> A plan with a single exact copy now says &ldquo;1 exact copy skipped&rdquo;, not &ldquo;1 exact copies&rdquo;."]))
b += release("1.0.49", "18 October 2026", "v1.0.49", "Scan everything: one scan that ends in a plan you can do in one go or one job at a time.", ticks([
  "<b>Scan everything.</b> Press it on Home or on Check. Photo Clinic reads what you chose, picks the recommended settings for it, and previews Fix, Tidy and Videos without changing anything.",
  "<b>Your plan.</b> The result is one card with a row per job: its count (for example <i>36 files would be copied and fixed: 26 dates, 15 places</i>), a tick box, <b>Open</b> to see the exact files, and <b>Do this one</b>.",
  "<b>Do the ticked ones.</b> One summary, then the jobs run one after the other. Fix goes first and copies into your save folder, then the next jobs work on that finished library, not your originals.",
  "<b>Safe by default.</b> Tidy deletes files, so it is never ticked for you and still asks you to type DELETE. Fix in place and moves still ask their own questions.",
  "<b>Fewer buttons that mean the same thing.</b> <b>Look at it</b> now only appears for old libraries, struggling drives and mixed folders, where it still adds a plan; for a Takeout or a folder, Scan everything covers it."]))
b += release("1.0.48", "18 October 2026", "v1.0.48", "A tidier app: Home starts with what you have, a slimmer header, and every picture on the site retaken.", ticks([
  "<b>Home starts with what you have.</b> The top card lists what you chose and what Photo Clinic thinks each thing is (a Takeout, a folder, an old library), with a <b>Look at it</b> button for each. The job tiles sit below it, and the separate first page of Start here is gone.",
  "<b>A slimmer header.</b> The folder path and the free space share one line, and the green Ready strip only appears when it has something to say. The <b>Help me</b> button is now <b>Something wrong?</b>, so it cannot be mistaken for <b>Help me choose</b>.",
  "<b>Quick jobs are a row of pills</b> on Fix, and the dashed box inside the options is gone, so the options sit in one clean frame.",
  "<b>Past runs</b> has a tile under Tools, and the runs use the same names as the tabs: Fix my photos, Move my photos, Tidy up, Look-alike photos and so on.",
  "<b>Small fixes.</b> Notes on result cards no longer look squashed, the five-styles table names every option correctly, the Count my photos window has a Close button, and source rows no longer break words in the middle.",
  "<b>On the website,</b> every screenshot is retaken for these screens."]))
b += release("1.0.46", "18 October 2026", "v1.0.46", "After a real run, Photo Clinic offers to switch to the finished library, and the website pictures are all new.", ticks([
  "<b>Switch to the finished library.</b> When a Fix or Move copy finishes, the result card says where the finished library is and offers to make it your source, with a fresh folder for the next result. Your original folders then become your backup.",
  "<b>New website pictures.</b> Every screenshot on the site shows the current screens, with the option counts and the window that opens from <b>Show the 26</b>."]))
b += release("1.0.45", "18 October 2026", "v1.0.45", "Every option now says what it did and opens the exact files, results finish with a clear All done, and Move can leave non-photos behind.", ticks([
  "<b>Every option explains itself.</b> After a preview, each option on Fix, Tidy, Videos, Move, Apple Photos and old libraries shows what it did or would do, with a count. Press <b>Show the 108</b> to open the exact files, dates before and after, albums, batches or folders behind that number, even for options you left off.",
  "<b>A clear finish.</b> A real run now ends with a green <b>All done</b> bar, and the result card has one button row, a before-and-after strip and a Details window with tabs.",
  "<b>Move got smarter.</b> Arrange by date and event (<code>2025/2025-04</code>, events such as <code>2025-04 Japan</code>), old libraries handled in the same place, <b>Photos and videos only</b> with an optional <b>Other</b> folder for everything else, and grouped options that match Fix and Tidy.",
  "<b>Fix applies every option you tick.</b> Time zones, folder dates, place names, GPS tracks, motion photos and the rest were being dropped before a run. They now reach it. There is also an optional <b>Look for damaged files first</b> step.",
  "<b>Help me choose</b> now sits beside Preview, and the window uses the room on a big screen instead of a narrow column.",
  "<b>Check my photos</b> shows its findings again and no longer clutters Past runs with a preview folder for every step. <b>Clear old previews</b> moves old preview folders to the Trash.",
  "<b>Fewer glitches.</b> The page no longer fades in and out when you change tab, option lines go stale when a setting changes, and the iCloud service check and the Look at my files result are repaired."]))
b += release("1.0.35", "17 October 2026", "v1.0.35", "Preview and Do it for real stay in view, quieter setup, one title on each tool, and a much fuller All tools page on the website.", ticks([
  "<b>The run button stays in view.</b> On Fix, Tidy, Videos and Move, <b>Preview</b> and <b>Do it for real</b> now stay at the bottom of the window while you scroll, so a long list of options never hides them.",
  "<b>Quieter setup.</b> The row of green ticks (Takeout added, Destination ready, ExifTool found, ffmpeg found) only appears when something needs fixing, and the &ldquo;Fixing: this &rarr; saved in that&rdquo; strip under each title is gone, because the two boxes at the top already say it. It comes back only when your Photos library is included.",
  "<b>One title on each tool.</b> A tool that opens over the page used to show its name twice. It now shows its own heading once.",
  "<b>Health over time</b> no longer tells you to run a Terminal command. It says what to press.",
  "<b>Arrange by date</b> uses year then year-month folders (<code>2025/2025-04</code>) by default, and tiles and cards no longer move or go dark when you hover over them.",
  "<b>On the website:</b> a new, fuller <a href=\"tools.html\">All tools</a> page covers every tool in the seven tabs, with what it does, whether it can change your files, how to use it, and a picture of each."]))
b += release("1.0.34", "16 October 2026", "v1.0.34", "One Preview button, one result card with every file listed, arranging photos into folders by date and event, and old libraries now live in Move.", ticks([
  "<b>Preview, then Do it for real.</b> The &ldquo;Preview only&rdquo; tick box is gone. Every tool has one button: <b>Preview</b>. When you like what you see it becomes <b>Do it for real</b>, and it goes back to Preview if you change a setting, so you never run for real on settings you have not seen.",
  "<b>One result card, with every file.</b> Move, Fix, Easy fix, Tidy, Videos, Apple Photos, merging similar folders, setting photos aside and the old library copy all end in the same card: a headline, a few facts, where it went (a link), an undo line, and a list of <b>every file</b> with where it came from, where it went and what happened, in plain words. The list shows one row each, 20 at a time, loads more as you scroll, shows the full path when you hover, and opens Finder when you click.",
  "<b>Arrange photos into folders by date and event.</b> In Move, tick <b>Arrange them by date and event too</b>. Pictures are filed by the date they were taken (<code>2025/2025-04</code> by default; year only, year, month and day, or one folder per month are one click away). A folder with a real name, such as <i>Japan 2025</i>, stays together as an event with its date first and <i>Japan 2025</i> and <i>2025 Japan</i> become one folder. A picture with no date goes in <code>_undated</code> if you prefer. Preview first, and Undo is in Past runs.",
  "<b>Old libraries are in Move.</b> Add an old iPhoto, Aperture or Photos library under What to work on and Move says so, reads its database, and offers the same choices: arrange by album, year, month or day, duplicates, copy gently. The Rescue tab opens Move.",
  "<b>A new Home and seven tabs.</b> Home has Start here and six jobs. The tabs are Home, Fix, Tidy, Move, Check, Rescue and Tools. The boxes at the top are now <b>What to work on</b> and <b>Where to save</b>, with one progress strip and one status bar, and confirmations appear inside the app with how many, how big and whether it can be undone.",
  "<b>Past runs</b> has filters and search and fewer buttons. <b>Tools</b> is grouped by what you want to know. <b>Compare</b> is one card. The <b>Add</b> picker opens inside the app, so its sidebar and your drives work.",
  "<b>Fixes.</b> A folder named like a Photos library but holding plain files is treated as a folder. Tiles no longer flicker or go dark when you hover them. The User guide is rewritten for the new tabs. This release also includes the changes from 1.0.29 to 1.0.33, which were never published on their own."]), latest=False)
b += release("1.0.28", "12 October 2026", "v1.0.28", "Every screen remembers its last result, and Compare two places can tag, set aside, trash or delete the identical files from one side.", ticks([
  "<b>Every screen remembers its last result.</b> Come back to Compare two places, the Old library extractor, Find damaged files, Fix, Tidy, Similar and the rest, and the last result is there with a &ldquo;Where you left off&rdquo; note, even after you quit the app. Compare&rsquo;s Clear and Copy buttons still work on a restored result.",
  "<b>Compare two places: clear the identical files from one side.</b> You choose how: <b>tag them in Finder</b> (a red tag, nothing moves), <b>set them aside</b>, <b>move to the Trash</b>, or <b>delete for good</b>. For an Apple Photos library the choice is an <b>album in Photos</b> to review, and Photos keeps what you delete in Recently Deleted. The panel now sits above the folded sections where you can see it.",
  "<b>The &ldquo;type DELETE&rdquo; confirmation works.</b> It is now a box inside the app. The old pop-up never appeared in the app window, so the button looked as if it did nothing.",
  "<b>Compare shows live progress</b> (files found while reading, then the GB compared and the file in hand), and the Add picker opens centred at a usable size."]), latest=False)
b += release("1.0.26", "12 October 2026", "v1.0.26", "Compare two places can now clear the identical files from one side, and the old library copy gets Keep trying and Clear the copied originals.", ticks([
  "<b>Compare two places</b> (it was called Compare libraries) takes any two folders or libraries. After comparing you can <b>remove the identical files from one side</b>: set them aside in a folder (safest), move them to the Trash, or delete them for good (you type DELETE). Every file is compared byte for byte with its twin just before it is removed, and the other side is never touched. It will not clear an Apple Photos library.",
  "<b>Old library copy: Keep trying</b> retries only the files that failed. <b>Clear the copied originals</b> moves the originals that are already safely copied out of the old library, to the Trash or deleted for good, after a preview with the count and size. Only files whose copy is in your folder and about the same size are touched, and a list is saved.",
  "<b>A failing drive no longer holds the copy up.</b> If the drive does not answer for 90 seconds, the files it stuck on are skipped and listed, the copy carries on, and they are tried last next time. <b>Copy gently</b> copies at about half speed with a rest after every file, for a struggling drive.",
  "<b>39 more Apple log lines explained</b> in Live watch, most as honest low-confidence readings with their sources. The status bar no longer covers the bottom of a tool, and the app saves a hang report if it stops answering."]), latest=False)
b += release("1.0.24", "11 October 2026", "v1.0.24", "The old library copy skips files that a failing drive sticks on, and carries on.", ticks([
  "<b>The old library copy no longer gets stuck on a bad file.</b> If the drive does not answer for 90 seconds, the files it stuck on are listed as skipped and the copy carries on with the rest. Running the copy again tries them last, for a short time each, so they cannot hold up the others. If 12 reads end up stuck in all, it stops cleanly and says so.",
  "<b>You are told what happened.</b> The summary says how many files the drive stuck on, and they appear in the failed list (files_that_failed.csv) with the reason."]), latest=False)
b += release("1.0.23", "11 October 2026", "v1.0.23", "A gentler copy for struggling drives, 32 more Apple log lines explained, and the status bar stops covering the window.", ticks([
  "<b>Copy gently.</b> A new option in the Old library extractor copies at about half speed and rests after every file, for a USB drive, cable or hub that is struggling. Running the copy again skips what is already copied, so it is safe to turn on part-way through.",
  "<b>32 more log lines explained.</b> Live watch now recognises the iCloud Drive thumbnail errors, the photo-analysis text-encoder lines, the iCloud transfer (MMCS) errors, the Photos library-state and extended-attribute lines, and more. Most are honest best readings at low confidence, with what was searched and what could not be found written beside each. Two existing entries now match whatever error number your Mac shows.",
  "<b>The status bar no longer covers a tool.</b> A tool such as the Old library extractor now ends above the bar while a job runs, instead of running underneath it.",
  "<b>If the app stops answering,</b> it now saves a report of what it was doing (in Documents / Photo Clinic / Hang reports), so the cause can be found.",
  "<b>The status bar title goes back to the task.</b> Click the name of the running job to return to it. The Last used tools take the same colours as their cards."]), latest=False)
b += release("1.0.21", "11 October 2026", "v1.0.21", "The old library copy keeps going when a drive fails, and the Photos tools are coloured by theme.", ticks([
  "<b>The old library copy copes with a failing drive.</b> A file that will not copy after a couple of quick tries, or that the drive does not answer for within two minutes, is set aside and the copy carries on. At the end the set-aside files get a second, more patient go, and anything still failing is listed by name with the reason, in the summary and in a saved list (files_that_failed.csv). Before, a bad file could use five retries and very long read timeouts, the counter only updated every ten files so it looked stopped, and after three bad files in a row every later file failed at once while the count still climbed.",
  "<b>Run it again to finish.</b> Running the same copy again skips what is already there, even if an earlier run was cut off before it could save its record, and a progress line shows how many files are waiting for a retry and the file in hand.",
  "<b>The status bar no longer cuts off the window.</b> The page leaves room for the bar along the bottom while a job runs.",
  "<b>Photos tools are coloured like Home:</b> purple for fixing, green for cleaning, orange for moving, blue for monitoring and teal for guides, with a small key."]), latest=False)
b += release("1.0.19", "10 October 2026", "v1.0.19", "The Old library extractor no longer fails when a drive is slow to answer, and your own library is only used if you ask.", ticks([
  "<b>Old library extractor and slow drives.</b> The check that finds an old library could wait forever on a drive that had stopped answering, and the extractor then said to add the library when it was already there. The check now gives up after ten seconds, the Look at the library button waits for it, and a drive that is not answering gets its own message.",
  "<b>Only the library you chose is used.</b> Include my Photos library and Skip pictures already in my current library are now off until you tick them."]), latest=False)
b += release("1.0.18", "10 October 2026", "v1.0.18", "iPhoto and Aperture libraries can be extracted, the Add button works, and Count and Compare say more.", ticks([
  "<b>Old library extractor reads iPhoto and Aperture libraries</b> (the kind with Database/apdb/Library.apdb, including .migratedphotolibrary), not only the Photos 1.x layout. It copies your original pictures into folders named for your albums and iPhoto events, with keywords, ratings, titles, dates and places written in. Edited versions, people and faces are not read for this kind of library yet.",
  "<b>Move my photos, Tidy up and Fix my photos now stop at an iPhoto or Aperture library</b> and point you to the extractor, because they would otherwise treat it as a heap of files and bring in its thumbnails, caches and database files.",
  "<b>The Add button works.</b> Versions 1.0.12 and 1.0.13 showed the dialog but never returned your choice. One dialog now takes folders, Takeout zips and Photos libraries. A folder that holds a mix of libraries and other things can be split into its parts, and a library in the older layout that is still named .photoslibrary is recognised as an old library.",
  "<b>Count tells you what is in your folders.</b> A What is in table by file type and a By folder table, with plain descriptions. A library's own thumbnails and edited copies are no longer counted as photos, and your Apple Photos library shows the size of its originals.",
  "<b>Fix my photos copies your other files</b> (PDFs, documents) beside the photos, so the copy is complete, with a tick to turn it off and Undo. A finished preview has a Do it for real button. <b>Compare libraries</b> says when its picture check stopped at 30,000 pictures and can look at every picture. Start here offers to compare two sources you chose.",
  "<b>Keep sync running</b> has a shield button beside Live watch. The menu shows the release number. Decorative looping animations are switched off, which should stop the flicker. Folders with a single year in the name go under that year when you tidy."]), latest=False)
b += release("1.0.13", "9 October 2026", "v1.0.13", "One Add button for anything, Do it for real after a preview, and tidier folders and reports.", ticks([
  "<b>One Add button</b> for folders, Takeout zips and Photos libraries: one system dialog, and Photo Clinic works out which each is. (Version 1.0.12 had this button but the dialog did not open; 1.0.13 fixes that.)",
  "<b>Do it for real.</b> A finished preview now has a Do it for real button that repeats it with exactly the same settings, after a confirmation, so you do not need to untick Preview. In Start here there is also Skip to the next step.",
  "<b>Ticks in the summary.</b> Each section gets a tick after a real run and a hollow circle after a preview.",
  "<b>Tidy up</b> also puts folders with a single year in the name under that year (AUSTRALIA 2015 WITH FRIENDS goes in 2015). Names with two years, or only a year and month, stay where they are.",
  "<b>Previews leave nothing in your Target.</b> Their CSV lists go to Documents/Photo Clinic/Spreadsheets, one folder per run.",
  "<b>Live watch chart</b> counts messages when they happened, so a filter window shows only that window. A finished copy step no longer blocks the next step in Start here."]), latest=False)
b += release("1.0.11", "9 October 2026", "v1.0.11", "A guided Start here, a Status tab, Keep sync running for when you are away, and tidier logs and reports.", ticks([
  "<b>Start here.</b> Choose what you have (a Google Takeout, an old library, a folder, your Photos library or a drive that struggles) and Photo Clinic works out what it is, lists what it found grouped by the tool that deals with it, and makes a step-by-step plan. Each step says why, checks that the Target, free space and tools are ready, and works on the copy once an earlier step has made one. Progress is remembered, a green banner says when a step finished, and a Back button returns you to the plan.",
  "<b>Status tab and a live status bar.</b> A Status tab in the side pane shows one bold number per check (for example Library 95/100), with grey rows you can check with one tap, and an Apple system status row. While anything runs, a bar along the bottom shows progress, counts, time left and Stop.",
  "<b>Keep sync running</b> (Tools, Monitor) watches iCloud while you are away. It does not restart on a timer: it restarts the iCloud Photos sync or iCloud Drive only when the sync backlog is stuck or a service is pinned at high CPU, gently, at most once every two hours, never while iCloud is throttling, and it stops and tells you after three restarts that did not help. It can keep the Mac awake while plugged in, and has a Check before I leave list.",
  "<b>Apple system status</b> asks Apple's public status page whether anything is not green, only when you press it. <b>Which file is iCloud Drive busy with?</b> lists files changing right now in iCloud Drive, Desktop and Documents.",
  "<b>Log cards are tidier.</b> Each is one summary line with a coloured count, the process's CPU, a one-line description and a chevron to open the detail. Live watch has an issues-over-time chart, and the filter and add-unrecognised buttons sit beside Start. New one-tap restarts for the iCloud sync service and the Photos analysis service, and a reversible Reset iCloud's local cache. <b>Fixed:</b> Restart iCloud Drive was restarting the wrong service.",
  "<b>Tidy up</b> can put date-named folders under their year (13 Sep 2014 goes in 2014), on by default. <b>Old library extractor</b> is one click from the look to the copy, and shows where it will copy.",
  "<b>Reports and spreadsheets</b> now live in Documents/Photo Clinic (Runs, Previews, Spreadsheets, Receipts). Files earlier versions left on the Desktop and in Documents/Shoebox Reports are moved there once, and past runs still open.",
  "<b>Sharing is more reliable.</b> Lines waiting to be shared are kept across restarts and the daily limit, the sender starts when the app opens, and the report inbox lists what is waiting, with Don't send and Send now.",
  "Versions 1.0.7 to 1.0.10 were not released, so this includes everything since 1.0.6. The Target editor now matches the Source, a Home card is back among the tool cards beside a Last used group, and the window opens close to the height of the screen."]), latest=False)
b += release("1.0.6", "9 October 2026", "v1.0.6", "Get photos out of an old library, find damaged files, and copy only the good ones.", ticks([
  "<b>Old library extractor</b> (Tools, Utility). Turns an old Apple Photos, iPhoto or Aperture backup into a clean folder of copies, by album, year or year-month, with edited versions beside the originals and keywords, titles, ratings and places written into the copies. It skips exact and probable duplicates, shows a preview first, and has Undo.",
  "<b>Find damaged files</b> lists photos and videos that are cut short, empty or will not open, and files that make a drive stop answering. It does not freeze when a drive stalls. Each row has copy-name, show and open-folder icons, and you can tag the damaged files in Finder.",
  "<b>Copy the good files</b> copies the healthy photos and videos, with their .json files, to your Target and leaves the bad ones behind, with an optional move once each copy is verified. It is safe to run again after an interruption, and a stall lets you skip, try the next files or retry.",
  "<b>Log messages explain more.</b> Ids in a log line get names where your Mac knows them (shared albums, photos) or a plain explanation where it does not, shown beside the untouched raw line with copy icons. Every finding has a line breakdown and a Plain or Technical wording switch.",
  "<b>Catalogue: 283 entries.</b> 23 entries were researched again and 10 new ones added. Most are still marked low confidence and unverified, and each entry says what is inference.",
  "<b>Calmer and tidier:</b> lines you have already sent are shown as sent, the Target shows on the Tools tab, sources are a tickable list, and the app repaints much less while it works. Live watch no longer hangs when a drive has stopped answering."]), latest=False)
b += release("1.0.5", "8 October 2026", "v1.0.5", "Fixes the menu hidden behind the side pane, and faster optional sharing.", ticks([
  "<b>The menu works again.</b> In 1.0.4 the three-line menu, the style box and some dialogs opened hidden behind the side pane. They now open on top of it.",
  "<b>Optional sharing is quicker and easier to see.</b> Lines you have agreed to share go out within a few minutes, there is a Send what is waiting now button, and the report inbox says what each status means.",
  "<b>More messages explained</b>, including iCloud push tokens, server lock and zone messages, the file-transfer engine, and connection set-up failures."]), latest=False)
b += release("1.0.4", "8 October 2026", "v1.0.4", "A side pane that keeps watch, quick jobs, and many more messages explained.", ticks([
  "<b>A side pane</b> with Activity, Live watch, Needs attention and the sync meter, each with a number on its tab. It collapses to a thin strip and you can drag it wider.",
  "<b>Live watch groups repeats</b> into one card with a running total, flashes when something happens again, marks problems that fixed themselves with a green tick, and has a filter (the last five minutes by default). Every finding can show the log lines around it.",
  "<b>Quick jobs</b> on the Fix screen and in Tools: fix metadata from Google's files only, dates only, places only, or fix in place. They tick only what that job needs.",
  "<b>Compare libraries</b> now reads old iPhoto and Aperture libraries, opens with a plain verdict, and can copy what only one library has into year and album folders without changing either.",
  "<b>Check my photos</b> also measures disk space and the sync meter, finds broken thumbnails, and fills a status row on Home.",
  "<b>Many more messages explained</b>, each saying how we know. New: Save for review, and an optional, off-by-default way to share log lines Photo Clinic could not explain (cleaned first, Apple lines only, never linked to you).",
  "<b>Clearer and calmer:</b> stray and missing files ignore what is already in Recently Deleted, the disk space tool shows the whole library's real size, no folder is chosen for you unless you ask, and the target drive's free space is shown."]), latest=False)
b += release("1.0.3", "7 October 2026", "v1.0.3", "One check for everything, one screen to fix, and findings sorted by how much they matter.", ticks([
  "<b>Check my photos:</b> one button runs a read-only check of your photos, the Photos library, iCloud uploads, the logs and folder health, with a checklist, saved results and a status strip on Home.",
  "<b>Fix my photos:</b> one screen for dates, places, captions, albums and Live Photos. Copy, move or fix in place.",
  "<b>Findings sorted by importance:</b> Must resolve, Should review and Pure FYI. A passing network blip no longer looks like a problem, and many more log messages are explained in plain words.",
  "<b>Compare libraries</b> (under Tools): compares two folders, Photos libraries, or old iPhoto and Aperture libraries, and can copy what only one has into year and album folders. Neither library is changed.",
  "<b>Library health score,</b> a chart of library size and iCloud originals, a sortable process table, a Help me button and a Tools launcher.",
  "<b>The app can update itself</b> from the next release."]), latest=False)
b += release("1.0.2", "6 October 2026", "v1.0.2", "Quieter, clearer log reading.", ticks([
  "<b>Harmless messages are left out.</b> Photos, iCloud and macOS print many error-looking lines on a healthy Mac. The common harmless ones are now recognised and hidden, and the results say how many were left out.",
  "<b>Four more real problems explained:</b> iCloud slowing the upload of photo-analysis data, a missing preview picture, an unreadable account list, and a dropped network connection.",
  "<b>The Photos Health monitor</b> ignores the same harmless noise."]), latest=False)
b += release("1.0.1", "6 October 2026", "v1.0.1", "The first release: signed and notarised for Apple silicon Macs.", ticks([
  "<b>Fix a Google Takeout:</b> dates, places, captions, people and favourites restored from Google's files, read straight from zips, with time zones, Live Photos, edited copies, albums and Motion Photos handled.",
  "<b>Dates and places from every clue:</b> file names, folders, neighbouring photos and GPX tracks, plus offline place names for about 144,000 towns and cities.",
  "<b>Monitor your library:</b> a Photos Health tab takes a reading every 15 minutes while the app is open, with trends and a plain verdict. If macOS blocks it, it says which permission to give and opens the settings.",
  "<b>Find what is not right:</b> upload progress, log reading, live watch, a sync meter, a disk-space check, about 170 known problems and 17 step-by-step fix guides.",
  "<b>Combine and tidy:</b> merge folders, remove exact copies, review look-alikes, convert old videos to MP4 with verification, and a photo health score.",
  "<b>Move to Apple Photos</b> in batches, oldest first, waiting for iCloud between batches.",
  "<b>Five styles</b> from Safest to I like risk, preview first, copy by default, stop and undo, and reports for every run."]), latest=False)
b += '<div class="callout"><b>Updating.</b> The app checks for updates and shows a banner when one is ready. The packaged Mac app asks you to download the newest version and replace the old one. <a href="%s">Download it here</a>.</div>' % DL
b += cta()
page("versions.html", "Versions", "Every Photo Clinic release, newest first, with what is new in each.", b, "versions.html")

# ---------------------------------------------------------------- privacy
b = head("Privacy", "What this website and the app do with your data", "The short version: the app collects nothing unless you switch on optional log sharing. The website uses Google AdSense, which uses cookies, and a privacy-focused visitor counter (GoatCounter).")
b += """<h2>The Photo Clinic app</h2>
%s
<h2>This website</h2>
%s
<h2>Questions</h2>
<p>Email <a href="mailto:thestocksoup@gmail.com">thestocksoup@gmail.com</a>.</p>
%s""" % (
 ticks(["Your photos, file names and Photos library <b>never leave your Mac</b>. There is no account and no analytics inside the app.", "The only network use is checking GitHub for a newer version and, if you choose to update, downloading it. GitHub can see your IP address when that happens, like any website.", "Reports and history stay on your Mac, in your own folders.", "<b>Optional sharing, off by default.</b> If you choose to help improve the explanations, Photo Clinic can send log lines it could not explain to a private review inbox (a Cloudflare Worker with a database). Only Apple's own system lines are eligible, and names, folders, file names, photo ids, email and network addresses, serial numbers and long numbers are removed first; a line that still looks personal is not sent. Your macOS and Photo Clinic versions go with it. There is no account and no id, so reports cannot be linked to you (which also means one cannot be found and deleted later). They are kept for 180 days. You see everything that was sent, inside the app, and can switch it off at any time. Cloudflare can see the IP address of the connection, like any website, and Photo Clinic does not store it."]),
 ticks(["The site is hosted on GitHub Pages. GitHub may log visitors' IP addresses as part of running the service.", "This site counts visits with <b>GoatCounter</b>, a privacy-focused service. It keeps only totals (for example how many people visited, which page, which site sent them, and their browser type, screen size and country), not your IP address or your browser's identifying text, and by its own description it cannot be used to identify a person. The totals are shown in the footer of every page.", "This site uses <b>Google AdSense</b>. Google and its partners may use cookies and similar technology to show and measure ads, including personalised ads where the law allows. You can manage this at <a href=\"https://adssettings.google.com\">adssettings.google.com</a> and read how Google uses data at <a href=\"https://policies.google.com/technologies/partner-sites\">policies.google.com/technologies/partner-sites</a>.", "We do not run our own analytics or sell any data, and the site has no accounts or forms.", "Downloads are served by GitHub, which counts how many times each file is downloaded."]),
 cta())
page("privacy.html", "Privacy", "What the Photo Clinic website and app do with your data.", b, "privacy.html")


# ---------------------------------------------------------------- copy iCloud Drive
b = head("Copy iCloud Drive", "How to copy iCloud Drive to an external drive on a Mac", "Finder fails on big iCloud Drive folders: files that are not downloaded do not copy, and you cannot tell what is missing. Photo Clinic copies slowly and carefully, shows you the gaps, and fills them in.")
b += """<h2>Why copying iCloud Drive is hard</h2>
%s
<h2>What Photo Clinic does differently</h2>
%s
<h2>Already copied some of it? Fill in the gaps</h2>
<p>If you tried a copy before (with Finder, another backup app or Photo Clinic itself), press <b>Compare with what is already copied</b>. It looks at your copy, wherever you point it, and shows:</p>
%s
<p>Then <b>Copy the gaps</b> copies only what is missing or cut short. Files that are already there, at the right size, are left alone.</p>
<h2>Step by step</h2>
%s
<h2>When some files fail</h2>
<p>A big copy always finds a few problems. Photo Clinic groups them by cause, so 50,000 messages become a handful of lines you can act on:</p>
%s
<p>Each group has <b>Show the list</b>, <b>Copy the list</b> and <b>Try these again</b>, and the full list is saved as a spreadsheet.</p>
<h2>Questions</h2>
<div class="faq">
<h3>Does it change anything in iCloud?</h3><p>No. It only reads iCloud Drive. Files it brings down for a copy are taken off your Mac again afterwards (if you leave that option ticked), and the optional Finder tag is only a label.</p>
<h3>How long does it take?</h3><p>It depends on your internet speed. Photo Clinic shows the current speed and an honest time left. The copy can be stopped and carried on at any time, even after a restart.</p>
<h3>Where do my files go?</h3><p>Into a folder called <i>iCloud Drive</i> inside the folder you choose, keeping your folder structure.</p>
<h3>Is it free?</h3><p>Yes, free for Macs with Apple silicon.</p>
</div>
%s%s""" % (
 ticks(["Files that are <b>only in iCloud</b> are not on your Mac, so Finder has to download each one first, and it gives up or skips some.", "Hundreds of gigabytes fill your Mac before they reach the drive.", "When the numbers do not match, <b>you cannot tell which files are missing</b>.", "Any stop, sleep or error means starting again."], "bad"),
 ticks(["<b>One file at a time.</b> It asks iCloud to send the file, copies it, checks the size, then <b>frees the space on your Mac</b> again (you can turn that off).", "<b>Resumable.</b> Running it again skips what is done. Close the app and it offers to continue next time, or can carry on by itself.", "<b>Honest numbers.</b> Live speed over the last minute and time left, based only on what still has to be copied.", "<b>Pick folders from a tree</b> with the size and how much is only in iCloud shown on every folder.", "<b>One clear line per file</b> in Activity, with a link to the copied file in Finder.", "<b>Checks the space</b> on your drive and your Mac, and waits instead of failing when it is nearly full.", "An optional green <b>Finder tag</b> on each original once its copy is checked."]),
 ticks(["how many files are in iCloud and how many are already in the copy, with sizes", "which are <b>missing</b> and which are <b>cut short</b> (same name, wrong size)", "<b>folder by folder</b>, what is copied and what is missing", "files that are only in your copy, not in iCloud"]),
 '<ol class="steps"><li><b>Choose your folders.</b> Open <b>Copy from the cloud</b> on Home and tick the iCloud Drive folders. Open a folder to choose something inside it.</li><li><b>Choose Where to save.</b> Pick a folder on your external drive.</li><li><b>Compare.</b> See what is already copied and what is missing.</li><li><b>Copy.</b> Press <b>Copy the gaps</b> (or <b>Copy the ticked folders</b> the first time). Watch the speed and time left at the top of the screen, and press Stop whenever you like.</li></ol>',
 ticks(["<b>Moved or deleted since the scan.</b> Harmless: nothing to do.", "<b>iCloud did not send it in time.</b> Check the internet, then try again.", "<b>Not allowed to read or write.</b> A button opens the macOS privacy setting.", "<b>The drive is full or was disconnected.</b> Fix it, then continue.", "<b>The file could not be read.</b> The file or the drive may be damaged."]),
 cta(), nextlinks(("tools.html", "All tools"), ("download-google-drive-folder-mac.html", "Download from Google Drive")))
page("copy-icloud-drive-to-external-drive-mac.html", "Copy iCloud Drive to an external drive on a Mac", "Copy iCloud Drive to an external drive on a Mac, even files only in iCloud. Slow and careful, resumable, shows which files are missing and fills the gaps. Free.", b, "copy-icloud-drive-to-external-drive-mac.html", ld='<script type="application/ld+json">' + __import__("json").dumps({"@context": "https://schema.org", "@type": "HowTo", "name": "Copy iCloud Drive to an external drive on a Mac", "step": [{"@type": "HowToStep", "name": "Choose your folders", "text": "Open Copy from the cloud and tick the iCloud Drive folders to copy."}, {"@type": "HowToStep", "name": "Choose where to save", "text": "Pick a folder on your external drive."}, {"@type": "HowToStep", "name": "Compare", "text": "See which files are already copied and which are missing."}, {"@type": "HowToStep", "name": "Copy the gaps", "text": "Copy only what is missing. It can be stopped and carried on at any time."}]}) + '</script>')

# ---------------------------------------------------------------- Google Drive
b = head("Google Drive", "How to download a Google Drive folder, or your Takeout files from an email, to your Mac", "Sign in with your own Google account, choose your own folders, and Photo Clinic copies them to your drive. It can only read your Drive, and it carries on where it stopped.")
b += """<h2>Download folders from Google Drive</h2>
%s
<h2>Got an email full of Drive links?</h2>
<p>After a Google Takeout to Drive, Google emails you a list: &ldquo;View 1 of 43 in Drive&rdquo;, &ldquo;View 2 of 43&rdquo; and so on. Clicking 43 links by hand is slow and easy to get wrong. In Photo Clinic, open <b>Copy from the cloud</b> and the <b>Links</b> tab, and paste the email.</p>
%s
<h2>Takeout download links (the ones that open in your browser)</h2>
<p>Links on <i>takeout.google.com</i> must be downloaded in your browser, and Google asks you to sign in again. Photo Clinic cannot do that for you, but it keeps track: press <b>Open</b> for a part, let it download, and Photo Clinic moves each finished file from Downloads into your folder and ticks it off. Partly downloaded and broken files are left alone.</p>
<h2>Step by step</h2>
<ol class="steps"><li><b>Connect Google Drive.</b> Press Connect. Google's own page opens: choose your account and allow read-only access. Photo Clinic never sees your password.</li><li><b>Choose folders</b> from My Drive or Shared with me, or paste a folder link. Open a folder to choose something inside it.</li><li><b>See the size</b> of each folder and whether your drive has room.</li><li><b>Copy.</b> Several files at once if you like, with the speed and time left. Stop whenever you want and carry on later.</li></ol>
<h2>Questions</h2>
<div class="faq">
<h3>Is it safe to sign in?</h3><p>You sign in on Google's own page. Photo Clinic only asks for permission to read, so it can never change or delete anything in your Drive, and the sign-in stays on your Mac. You can sign out at any time and withdraw access in your Google account.</p>
<h3>Does it work with links to other services?</h3><p>It works with any Google Drive file or folder link your account can open. Dropbox, WeTransfer and similar links are listed as skipped.</p>
<h3>What if Google stops the downloads?</h3><p>Google sometimes limits downloads for a day. Photo Clinic says so in plain words, keeps what it has, and carries on when you try again.</p>
<h3>What about files with the same name?</h3><p>Google Drive allows two files with the same name in one folder. Photo Clinic keeps them all, naming the extras <i>Name (dup1)</i>.</p>
</div>
%s%s""" % (
 ticks(["<b>Your own account.</b> Sign in on Google's page; read-only.", "<b>Your own folders.</b> Browse My Drive and Shared with me, or paste a link.", "<b>Resumable.</b> Run it again and finished files are skipped; a restart offers to continue.", "<b>Checks at the end</b> that everything arrived.", "<b>Files that share a name</b> are all kept.", "<b>Clear problems.</b> Quota, permission and not-found are explained, with what to do."]),
 ticks(["It finds every Google Drive and Takeout link, even when the email was copied with its links hidden behind the words.", "Puts them in order by their &ldquo;1 of 43&rdquo; labels and drops repeats.", "Makes a <b>checklist</b>: waiting, downloading with speed, done, or failed with the reason.", "Downloads several parts at once (you choose how many) and skips parts it already has when you run it again.", "Offers to use the downloaded zips as your Takeout source, ready to fix."]),
 cta(), nextlinks(("copy-icloud-drive-to-external-drive-mac.html", "Copy iCloud Drive"), ("fix-takeout.html", "Fix your Takeout")))
page("download-google-drive-folder-mac.html", "Download a Google Drive folder or Takeout files to a Mac", "Download a Google Drive folder, or the files in a Google Takeout email (View 1 of 43 in Drive), to your Mac. Your own account, read-only, resumable, free.", b, "download-google-drive-folder-mac.html")

# ---------------------------------------------------------------- not in Apple Photos
b = head("Not in Photos yet", "How to find which photos are not in Apple Photos yet", "Before you drag a big folder into Photos, find out what Photos already has. It saves hours, and it stops the &ldquo;Cannot import&rdquo; and duplicate messages.")
b += """<h2>The problem</h2>
%s
<h2>What Photo Clinic shows you</h2>
<p>Choose a folder and your Photos library, and press <b>Check what is missing</b>. You get four numbers:</p>
%s
<h2>See them side by side</h2>
<p>Press <b>Show me</b> to see your file next to the picture Photos holds under that name, with their sizes, a link to your file in Finder, and a button to show the Photos one in the Photos app. A short note says what it probably means, for example that a RAW file is usually stored with the JPEG of the same name.</p>
<h2>Then what?</h2>
%s
<h2>How it knows</h2>
<p>Two ways, both read-only. It compares the content of your files with the full-size originals Photos keeps on this Mac. And it reads Photos' own records, which list every picture's original name and exact size, so it also recognises pictures that live <b>only in iCloud</b>. Photos you deleted (in Recently Deleted) are not counted as being in the library.</p>
<div class="callout"><b>Honest about what it cannot know.</b> A different file under the same name might be a better copy, a smaller copy, or a different picture that shares a camera number. Photo Clinic shows both sizes and leaves the choice to you.</div>
%s%s""" % (
 ticks(["Photos does not tell you which pictures in a folder it already has.", "Importing thousands of files you already own wastes hours and disk space.", "A big drag-in can end with <b>&ldquo;Cannot import&rdquo;</b> or hundreds of duplicate questions.", "Pictures that exist only in iCloud cannot be checked by looking at files on your Mac."], "bad"),
 ticks(["<b>Pictures in your folder</b>", "<b>Already in Photos</b>, the same file", "<b>Photos has the name, but a different file</b>, which could be an edited, resized or better copy", "<b>Not in Photos at all</b>"]),
 ticks(["<b>Copy the missing ones</b> into a new folder, ready to import. They are filed in a folder named after the album that fits best (the album most of that folder's other pictures are already in), so Photo Clinic's album-from-folder import files them correctly.", "<b>Move the ones Photos already has aside</b> into a folder called <i>_already_in_Photos</i> inside your own folder. Nothing is deleted, you can undo it, and you delete that folder yourself when you are sure.", "<b>Send them to Apple Photos</b> in careful batches, with a small test first."]),
 cta(), nextlinks(("apple-photos.html", "Send to Apple Photos"), ("find-duplicate-photos-mac.html", "Find duplicates")))
page("photos-not-in-apple-photos.html", "Find photos that are not in Apple Photos yet", "Find which photos in a folder are not already in your Apple Photos library, even pictures only in iCloud, and import only those. Free Mac app.", b, "photos-not-in-apple-photos.html")

# ---------------------------------------------------------------- damaged photos
b = head("Damaged photos", "How to find damaged or unreadable photos on a Mac", "A photo that stopped short, an empty file, or a zip that never finished downloading can cause import errors later. Find them first, and rescue the good files from a failing drive.")
b += """<h2>What it finds</h2>
%s
<h2>Check more files, if you want to be thorough</h2>
<p>The normal check looks at the structure of every file, which is quick. <b>Check more files (slower)</b> also reads each file all the way through and opens pictures and videos to catch ones that are corrupt on the inside.</p>
<h2>Rescue the good files from a failing drive</h2>
%s
<h2>Zip files that did not finish</h2>
<p>If a Google Takeout zip stopped early, Photo Clinic says which one, so you can download it again, and still fixes everything else.</p>
%s%s""" % (
 ticks(["Pictures and videos that are <b>cut short</b>, with the end missing.", "<b>Empty</b> files with a name and nothing inside.", "Files that <b>cannot be opened</b> or are named as one type and are really another.", "Zip files that are damaged or incomplete.", "Each one is listed with the reason, in plain words, and left out of a fixed copy."]),
 ticks(["Copies what still reads, <b>gently</b>, so a struggling drive is not pushed harder.", "Skips a stuck file after a short wait, carries on, and lists what it skipped.", "Tries the stuck ones again last, and can try again later.", "Lists a good copy elsewhere when it finds one."]),
 cta(), nextlinks(("old-libraries.html", "Old libraries"), ("tidy.html", "Duplicates and tidy-up")))
page("find-damaged-photos-mac.html", "Find damaged or unreadable photos on a Mac", "How to find damaged, cut-short or empty photos and videos on a Mac, and rescue the good files from a failing drive. Free.", b, "find-damaged-photos-mac.html")


# ---------------------------------------------------------------- long guides
REVIEWED = "26 October 2026"


def article(fname, title, desc, kicker, h1, lead, body, related):
    ld = '<script type="application/ld+json">' + __import__("json").dumps({"@context": "https://schema.org", "@type": "Article", "headline": h1, "description": desc, "datePublished": "2026-10-26", "dateModified": "2026-10-26",
                                                                           "author": {"@type": "Organization", "name": "Photo Clinic"}, "publisher": {"@type": "Organization", "name": "Photo Clinic", "url": "https://photoclinic.org/"},
                                                                           "mainEntityOfPage": SITE + fname}) + '</script>'
    b = head(kicker, h1, lead)
    b += '<p class="note" style="margin-top:0">Last reviewed %s. Written by the Photo Clinic team from what we learned moving large photo libraries. See <a href="editorial-policy.html">how we write these guides</a>.</p>' % REVIEWED
    b += body
    b += '<h2>Related</h2><ul class="ticks">%s</ul>' % "".join('<li><a href="%s">%s</a></li>' % r for r in related)
    b += cta()
    page(fname, title, desc, b, fname, ld=ld)


# 1 --------------------------------------------------------------------------------------------------------------
article("why-icloud-drive-copy-sizes-do-not-match.html", "Why the size and file count do not match after copying iCloud Drive",
        "Why a copy of an iCloud Drive folder has a different size or file count, and how to find which files are missing: placeholders, hidden files and file systems.",
        "Guide", "Why the size and file count do not match after copying iCloud Drive",
        "You copied a big iCloud Drive folder to an external drive and the two folders show different sizes and different numbers of files. Some of that is normal. Some of it means files are missing. Here is how to tell which.",
        """<h2>1. Files that are only in iCloud</h2>
<p>With <b>Optimise Mac Storage</b> on, many iCloud Drive files are not on your Mac at all. They show a cloud icon, and the Mac only holds a small placeholder. Finder shows the full size of such a file, but it takes almost no space on disk. To copy it, macOS first has to download it. If the download is slow, you are offline, or the file is huge, Finder may stop, show an error, or skip it. This is the most common reason a copy comes out short.</p>
<p>Check: in Finder, a small cloud icon with a down arrow beside a name means the file is not downloaded.</p>
<h2>2. Size and &ldquo;size on disk&rdquo; are different numbers</h2>
<p>Get Info shows two sizes. <b>Size</b> is how many bytes the files contain. <b>Size on disk</b> is how much space they occupy, rounded up to the drive's allocation unit. Many small files take more space on a drive with a big allocation unit (exFAT drives can use units far larger than a Mac's own drive), so a folder can look larger on the copy while holding the same files. Compare <b>Size</b>, not <b>Size on disk</b>.</p>
<h2>3. Hidden files change the count</h2>
<ul>
<li><b>.DS_Store</b> files hold Finder's view settings for each folder. They are created and removed freely.</li>
<li><b>._name</b> files (called AppleDouble files) appear when you copy to a drive that is not formatted for Macs, such as FAT or exFAT. They hold extra Mac information for the file next to them. They add to the file count and are not a sign of a problem.</li>
<li>Finder's item counts leave hidden files out, but Terminal's counts include them. Counting in two different ways produces two different numbers.</li>
</ul>
<h2>4. Packages are one item that holds many files</h2>
<p>A <b>.pages</b> or <b>.numbers</b> document, a <b>.photoslibrary</b>, or an app, looks like one file in Finder but is really a folder full of files. A tool that counts one will not match a tool that counts the other.</p>
<h2>5. Names the destination cannot hold</h2>
<p>Some file systems refuse certain characters, very long names, or treat accented letters differently from the Mac. A file with a name the destination cannot store can fail to copy, or arrive under a slightly different name. If you see &ldquo;file not found&rdquo; for a name that looks fine, this is a likely reason.</p>
<h2>6. Files that changed or moved during the copy</h2>
<p>iCloud Drive keeps syncing while you copy. A file you moved or deleted after the copy began cannot be found any more, which produces a &ldquo;file not found&rdquo; message. Those are harmless, but they add up when you move many files.</p>
<h2>How to find exactly what is missing</h2>
<p>Do not compare folder sizes. Compare lists of files. Two ways:</p>
<ol class="steps">
<li><b>In Terminal.</b> Count real files on each side, leaving out the .DS_Store noise: <code>find "SOURCE" -type f ! -name ".DS_Store" | wc -l</code> and the same for the copy. To list the differences, compare the relative paths of both sides with <code>diff</code>. On older versions of macOS, files that are not downloaded appear in Terminal as small <code>.name.icloud</code> placeholder files.</li>
<li><b>With Photo Clinic.</b> Open <b>Copy from the cloud</b>, tick the same folders, and press <b>Compare with what is already copied</b>. It looks at your existing copy wherever it is, and shows how many files are already there with the right size, which are missing, which are cut short, and which exist only in the copy, folder by folder. Then <b>Copy the gaps</b> copies only those files.</li>
</ol>
<div class="callout"><b>A file with the same name and a smaller size is a cut-short copy.</b> Compare sizes as well as names: a copy that stopped part-way leaves a file that exists but is not complete.</div>""",
        [("copy-icloud-drive-to-external-drive-mac.html", "How to copy iCloud Drive to an external drive on a Mac"), ("download-google-drive-folder-mac.html", "Download a Google Drive folder to your Mac"), ("find-damaged-photos-mac.html", "Find damaged or unreadable photos")])

# 2 --------------------------------------------------------------------------------------------------------------
article("whats-in-a-google-takeout-and-how-to-check-it.html", "What is in a Google Takeout of Google Photos, and how to check you have it all",
        "What the zip files, JSON files and folders in a Google Takeout of Google Photos are, why names are cut short, and how to check that every archive downloaded.",
        "Guide", "What is in a Google Takeout of Google Photos, and how to check you have it all",
        "A Google Takeout arrives as a pile of zip files with strange names. Inside are your photos, and beside each one a small file of information. Here is what everything is, and how to be sure nothing is missing before you delete anything.",
        """<h2>The zip files</h2>
<p>Google splits a large export into several archives. They are named like <code>takeout-20241027T093500Z-001.zip</code>, <code>-002.zip</code> and so on, in order. When you create the export you choose the archive size (for example 2 GB or 50 GB), so a big library can be dozens of zip files. If you chose to send them to Google Drive instead, they are files in a Drive folder, and Google emails you a list of links.</p>
<p>Two limits catch people out. The download links <b>expire</b> after a few days, and each archive can only be downloaded a limited number of times. Download everything promptly, and keep the zip files until you have checked the result.</p>
<h2>The folders inside</h2>
<ul>
<li><b>Photos from 2019</b> (one folder per year): every photo and video taken that year, in a flat list.</li>
<li><b>Album folders</b>: one folder for each album you made. The same photo can appear in a year folder and in an album, so a Takeout holds more files than you have pictures.</li>
<li><b>Trash, Archive and other folders</b> may appear, depending on what you exported.</li>
</ul>
<h2>The small JSON file beside each photo</h2>
<p>Next to each picture is a file ending in <code>.json</code> (in newer exports, <code>.supplemental-metadata.json</code>). It holds what Google knows about the photo: the date it was taken, the place, the description, the people, and whether you marked it as a favourite. The photo itself often has none of this. That is why photos from a Takeout can show the day you downloaded them, with no place or caption, until something reads the JSON files and writes the information back.</p>
<h2>Why some names look cut short</h2>
<p>Google limits the length of these file names, so a long photo name is shortened, and the matching JSON name is shortened too, in a way that does not always line up. A tool that just adds <code>.json</code> to the photo name will miss some. Photo Clinic matches by several rules, including the shortened forms, numbered duplicates like <code>photo(1).jpg</code>, and edited copies.</p>
<h2>Edited copies, Live Photos and Motion Photos</h2>
<ul>
<li>An edit you made in Google Photos appears as a second file with <code>-edited</code> in the name, next to the original.</li>
<li>A Live Photo arrives as a still picture plus a separate short video with the same name.</li>
<li>A Motion Photo from some Android phones has a video hidden inside the picture file.</li>
</ul>
<h2>How to check that you have everything</h2>
<ol class="steps">
<li><b>Count the zip files</b> against the number in Google's email or the export page. Check the numbers run without gaps (001, 002, 003 &hellip;).</li>
<li><b>Check each zip opens.</b> A zip that stopped part-way will not open, or will report errors. Photo Clinic reads every zip and tells you which ones could not be read, so you can download only those again.</li>
<li><b>Compare the picture count</b> with what Google Photos shows (allowing for the extra album copies and the -edited files).</li>
<li><b>Keep the originals</b> until you have looked at the fixed copy and checked it in your photo app.</li>
</ol>
<div class="callout"><b>Photo Clinic never changes your zip files.</b> It reads them, and writes the fixed photos into a new folder you choose.</div>""",
        [("how-to-fix-google-takeout-metadata-mac.html", "How to fix Google Takeout metadata on a Mac"), ("google-takeout-json-files.html", "What are all those .json files?"), ("download-google-drive-folder-mac.html", "Download your Takeout files from Google Drive")])

# 3 --------------------------------------------------------------------------------------------------------------
article("apple-photos-cannot-import-and-duplicate-messages.html", "Apple Photos: &ldquo;Cannot Import&rdquo; and duplicate messages, and what to do",
        "Why Apple Photos shows Cannot Import with Unknown error, or asks about each duplicate, when you import a big folder, and how to avoid wasting hours.",
        "Guide", "Apple Photos says &ldquo;Cannot Import&rdquo; or asks about every duplicate: what is going on",
        "You drag a large folder into Photos and get &ldquo;Cannot Import 4,418 Items&rdquo; with &ldquo;Unknown error&rdquo; against each file, or a never-ending &ldquo;import this duplicate?&rdquo; question. These are the usual causes, and a better way to import.",
        """<h2>The two messages</h2>
<p><b>&ldquo;Would you like to import the following duplicate item?&rdquo;</b> means Photos found a picture in your library that matches the one you are importing. It shows both, and lets you tick <b>Apply to all duplicates</b> to answer once. If most of a folder is already in your library, you will see this again and again.</p>
<p><b>&ldquo;Cannot Import&hellip; Unknown error.&rdquo;</b> means Photos tried and could not add the file. The dialog does not say why. The usual causes are below, with the most common first.</p>
<h2>Why imports fail with &ldquo;Unknown error&rdquo;</h2>
<ol class="steps">
<li><b>Low disk space.</b> Photos needs room on the drive that holds the library, and Photos and macOS also use space on the drive your Mac starts from while importing. When either gets low, files near the end of a big import fail. Check both before a large import.</li>
<li><b>The drive stopped or slept.</b> Importing from an external drive that spins down, loses power, or is read at the same time as it is written to, can fail files at random.</li>
<li><b>Damaged or cut-short files.</b> A picture that never finished downloading cannot be added. These are usually a handful, not thousands.</li>
<li><b>A name that does not match the content.</b> A WebP or PNG saved as <code>.jpg</code>, or a format Photos does not support, is refused.</li>
<li><b>Too many at once.</b> A single huge drag overloads the import. Batches are kinder to Photos and to iCloud.</li>
</ol>
<h2>A better way: find out what is not in Photos first</h2>
<p>Before importing, work out which pictures Photos does not have. Photos' own records list each picture's original name and exact size, so a folder can be compared with the library without importing anything, even for pictures that live only in iCloud. The ones that match are already there. A name that matches with a different size is a different version, such as an edited, resized or better copy. A RAW file is usually stored together with the JPEG of the same name.</p>
<p>Photo Clinic does this in <b>What is not in Photos yet?</b>: it shows your file next to the one in Photos, copies only the missing pictures into a new folder, and can move the ones Photos already has aside (never deleting them).</p>
<h2>Importing a big library safely</h2>
<ul class="ticks">
<li><b>Look at free space</b> on the library drive and on your Mac first.</li>
<li><b>Try 20 photos</b> and look at them in Photos before sending the rest.</li>
<li><b>Send in batches</b>, oldest first, and let iCloud catch up between them.</li>
<li><b>Remember that Photos has no undo for an import.</b> Keep your originals until you are happy.</li>
</ul>""",
        [("photos-not-in-apple-photos.html", "Find which photos are not in Apple Photos yet"), ("apple-photos.html", "Moving a large library into Apple Photos"), ("find-damaged-photos-mac.html", "Find damaged or unreadable photos"), ("icloud-photos-stuck-syncing.html", "Is iCloud Photos slow, or stuck?")])

# 4 --------------------------------------------------------------------------------------------------------------
article("how-to-tell-if-photos-are-duplicates.html", "How to tell if two photos are really duplicates",
        "Exact duplicates, look-alikes, edits and RAW plus JPEG pairs explained, and why names and sizes are not enough to decide which photos are safe to remove.",
        "Guide", "How to tell if two photos are really duplicates",
        "Two photos with the same name might be different pictures. Two with different names might be the same picture. Here is how to decide, and which kinds are safe to remove.",
        """<h2>Four kinds of &ldquo;the same&rdquo;</h2>
<ol class="steps">
<li><b>Exact copies.</b> The files are identical, byte for byte. They may have different names or sit in different folders (<code>IMG_0042.jpg</code>, <code>IMG_0042 (1).jpg</code>). One can be removed with no loss.</li>
<li><b>The same picture at a different size or quality.</b> A smaller copy, a re-saved copy, or a copy exported by another app. The pictures look alike, but the files are different, and one is better.</li>
<li><b>An original and an edit.</b> The same photo after cropping, filters, or red-eye fixes. You may want both.</li>
<li><b>RAW and JPEG pairs.</b> A camera that saves both makes two files with the same name. They are not duplicates: the RAW is the negative, and the JPEG is the picture made from it.</li>
</ol>
<h2>Why names and sizes are not enough</h2>
<ul>
<li>Cameras restart their numbering, so two different photos can both be called <code>IMG_1234.jpg</code>.</li>
<li>Copies get names like <code>(1)</code> added when a file with the same name already exists.</li>
<li>Two files can have the same size by chance, so size alone is not proof.</li>
<li>Re-saving a photo changes its size without changing how it looks.</li>
</ul>
<h2>How exact copies are found</h2>
<p>The reliable test is the content. A good tool groups files by size first (cheap), then compares a fingerprint of the content, and confirms the whole file before calling two files identical. Photo Clinic does this, keeps the first copy and moves the others into a spare folder. It does not delete them, and you can see both pictures side by side before you decide.</p>
<h2>How look-alikes are found</h2>
<p>For pictures that are the same but not identical, the tool compares how they look, using a small fingerprint of the picture's shape and brightness. Two photos whose fingerprints are close are probably the same picture. It is a good hint and a poor judge, so the right answer is to show them side by side, suggest a keeper (for example the larger one, or the one you marked as a favourite), and let you choose.</p>
<h2>Which to keep</h2>
<ul class="ticks">
<li>A <b>favourite</b>, or one with an <b>edit</b>, usually wins.</li>
<li>Otherwise the one with <b>more pixels</b> and the <b>larger file</b>.</li>
<li>The one with <b>more information inside</b> (date, place, caption).</li>
</ul>
<div class="callout"><b>Move aside first, delete later.</b> Move the extras into a folder, look through your library for a while, then delete the folder when you are sure. That is how Photo Clinic works, and you can check again afterwards that nothing is left.</div>""",
        [("find-duplicate-photos-mac.html", "How to find and remove duplicate photos on a Mac"), ("photos-not-in-apple-photos.html", "Find which photos are not in Apple Photos yet"), ("tidy.html", "Duplicates and tidy-up tools")])

# 5 --------------------------------------------------------------------------------------------------------------
article("photo-dates-and-time-zones-explained.html", "Photo dates and time zones: why a photo shows the wrong time",
        "Why photos and videos show the wrong date or a time hours off after a copy, export or conversion: EXIF dates, UTC video dates, file dates and file names explained.",
        "Guide", "Photo dates and time zones: why a photo shows the wrong day or hour",
        "A photo taken at 2:34 pm shows 12:34 am. A video is a day out. A whole folder shows the day you copied it. All of this comes down to a few different &ldquo;dates&rdquo; stored in different places.",
        """<h2>One photo, several dates</h2>
<ul>
<li><b>The date taken, inside the picture</b> (EXIF). Written by the camera, as the clock on the wall showed. It usually has <b>no time zone</b>, and newer cameras add a separate offset.</li>
<li><b>The date in a video file</b> (QuickTime). By convention it is stored in <b>UTC</b>, the universal clock. A video shot at 2:34 pm in Mongolia is stored as 06:34 UTC, and apps that forget to convert show the wrong hour.</li>
<li><b>The file's own dates</b>, which Finder shows as Created and Modified. They are set by the file system, not the camera. Copying, downloading, converting or restoring a file can set them to the day it happened.</li>
<li><b>The date in the file name</b>, such as <code>20120630143447.mp4</code> or <code>IMG_20190704_123456.jpg</code>. Most phones and many cameras write the time into the name, in local time.</li>
<li><b>Google Takeout's JSON date</b>, a number of seconds since 1970 in UTC.</li>
</ul>
<h2>Why the hour is wrong</h2>
<p>If a tool writes a local time as if it were UTC, or the other way round, the result is out by your time zone difference. For example, 14:34 written as UTC and read back in a time zone ten hours ahead shows 00:34 the next day, which puts the picture on the wrong day.</p>
<h2>Why the day is wrong</h2>
<ul>
<li>The file dates were reset by a copy, so the library falls back on the day you copied.</li>
<li>There was no date inside, and the app used the file date.</li>
<li>The camera clock was wrong, or a time zone was never set on holiday.</li>
</ul>
<h2>What a good fix does</h2>
<ol class="steps">
<li><b>Use the best source.</b> The date inside the picture first, then Google's JSON, then the file name, then the folder name. Never make up a date when a real one exists.</li>
<li><b>Fill, do not overwrite.</b> Only add a date when one is missing, and say where it came from.</li>
<li><b>Handle the time zone properly.</b> Store local time with the right offset, using the picture's location when it has one.</li>
<li><b>Show before and after</b> for a few real photos before anything is written, and write the result into a copy.</li>
</ol>
<p>That is what Photo Clinic's <b>Fix my photos</b> does. Its preview lists exactly which files have no date stored inside, the date Finder shows for each, and the date that would be stored (for example the one in the name), so you can decide whether to trust the names.</p>""",
        [("google-takeout-dates-wrong.html", "Why do my Google Takeout photos show the wrong date?"), ("how-to-fix-google-takeout-metadata-mac.html", "How to fix Google Takeout metadata on a Mac"), ("organise-photos-by-date-mac.html", "Organise photos by date")])

# ---------------------------------------------------------------- guides index, about, contact, how we write
b = head("Guides", "Photo Clinic guides", "Plain-language guides to getting your photos and files in order: Google Takeout, iCloud, Apple Photos, duplicates and dates.")
b += """<h2>Moving and copying</h2>
%s
<h2>Understanding what you have</h2>
%s
<h2>Apple Photos and iCloud</h2>
%s
<h2>Fixing problems</h2>
%s
%s""" % (
 ticks(['<a href="copy-icloud-drive-to-external-drive-mac.html">How to copy iCloud Drive to an external drive on a Mac</a>', '<a href="why-icloud-drive-copy-sizes-do-not-match.html">Why the size and file count do not match after copying iCloud Drive</a>', '<a href="download-google-drive-folder-mac.html">How to download a Google Drive folder, or Takeout files from an email</a>', '<a href="move-google-photos-to-apple-photos.html">How to move from Google Photos to Apple Photos</a>', '<a href="organise-photos-by-date-mac.html">How to organise photos by date on a Mac</a>']),
 ticks(['<a href="whats-in-a-google-takeout-and-how-to-check-it.html">What is in a Google Takeout, and how to check you have it all</a>', '<a href="google-takeout-json-files.html">What are all those .json files in my Takeout?</a>', '<a href="photo-dates-and-time-zones-explained.html">Photo dates and time zones: why a photo shows the wrong time</a>', '<a href="how-to-tell-if-photos-are-duplicates.html">How to tell if two photos are really duplicates</a>', '<a href="find-duplicate-photos-mac.html">How to find and remove duplicate photos on a Mac</a>']),
 ticks(['<a href="apple-photos-cannot-import-and-duplicate-messages.html">Apple Photos: &ldquo;Cannot Import&rdquo; and duplicate messages</a>', '<a href="photos-not-in-apple-photos.html">How to find which photos are not in Apple Photos yet</a>', '<a href="icloud-photos-stuck-syncing.html">Is iCloud Photos slow, or stuck?</a>', '<a href="apple-photos.html">Moving a large library into Apple Photos</a>']),
 ticks(['<a href="how-to-fix-google-takeout-metadata-mac.html">How to fix Google Takeout metadata on a Mac</a>', '<a href="google-takeout-dates-wrong.html">Why do my Google Takeout photos show the wrong date?</a>', '<a href="find-damaged-photos-mac.html">How to find damaged or unreadable photos</a>', '<a href="old-libraries.html">Rescue photos from an old iPhoto or Aperture library</a>']),
 cta())
page("guides.html", "Guides", "Plain-language guides on Google Takeout, iCloud Drive, Apple Photos, duplicates and photo dates, from the Photo Clinic team.", b, "guides.html")

b = head("About", "About Photo Clinic", "Photo Clinic is a free Mac app and a set of plain-language guides, made by people who got stuck moving a large family photo library.")
b += """<h2>Why it exists</h2>
<p>We set out to move a large family photo library out of Google Photos and into Apple Photos. Dates came out wrong, places and captions went missing, duplicates piled up, iCloud stalled without saying why, and copies of iCloud Drive came out with files missing and no way to see which. Existing tools each solved a piece of it. We built Photo Clinic to solve all of it in one place, and wrote down what we learned.</p>
<h2>What it is</h2>
%s
<h2>Who it is for</h2>
<p>Anyone with a large personal photo library on a Mac who wants to know what they have, get it out of one service, put it into another, or just check that it is safe and complete. You do not need to be technical: every job starts with a preview and says what it will do in plain words.</p>
<h2>How it is made and checked</h2>
%s
<h2>How it is paid for</h2>
<p>The app is free. The website may show advertising to help pay for hosting and development. Ads never appear inside the app, and the app contains no tracking.</p>
<h2>Get in touch</h2>
<p>Questions, problems and ideas are welcome: see <a href="contact.html">Contact</a>.</p>
%s""" % (
 ticks(["A <b>free Mac app</b> (Apple silicon) under the MIT licence. Signed and checked by Apple.", "A growing set of <a href=\"guides.html\">guides</a> that explain the problems in plain words, whether or not you use the app.", "An independent project, not affiliated with Google or Apple."]),
 ticks(["Every change the app makes starts as a <b>preview</b>, and copies are made instead of moving your originals.", "The app has nearly two hundred <b>automated tests</b> that run on every change, using made-up photo libraries, zip files and folders.", "It is tried on real libraries as well as test ones, not only on made-up data.", "Explanations of Apple Photos and iCloud messages say how sure we are. See <a href=\"editorial-policy.html\">how we write</a>."]),
 cta())
page("about.html", "About", "About Photo Clinic: a free Mac app and plain-language guides, made by people who got stuck moving a large family photo library.", b, "about.html")

b = head("Contact", "Contact Photo Clinic", "The best way to reach us is by email. We read everything, and we would like to hear what went wrong.")
b += """<h2>Email</h2>
<p><a href="mailto:thestocksoup@gmail.com">thestocksoup@gmail.com</a></p>
<h2>What helps us help you</h2>
%s
<h2>Found a mistake on this site?</h2>
<p>Tell us the page and what is wrong. We correct errors and note the date on the guide.</p>
<h2>Privacy</h2>
<p>What we do with your email and with visits to this site is in the <a href="privacy.html">privacy policy</a>.</p>
%s""" % (
 ticks(["Which version of Photo Clinic you are using (the number at the top of the app).", "What you were trying to do, and what happened instead.", "Whether it was a preview or a real run.", "If you can, the report the app saved (Past runs shows where). It does not contain your photos."]),
 cta())
page("contact.html", "Contact", "How to contact the Photo Clinic team: questions, problems, ideas and corrections.", b, "contact.html")

b = head("How we write", "How we write and check our guides", "What goes into the guides on this site, how we check them, and how we handle corrections.")
b += """<h2>What we write about</h2>
<p>Only things we have actually run into while moving, copying and checking large photo libraries. We would rather write less and have it be right than write a lot.</p>
<h2>How we check</h2>
%s
<h2>Saying how sure we are</h2>
<p>Apple does not document most of the messages that Photos and iCloud write to their logs. Where we explain one, we say whether it comes from Apple's documentation, from what we observed, or is our best reading. If we are not sure, we say so, and we do not present a guess as fact.</p>
<h2>Corrections and updates</h2>
<p>Each guide shows when it was last reviewed. When something changes, such as a new version of macOS or a change in how Google exports photos, we update the guide and the date. To report a mistake, <a href="contact.html">contact us</a>.</p>
<h2>Advertising</h2>
<p>Ads, if shown, never decide what we write. We do not take payment to recommend anything, and Photo Clinic itself is free.</p>
%s""" % (
 ticks(["Steps are tried on a real Mac, on a real library, before they are written down.", "Numbers in examples come from real runs, with names and paths changed or removed.", "Claims about how other products behave are checked against the product's own documentation where it exists.", "Where the app and the guide disagree, we fix whichever is wrong."]),
 cta())
page("editorial-policy.html", "How we write", "How the Photo Clinic team writes and checks the guides on this site, how sure we are about Apple and Google behaviour, and how we correct mistakes.", b, "editorial-policy.html")

import datetime
_today = datetime.date.today().isoformat()
_pages = ["", "story.html", "how-to-fix-google-takeout-metadata-mac.html", "google-takeout-dates-wrong.html", "google-takeout-json-files.html", "move-google-photos-to-apple-photos.html", "icloud-photos-stuck-syncing.html", "find-duplicate-photos-mac.html", "organise-photos-by-date-mac.html", "copy-icloud-drive-to-external-drive-mac.html", "download-google-drive-folder-mac.html", "photos-not-in-apple-photos.html", "find-damaged-photos-mac.html", "guides.html", "why-icloud-drive-copy-sizes-do-not-match.html", "whats-in-a-google-takeout-and-how-to-check-it.html", "apple-photos-cannot-import-and-duplicate-messages.html", "how-to-tell-if-photos-are-duplicates.html", "photo-dates-and-time-zones-explained.html", "about.html", "contact.html", "editorial-policy.html", "tools.html", "fix-takeout.html", "monitor.html", "problems.html", "tidy.html", "old-libraries.html", "apple-photos.html", "safety.html", "versions.html", "privacy.html"]
import hashlib, json as _json
_lm_file = pathlib.Path(__file__).resolve().parent / "lastmod.json"
try:
    _lm = _json.loads(_lm_file.read_text(encoding="utf-8"))
except (OSError, ValueError):
    _lm = {}
_dates = {}
for _p in _pages:                                  # a page's date changes only when the page itself changed, so Google can trust it
    _f = OUT / (_p or "index.html")
    _h = hashlib.sha1(_f.read_bytes()).hexdigest() if _f.exists() else ""
    if _lm.get(_p, {}).get("hash") != _h:
        _lm[_p] = {"hash": _h, "date": _today}
    _dates[_p] = _lm[_p]["date"]
_lm_file.write_text(_json.dumps(_lm, indent=0, sort_keys=True), encoding="utf-8")
(OUT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join("<url><loc>%s%s</loc><lastmod>%s</lastmod></url>\n" % (SITE, p, _dates[p]) for p in _pages) + "</urlset>\n", encoding="utf-8")
(OUT / "robots.txt").write_text("User-agent: *\nAllow: /\n\nSitemap: %ssitemap.xml\n" % SITE, encoding="utf-8")
(OUT / "ads.txt").write_text("google.com, pub-4156851882993001, DIRECT, f08c47fec0942fa0\n", encoding="utf-8")
(OUT / "style.css").write_text(CSS, encoding="utf-8")
print("built")
