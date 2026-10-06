import html, pathlib
OUT = pathlib.Path(__file__).resolve().parent.parent
DL = "https://github.com/daviddef/photoclinic-releases/releases/latest"
NAV = [("fix-takeout.html", "Clean up Takeout"), ("monitor.html", "Monitor"), ("problems.html", "Find problems"), ("tidy.html", "Combine &amp; tidy"), ("apple-photos.html", "Apple Photos"), ("safety.html", "Safety"), ("versions.html", "Versions")]

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
.hero{display:grid;grid-template-columns:1.2fr .8fr;gap:32px;align-items:center;padding:48px 0 16px}
.phead{padding:12px 0 8px;display:grid;grid-template-columns:1.3fr .7fr;gap:32px;align-items:center}
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
.cta{text-align:center;margin-top:56px;padding:32px 20px;background:var(--soft);border:1px solid var(--line);border-radius:22px}
.cta h2{margin-top:0}
.next{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;margin-top:40px;font-weight:700}
.next a{text-decoration:none}
footer{margin-top:48px;color:var(--mute);font-size:14px;text-align:center}
@media (max-width:760px){.hero,.phead{grid-template-columns:1fr}.hero figure,.phead figure{max-width:340px;margin:0 auto}}
"""

def nav(cur):
    items = "".join('<a href="%s"%s>%s</a>' % (h, ' aria-current="page"' if h == cur else "", t) for h, t in NAV)
    return '<nav><div><b><a href="index.html" style="text-decoration:none;color:inherit">Photo Clinic</a></b>%s</div></nav>' % items

def page(fname, title, desc, body, cur=None):
    t = "Photo Clinic" if fname == "index.html" else "%s - Photo Clinic" % title
    doc = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%s</title>
<meta name="description" content="%s">
<link rel="stylesheet" href="style.css">
</head>
<body>
%s
<main>
%s
<footer>
<p>Photo Clinic is free to use, under the MIT licence. It is an independent project and is not affiliated with Google or Apple. Google, Google Photos, Apple, iCloud, iPhone and macOS are trademarks of their owners.</p>
<p><a href="%s">Download</a> &middot; <a href="https://github.com/daviddef/photoclinic-releases">Release notes</a> &middot; <a href="safety.html">Safety</a> &middot; <a href="versions.html">Versions</a></p>
</footer>
</main>
</body>
</html>
""" % (html.escape(t), html.escape(desc), nav(cur), body, DL)
    (OUT / fname).write_text(doc, encoding="utf-8")

def head(kicker, h1, lead, img=None, alt="", cap=""):
    fig = '<figure><img class="shot" src="img/%s" width="620" height="940" alt="%s"><figcaption>%s</figcaption></figure>' % (img, alt, cap) if img else ""
    return '<p class="crumb"><a href="index.html">&larr; Photo Clinic</a></p><div class="phead"><div><p class="kicker">%s</p><h1>%s</h1><p class="lead">%s</p><a class="btn" href="%s">Download for Mac</a></div>%s</div>' % (kicker, h1, lead, DL, fig)

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
<h1>Get your photos <span>out of the shoebox</span></h1>
<p class="lead">Photo Clinic cleans up your Google Photos download, watches over Apple Photos and iCloud, and tells you in plain words what is wrong and what to do about it.</p>
<a class="btn" href="%s">Download for Mac</a>
<p class="note">Free &middot; Apple silicon Macs &middot; signed and checked by Apple &middot; nothing is uploaded</p>
</div>
<figure><img class="shot" src="img/home.jpg" width="620" height="940" alt="The Photo Clinic home screen"><figcaption>The home screen</figcaption></figure>
</section>

<h2>What Photo Clinic does</h2>
<p class="sub">Five jobs, in the order most people need them, and a promise. Choose one to see exactly what it does.</p>
<div class="cards">
<div class="card"><i>&#129529;</i><h3>Clean up your Google Takeout</h3><p>Puts back the dates, places and captions Google strips out, and sorts out the duplicates and clutter.</p><a class="more" href="fix-takeout.html">See how &rarr;</a></div>
<div class="card"><i>&#128200;</i><h3>Monitor your Photos library</h3><p>A reading every 15 minutes shows whether Photos and iCloud are syncing, stalled or erroring.</p><a class="more" href="monitor.html">See how &rarr;</a></div>
<div class="card"><i>&#129658;</i><h3>Find what is not right</h3><p>Reads the hidden Photos and iCloud messages, explains the problem and gives you fixes to try.</p><a class="more" href="problems.html">See how &rarr;</a></div>
<div class="card"><i>&#129513;</i><h3>Combine and tidy</h3><p>Merge libraries, remove copies, review look-alikes and convert old videos, with a health score.</p><a class="more" href="tidy.html">See how &rarr;</a></div>
<div class="card"><i>&#127822;</i><h3>Move to Apple Photos</h3><p>Sends your library in careful batches, oldest first, and waits for iCloud to keep up.</p><a class="more" href="apple-photos.html">See how &rarr;</a></div>
<div class="card"><i>&#128737;&#65039;</i><h3>Safe and private</h3><p>Preview first, copies not originals, undo, and nothing ever leaves your Mac.</p><a class="more" href="safety.html">See how &rarr;</a></div>
</div>

<h2>How it works</h2>
<ol class="steps">
<li><b>Choose your photos.</b> Drop in your Google Takeout zip files or a folder.</li>
<li><b>Look at the preview.</b> It shows what would change. Nothing is touched yet.</li>
<li><b>Press go.</b> Your photos come out fixed, in a new folder, ready for Apple Photos.</li>
</ol>
%s""" % (DL, cta())
page("index.html", "Photo Clinic", "Fix your Google Photos download, check Apple Photos and iCloud, and watch your library's health. Free, private, runs on your Mac.", home)

# ---------------------------------------------------------------- fix takeout
b = head("Clean up your Google Takeout", "Give every photo its story back", "Google keeps the dates, places and captions in separate files and leaves the photos themselves bare. Photo Clinic reads those files and writes everything back.", "easy-fix.jpg", "The Easy fix screen with the five styles", "Easy fix: choose a style, then look at your files")
b += """<h2>What goes wrong in a Takeout</h2>
%s
<h2>What Photo Clinic puts right</h2>
%s
<h2>Dates and places, even when Google has none</h2>
%s
<h2>Choose how careful to be</h2>
<p class="sub">Five styles set every option for you. <b>Balanced</b> is the recommended mix.</p>
<div class="phead" style="padding-top:0"><div>%s</div><figure><img class="shot" src="img/styles.jpg" width="620" height="940" loading="lazy" alt="A table comparing what the five styles turn on and off"><figcaption>All five styles side by side</figcaption></figure></div>
<h2>See it before it happens</h2>
%s
<div class="callout"><b>Good to know.</b> Some old video formats (AVI, MKV, WMV, MPG, MTS) and BMP files cannot hold this kind of information, so those only get their file date fixed.</div>
%s%s""" % (
 ticks(["Every photo shows the day you <b>downloaded</b> it, not the day you took it.", "Locations and captions are missing from the pictures.", "Live Photos arrive split into a picture and a separate video.", "Google's <code>-edited</code> copies sit next to the originals.", "Albums become folders full of duplicate copies.", "Hundreds of <code>.json</code> files clutter the folders, and names get cut off or numbered <code>(1)</code>."], "bad"),
 cards([("Dates, places, captions", "Restored from Google's own files: dates, locations, captions, people and favourites, across many zips and batches."), ("Time zones done properly", "Google stores times in UTC. Photo Clinic writes local time with the right offset, using the photo's location or this Mac's time zone."), ("Live Photos back together", "The picture and its video are paired again so Apple Photos treats them as one."), ("Edited copies matched", "Choose to keep both, keep the edit or keep the original."), ("Albums kept", "One copy of each photo is kept, and the albums are written out as keywords and a list so nothing is lost."), ("Motion Photos", "The video hidden inside a Google Motion Photo is pulled out and saved as a normal MP4.")]),
 ticks(["<b>Missing dates rebuilt</b> from the file name (<code>IMG_20190704_&hellip;</code>, <code>PXL_&hellip;</code>, screenshots), neighbouring photo numbers, the folder name and the file's own time. Each guess has a confidence you can review.", "<b>Places filled in</b> from nearby photos or a GPX track, or guessed from a folder name like <code>Johannesburg</code>. Guesses are labelled as guesses and never replace a real location.", "<b>Place names written in</b> (city, region, country) from an offline list of about 144,000 towns and cities. No internet needed.", "<b>Wrong dates flagged</b>, such as future dates or a year that disagrees with the folder."]),
 ticks(["Every style starts as a <b>preview</b>. Nothing changes until you untick it and press start.", "Compare all five in one table, and save your own settings as a favourite with the star."]),
 ticks(["A <b>pre-flight check</b> tells you what is in your Takeout before anything runs.", "A <b>before-and-after storyboard</b> shows a few of your real photos with what changes in the date, place and caption.", "Your originals are <b>copied, not touched</b>."]),
 cta(), nextlinks(None, ("monitor.html", "Monitor your Photos library")))
page("fix-takeout.html", "Clean up your Google Takeout", "How Photo Clinic restores dates, places, captions, Live Photos and albums in a Google Takeout.", b, "fix-takeout.html")

# ---------------------------------------------------------------- monitor
b = head("Monitor your Photos library", "A reading every 15 minutes", "Big iCloud libraries can take days or weeks to sync, and from the outside it is hard to tell working from stuck. Photo Clinic records how your library is doing and shows the trend, so you do not have to guess.", "photos-health.jpg", "The Photos Health tab showing a verdict, library counts and a trend chart", "Photos Health (sample data)")
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
<h2>When it runs</h2>
%s
<div class="callout"><b>One permission.</b> To read the Photos database, macOS needs you to give Photo Clinic <b>Full Disk Access</b> once. If it is missing, the Photos Health tab says so, names the program and opens the settings page for you.</div>
%s%s""" % (
 cards([("Your library", "Photos and videos (visible, hidden, deleted), albums and how many have been analysed."), ("iCloud's sync backlog", "The size of the queue iCloud works through. It should shrink over time."), ("Errors", "iCloud error counts, and how busy the sync process is."), ("Trends", "A chart for each number, the change over 24 hours, and a warning if the backlog has not moved for hours.")]),
 ticks(["Anything it cannot measure is shown as <b>unknown</b>, not as good or bad.", "A steady heartbeat in the logs is <b>not</b> treated as progress or as a stall.", "<b>Stuck</b> needs all three: the merge has run for hours, the backlog has not moved, and the sync process is busy. Then it tells you to leave the library alone and keep the evidence."]),
 ticks(["<b>While Photo Clinic is open</b>, it takes a reading every 15 minutes. You can leave it in the background.", "<b>A separate background job</b> is optional, so readings continue while the app is closed.", "A <b>full dashboard page</b> adds a gap check against iCloud.com, a by-year breakdown and your own to-do list."]),
 cta(), nextlinks(("fix-takeout.html", "Clean up Takeout"), ("problems.html", "Find what is not right")))
page("monitor.html", "Monitor your Photos library", "Photos Health records how your Apple Photos and iCloud library is doing every 15 minutes and tells you if it is syncing, stuck or erroring.", b, "monitor.html")

# ---------------------------------------------------------------- problems
b = head("Find what is not right", "Photos and iCloud fail quietly", "Photo Clinic reads what they will not tell you and explains it in plain words, with fixes to try. It only looks. It changes nothing.", "check-photos.jpg", "The Check Photos screen", "Check Photos: one tap checks everything")
b += """<h2>One tap for the big picture</h2>
<p class="sub"><b>Check everything for me</b> gives one verdict (healthy, needs attention or problem) from four checks:</p>
%s
<h2>Is it all in iCloud?</h2>
%s
<h2>Reads the messages you never see</h2>
%s
<h2>Fixes, in order</h2>
%s
<div class="callout"><b>Honest about its limits.</b> Apple does not document the Photos database and it changes between macOS versions, so upload counts are a strong hint, not a guarantee. The problem catalogue is a draft: fixes beyond the safe steps are leads to check, and every entry carries a confidence level. Give Apple's servers days, not minutes, before deciding something is permanently stuck.</div>
%s%s""" % (
 cards([("Your library files", "Empty, wrongly named and duplicate files, older formats and look-alike folders."), ("Photos upload progress", "Whether Photos is progressing or stuck, with time left."), ("Photos and iCloud logs", "Problems in the system logs, explained with fixes."), ("This Mac", "Free space, battery, power mode and heat.")]),
 ticks(["<b>Is it all uploaded?</b> Counts what is in Photos and what has reached iCloud, works out your speed and time left, and says so if nothing has moved for about 45 minutes.", "<b>Which photos have not uploaded?</b> Lists each one with its size, date and the likely reason: an empty file, a wrong extension, an unusual type, a huge file or a missing original.", "<b>Did my albums and Live Photos arrive?</b> Compares what you sent with what Photos holds.", "<b>Sync queue and meter.</b> Shows how fast Photos talks to iCloud, and whether iCloud's own queue is shrinking or going round in circles.", "<b>Where is my disk space going?</b> For when Optimise Mac Storage is on but the library is not shrinking."]),
 ticks(["<b>Log issues.</b> Recent Photos, iCloud and crash messages, grouped and explained: a full disk, a full iCloud plan, a dropped network, a sign-in problem, a damaged library, a repair in progress, files Photos refused to import and more.", "<b>Live watch.</b> Streams the messages as they happen, and shows the real file name, date and albums of the photo a message is about, not a long id.", "<b>Look up a photo</b> from an id in a log, or part of a file name.", "<b>Migration receipt.</b> A page you can share: what was done, how complete the metadata is, and what arrived in Photos and iCloud."]),
 cards([("About 160 known problems", "A built-in catalogue with the error codes and messages each one shows, the likely causes, and fixes to try, safest first. Covers iCloud, library, import, disk and drives, permissions and media."), ("17 fix guides", "Step-by-step checklists: iCloud stuck or paused, &ldquo;Unable to Upload&rdquo;, ghost files, a library that will not open, copy error -36, a slow or hot Mac, shared albums and more. Each step says who does it: Photo Clinic, you, or a Terminal command you can copy."), ("Set it up for me", "Where a problem has a matching tool, one button switches to it and sets the options. It always leaves Preview on, never presses Start, and has an undo.")]),
 cta(), nextlinks(("monitor.html", "Monitor"), ("tidy.html", "Combine and tidy")))
page("problems.html", "Find what is not right", "Photo Clinic reads the hidden Photos and iCloud messages, explains problems in plain words and gives fixes to try.", b, "problems.html")

# ---------------------------------------------------------------- tidy
b = head("Combine and tidy", "Get the whole library in order", "Merge folders, remove copies, review look-alikes and clean up. Nothing is deleted without a preview and a way back.")
b += """<h2>Library health score</h2>
<p class="sub">A score out of 100 with a plain list of what is wrong, and a button to the tool that fixes it. It keeps a history so you can see whether your library is getting tidier.</p>
%s
<h2>Combine</h2>
%s
<h2>Clean up</h2>
%s
<div class="callout"><b>You stay in control.</b> Every one of these starts as a preview, copies by default, can be stopped, and can be undone from the Past runs tab.</div>
%s%s""" % (
 ticks(["Duplicate files, and the same file saved in several formats.", "Empty (0-byte) files, wrongly named files, temporary and leftover files.", "Look-alike folders, such as <code>Japan 2025</code> and <code>delete-Japan 2025</code>.", "Old video formats, and files only in iCloud Drive that are not on this disk.", "Photos with no date, and an estimate of the space you could win back."]),
 cards([("Merge folders", "Combine libraries into one. Same-name folders are merged, and exact copies are dropped."), ("Review look-alikes", "The same photo at different sizes or re-saved. Shown side by side with a suggested keeper. Never deleted automatically."), ("Keeper rules", "Choose which copy to keep: favourite, edited, resolution, size, metadata, album. Bursts are kept by default."), ("Compare libraries", "See how alike two libraries are and which copy a merge would keep, before you merge.")]),
 cards([("Convert old videos", "Turn old formats into MP4. Each conversion is verified before the original is replaced."), ("Junk and empty folders", "Clear leftover files and empty folders, and tidy odd names."), ("Blurry and screenshots", "Spot blurry pictures and screenshots so your keeper rules can prefer the sharp one."), ("Smart folder consolidation", "Fold look-alike folders together safely.")]),
 cta(), nextlinks(("problems.html", "Find what is not right"), ("apple-photos.html", "Move to Apple Photos")))
page("tidy.html", "Combine and tidy", "Merge libraries, remove duplicates, review look-alike photos, convert old videos and get a library health score.", b, "tidy.html")

# ---------------------------------------------------------------- apple photos
b = head("Move to Apple Photos", "Send it slowly, safely", "Importing a huge library all at once can fill your Mac and confuse iCloud. Photo Clinic sends it in careful batches and waits for iCloud to keep up.")
b += """<h2>How it sends</h2>
%s
<h2>Waiting for iCloud</h2>
<p class="sub">Between batches it waits so Photos can upload. You choose how:</p>
%s
<h2>Before you start</h2>
%s
<div class="callout"><b>Photos has no undo for imports</b>, and Photo Clinic cannot take photos back out of Photos. That is why it starts with a preview and a small test. Keep your finished library and your Takeout until you have checked everything in Photos and iCloud.</div>
%s%s""" % (
 ticks(["<b>Batches of about 2 to 50&nbsp;GB</b>, oldest first, so your timeline fills in order.", "A Live Photo's picture and video always travel together.", "Folders that are albums become Photos albums.", "Photos skips what it already has, so running it again never duplicates.", "Files Photos cannot import (such as AVI, MKV, WMV) are listed and left out. Convert them first."]),
 cards([("Until it reaches iCloud", "The default. Reads the Photos database to see each batch uploaded, and can make batches smaller or bigger depending on how iCloud keeps up."), ("Until there is room", "Waits until your Mac has the free space you choose."), ("Pause for me", "Stops between batches and waits for you to press Continue."), ("Do not wait", "Sends the next batch straight away.")]),
 ticks(["In Photos, turn on <b>iCloud Photos</b> and choose <b>Optimize Mac Storage</b>.", "<b>Preview</b> first, then <b>send a small test of 20 photos</b> and look at it in Photos.", "Leave Photos open and the Mac awake.", "Short of space? Build the library on an <b>external drive</b>.", "The first time, macOS asks if Photo Clinic may control Photos. Allow it."]),
 cta(), nextlinks(("tidy.html", "Combine and tidy"), ("safety.html", "Safe and private")))
page("apple-photos.html", "Move to Apple Photos", "How Photo Clinic sends a large library to Apple Photos in careful batches and waits for iCloud.", b, "apple-photos.html")

# ---------------------------------------------------------------- safety
b = head("Safe and private", "Built so you can trust it with your only copy", "Your photos are the one thing you cannot get back, so everything here is built around not hurting them.")
b += """<h2>Safe</h2>
%s
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
 ticks(["<b>Preview first, always.</b> Every run starts as a preview showing exactly what would change.", "<b>Copy by default.</b> Your originals stay where they are unless you choose otherwise.", "<b>Stop and undo.</b> Stop any job, and put everything back from a copy or move run with one click.", "<b>Reports and logs</b> of every run, and a one-tap diagnostic summary if you need help.", "<b>Faulty drives handled.</b> Copying waits, retries and carries on where it stopped."]),
 ticks(["It runs on your Mac. <b>No account, nothing uploaded, nothing phones home.</b>", "The app can only be reached from your own computer.", "Checks read a <b>copy</b> of Photos' database, never the original. Sending photos to Photos goes through Photos' own import."]),
 ticks(["<b>Full Disk Access</b> to read the Photos database for the checks and the monitor.", "<b>Photos control</b> if you use the send-to-Photos step.", "macOS asks the first time, and the app explains what to do if it is missing."]),
 ticks(["It reads the <b>Photos library and its database</b>, which belong to another app, to count uploads and check sync.", "It reads <b>any folder you choose</b>, including whole drives and Takeout zips.", "It reads the <b>system log</b> to explain Photos and iCloud problems.", "It <b>controls Photos</b> to import in batches.", "It runs helper programs (ExifTool and ffmpeg) to read and write photo details and convert video."]),
 cta(), nextlinks(("apple-photos.html", "Move to Apple Photos"), None))
page("safety.html", "Safe and private", "How Photo Clinic keeps your photos safe: preview first, copies by default, undo, and nothing leaves your Mac.", b, "safety.html")


# ---------------------------------------------------------------- versions
REL = "https://github.com/daviddef/photoclinic-releases/releases/tag/"
def release(ver, date, tag, note, items, latest=False):
    badge = ' <span class="badge">Latest</span>' if latest else ""
    return '<section class="rel" id="v%s"><div class="relhead"><h2>%s%s</h2><span class="reldate">%s</span></div><p class="sub">%s</p>%s<p><a href="%s%s">Download and release notes on GitHub &rarr;</a></p></section>' % (ver, ver, badge, date, note, items, REL, tag)

b = head("Versions", "What is new in each version", "Every release, newest first. The app tells you when an update is ready, so you never have to check.")
b += release("1.0.1", "6 October 2026", "v1.0.1", "Shoebox becomes Photo Clinic, and the monitor moves into the app.", ticks([
  "<b>New name.</b> Shoebox is now Photo Clinic, with a new app id. macOS will ask again for Full Disk Access, Photos and Automation the first time you open it.",
  "<b>Photos Health tab.</b> A reading every 15 minutes while the app is open, with trends and a plain verdict: healthy, downloading, merging, waiting on sync, errors or stuck.",
  "<b>Tells you when macOS is blocking it.</b> If a permission is missing, it names the program, shows since when, and opens the settings page for you.",
  "<b>Check Photos remembers.</b> The iCloud queue check now compares against the Photos Health history, so you no longer have to wait hours between two taps.",
  "<b>A calmer header.</b> An arrow between where your photos come from and where they go, and a star icon for favourites.",
  "<b>A simpler five-styles table.</b> It opens showing only what differs between the styles.",
  "<b>Clearer updates.</b> The update banner now says why an update was refused, for example when a job is still running."]), latest=True)
b += release("1.0.0", "5 October 2026", "v1.0.0", "The first signed and notarised release, published under the name Shoebox.", ticks([
  "<b>Fix a Google Takeout:</b> dates, places, captions, people and favourites restored from Google's files, read straight from zips, with time zones, Live Photos, edited copies, albums and Motion Photos handled.",
  "<b>Dates and places from every clue:</b> file names, folders, neighbouring photos and GPX tracks, plus offline place names for about 144,000 towns and cities.",
  "<b>Combine and tidy:</b> merge folders, remove exact copies, review look-alikes, convert old videos to MP4 with verification, and a library health score.",
  "<b>Check Apple Photos and iCloud:</b> upload progress, log reading, live watch, a sync meter, a disk-space check, about 160 known problems and 17 step-by-step fix guides.",
  "<b>Move to Apple Photos</b> in batches, oldest first, waiting for iCloud between batches.",
  "<b>Five styles</b> from Safest to I like risk, preview first, copy by default, stop and undo, reports for every run."]))
b += '<div class="callout"><b>Updating.</b> The app checks for updates and shows a banner when one is ready. The packaged Mac app asks you to download the newest version from the <a href="%s">downloads page</a> and replace the old one.</div>' % DL
b += cta()
page("versions.html", "Versions", "Every Photo Clinic release, newest first, with what is new in each.", b, "versions.html")

(OUT / "style.css").write_text(CSS, encoding="utf-8")
print("built")
