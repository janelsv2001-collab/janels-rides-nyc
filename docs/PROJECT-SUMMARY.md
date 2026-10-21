# Janel's Rides NYC — Project Summary

*Kept for Janel — she'll use this later for GitHub and LinkedIn.*

## The business
- **Name:** Janel's Rides NYC
- **Driver:** Janel Santos — NYC taxi/rideshare driver based in the Bronx (Riverdale area)
- **Service area:** All five boroughs + JFK / LaGuardia / Newark airport trips

## The page
- Mobile-first driver contact & payment page, built 2026-10-20 (dark, taxi-yellow design)
- Opens from a QR code riders scan in the car
- Exported standalone HTML (for GitHub): `janel-s-rides-nyc.html`
- Status: built and reviewed by Janel ("looking pretty good"). **Live** at https://janels-rides-nyc.netlify.app (Netlify, her account, Public — verified 2026-10-20). QR code generated from that URL (janels-rides-nyc-qr.png in the project files).
- Stripe: account fully active (live mode). Payment link "Ride Fare" (customers choose what to pay, min $1.00): https://buy.stripe.com/cNicN6acL6omgKzgK583C00 — wired into the live page's Credit Card and Apple Pay options (verified on the public site 2026-10-20).
- **Updated 2026-10-20:** added (1) a trip estimator — pickup/destination/date/time, a "Plan this trip in Waze" deep link, miles/minutes entry, and an itemized TLC-rate breakdown ($3.00 initial, $3.50/mile, slow-traffic time share, MTA $0.50, improvement $1.00, NYS congestion $2.50, congestion pricing $0.75, LGA pickup +$7, auto rush-hour $2.50 / overnight $1.00, tip options, JFK↔Manhattan $70 flat-fare mode, verified with test trips); and (2) a receipt generator — trip/payment details with auto-summed total and receipt number, rendered as a clean card the rider screenshots or prints (nothing is stored). Exported HTML refreshed the same day.

## Payment links (live on the page)
- Cash App: https://cash.app/$janelSV ($janelSV)
- Venmo: https://venmo.com/u/Janelsantos (@Janelsantos)
- Zelle: janel2098@hotmail.com (shown with a tap-to-copy button)

## Still to add
- **Pay by card:** Stripe payment link ("customers choose what to pay") — Janel creates a free Stripe account, then the link gets wired into the "Pay by card" button already in the layout. Stripe fee: 2.9% + $0.30 per charge.
- **Business phone:** Google Voice number to be created — then Call / Text / WhatsApp buttons (already in the layout as Coming Soon) go live. Her personal number stays off the page.
- **Photo:** her decision pending (photo she sent shows a man next to her Kona — asked whether to include him, crop to the car, or use a solo shot of her).
- **QR code:** generated as soon as the page is published.

## For GitHub / LinkedIn later
- The exported HTML file is self-contained (styles + QR images inlined) — can go straight into a GitHub repo.
- Good LinkedIn framing: a real small-business web project — mobile-first design, payment integrations (Cash App, Venmo, Zelle, Stripe), QR-based customer flow.

## Update — 2026-10-20 evening: redesign, alerts, and quick wins LIVE

The Uber-style rebuild Janel approved ("Yes to all 5") is live on https://janels-rides-nyc.netlify.app and verified end to end:

- Booking flow: "Where to?" card, quick destinations (JFK, LaGuardia, Penn Station, Times Square, Yankee Stadium), Now default with Plan-ahead date/time tucked away, ride list rows with live prices, collapsed price details, no payment-method picker. Confirmation screen carries exactly one payment action — "Pay $XX.XX with Apple Pay" (tries the pre-filled checkout function first, falls back to the Stripe payment link).
- Top map reduced twice at her request: 45% → 28% → 20% of screen height (drag 12–50%, tap toggle 14%/38%).
- Booking alerts ("Add both: email + WhatsApp booking alerts"): rider name + phone required to confirm; every booking POSTs to the Netlify "booking" form; form detection enabled and email notifications switched on to janel2098@hotmail.com. WhatsApp/SMS send buttons + top contact pills are wired to a single CONFIG.BUSINESS_PHONE, empty until her Google Voice number exists.
- Proof: two labeled test bookings (JR-20261020-6455; JR-20261020-1642 with flight AA1234) appear in the Netlify Forms dashboard with every field. No real payments were made.
- Quick wins (her "Yes knock them all"), all live and verified: factual trust strip (★ 5.0 rated driver, All-electric Kona, Quiet & Clean, Airport specialist) — reviews module present but hidden until real rider quotes are supplied, nothing invented; full EN | ES interface toggle with localStorage persistence; optional flight-number field on airport trips flowing into the form, confirmation, receipt, and WhatsApp/SMS message; Open Graph/Twitter link preview with a branded cover at /og-cover.png; Add-to-Home-Screen install bar, manifest, and app icons.
- Still outstanding: Google Voice business number (hers to create; walkthrough delivered), STRIPE_SECRET_KEY Netlify env var (her secure paste; activates pre-filled fares), real rider reviews for the reviews module.
- 2026-10-20 bigger lifts (her "Do the bigger lifts 6 7 and 8"): #6 real address search + live-traffic fares (Google Places/Distance Matrix, key-gated with fallback to the built-in system) and #7 automatic booking texts (a Twilio submission-created Netlify function, inert until she adds Twilio env vars) were built the same evening. #8 custom domain: janelsrides.nyc was AVAILABLE on Porkbun at $26.26/yr (checked 2026-10-20, standard price) — she chose "Hold off on the domain for now"; do not re-pitch it unprompted.
- Deploy packages: janels-rides-nyc-netlify-v7.zip is the current live build.

## Marketing — 2026-10-20

Seatback sign designed and delivered (print-ready PNG + PDF at 300dpi in the project files): dark/amber design matching the site — "ENJOYED THIS RIDE? BOOK ME DIRECT", "Skip the surge…" subline, benefit chips (Upfront fares, Airport trips, Apple Pay, English • Español), big QR to janels-rides-nyc.netlify.app, driver/hours lines, and a Spanish line at the bottom. Concept: convert happy Uber/Lyft passengers into direct pre-booked (especially airport) riders. Optional unprinted booster she hasn't decided on: $5 off a first direct airport ride for riders who mention the sign.

## Update — 2026-10-20 late evening: profile card, pricing tune, print pieces

- **Mini business cards** — delivered the same evening, matching the seatback sign and the site (front + back, standard 3.5×2), print-ready for VistaPrint, Staples, or MOO.
- **Driver profile card (live)** — at her request, her photo on the page now taps open into an expanded card: name "Janel", ★5.0, the black 2023 Hyundai Kona Electric as caption, tap-away to close. The card mirrors her Uber driver profile screenshot with her real combined numbers: plate **T112558C**, **10k+ rides • ★5.0 • 3.4 years**, the safety line, and the Friendly driver section. Verified live on the site 2026-10-20. Car photo: she supplied a real photo of the black Kona for the card; she then asked for a background-removed (car-only) version — in progress at the end of the evening.
- **Pricing retune** — she felt the page's quotes ran higher than Uber, so fares were tuned closer to Uber pricing: per-mile $3.50 → $2.95, slow-traffic time $0.70 → $0.45/min. Everything else kept ($3 start, all city surcharges, airport fees, rush/overnight, $70 JFK flat option, tips). Copy changed with it: the page no longer says "TLC fares" and now says **"Upfront fares — no surge pricing"**. (Old example she saw: Riverdale → JFK quoted ~$156 before the tune.)
- **Pricing sanity check** — she shared two TLC driver-pay PDFs (March 2025 promulgation, June 2025 driver-pay rules); both set what Uber/Lyft must pay *her*, not passenger prices. Page pricing checked out against them (her direct ~$31 vs the ~$29.07 driver-pay floor on a 7.5-mile/30-min trip) and against the NYC taxi meter it mirrors. Noted for the record: the $5 airport access and +$7 LGA pickup are her own add-ons, not TLC line items.

## Update — 2026-10-20 late evening: profile card, fare tune, marketing (v11 current)

- Driver profile card added at her request: tapping the driver photo opens an Uber-style card modeled on her own Uber screenshot — "Janel", "Hyundai Kona EV", large circular photo, black 2023 Kona Electric graphic, plate pill T112558C, safety line, stats 10k+ Rides (her corrected combined Uber+Lyft total) / ★5.0 / 3.4 Years, "What Janel is known for" + Friendly driver card. Fully bilingual.
- Car image finalized the same night: first her real Kona photo as a band, then — at her "without background, just the actual car" — a background-removed cutout (rembg u2netp; the full model OOM-killed on this VM) floating on the dark sheet. Cutout files kept in the project files (kona-cutout.png).
- Fare tune (her choice over keeping the taxi meter, after she compared against Uber and uploaded the TLC driver-pay rule PDFs — which set what apps must pay drivers, not passenger fares): per-mile $3.50 → $2.95, slow-traffic $0.70 → $0.45/min; all surcharges/fees, JFK $70 flat toggle, +$10 Priority, tips unchanged. "TLC fares" copy reworded to "Upfront fares — no surge pricing". Verified live: Penn Station → JFK $89.22 (was ~$101).
- Marketing delivered: seatback sign + mini business cards (front/back, print-ready PNG/PDF in project files), hook "Enjoyed this ride? Book me direct / Skip the surge". Optional $5-off-first-airport-ride booster not yet decided.
- Current live build: janels-rides-nyc-netlify-v11.zip.

## v12 — Bigger driver photo + clearer expand cue (2026-10-21)
At Janel's request ("Make the picture bigger so people can see more clearly that it expands"): the driver-bar avatar grew from 56px to 96px, the expand badge is now a prominent 32px orange badge, and a caption under the photo reads "Tap photo to expand" (ES: "Toca la foto para ampliarla"). Deployed to Netlify as v12 (deploy 6ad904e20e8ca12d1b9e97f6, 2026-10-21 2:30 PM EDT) and verified live: photo/badge/caption render as designed, tapping still opens the profile card (Kona cutout, plate T112558C, 10k+/5.0/3.4 stats) and closes cleanly.

## v13 — "Share this profile" button (2026-10-21)
At Janel's request (she marked the spot on a screenshot): a share pill at the map's top-right — dark pill, orange share icon + outline, mirroring the "Janel's Rides NYC" badge; collapses to an icon-only circle at phone width. Tap opens the native share sheet with the public URL + booking blurb (navigator.share); fallback copies the link with a "Link copied — send it to anyone who needs a ride" toast. ES: "Compartir este perfil". Deployed as v13 (deploy 6ad90dc89f193418b1ac1fe5, 2026-10-21 3:09 PM EDT) and verified live (button placement, copy toast, ES label, v12 photo changes intact).

## v14 — Payment symbol row under the contact buttons (2026-10-21)
At Janel's request: a symbols-only row of the four payment brand tiles (green Cash App $, blue Venmo V, orange card, purple Zelle Z) directly under the Call / WhatsApp / SMS buttons ("Ways to pay Janel"). Each tile leads to its payment — Cash App and Venmo open her payment pages, the card tile opens the Stripe checkout link, and the Zelle tile copies her Zelle email with a confirmation toast (EN/ES). The full "Your usual ways to pay" section below the booking form is unchanged. Deployed as v14 (deploy 6ad90f6ad4e609f2d954895a, 2026-10-21 3:16 PM EDT) and verified live (tile placement, all four destinations, pay section intact, v12/v13 features intact).

## v15 — Bottom nav bar + page cleanup (2026-10-21)
At Janel's request ("make all this things a reacting bottom, name the bottom so people know what it is; clean the page — too much information when it's not needed"; she picked the full scope: receipt, ways to pay, ride extras): a labeled bottom navigation bar is pinned at the bottom — Book a ride · Ride extras · Ways to pay · Receipt (icons + text, highlights the section you're viewing; ES: Reservar / Extras del viaje / Formas de pago / Recibo). The three sections now start tucked behind one-line tap-to-open headers: "Ride extras — Airport trips & big luggage, handled", "Your usual ways to pay — Cash App · Venmo · Apple Pay & Cards · Zelle", "Get a receipt — For a trip you already paid for". Bottom-bar buttons scroll to and open their sections. Verified live after deploy 6ad914eb40b5af9a288495de (2026-10-21 3:39 PM EDT): sections collapsed on load, all expand correctly (Ways to pay shows all rows + Zelle box + both QRs; Receipt form complete; Ride extras card selectable with "· selected" tag + flight field), booking fares live (Riverdale→JFK $118.10 / $128.10 priority), Share button + symbol tiles intact, EN/ES working. Note: the local GitHub export repo's index.html still holds v14 — sync it when the parked GitHub publish resumes.

## v16 — Confirm bar only when booking (2026-10-21)
At Janel's request (she screen-recorded the Confirm bar floating over every section): the "Confirm & Request Janel" bar now belongs to the booking flow only. Hidden entirely while browsing the profile, Ways to pay, or Receipt; appears once a trip is priced (pickup + destination), showing the fare ("Confirm & Request Janel · $XX"); returns when the rider comes back to Book a ride. Deployed as v16 (deploy 6ad91f0664ded8420c598772, 2026-10-21 4:22 PM EDT) and verified live end-to-end (absent on fresh page and in Receipt/Ways to pay with a priced trip; present in booking view at $27.05 Riverdale→Yankee Stadium; bottom nav, Share button, symbol tiles intact).

## v17 — Collapsible Your details, airports-only quick places, Home button (2026-10-21)
Three of Janel's changes in one build: (1) "Your details" is now an expanding section like the others — starts closed ("Name & phone for your pickup"), opens to name/phone (and flight number on airport trips); ES "Tus datos". (2) Quick destinations reduced to the 3 major airports only — JFK, LaGuardia, and NEWLY ADDED Newark (EWR) with its own $5 airport access surcharge; Penn Station, Times Square, Yankee Stadium removed (free-text "Where to?" still accepts any address). (3) A "Home" button (house icon, ES "Inicio") added first in the bottom bar — now five buttons — smoothly scrolling to the very top of the page. Deployed as v17 (deploy 6ad926b30fd14d532cef5436, 2026-10-21 4:55 PM EDT) and verified live: exactly 3 airport rows, Riverdale→EWR priced $129.85 ($141.85 with Priority), Your details expand + Confirm gating works, Home scroll + highlight works, ES labels correct, Confirm-bar gating and Share/tiles intact. (A build-time content critic's claim that the airport reduction hadn't landed was contradicted by the rendered tree, the built-file grep, and this live check.)

## v18 — Entry animation on every page open (2026-10-21)
Janel's idea, her pick ("every time the page opens" over QR-only): an intro splash in the page's map style — amber route line draws from the pickup pin to the destination square while "Janel's Rides NYC" and the tagline "Private rides across New York City" rise in; ~1.5s, then it lifts away and the page staggers in. Pure CSS (no storage flag), so it replays on every open; tapping skips it; reduced-motion visitors skip it entirely. Deployed as v18 (deploy 6ad92b74b002ee69212980d2, 2026-10-21 5:15 PM EDT) and verified live across three reloads (mid-draw frame, full-route frame, tap-to-skip from the first frame) plus a post-intro booking price check (Riverdale→JFK $112.12, all sections intact). Current live version: v18.

## v19 — "Use my current location" pickup option (2026-10-21)
Janel's request ("one last thing today"): a live-location option for pickup. A "Use my current location" button sits under the pickup/destination fields ("Pick up right where you are — we'll ask permission first"). On tap (never on page load) it requests browser geolocation; granted GPS becomes the pickup (coordinate-driven fare/map/route; a known place like an airport keeps its name + airport handling), and the exact coordinates travel with the booking — confirmation, receipt, WhatsApp/SMS summary with a tappable Google Maps link, and a pickup_coords field in the email alert — so Janel can navigate straight to the rider. Denied/unavailable shows a friendly in-flow message and typed pickup works as before. EN/ES complete. Deployed as v19 (deploy 6ad9336b3ce198492b8496d4, 2026-10-21 5:49 PM EDT); verified live: button placement/copy, denied path + message, regression pricing (Riverdale→JFK $112.12), animation + 5-button nav intact. The GRANT path (prompt → allow → GPS-filled pickup) could not be exercised in the automated browser (location blocked, no position provider) — Janel to confirm on her real phone; if it misbehaves she'll report and it gets fixed via artifact.inspect/edit. Current live version: v19.
