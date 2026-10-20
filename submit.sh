#!/bin/sh

set -eu

server="${RAJDHANI_SERVER:-coc.apucomputing.in}"
staging="/srv/submissions/coc-rajdhani/staging"
tempdir=$(mktemp -d "${TMPDIR:-/tmp}/coc-rajdhani.XXXXXX")
archive="$tempdir/submission.zip"

cleanup() {
    rm -rf "$tempdir"
}
trap cleanup EXIT HUP INT TERM

username=$(ssh "$server" id -un)
case "$username" in
    *[!A-Za-z0-9._-]* | "")
        printf 'Unsupported server username: %s\n' "$username" >&2
        exit 1
        ;;
esac
archive_name="submission-${username}-$(date -u +%Y%m%dT%H%M%SZ)-$$.zip"

zip -qr "$archive" . \
    -x '.git/*' '.venv/*' 'data/*' 'checks.json' '__pycache__/*' '*/__pycache__/*' '*.pyc' '*.zip'

scp "$archive" "$server:$staging/$archive_name"
ssh "$server" chmod 0644 "$staging/$archive_name"
printf '%s\n' "$archive_name" | \
    ssh "$server" sudo -n -u submitter /usr/local/bin/coc-receive-submission
