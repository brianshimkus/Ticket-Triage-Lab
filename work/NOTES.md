# Learning journal

For each lesson record your prediction, observed result, explanation,
one failure, and one change you made independently.

## Interview evidence

Problem:
My contribution:
Input to output:
Alternative considered:
Failure and fix:
Measured result and sample size:
Limitation:
Next experiment:

## Experiment log

Date | Data split | Mode | Model | Change | Metric | Result | Interpretation

2026-09-27 | ticket.json | live | gpt-4.1-mini | first live call | category | billing, 134 in / 21 out, 4442 ms | duplicate invoice routed to billing

2026-09-27 | holdout | mock | none (keyword rules) | no change | accuracy | 2/5, 0.4 | T6, T7, and T8 missed: "money", "sign in", and "times out" are not the keywords invoice/charged, login, or timeout

2026-09-28 | dev | live | gpt-4.1-mini | no prompt change | accuracy | 5/5, 1.0 | matched the keyword rules on all five dev tickets; no errors to inspect

2026-09-28 | dev | live | gpt-4.1-mini | judge by meaning | accuracy | 5/5, 1.0 | no regression on dev; the wording change is still untested on holdout

2026-09-28 | holdout | live | gpt-4.1-mini | judge by meaning | accuracy | 5/5, 1.0 | fixed the three keyword misses; prompt was written after seeing those tickets, so this is not an unseen test
