## Learning journal

For each lesson record your prediction, observed result, explanation,
one failure, and one change you made independently.

## Experiment log

### 2026-09-27
* **Data Split:** ticket.json
* **Mode:** live
* **Model:** gpt-4.1-mini
* **Change:** first live call
* **Metric:** category
* **Result:** billing 134 in / 21 out, 4442 ms
* **Interpretation:** duplicate invoice routed to billing

### 2026-09-27
* **Data Split:** holdout
* **Mode:** mock
* **Model:** none (keyword rules)
* **Change:** no change
* **Metric:** accuracy
* **Result:** 2/5, 0.4
* **Interpretation:** T6, T7, and T8 missed: "money", "sign in", and "times out" are not the keywords invoice/charged, login, or timeout

### 2026-09-28
* **Data Split:** dev
* **Mode:** live
* **Model:** gpt-4.1-mini
* **Change:** no prompt change
* **Metric:** accuracy
* **Result:** 5/5, 1.0
* **Interpretation:** matched the keyword rules on all five dev tickets; no errors to inspect

### 2026-09-28
* **Data Split:** dev
* **Mode:** live
* **Model:** gpt-4.1-mini
* **Change:** judge by meaning
* **Metric:** accuracy
* **Result:** 5/5, 1.0
* **Interpretation:** no regression on dev; the wording change is still untested on holdout

### 2026-09-28
* **Data Split:** holdout
* **Mode:** live
* **Model:** gpt-4.1-mini
* **Change:** judge by meaning
* **Metric:** accuracy
* **Result:** 5/5, 1.0
* **Interpretation:** fixed the three keyword misses; prompt was written after seeing those tickets, so this is not an unseen test
