# Harbor: docassemble intake demo screenshot gallery

[Source repository](https://github.com/lemmalegalconsulting/docassemble-HarborIntakeDemo) · Built by Lemma Legal Consulting

Nine screenshots from the running localhost interview, using entirely fictional data. Images are hosted in the repository and pinned to the captured commit. This gist supplies an embeddable gallery and reusable captions.

The LegalServer handoff is entirely offline: it maps entered answers into a demo-owned schema, creates a receipt, and sends no network request. It is not a production LegalServer API contract.

## A welcoming first step

Warm paper, navy, and teal give a real docassemble interview a distinctive identity.

![A welcoming first step](https://raw.githubusercontent.com/lemmalegalconsulting/docassemble-HarborIntakeDemo/48abae6b552ffcdad40e3e758a22460c44e4a466/docs/screenshots/01-welcome-desktop.png)

## The same welcome on mobile

Cards stack and the section navigation stays available on a narrow screen.

![The same welcome on mobile](https://raw.githubusercontent.com/lemmalegalconsulting/docassemble-HarborIntakeDemo/48abae6b552ffcdad40e3e758a22460c44e4a466/docs/screenshots/02-welcome-mobile.png)

## Contact on the client’s terms

Choosing email reveals an email field; safe-contact instructions travel with the record.

![Contact on the client’s terms](https://raw.githubusercontent.com/lemmalegalconsulting/docassemble-HarborIntakeDemo/48abae6b552ffcdad40e3e758a22460c44e4a466/docs/screenshots/03-contact-preferences.png)

## Questions that follow the story

The housing follow-up appears only after housing is selected.

![Questions that follow the story](https://raw.githubusercontent.com/lemmalegalconsulting/docassemble-HarborIntakeDemo/48abae6b552ffcdad40e3e758a22460c44e4a466/docs/screenshots/04-housing-branch.png)

## A chance to get it right

Review sections offer edits before the handoff.

![A chance to get it right](https://raw.githubusercontent.com/lemmalegalconsulting/docassemble-HarborIntakeDemo/48abae6b552ffcdad40e3e758a22460c44e4a466/docs/screenshots/05-review.png)

## An explicit handoff

The person authorizes an offline simulation using their actual interview answers.

![An explicit handoff](https://raw.githubusercontent.com/lemmalegalconsulting/docassemble-HarborIntakeDemo/48abae6b552ffcdad40e3e758a22460c44e4a466/docs/screenshots/06-handoff.png)

## A concrete result

The simulated receipt shows the client, routing, and demo reference. No request is sent to LegalServer.

![A concrete result](https://raw.githubusercontent.com/lemmalegalconsulting/docassemble-HarborIntakeDemo/48abae6b552ffcdad40e3e758a22460c44e4a466/docs/screenshots/07-receipt.png)

## From conversation to structured data

The JSON preview exposes the demo mapping, including document metadata and contact preferences.

![From conversation to structured data](https://raw.githubusercontent.com/lemmalegalconsulting/docassemble-HarborIntakeDemo/48abae6b552ffcdad40e3e758a22460c44e4a466/docs/screenshots/08-payload.png)

## The receipt on mobile

The final record remains readable on a small screen.

![The receipt on mobile](https://raw.githubusercontent.com/lemmalegalconsulting/docassemble-HarborIntakeDemo/48abae6b552ffcdad40e3e758a22460c44e4a466/docs/screenshots/09-receipt-mobile.png)

## Blog notes


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
