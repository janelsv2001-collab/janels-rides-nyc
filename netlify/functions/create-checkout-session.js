// Creates a Stripe Checkout Session for the exact fare amount, so the rider
// never has to type the amount. Requires the STRIPE_SECRET_KEY environment
// variable in the Netlify site settings; until it is set, this returns 501
// and the page falls back to the plain Stripe payment link.
exports.handler = async (event) => {
  if (event.httpMethod !== 'POST') {
    return { statusCode: 405, body: JSON.stringify({ error: 'Method not allowed' }) };
  }
  const key = process.env.STRIPE_SECRET_KEY;
  if (!key) {
    return { statusCode: 501, body: JSON.stringify({ error: 'Payments not configured yet' }) };
  }
  let payload;
  try {
    payload = JSON.parse(event.body || '{}');
  } catch {
    return { statusCode: 400, body: JSON.stringify({ error: 'Bad request' }) };
  }
  const amount = Math.round(Number(payload.amount_cents));
  if (!Number.isFinite(amount) || amount < 100 || amount > 200000) {
    return { statusCode: 400, body: JSON.stringify({ error: 'Invalid amount' }) };
  }
  const site = 'https://janels-rides-nyc.netlify.app';
  const params = new URLSearchParams();
  params.set('mode', 'payment');
  params.set('payment_method_types[0]', 'card');
  params.set('line_items[0][quantity]', '1');
  params.set('line_items[0][price_data][currency]', 'usd');
  params.set('line_items[0][price_data][unit_amount]', String(amount));
  params.set('line_items[0][price_data][product_data][name]', "Ride Fare — Janel's Rides NYC");
  params.set('success_url', site + '/?paid=1');
  params.set('cancel_url', site + '/?paycancel=1');
  if (payload.booking_ref) params.set('metadata[booking_ref]', String(payload.booking_ref).slice(0, 100));
  if (payload.description) params.set('metadata[trip]', String(payload.description).slice(0, 200));

  let resp;
  try {
    resp = await fetch('https://api.stripe.com/v1/checkout/sessions', {
      method: 'POST',
      headers: {
        Authorization: 'Bearer ' + key,
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: params.toString(),
    });
  } catch {
    return { statusCode: 502, body: JSON.stringify({ error: 'Stripe unreachable' }) };
  }
  const data = await resp.json().catch(() => ({}));
  if (!resp.ok || !data.url) {
    return { statusCode: 502, body: JSON.stringify({ error: 'Stripe checkout unavailable' }) };
  }
  return {
    statusCode: 200,
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ url: data.url }),
  };
};
