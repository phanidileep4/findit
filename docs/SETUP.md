# Development setup
## 1. Get the planning repo
```sh
git clone https://github.com/phanidileep4/findit.git
cd findit
```
No FindIt build command exists yet.

## 2. Establish the official hardware baseline
Use a Mac, Apple development signing, a physical iPhone, the Meta AI companion app, and paired Ray-Ban Meta Gen 2 glasses. Confirm current supported firmware/device requirements in the [DAT docs](https://wearables.developer.meta.com/docs/develop/).

Clone the official SDK separately:
```sh
git clone https://github.com/facebook/meta-wearables-dat-ios.git
cd meta-wearables-dat-ios
git rev-parse HEAD
open samples/CameraAccess/CameraAccess.xcodeproj
```
Record the revision before making changes. Follow that revision's [sample instructions](https://github.com/facebook/meta-wearables-dat-ios/blob/main/samples/CameraAccess/README.md); the current sample specifies iOS 17.2+, Xcode 26.4+, and Swift 6.3+.

Configure your signing team and unique app identifier in Xcode. On iPhone, enable Apple Developer Mode if required for deployment. Separately enable glasses Developer Mode inside Meta AI. The sample's developer-mode flow does not require Meta app credentials; other release channels do.
Run on the iPhone, complete Connect registration, then start a session and preview. Test a capture and clean shutdown. Returning from the background requires a new session in the current sample.
Use the sample's update controls if firmware or the glasses component is outdated.

## 3. Build FindIt after baseline succeeds
Create a SwiftUI app under ios/ and add DAT through Swift Package Manager from the official repository, pinning the tested version. Preserve required registration, URL callback, permission descriptions, and lifecycle configuration from the matching official guidance. Do not copy upstream code without retaining its applicable license.
Keep signing overrides and secrets untracked. Add a local configuration example only when actual app settings exist.

## 4. Model access
Select an available Meta vision model and verify its current API documentation. Build a server-side gateway before entering any provider keys. Configure credentials outside source control; never embed them in the iPhone app.
Test with a staged, non-sensitive image before glasses integration. Enable bounded requests only after verifying the provider balance and billing behavior.

## Troubleshooting checklist
Pairing visible in Meta AI; developer mode enabled in the correct place; physical iPhone selected; signing valid; registration returned to the app; permissions granted; supported firmware and pinned SDK compatible.
First reproduce problems in the unmodified sample, then isolate FindIt changes. MockDeviceKit can support development but cannot establish real hardware compatibility.

## Terms
Review [DAT developer terms](https://wearables.developer.meta.com/terms) and [acceptable use](https://wearables.developer.meta.com/acceptable-use-policy) before SDK use. SDK analytics and crash reporting have separate opt-out settings documented in its README.
