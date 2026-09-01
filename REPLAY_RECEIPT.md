# Replay receipt

Status: **PASS**  
Captured: `2026-09-01T10:58:17Z`  
Role: **post-repair confirmation target**  
Assurance class: **producer-side deterministic replay**

The repaired substantive manifest contains 53 files and has SHA-256
`02ae4230854ef9f6caa49907e94b356ef24ad5686c97b77cf72f0ee6b6cc5e3f`.
The exact inventory plus the manifest and receipt surfaces was extracted under
`/tmp/aim0203-confirm.GnU6TV/replay`; `bash run_all.sh` passed. The captured
replay output has SHA-256
`734713e7ae14e7dd139bb33af2b58d170ad86c9dc213b4f688105b5542349df8`.

The manifest excludes `MANIFEST.sha256`, `REPLAY_RECEIPT.md`, and
`REPLAY_RECEIPT.json` to avoid circular hashing. The outer archive checksum
binds the complete ZIP.

## Results

- 42 fixed-width formula samples passed under normal and optimized Python;
- 16 unit and mutation tests passed under normal and optimized Python;
- theorem-critical LaTeX, Markdown, and claim-scope markers agreed;
- PDF text, complete normalized-text digest, and raw-TeX leakage gates passed;
- `qpdf` structural validation passed;
- all 53 manifest entries were present and matched;
- the package gate and complete read-only replay passed.

## Bound objects

| Object | SHA-256 | Size/detail |
|---|---|---|
| `paper.pdf` | `cfe29bf42f5656aeaa91eb27c3469c2e21c71b17bb6dc9dc0cfc5d4f8bccdd4c` | 125,993 bytes; 9 A4 pages; untagged |
| `paper.tex` | `eb0be745d45f52116f7ad9544f10fb64af83112c80aa4e91c47e325351c21f94` | canonical source |
| `paper.md` | `5d620308a90293642c1743256da5fcce462a579b108b44608754c12b46d1dcee` | accessible-text fallback |
| `MANIFEST.sha256` | `02ae4230854ef9f6caa49907e94b356ef24ad5686c97b77cf72f0ee6b6cc5e3f` | 53 payload entries |

## Extraction convention

- executable: `/opt/homebrew/bin/pdftotext`;
- version: Poppler `pdftotext 26.01.0`;
- command: `pdftotext -layout paper.pdf raw.txt`;
- raw text: 31,307 bytes, SHA-256
  `17a5e285d6323b59d5e70f4e22cf1ce997980b51d46e2eeb66f231b7bca84020`;
- normalization: split on ASCII whitespace, join with one ASCII space, append
  one newline;
- normalized text: 25,838 bytes, SHA-256
  `1ef1c843fe658115f7905b850055b206bbc42bd51a15eb92bd9d7fd2fad517e9`.

This supersedes the pre-editorial 43-file, 8-page, 14-test receipt.

## Claim boundary

The receipt establishes successful producer-side execution, PDF extraction,
and payload completeness only. It is not independent reconstruction,
specialist review, peer review, formal verification, or a novelty certificate.
