import weechat
import re

SCRIPT_NAME = "matrirc_msgid"
SCRIPT_AUTHOR = "matrirc"
SCRIPT_VERSION = "0.1.1"
SCRIPT_LICENSE = "GPL3"
SCRIPT_DESC = "Prefix incoming matrirc messages with [id] from msgid tag"

def msgid_modifier_cb(data, modifier, modifier_data, string):
    # Match tags, prefix (optional), command, target, and body
    # Format: @tags rest
    if not string.startswith('@'):
        return string

    # Split tags and the rest of the message
    parts = string.split(' ', 1)
    if len(parts) < 2:
        return string

    tags_str, rest = parts[0], parts[1]

    # Extract msgid tag
    msgid_match = re.search(r'[;@]?msgid=([^; ]+)', tags_str)
    if not msgid_match:
        return string

    msgid_raw = msgid_match.group(1)
    # Unescape some common IRC tag characters
    msgid = msgid_raw.replace('\\:', ';').replace('\\s', ' ').replace('\\\\', '\\').replace('\\r', '\r').replace('\\n', '\n')

    # Find PRIVMSG and the body part
    # Group 1: Everything up to and including the target and the following space
    # Group 2: Optional colon before the body
    # Group 3: The body itself
    match = re.search(r'^(.*?\s+PRIVMSG\s+\S+\s+)(:?)(.*)$', rest)
    if match:
        prefix_and_target = match.group(1)
        body = match.group(3)
        # Reconstruct the message with the [id] prefix in the body.
        return f"{tags_str} {prefix_and_target}:[{msgid}] {body}"

    return string

if weechat.register(SCRIPT_NAME, SCRIPT_AUTHOR, SCRIPT_VERSION, SCRIPT_LICENSE, SCRIPT_DESC, "", ""):
    # Register the msgid modifier callback
    weechat.hook_modifier("irc_in_privmsg", "msgid_modifier_cb", "")
