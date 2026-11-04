# Next executable milestone — October 31, 2026

## Verified status
The public main branch was documentation only. This branch adds a local Python prototype, not an iPhone app or a deployed gateway. Three automated tests pass (provider mocked): claim validation, timestamp validation, chronological retrieval, evidence integrity, request cap, and failure without saved claims. These tests do not establish image quality, model accuracy, or hardware compatibility.

Official CameraAccess downloaded separately at revision `bbae597cd1c748cd29b9375a1624a8d75b1c9e14`. It is untouched and retains its upstream license. It is not included in this repository. No hardware capture or Xcode build has been verified. This Mac has command-line tools selected and no Xcode application installed. No BASETEN_API_KEY is configured in the execution environment. Earlier chat reported a text response, but that is not a fresh API or vision verification.

## Gate 1: physical iPhone and glasses baseline
Follow the pinned [official sample README](https://github.com/facebook/meta-wearables-dat-ios/blob/bbae597cd1c748cd29b9375a1624a8d75b1c9e14/samples/CameraAccess/README.md). Requirements at that revision: iOS 17.2+, Xcode 26.4+, Swift 6.3+.

1. On Mac: install the required full Xcode, open it and complete first launch; select it in Xcode Settings → Locations → Command Line Tools. Confirm `xcodebuild -version`.
2. Get the official sample separately, preserving its license:
   ```sh
   git clone https://github.com/facebook/meta-wearables-dat-ios.git
   cd meta-wearables-dat-ios
   git checkout bbae597cd1c748cd29b9375a1624a8d75b1c9e14
   open samples/CameraAccess/CameraAccess.xcodeproj
   ```
3. Physical iPhone: unlock, connect to Mac, trust the computer if asked. Enable iOS Developer Mode if requested by Xcode, including its restart/confirmation flow. Select that iPhone as the run destination.
4. Physical glasses/iPhone: charge and power on glasses, unfold and wear them; confirm Gen 2 pairing and connection in Meta AI. Enable glasses Developer Mode in Meta AI (separate from iOS Developer Mode). Use Meta's current device settings guidance if that option is unavailable; do not guess hidden activation taps.
5. On Mac: set your Apple signing team and unique bundle identifier in the CameraAccess target. Keep the sample URL callback, permissions and lifecycle settings intact. Developer Mode does not require Meta app ID/client token. Resolve packages and run on the physical iPhone.
6. On iPhone: tap **Connect**, complete registration in Meta AI and return to CameraAccess. Approve requested Bluetooth/camera access. Record denial behavior before retrying if feasible.
7. Wearing glasses: point at staged keys on a table. On iPhone tap **Start Session**, then **Preview**. Confirm the live image follows the glasses' view by turning your head, then capture a photo. Inspect the photo, including whether the keys are clearly visible. MockDeviceKit does not count as this check.
8. On iPhone: preview/share the captured photo; AirDrop or save it to Mac. Keep its actual capture time with timezone, and export JPEG/PNG if necessary. Do not substitute the transfer time. Keep scenes free of sensitive material.
9. Test **Stop preview → End session → restart**. Background the app and return; at this revision start a fresh session. Test disconnect/reconnect. If prompted use **Update firmware** or **Update app on glasses**, then retry.
10. Log date, exact upstream revision, iPhone model/iOS, glasses firmware, Meta AI version, Xcode version, signing result, first frame, exported capture, background recovery, disconnect recovery, and any error text. Leave untested entries explicitly pending. Never record credentials.

Gate passes only after a real glasses photo is exported and restart works. Do not modify upstream lifecycle code before this baseline.

## Gate 2: minimal evidence memory on Mac
This intentionally uses manual photo export to unblock evaluation before building the iPhone UI. No provider secret goes on the iPhone. Python 3.9+; no third-party packages required. Run from repository root.

Configure a replacement Baseten key privately as `BASETEN_API_KEY` in your terminal/password-manager workflow. The prior chat included an exposed key; do not reuse it. Never paste keys into chat or commit them.

```sh
python3 -m unittest discover -s tests -v
python3 backend/findit.py capture /absolute/path/keys.jpg \
  --captured-at '2026-10-31T13:00:00-07:00' \
  --source RAYBAN_META_CAMERA --allow-cloud
python3 backend/findit.py search keys
python3 backend/findit.py delete-all
```
The timestamp above is illustrative: replace it with the actual capture time. Source is an operator assertion, not authenticated device provenance. Use TEST_IMAGE for fixtures and IPHONE_CAMERA for phone photos.

Each capture explicitly authorizes one image upload to Baseten. A store permits ten attempts total, including failures; delete-all does not reset the budget. At most 4 MiB JPEG/PNG input and 1,500 output tokens per call, 45-second timeout, no automatic retries. This is a request cap, not a dollar cap; check private balance and provider rates before running. Separate stores have separate caps. Signature checks are basic; this is a trusted local CLI, not an internet upload service.

Successful validated results save original bytes, SHA-256, operator-supplied capture timestamp/source, model ID, and model claims in ignored `data/memory`. Claims are MODEL_INFERRED and never auto-upgraded to observed or verified. Original image is the evidence; model confidence is uncalibrated. Search returns historical candidates newest first and current_location UNKNOWN, with an integrity flag. Empty results mean no saved matching claim, not proof an object is absent. delete-all removes managed image files and database rows; it is not secure forensic erasure (SQLite free pages/backups may remain). Local storage is not encrypted by this prototype; use a protected Mac account and FileVault. Do not commit private captures.

Default model is the event-specific `meta-models/muse-spark-open-1026` from prior project instructions. Current [Meta deployment docs](https://dev.meta.ai/docs/muse-spark-open/deploy) list Baseten's general model as `meta-models/muse-spark-open` and standard image_url content parts. If the event ID is unavailable, confirm account entitlement and deliberately pass `--model meta-models/muse-spark-open`; no automatic fallback is performed. Live endpoint entitlement, JSON behavior, and image accuracy remain unverified.

Acceptance: capture keys on table, then on shelf, retaining both timestamps/images; retrieve newest first; query an unseen ring; inspect empty/uncertain output; test malformed/failed provider response without false saved memories. Human review is required to judge whether location claims are supported. A future second pass may only remove claims, not certify them automatically.

## Deadline and scope
[Official Meta event page](https://dev.meta.ai/events/global-hackathon): November 4, 2026, 9 PM Eastern = 6 PM Pacific (standard time). Recheck before submitting.

Oct 31–Nov 1: real CameraAccess baseline and first live Baseten image. Nov 2: staged two-location memory demo and minimal iPhone bridge only if both gates pass. Nov 3: test failures, correction/deletion and record the three-minute demo required by existing project checklist. Nov 4: submission buffer before 6 PM Pacific. Keep original FindIt code distinct from upstream CameraAccess. Defer continuous capture, embeddings, voice invocation, and production hosting. No public deployment or paid infrastructure created.

Remaining blockers: full Xcode installation/signing, physical iPhone/glasses actions, replacement private Baseten credential and vision request, iPhone UI/automatic capture transfer, correction/verification workflow, measured evaluation and final demo. Do not present the manual-export prototype as a complete wearable app.
