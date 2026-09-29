# TODO

What the site is still missing. `CONTEXT.md` § 11 is the same list from the
business side; this one is the build.

## Blocked on Mark

- [ ] **Phone number.** Mark is getting a Google Voice number (2026-09-28).
      `config.extra.phone` is commented out in `config.toml`; uncomment it and
      the footer picks it up. Add it to `contact.md` by hand.
- [x] **Business email on the domain.** *Mark: stay on Gmail for now
      (2026-09-28).* Everything currently points at
      `mechanicalsuperiority@gmail.com`, the address already public at the
      foot of the essay. `mark@mechanicalsuperiority.com` is a better address
      to hand a stranger a drawing package.
- [x] **Photographs of finished work, 6–10, plus one or two in-process.**
      *Received 2026-09-26: five projects, model and build pictures for each,
      held privately in `from-mark/`. Nothing publishes until Mark has
      reviewed the sketches and cleared one customer's pictures.*
      This is the page that converts and the only reason `/work/` does not
      exist yet — an empty Work page in the nav is worse than no Work page.
      The caption pattern is settled: *what it is — what the problem was —
      what was done.*
- [x] **A bio paragraph for About.** *Received 2026-09-26 (resume and a
      paragraph in his own words), held in `from-mark/`; waiting on his review.*
- [x] **Exact legal name** as filed with the Colorado Secretary of State.
      `config.extra.legal_name` says "Mechanical Superiority LLC"; it must
      match the filing exactly, because SAM.gov rejects mismatches.
- [x] **Shop address, or Fort Collins only?** *Fort Collins only; the
      address stays private (2026-09-28).* The structured data in
      `head.html` currently gives the locality with no street address.
- [ ] **The capability statement PDF.** Drop it in `static/` and link it from
      Services and Contact.
- [x] **CAD package(s) he uses** *SolidWorks, and Fusion through Ehpro.*, for the Services page and the capability
      statement.

- [x] **His review of the site sketches.** *Answered 2026-09-28 and built.* Several directions for the home
      page, plus Work, About, Services and Contact, are in `from-mark/sketches/`
      with a page of questions. His answers decide what gets built here.

- [x] **The travel pods with Ehpro.** *Added 2026-09-28 as the first
      project, with Scott at Ehpro's permission.* One picture is held: a
      Thunderbirds F-16 in flight watermarked "Photography by Kevin Clarke",
      which needs the photographer's permission before it can be used.
- [ ] **An introduction video** for the home page. Mark is making one. Put it
      at `static/video/intro.mp4` (H.264 MP4, a minute or two, under about
      25 MB) and uncomment `intro_video` in `config.toml`; the home page shows
      it in place of the photo, with no JavaScript.
- [ ] **UEI and CAGE.** Mark is registering through the Colorado APEX
      Accelerator, and asked to be reminded. They never go on the website
      (his decision); they go on the capability statement. When they exist,
      change "Registration in process" in `templates/government.html`.

## Retiring Ghost

The decision is made: the Ghost site goes. Order matters.

- [ ] Point DNS here and confirm the site answers on the domain — README
      § moving the domain.
- [ ] Only then cancel Ghost. The account also holds the newsletter list;
      **export the members before cancelling**, even if the list is tiny.
      This site has no newsletter, and that is a deliberate loss, not an
      oversight — say so to Mark before the export window closes.
- [ ] `/coming-soon/` and `/about/` existed on Ghost. `/about/` exists here;
      `/coming-soon/` is gone on purpose. Nothing links to it.

## Second pass on the build

- [x] A `/work/` page, the moment photographs exist.
- [ ] `LocalBusiness` structured data is in `head.html` but carries no street
      address or phone. Fill it in when those are settled.
- [ ] Power vs. Torque Pt. 2 is promised in the text of Pt. 1 and has never
      appeared. Pt. 3 is promised in the closing paragraph. Both promises are
      live on the site again now that the essay is.
