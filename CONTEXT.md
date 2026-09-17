# Mechanical Superiority LLC — project context

Everything needed to build or rebuild the website for Mechanical Superiority LLC, plus the business
strategy behind it, so design and copy decisions have the reasoning attached.

Compiled September 2026 from a working session. Anything in `[brackets]` is unknown and must be
supplied by Mark before launch.

---

## 1. Who and what

**Business:** Mechanical Superiority LLC — a one-man design-and-build shop in Fort Collins, Colorado.
**Owner:** Mark Mataczynski. Brother-in-law of Kyle Parker Cunningham, who commissioned this work.
**Domain:** mechanicalsuperiority.com (live, Ghost-hosted).
**Partner shop:** Ehpro Custom Fabrication, LLC — Trinity, Texas. Mark's uncle's business, est. 1979,
large-scale fabrication, already registered for federal work (UEI SS6XWF1KDCU8, CAGE 38WS2,
self-certified Small Disadvantaged Business, past performance in aircraft travel pod refurbishment).

**Capabilities, in Mark's own words:**

> * **CAD Design:** Part design, assemblies, all the way up to full machine design. Can also make
>   drawings. Very well versed in reverse-engineering existing parts, and making models from simple
>   hand drawings.
> * **Small-scale Machining:** Bridgeport knee mill can be used for small precision machining of parts.
> * **Welding:** Simple MIG welding carbon steel, or TIG welding for aluminum and stainless steel. Can
>   do repairs, or welded tube frames, etc...
> * **Plasma Table:** Can cut 2D shapes from sheet metal. Can also use CAD capability to turn a 3D
>   concept into individual pieces for welded assemblies.
> * **Riveted Sheet Metal:** Can design and build for riveted assemblies, which can be a better
>   solution than welding for some applications.
> * **Integrated Capabilities:** One-man shop can integrate the above capabilities to take an idea from
>   napkin-concept to reality.

**Constraint to respect in all copy:** one person, one manual knee mill. This shop does not compete on
volume machining and the site should never imply it does. It competes on design plus build in the
same hands.

---

## 2. Positioning (the thesis behind every page)

**Lead with CAD, not the mill.** The Front Range has dozens of CNC shops that will underbid a
Bridgeport on production parts. Almost none of them can model. Shops routinely turn away the customer
who arrives with a broken part and no drawing, or a sketch and an idea. That refusal is the market.

Three things follow, and the site should express all three:

1. **Design and build under one roof** — the person who drew it is standing at the machine when
   something doesn't fit. No drawing package thrown over a wall.
2. **Drawings from anything** — a worn part, a photo, a napkin sketch becomes a dimensioned,
   manufacturable model. Reverse-engineering is a headline service, not a footnote.
3. **Scale through Ehpro** — work beyond one shop's size goes to a partner with heavy fabrication
   capacity and federal history. Mentioned as capability, never overstated as staff.

**Audiences, in priority order:**
- Other shops (fabricators and welders who need CAD, plasma cutting and machined parts; CNC shops who
  turn away design-and-build requests)
- Local businesses and contractors who need a thing that doesn't exist yet
- Federal, state and municipal buyers evaluating a small vendor
- Blog readers (car and engineering enthusiasts) — the existing audience, worth keeping, not the
  revenue source

---

## 3. Current site state (as fetched September 2026)

Platform: **Ghost 6.x**, hosted (storage.ghost.io asset URLs).

| Page | State |
|---|---|
| Home | Ghost default index. Tagline: "Custom engineering solutions, education for all things mechanical." Lists posts by tag (News, Education, Racing). |
| `/about/` | **Still Ghost's stock boilerplate** about subscriptions and "meet people like you." Actively harmful. |
| `/power-vs-torque/` | The one real essay. Feb 28 2023, ~12 min read, tagged Education + Racing. |
| `/coming-soon/` | Sept 2022 placeholder post, **still published**, second item on the homepage. |
| Navigation | Home, About only. |
| Contact | None, except `mechanicalsuperiority@gmail.com` at the foot of the essay. |
| Services / Work / photos | Do not exist. |

Assets: logo at `/content/images/2022/09/Logo-Avatar-01.png`, header/footer logo
`/content/images/2023/02/logo---header-footer.png`, cover image `/content/images/2022/09/cover-image-1500-2.png`.
Site footer reads "Est. 2022."

**First decision for the build:** stay on Ghost (add Pages, edit theme) or rebuild as a static site?
Ghost already handles the newsletter, membership and post archive, and the essays are the site's main
asset — so unless there's a reason to move, adding Pages and lightly customizing the theme is the
lower-risk path. If rebuilding, the post archive must come along and URLs must be preserved
(`/power-vs-torque/` especially).

---

## 4. Voice

The essay is the best guide, and the voice is a genuine differentiator — no competitor in the region
sounds like a person. In the essay Mark works through the math from first principles, defines his
terms, uses units to make concepts intuitive, calls out sloppy thinking in his industry, and drops in
jokes and mild profanity. It reads as someone who knows the subject cold and is slightly annoyed that
everyone else gets it wrong.

**Rules for the build:**
- Blog and About pages: keep the personality, including the jokes.
- Services, Work and Contact pages: plain, concrete, no marketing adjectives. Federal buyers and shop
  owners read these.
- Never use: "solutions provider," "passionate about," "cutting-edge," "world-class," "synergy."
- Prefer concrete nouns — weldment, bracket, nested plate, knee mill — over abstractions.
- Short sentences. Say the thing.

---

## 5. Site structure to build

Six pages. In Ghost, Services / Work / About / Contact are **Pages**; essays stay as posts.

Navigation order: **Services · Work · Writing · About · Contact**

Housekeeping, do first:
- Unpublish or delete `/coming-soon/`
- Replace the `/about/` boilerplate
- Update site meta description (Settings → General):
  *Custom design and fabrication in Fort Collins, Colorado. CAD, CNC plasma cutting, welding,
  machining, and sheet metal — one shop from concept to finished part.*
- Footer on every page: **Mechanical Superiority LLC · Fort Collins, Colorado** + phone + email
- Move the subscribe box below the fold on the homepage (right for the blog, wrong as the first thing
  a paying customer sees)
- Upload the capability statement PDF, link from Services and Contact

---

## 6. Page copy (ready to use, edit freely)

### Home

**Tagline (replaces current):**

> Design and build under one roof. CAD, machining, welding, and fabrication in Fort Collins, Colorado.

**Opening:**

> Most shops either design things or build them. This one does both, which means the person who drew
> your part is the person standing at the machine when something doesn't fit.
>
> Bring a sketch on a napkin, a worn-out part with no drawing left anywhere, or a full print package.
> It comes back as finished hardware.

**Three blocks:**

> **Design** — Part design, assemblies, and complete machine design. Reverse-engineering of existing
> parts. Production drawings from hand sketches or samples.
>
> **Build** — CNC plasma cutting, MIG and TIG welding, precision machining on a Bridgeport knee mill,
> and riveted sheet-metal assembly.
>
> **Scale** — Teamed with Ehpro Custom Fabrication in Trinity, Texas for work beyond one shop's size —
> heavy fabrication with decades of history and federal past performance behind it.

**CTA:** `Tell me what you're trying to build: [phone] · [email]`

### Services

> ## What this shop does
>
> ### CAD design and drawings
> Part design, assemblies, all the way up to full machine design, plus the drawings to go with them.
> Reverse-engineering is a specialty: bring in a part that broke and has no print, or a sketch on the
> back of an envelope, and it comes back as a dimensioned model you can actually manufacture from.
> Files delivered in native format or as STEP, IGES, DXF, or PDF.
>
> ### Precision machining
> A Bridgeport knee mill handles small precision work — parts, fixtures, modifications, and one-off
> replacements for equipment nobody supports anymore.
>
> ### Welding
> MIG on carbon steel. TIG on aluminum and stainless. Repairs, weldments, welded tube frames, and
> structures built from a drawing or from scratch.
>
> ### CNC plasma cutting
> 2D profiles cut from sheet and plate. Combined with the CAD side, a 3D concept gets flattened into
> individual pieces, nested, and cut as a kit ready to weld — which is often the fastest and cheapest
> way to get from an idea to a welded assembly.
>
> ### Riveted sheet metal
> Design and construction of riveted assemblies. For some applications riveting beats welding
> outright: no heat distortion, no warped panels, and serviceable later. Knowing which method a job
> actually calls for is part of the service.
>
> ### Putting it together
> One shop, all of the above. A concept becomes a model, becomes a cut kit, becomes a welded and
> machined assembly, becomes a finished thing on a truck. No handoffs between four vendors, no drawing
> package thrown over a wall to a shop that never spoke to the designer.
>
> **Typical work:** weldments, frames, brackets, guards, covers, skids, racks and enclosures ·
> trailers, truck bodies and equipment upfits · riveted and welded sheet-metal structures ·
> replacement parts for obsolete equipment · drawing packages for parts that need reproducing.
>
> **Working with other shops:** if you're a shop that's full, missing a capability, or needs a second
> source, call. Overflow work and referrals go both directions.

### Work

Blocked on photos. Six to ten finished pieces, each captioned **what it is — what the problem was —
what was done**, e.g.:

> **Aluminum equipment frame.** Customer had a sketch and a load requirement. Modeled, nested, plasma
> cut, TIG welded, delivered in [X] weeks.

Build the template so captions are short and images carry the page. Include at least one in-process
shot (sparks, a part on the mill, a nested plate) — those read as real where catalog shots don't.

### About

> ## About
>
> Mechanical Superiority is Mark Mataczynski's shop in Fort Collins, Colorado.
>
> [2–3 sentences of background: where he trained, industries worked in — heavy industry and machine
> design come through in the writing — and what made him hang out his own shingle.]
>
> The work here runs from single replacement parts to complete machines. The through-line is that
> design and fabrication happen in the same place, by the same person, which is why a problem found at
> the machine gets solved that afternoon instead of in a week of emails.
>
> The writing on this site is the other half of the same instinct: most mechanical concepts aren't
> actually that complicated, but they're explained badly. [Link to the torque essay.]
>
> [Phone] · [email] · Fort Collins, CO

### Contact

> ## Get a quote
>
> [Phone] · [email]
> Fort Collins, Colorado
>
> **What helps:** whatever you've got. A drawing, a photo of the broken part, a sketch, or just a
> description of what the thing needs to do. Quantity, material if you know it, and when you need it.
> If you don't know the material or the tolerances, that's a normal question and part of what you're
> hiring for.
>
> **Download:** [capability statement (PDF)]

---

## 7. Capability statement (mirror this content on the site)

A one-page PDF exists with this content; keep the site and the PDF in sync.

- **Header:** Mechanical Superiority LLC · Design · Machining · Welding · Plasma Cutting · Sheet Metal
  · Fort Collins, Colorado · mechanicalsuperiority.com
- **Company data:** Colorado LLC · small business · UEI `[pending]` / CAGE `[pending]` · CAD software
  `[TBD]` · partner Ehpro Custom Fabrication, LLC (CAGE 38WS2, UEI SS6XWF1KDCU8)
- **NAICS:** 332710 Machine Shops · 332312 Fabricated Structural Metal · 332322 Sheet Metal Work ·
  332999 Misc. Fabricated Metal · 541330 Engineering Services · 541340 Drafting Services
- **Differentiators:** design and build in the same hands · drawings from anything · prototype and
  low-volume welcome · large-scale partner

---

## 8. SEO and technical notes

- Target phrases: *CAD design Fort Collins*, *custom fabrication Fort Collins*, *CNC plasma cutting
  Northern Colorado*, *reverse engineering parts Colorado*, *TIG welding aluminum Fort Collins*,
  *custom weldments Colorado*.
- "Fort Collins, Colorado" in the footer, the About page, the meta description, and the page titles.
- Preserve `/power-vs-torque/` and all existing post URLs. Redirect anything that moves.
- Add LocalBusiness structured data once the address and phone are confirmed.
- Email on the domain (`mark@mechanicalsuperiority.com`), not Gmail — matters to buyers deciding
  whether to send a stranger a drawing package.
- Keep it fast and light. No hero video, no carousel, no chat widget.
- Accessibility: real alt text on the Work photos (they're the content).

---

## 9. Writing strategy (the blog earns the trust)

Nobody hires a fabricator because of a blog, but plenty of people hire one after reading something and
concluding this person knows what they're doing. The essay is the moat.

- **Finish the Power vs. Torque series.** Parts 2 and 3 are promised in the text of Part 1 and never
  appeared. A promised follow-up that never came is worse than not promising it.
- Shop-adjacent topics pull in customers rather than car enthusiasts: when riveting beats welding, why
  that part failed at the weld, what a drawing actually needs on it before a shop can quote it, how to
  describe a part so you don't get a useless quote.
- Two or three a year is plenty. They don't expire.

---

## 10. Business context the site supports

### Federal contracting track
- Register **Mechanical Superiority LLC** in SAM.gov under the exact name on the Colorado filing (free;
  a few weeks). The UEI and CAGE attach to the entity, so past performance accrues to the company.
- Then: DLA DIBBS (needs CAGE), JCP access via form DD 2345 for export-controlled drawings, SBA
  SubNet, Colorado VSS, Texas ESBD/CMBL.
- Free help: **Colorado APEX Accelerator**, Fort Collins office at CSU Powerhouse Energy Campus Room
  419; counselor John Papile; coloradoapex.org. Ehpro's side: UT Arlington Cross Timbers APEX
  (serves Trinity County).
- CMMC status as of July 13 2026: Phase II (third-party certification) **suspended** pending review;
  Phase I self-assessments and DFARS 252.204-7012 still apply.
- **Chase:** weldments, brackets, frames, guards, enclosures, trailers, truck bodies, drawing packages,
  reverse-engineered and obsolete parts. **Skip:** screws, washers, seals, fasteners, screw-machine
  work, anything needing source approval or production volume.
- Risk to manage: one person means schedule risk. Subcontract under Ehpro for anything with liquidated
  damages; bid alone on small simplified-acquisition buys.

### Current leads (September 2026 — verify on SAM.gov, dates move by amendment)

| Tier | Lead | Due |
|---|---|---|
| Bid alone | Tree Cooler Trailer, USDA Colorado (1240LP26Q0183) | Sept 21 |
| Bid alone | Gun Shield (DoD) | Oct 2 |
| Bid alone | A7 Enclose w/ Frame, Maryland | Oct 1 |
| Bid alone | HRD Shield Enclosure, New York | Oct 6 |
| Bid alone | Bracket, Mounting | Sept 30 |
| Bid alone | Chassis Assembly | Oct 8 |
| Bid alone | Body, Cargo Truck | Sept 28 |
| CAD-led | ATPS Canopy Release Assembly design optimization, Army (MA) | Oct 6 |
| CAD-led | Robotic Sheet Metal Forming RFI (DoD) | Oct 27 |
| CAD-led | Red River Army Depot OIB Modernization CSO (TX) | Sept 30 |
| CAD-led | **Crane Army RASP Basic Ordering Agreement (IN) — highest value; multi-year orders** | Oct 26 |
| Ehpro-led | Trash Racks, Lac qui Parle Dam (USACE St. Paul) | Oct 8 |
| Ehpro-led | MNA Vertical Pump Storage Platform (WA) | Dec 8 |
| Ehpro-led | S-Farm Ventilation Duct & Condensate Supports (WA) | Oct 5 |
| Subcontract | BLM-CO Warehouse Improvement (140L1726R0001) | Oct 23 |
| Subcontract | City of Aurora Sand Creek WRF Gates & Clarifier, via GSE Construction | Sept 30 |

Standing search keywords: fabricate, weldment, bracket, frame, guard, cover, skid, rack, enclosure,
housing, trailer, truck body, sheet metal, riveted, drawing package, technical data package, reverse
engineer, obsolete part. Niche worth a standing search: **aircraft ground support equipment, pods,
shelters, containers and shipping frames** — Ehpro's travel-pod history plus Mark's riveted aluminum.

### Shop-to-shop track
A 58-shop call list exists covering Fort Collins, Loveland, Berthoud, Windsor, Greeley, Longmont,
Boulder, north Denver and Cheyenne. The pitch inverts the obvious one: don't ask CNC shops for
overflow milling — offer them what they lack (design and drawings, plasma cutting and nesting, TIG on
aluminum and stainless, weldment assembly), and ask what they're currently turning away. Offer
referrals both directions. Fabrication and welding shops are better first calls than machine shops.
The site's Services page exists largely to support these calls.

---

## 11. Open items — needed from Mark before launch

- [ ] Phone number and business email
- [ ] Shop address (or "Fort Collins, CO" only, if he'd rather not publish it)
- [ ] Exact legal name as filed with the Colorado Secretary of State
- [ ] CAD package(s) he uses
- [ ] 2–3 lines of past performance: what was built, for whom, roughly when
- [ ] 6–10 photos of finished work, plus one or two in-process shots
- [ ] Bio paragraph for the About page
- [ ] Decision: publish the shop address, or contact-only?
- [ ] Decision: stay on Ghost, or rebuild?

## 12. Related files from the working session

- `Mechanical_Superiority_Capability_Statement.pdf` — one-page capability statement
- `Recommendations_for_Mark.pdf` — the strategy argument in full (CAD-first positioning, pricing,
  federal approach, 90-day plan, risks)
- `Government_Contracting_Brief.pdf` — federal contracting how-to and the original 34 leads
- `Opportunity_Targets_Revised.pdf` — leads re-cut against actual capabilities, in three tiers
- `NoCo_Machine_Shop_Outreach_List.pdf` — 58 shops with phone numbers, angles and a call script
- `mechanicalsuperiority-site-update.md` — the site plan this file supersedes and expands
