# Local message bus (fallback)

The primary channel between roles is the event room, provided by your agent factory. This folder
exists for a **file-driven dry run** where separate sessions are not available.

- `inbox/` — simulated inbound messages. Drop a file from `fixtures/` here and deliver it to the
  owning role.
- `outbox/` — drafts only, never sent.

A message dropped here is not a delivered message unless the receiving session reads it. If you use
this folder instead of real sessions, mark collaboration as untested rather than passed.
