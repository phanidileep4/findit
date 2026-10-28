# FindIt
Visual memory for everyday objects, built for Ray-Ban Meta Gen 2 and an iPhone during the Meta Global AI Developer Hackathon (Oct 26–Nov 4, 2026).

## The experience
Remember where you put your keys, then ask where they were last seen. FindIt will connect an intentional glasses capture to an object, time, and scene description; retrieve evidence later; and guide a fresh search when the object may have moved.

**Status:** planning scaffold. There is no runnable FindIt app or backend yet; device compatibility and model quality still need testing.

## MVP
- User starts a visible capture session and saves an observation.
- A Meta multimodal model extracts object labels and relative scene context.
- iPhone stores observations and lets the user correct them.
- Search returns the best last-seen evidence with timestamp and uncertainty.
- A new scan verifies whether the object is currently visible; a missing match produces an honest unknown.
- Delete individual observations or all local history.

This is a temporal remember → retrieve → verify workflow, intended to go beyond a single-image analyzer or basic RAG demo. Eligibility is determined by organizers.

## Start here
- [Hardware and development setup](docs/SETUP.md)
- [Architecture](docs/ARCHITECTURE.md)
- [MVP milestones and acceptance checks](docs/MVP.md)
- [Hackathon requirements and credits](docs/HACKATHON.md)

## Planned layout
`ios/` SwiftUI companion app; `backend/` model gateway; `docs/` design and setup.
Only documentation is initialized today. Provider keys must stay on the server.

## Official references
- [Participant guide](https://cerebralvalley.ai/e/meta-ai-developer-hackathon/details)
- [Meta Wearables DAT iOS](https://github.com/facebook/meta-wearables-dat-ios)
- [CameraAccess sample](https://github.com/facebook/meta-wearables-dat-ios/tree/main/samples/CameraAccess)
- [Wearables documentation](https://wearables.developer.meta.com/docs/develop/)

CameraAccess is an official sample in the Device Access Toolkit (DAT), not a separate SDK. FindIt original code is MIT licensed; Meta SDK, samples, models, and services retain their own terms. No upstream sample code is vendored here.
