# MVP implementation plan
All items are planned, not completed.

1. **Hardware baseline:** run untouched official CameraAccess on the paired iPhone and Gen 2 glasses. Record SDK revision, firmware, iOS, Xcode, and signing setup. Confirm capture, disconnect, and background behavior.
2. **Intentional memory capture:** implement SwiftUI session controls and observation storage, with preview and delete.
3. **Meta model integration:** select a vision-capable Meta model available to this account; add server-held credentials, output validation, bounded retries, and per-session limits.
4. **Retrieval:** object/alias search returns timestamped evidence; allow correction and multiple candidates.
5. **Closed-loop search:** new scan verifies a candidate and distinguishes current evidence from history.
6. **Demo and submission:** record a three-minute walkthrough, publish only consented demo assets, document original contributions and dependency licenses.

## Acceptance scenarios
- Save keys on a table; query later; show correct evidence and timestamp.
- Move keys; old evidence is marked historical; rescan updates the result.
- Two similar objects produce ambiguity, not a fabricated match.
- Never-seen object returns unknown.
- Permission denial/disconnect/backgrounding returns the UI to a recoverable state.
- Offline mode can search saved history; cloud operations fail clearly.
- Delete removes image and corresponding searchable metadata.
- Budget exhaustion prevents additional provider requests.

## Evidence to collect
Use consented staged scenes with at least ten objects, repeated placements, distractors, and absent objects. Record retrieval accuracy, false found rate, end-to-end latency, and estimated cost per capture. Report sample size and failures. Do not claim hardware validation before it has happened.

## Hackathon positioning
Theme: Build for Your World. Provisional solo Indie track.
Highlight memory across time, correction, and verification using Meta models. Clearly distinguish our event work from Meta's pre-existing sample. Review anti-project examples with the organizers if scope becomes a simple image analyzer.
