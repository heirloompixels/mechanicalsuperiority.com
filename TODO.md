# TODO

What the site is still missing. `CONTEXT.md` § 11 is the same list from the
business side; this one is the build.

## Blocked on Mark

- [ ] **Phone number.** The site ships with email only. `config.extra.phone`
      is commented out in `config.toml`; uncomment it and the footer and
      Contact page pick it up.
- [ ] **Business email on the domain.** Everything currently points at
      `mechanicalsuperiority@gmail.com`, the address already public at the
      foot of the essay. `mark@mechanicalsuperiority.com` is a better address
      to hand a stranger a drawing package.
- [ ] **Photographs of finished work, 6–10, plus one or two in-process.**
      This is the page that converts and the only reason `/work/` does not
      exist yet — an empty Work page in the nav is worse than no Work page.
      The caption pattern is settled: *what it is — what the problem was —
      what was done.*
- [ ] **A bio paragraph for About.** The page currently runs without the
      background paragraph rather than shipping `[brackets]`.
- [ ] **Exact legal name** as filed with the Colorado Secretary of State.
      `config.extra.legal_name` says "Mechanical Superiority LLC"; it must
      match the filing exactly, because SAM.gov rejects mismatches.
- [ ] **Shop address, or Fort Collins only?** The structured data in
      `head.html` currently gives the locality with no street address.
- [ ] **The capability statement PDF.** Drop it in `static/` and link it from
      Services and Contact.
- [ ] **CAD package(s) he uses**, for the Services page and the capability
      statement.

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

- [ ] A `/work/` page, the moment photographs exist.
- [ ] `LocalBusiness` structured data is in `head.html` but carries no street
      address or phone. Fill it in when those are settled.
- [ ] Power vs. Torque Pt. 2 is promised in the text of Pt. 1 and has never
      appeared. Pt. 3 is promised in the closing paragraph. Both promises are
      live on the site again now that the essay is.
