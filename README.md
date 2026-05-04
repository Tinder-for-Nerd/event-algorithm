# ProMatch Recommendation Algorithm

This project now contains only the Student/Pro recommendation algorithm. The website, React routes, Vite shell, styles, and UI components have been removed.

## Core Flow

Both user types feed into the same engine:

```text
userSignal -> scoreProfiles.js + scoreEvents.js -> recommendationEngine.js
```

The key difference is the scorer weight:

- Student profile scoring gives skill overlap the highest weight at `0.50`.
- Pro profile scoring gives mutual connections the highest weight at `0.40`.

Both modes return:

- ranked profile cards
- ranked event cards
- a 10% exploration slot
- updated ranking after connect, RSVP, or dwell feedback

## Run

Use Node.js 18 or newer.

```bash
npm install
npm run demo
```

If this Windows machine still cannot find global `npm`, use the portable Node already in `.tools`:

```powershell
$env:PATH = "$PWD\.tools\node-v20.12.2-win-x64;$env:PATH"
.\.tools\node-v20.12.2-win-x64\npm.cmd install
.\.tools\node-v20.12.2-win-x64\npm.cmd run demo
```

## Test

```bash
npm test
```

## Main Files

- `src/recommendationEngine.js` - pure algorithm API
- `src/index.js` - public exports
- `src/data/recommendationData.js` - sample profile and event catalog
- `src/features/recommendations/userSignal.js` - signal creation and feedback reducer
- `src/features/recommendations/scoreProfiles.js` - Student/Pro profile scoring
- `src/features/recommendations/scoreEvents.js` - Student/Pro event scoring
- `test/recommendationEngine.test.js` - algorithm checks

## API Example

```js
import { applyFeedback, createUserSignal, getRecommendations } from "./src/index.js";

const signal = createUserSignal("student");
const firstRun = getRecommendations({ signal });
const updatedSignal = applyFeedback(signal, {
  type: "connect",
  profile: firstRun.profileCards[0]
});
const secondRun = getRecommendations({ signal: updatedSignal });
```
