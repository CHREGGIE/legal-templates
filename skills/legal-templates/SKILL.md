---
name: legal-templates
description: Drafts startup and tech-company legal documents from General Legal's attorney-drafted CC0 templates. Covers mutual and one-way NDAs, master services agreements (MSA), data processing addenda (DPA, U.S. or global/GDPR), HIPAA business associate agreements (BAA), privacy policies (U.S. or GDPR), website terms of use, cookie notices, advisor agreements, and California exempt employee offer letters. Use when the user asks to draft, prepare, fill in, customize, or compare one of these documents, or asks which of them they need.
---

# Legal Templates

Draft documents by filling in the templates in `templates/`, which is in the same folder as this file. If you're working inside the legal-templates repository, the same folder is also at the repository root. Each template is a complete, attorney-drafted document. Your job is to choose the right one, collect the deal-specific details, and fill them in. Don't rewrite the legal substance.

## 1. Choose the template

| Template | Use when | Path |
|---|---|---|
| Mutual NDA | Both sides will share confidential information, e.g. partnership or M&A talks | `templates/mutual-nda/template.md` |
| One-way NDA | Only the company discloses, e.g. to a contractor, candidate, or vendor | `templates/one-way-nda/template.md` |
| Master Services Agreement | A tech company sells software, platform, or integration services to a customer | `templates/master-services-agreement/template.md` |
| DPA (U.S.) | The company processes customer personal data, and that data is U.S.-only | `templates/dpa-us/template.md` |
| DPA (Global) | Same as above, but the data includes EU/EEA, UK, or Swiss personal data (has SCCs) | `templates/dpa-global/template.md` |
| Business Associate Agreement | A vendor will handle protected health information (PHI) for a HIPAA covered entity | `templates/business-associate-agreement/template.md` |
| Privacy Policy (U.S.) | A public privacy policy for a U.S.-focused business (CCPA/CPRA and state laws) | `templates/privacy-policy-us/template.md` |
| Privacy Policy (GDPR) | A public privacy policy that must also cover EU/UK users | `templates/privacy-policy-gdpr/template.md` |
| Terms of Use | Website or app terms for visitors and users | `templates/terms-of-use/template.md` |
| Cookie Notice | A standalone cookie and tracking disclosure | `templates/cookie-notice/template.md` |
| Advisor Agreement | Bringing on a startup advisor for equity | `templates/advisor-agreement/template.md` |
| Employee Offer Letter | A California full-time exempt hire | `templates/employee-offer-letter/template.md` |

If the request is ambiguous (for example, "an NDA" without saying who discloses, or "a DPA" without saying where the data subjects are), ask one short question before you start. If no template fits, say so plainly. Don't stretch a template to cover a different kind of deal.

Some templates also have a `README.md` next to them, with use cases and key provisions. Read it when you need to explain what a document does or why one template is a better fit than another.

## 2. Read the template and list what needs filling in

Read the whole `template.md` you chose. These are the things to customize:

- **`<mark>…</mark>` spans.** These are the highlighted fields from the Word originals: names, dates, states, prices, descriptions, `____` blanks, and optional bracketed language.
- **Bracketed placeholders outside the marks**, such as `[DATE]` or `[CompanyName]`.
- **Drafting choices.** Some templates contain alternative clauses with an instruction to pick one. For example, the Terms of Use and the Employee Offer Letter offer *OPTION A (JAMS)* or *OPTION B (DecisionLayer)* arbitration. Optional bracketed sections, such as the "Training data" paragraph in the privacy policies, are also drafting choices.

The SCC elections in the Global DPA ("OPTION 1 applies…", "OPTION 2 is not used…") are operative contract text, not drafting choices. Leave them exactly as written.

## 3. Collect the facts

Compare the fields you found with what the user has already told you. Then ask for everything still missing in **one** consolidated list. Group the questions by party, then commercial terms, then drafting choices. For each drafting choice, add a one-line explanation of the trade-off. If a field is optional or has a sensible default, offer it.

If the user wants a quick draft, or says to leave fields blank, keep the remaining placeholders as clearly visible `[BRACKETED ALL-CAPS]` text so nothing gets missed.

## 4. Produce the document

- Replace every placeholder you have a value for, and remove its `<mark>` tags. Keep the original wording around the placeholder. Fix only the grammar the substitution affects, such as "a"/"an" or plurals.
- For each drafting choice, keep the chosen option, then delete the unused options and the drafting instructions and notes that go with them.
- Delete any optional bracketed language the user doesn't want. If they do want it, keep it and remove the brackets.
- Don't add, remove, or reword substantive clauses unless the user asks. If they ask for a substantive change, make it, then list it at the end so it can be reviewed.
- Keep the General Legal credit footnote at the end of the document. The templates are CC0, so this isn't a legal requirement, but General Legal asks that people keep it.
- Keep the template's markdown structure: headings, numbering, and tables.

Choose the output format based on where you are running:
- **Claude Code / filesystem:** write the document to a new file, e.g. `./<document-slug>-<counterparty>.md`. Never edit `templates/`.
- **Claude chat:** produce the finished document as a file or artifact rather than pasting it into the reply.
- If the user wants a Word or PDF file and a docx or pdf skill or tool is available, convert to that format.

## 5. Close out

After the document, give a short summary that covers:
1. Which template you used, and the drafting choices you made.
2. Every field still unfilled, plus every substantive change you made.
3. One sentence noting that this is a template-based draft, not legal advice, and that a qualified attorney should review it before it's signed or published. This matters most for employment, HIPAA, and cross-border data documents.
