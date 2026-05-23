# Changelog

## 0.3.0 — 2026-05-22

### Action required

Re-run `matrirc install-irssi --force` after upgrading. The bundled
`matrirc.pl` gained the IRCv3 `msgid` renderer; without the new script
inbound messages won't carry a `[id]` and `!r` replies have nothing to
target.

### Added

- `!r <id> text` replies. matrirc tags inbound matrix messages with a
  3-letter `msgid`; `!r abc text` resolves the short, sets
  `m.in_reply_to` + body fallback, sends.
- `/msg matrirc join <#alias:server | !room:server>` — join by alias
  or room id.
- `/msg matrirc knock <target> [reason]` — knock on invite-only rooms.
- `/msg matrirc ids on|off|toggle|status` — per-connection toggle for
  reply ids. `show_reply_ids` in `config.toml` for the daemon default.
- `/msg matrirc dump <window>` — inspect the reply-id ring.
