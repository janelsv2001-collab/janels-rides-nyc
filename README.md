# Janel's Rides NYC

**Live site:** https://janels-rides-nyc.netlify.app

![Janel's Rides NYC cover](og-cover.png)

A driver-direct booking and payment page for a New York City rideshare driver — **10,000+ completed rides, ★ 5.0 rating** — built so riders can book pre-arranged trips (especially airport runs) and pay the driver directly, with no middleman taking a cut.

## What it does

- **Uber-style booking flow** — "Where to?" pickup/destination card, *Now* vs *Plan ahead* scheduling, live upfront fare per ride option, price breakdown on tap
- **Upfront fare engine** — distance + time pricing with NYC-specific components (congestion surcharges, MTA fee, airport access, JFK/LGA pickups, rush-hour and overnight fees), tuned to real rideshare prices, plus tip options and a receipt generator
- **One-tap payment** — a serverless function creates a **Stripe Checkout session for the exact fare**, so the rider never types an amount; Cash App, Venmo, and Zelle deep links offered alongside
- **Instant booking alerts** — every confirmed booking posts to Netlify Forms and emails the driver the rider's name, phone, trip details, and flight number
- **Driver profile card** — tap-to-expand sheet with driver photo, vehicle, license plate, stats, and a safety line ("always confirm the plate and your driver"), including a background-removed photo of the actual car
- **Fully bilingual** — complete English/Spanish toggle across the whole experience
- **Installable PWA** — add-to-home-screen prompt, web manifest, icons, and Open Graph link previews
- **Print marketing** — matching seatback sign and business cards with a QR code to the live site (see `docs/marketing/`), generated programmatically

## Tech

| Layer | Tools |
|---|---|
| Front end | Single-file HTML / CSS / JavaScript — no framework, custom animated route map |
| Hosting & backend | Netlify (static hosting + serverless Functions in Node.js) |
| Payments | Stripe — Checkout Sessions via API, payment-link fallback |
| Booking intake | Netlify Forms with email notifications |
| Messaging (ready) | Twilio SMS confirmation function — activates when account keys are set |
| Maps (ready) | Google Places + Distance Matrix integration — activates when an API key is set |
| Print & image assets | Python (Pillow, rembg) generator scripts in `scripts/` |

## Product decisions worth noting

- **Privacy by design:** the driver's personal phone number appears nowhere on the page or in this repo. Call/Text/WhatsApp buttons are driven by a single config value that stays empty until a business (Google Voice) number exists.
- **Honest social proof:** the reviews section renders only from real rider quotes — it ships empty and hidden rather than inventing testimonials.
- **Pricing research:** the fare model was rebuilt after reviewing NYC TLC driver-pay rules and comparing against live rideshare quotes; the page advertises "upfront fares — no surge pricing," never meter claims it can't back up.

Full build history and decision log: [`docs/PROJECT-SUMMARY.md`](docs/PROJECT-SUMMARY.md)

## Repository layout

```
index.html                  The complete site (self-contained)
netlify.toml                Deploy + functions config
netlify/functions/          create-checkout-session.js · submission-created.js
icons/, manifest, og-cover  PWA + link-preview assets
assets/                     QR code to the live site · vehicle photo cutout
docs/PROJECT-SUMMARY.md     Build log and product decisions
docs/marketing/             Print-ready seatback sign + business cards
scripts/                    Python generators for the print/image assets
```

## Run it

It's a static site — open `index.html`, or deploy this folder to Netlify. To enable pre-filled Stripe checkout, set a `STRIPE_SECRET_KEY` environment variable in Netlify (the function degrades gracefully to a payment link without it). Twilio and Google Maps keys are optional and activate their features the same way.

## Roadmap

- Business phone number activation (Google Voice) for Call/Text/WhatsApp
- Live-traffic fares via Google Distance Matrix
- **The bigger vision:** turn the driver card into a product for other independent drivers — their own booking page, payment links, and alerts, with the driver keeping 100% of every fare

## About the builder

**Janel Santos Veras** — Bronx-based driver and computer science student at Bronx Community College (CompTIA / cybersecurity track). She designed and directed this project end to end — product, pricing, branding, and road-testing it with real riders — building with an AI pair-programmer (Muse by Meta).

© 2026 Janel Santos Veras
