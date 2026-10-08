# TODO

What the site is still missing. `CONTEXT.md` § 11 is the same list from the
business side; this one is the build.

## Blocked on Mark

- [x] **Phone number.** *970-587-3271, Google Voice (2026-10-08).* In
      `config.toml` as `phone` (shown) and `tel` (dialled): the footer, the
      closing ask, Gov. Customers and the structured data read it.
      `contact.md` carries it by hand.
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

- [x] **The travel pods with EhPro.** *Added 2026-09-28 as the first
      project, with Scott at EhPro's permission.* The Thunderbirds F-16 in
      flight watermarked "Photography by Kevin Clarke" stays off the site.
      *2026-09-30:* a different in-flight Thunderbirds picture, with no
      credit on it, took its place (`pods-thunderbirds-flight`). Who took it
      is not recorded; confirm with Mark that it is his, EhPro's or an Air
      Force release before the site goes live. *2026-10-08: Mark doesn't
      know who took it and has no permission, so it is off the site and out
      of `static/`. The pods page shows five pictures.*
- [x] **His notes on the built site.** *Applied 2026-09-30:* his own words
      on Home, About, Gov. Customers, Replacement parts, Remote CAD ("Need
      design help?"), the travel pods and the tractor frame. He is "Mark"
      everywhere except the Gov. Customers point of contact, and controls
      engineering is no longer advertised. He has not yet read the third
      offer on the home page (aluminum and stainless), because the report's
      screenshot cut it off.
- [ ] **An introduction video** for the home page. Mark is making one. Put it
      at `static/video/intro.mp4` (H.264 MP4, a minute or two, under about
      25 MB) and uncomment `intro_video` in `config.toml`. It shows in its own
      band after the three offers, where the travel pods band was until Mark
      took it out (2026-10-08); the hero keeps the clouds photo. No
      JavaScript.
- [x] **His second round of notes** *(2026-10-08)*: answers to the four
      questions, the phone number, and his words on Services, the four
      smaller Work projects, the home page's lower half, the closing ask and
      Contact. Open from it: the home page calls the third offer "Specialty
      fabrication jobs: aluminum and stainless" while Services keeps
      "Aluminum and stainless, made small" (both his); and About says "Near
      Fort Collins, CO" and Contact now does too, while the footer and the
      home page say "Fort Collins, Colorado".
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
