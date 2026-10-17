# Harbor: an intake that feels like a first conversation

Suggested blog angle: docassemble can support a distinctive, approachable intake experience while preserving structured data for the next step in a legal services workflow.

## Story outline

1. Start with the welcome screen: a fictional legal aid identity, plain-language expectations, and three concrete steps.
2. Show contact preferences: the form asks for email or phone only when selected, and captures safe-contact instructions.
3. Follow the housing branch: a client's answer changes what comes next. A deadline flags the record for review without promising legal help.
4. Add a fictional document and review: the person can correct their answers before authorizing the next step.
5. Reveal the handoff: the actual entered answers become structured JSON, with a deterministic demo receipt and an explicit simulation label.
6. Close with mobile: the same interview works in a narrow viewport, with stacked cards and readable controls.

## Accurate claims to make

- The screenshots show a running docassemble interview, not static design mockups.
- The adapter uses the answers entered during that session.
- No data is sent to LegalServer. The payload is a demo schema, not a universal LegalServer API format.
- Document metadata is included; uploaded file contents are not transferred.
- Language preference is captured, but the interview itself is English-only.
- Household information is collected, but the demo does not determine eligibility.

## Sample persona

Jordan Rivera, jordan.rivera@example.com, three household members, $2,450 monthly household income. Fictional housing notice and November 5, 2026 hearing. All screenshot data is fabricated.

## Design details

Navy (#142e3a), teal (#14675f), warm paper (#f6f4ee), and a brass accent. Georgia headings pair with system-font body text. No remote font or image services. The stylesheet is loaded by this interview, so it does not reskin other installed interviews.

## Validation

The repository includes unit tests for payload mapping, inactive-field exclusion, consent, and stable references. The Playwright walkthrough captures desktop/mobile images, checks horizontal overflow, exercises upload and blocked consent, and runs housing and non-housing scenarios. This is focused functional verification, not a full accessibility audit.
