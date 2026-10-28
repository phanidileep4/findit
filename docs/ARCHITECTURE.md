# Architecture proposal
## Data flow
Ray-Ban Meta Gen 2 → DAT camera session → SwiftUI iPhone app → HTTPS model gateway → Meta multimodal model → validated observation → local iPhone store → retrieval and current-view verification.

## Responsibilities
- **iPhone:** explicit session controls, registration/permission handling, frame sampling, resize/compression, encrypted local storage using platform protection, search UI, deletion, and optional spoken results through standard iOS audio routing.
- **Gateway:** holds provider credentials, authenticates the app, validates payload size/type, applies request/time budgets, calls the configured Meta model, validates structured output, and avoids retaining images or logging secrets.
- **Model adapter:** primary Meta Model API; optional Baseten, Modal, or Fireworks adapters only after access is granted and the chosen model's image modality is verified.
- **Memory:** local-first object observations, searchable labels and context. Begin with text/keyword ranking and recency; add embeddings only if evaluation shows a benefit.

## Observation contract
Proposed fields: id, capturedAt, objectLabel, userAlias, sceneContext, localEvidencePath, modelId, provider, evidenceSource, and userConfirmed.
Model confidence is not calibrated probability. Keep model claims separate from user corrections. A result describes a last observation, never a guaranteed current location.

## Verification loop
Retrieve likely evidence → show timestamp and context → request intentional rescan → compare current evidence → report found, not seen, or ambiguous. Track moved-object cases and ask for correction.

## Privacy and failure behavior
Capture only with clear user intent. Keep raw imagery local unless cloud analysis is explicitly enabled; disclose provider processing and retention policies. No face identification, continuous background surveillance, or medical/navigation safety claims.
Handle permission denial, device disconnect, app backgrounding, timeout, budget exhaustion, malformed model responses, and offline mode. Cancellation stops queued uploads. Deletion removes evidence plus indexes.
Gen 2 has no display: results appear on iPhone, with optional audio after device testing. Do not assume custom Hey Meta invocation or unrestricted background capture.

## Decisions before implementation
Pin a tested DAT revision; confirm model ID and modalities; choose a minimal gateway runtime; document provider terms; set a hard server-side request budget before enabling calls. No paid deployments are created by this scaffold.
