// Netlify invokes a function named "submission-created" after every form
// submission on the site. This one texts the rider an automatic booking
// confirmation (and optionally texts Janel) via Twilio.
//
// Inert until these environment variables are set in Netlify site settings:
//   TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_FROM_NUMBER
// Optional: JANEL_PHONE (E.164) to also text Janel a copy.
// With any required var missing it returns 200 and does nothing, so form
// processing is never affected.
exports.handler = async (event) => {
  const done = (msg) => ({ statusCode: 200, body: JSON.stringify({ ok: true, msg }) });

  const sid = process.env.TWILIO_ACCOUNT_SID;
  const token = process.env.TWILIO_AUTH_TOKEN;
  const from = process.env.TWILIO_FROM_NUMBER;
  if (!sid || !token || !from) return done('twilio not configured');

  let payload;
  try {
    payload = JSON.parse(event.body || '{}');
  } catch {
    return done('unparseable event');
  }
  if (payload.form_name && payload.form_name !== 'booking') return done('not a booking');

  const d = payload.data || {};
  const name = (d.rider_name || 'there').toString().trim() || 'there';
  const phoneRaw = (d.rider_phone || '').toString().replace(/[^\d]/g, '');
  if (!phoneRaw) return done('no rider phone');

  const to = phoneRaw.length === 10 ? '+1' + phoneRaw : '+' + phoneRaw;
  const when =
    (d.when_type || '').toString().toLowerCase() === 'now'
      ? 'as soon as possible'
      : (d.pickup_datetime || 'your scheduled time').toString();
  const total = d.total ? '$' + d.total : '';
  const flight = d.flight_number ? ` Flight ${d.flight_number}.` : '';

  const riderBody =
    `Janel's Rides NYC: Hi ${name}, your booking request is in (Ref ${d.booking_ref || ''}). ` +
    `${d.pickup || ''} to ${d.destination || ''}, ${when}. ${total ? 'Total ' + total + '. ' : ''}` +
    `${flight} Janel will text you shortly to confirm.`;

  const auth = Buffer.from(sid + ':' + token).toString('base64');
  const sendSms = async (toNumber, body) => {
    const params = new URLSearchParams({ From: from, To: toNumber, Body: body });
    const resp = await fetch(
      'https://api.twilio.com/2010-04-01/Accounts/' + sid + '/Messages.json',
      {
        method: 'POST',
        headers: {
          Authorization: 'Basic ' + auth,
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: params.toString(),
      }
    );
    return resp.ok;
  };

  try {
    await sendSms(to, riderBody);
    const janelPhone = process.env.JANEL_PHONE;
    if (janelPhone) {
      const janelBody =
        `New booking ${d.booking_ref || ''}: ${name} (${d.rider_phone || ''}), ` +
        `${d.pickup || ''} to ${d.destination || ''}, ${when}, ${total}.${flight}`;
      await sendSms(janelPhone, janelBody);
    }
    return done('texts sent');
  } catch {
    // Never fail the form pipeline because of a texting error.
    return done('texting error (ignored)');
  }
};
