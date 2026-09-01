# Replay receipt

Status: **PASS**  
Captured: `2026-09-01T11:10:56Z`
Role: **public-release payload replay**
Assurance class: **producer-side deterministic replay**

The DOI-bearing public-release manifest contains 55 files and has SHA-256
`1cbdb35930c1c3a060a28c808cc947332d58592164e0db7efbdab804f97a39d2`.
The exact inventory plus the manifest and receipt surfaces was extracted in a
newly created host temporary directory; `bash run_all.sh` passed. The captured
replay output, after replacing only unittest's variable
`Ran 16 tests in [0-9.]+s` lines with `Ran 16 tests in <elapsed>s`, has
SHA-256 `0acdb359c9def4be55c172a5a300bed54d2dd3a35808ffae1add806ccd5a18e0`.

The manifest excludes `MANIFEST.sha256`, `REPLAY_RECEIPT.md`, and
`REPLAY_RECEIPT.json` to avoid circular hashing. The outer archive checksum
binds the complete ZIP.

## Results

- 42 fixed-width formula samples passed under normal and optimized Python;
- 16 unit and mutation tests passed under normal and optimized Python;
- theorem-critical LaTeX, Markdown, and claim-scope markers agreed;
- PDF text, complete normalized-text digest, and raw-TeX leakage gates passed;
- `qpdf` structural validation passed;
- all 55 manifest entries were present and matched;
- the package gate and complete read-only replay passed.

## Bound objects

| Object | SHA-256 | Size/detail |
|---|---|---|
| `paper.pdf` | `99237675ba1a60d1ebd538c83a082cadfd39bc0cfbf3a2c8e91bcd6f03a91cc5` | 126,394 bytes; 9 A4 pages; untagged |
| `paper.tex` | `88bc93d6e790c0d49b0e0fde22046d93abb12ec84700c403c4577789d8dd9af0` | canonical source |
| `paper.md` | `b409448ca63d4e0e0f5456e4e8bd5131c598ec191b72d4cbffb85a94adb75922` | accessible-text fallback |
| `MANIFEST.sha256` | `1cbdb35930c1c3a060a28c808cc947332d58592164e0db7efbdab804f97a39d2` | 55 payload entries |

## Extraction convention

- executable: `/opt/homebrew/bin/pdftotext`;
- version: Poppler `pdftotext 26.01.0`;
- command: `pdftotext -layout paper.pdf raw.txt`;
- raw text: 31,375 bytes, SHA-256
  `d9354b9f01d654de16259f9c314661bd39e60987e276d7952f71d7a05d8b0dfe`;
- normalization: decode as UTF-8, apply Unicode NFKC, remove all Unicode
  whitespace and ASCII hyphens, then append one newline;
- normalized text: 20,249 bytes, SHA-256
  `d68586f0b9316b576ab662adbfb38f50994bbd0a359b0a7356c58034e4392d05`.

This supersedes the pre-editorial 43-file, 8-page, 14-test receipt.

## Claim boundary

The receipt establishes successful producer-side execution, PDF extraction,
and payload completeness only. It is not independent reconstruction,
specialist review, peer review, formal verification, or a novelty certificate.
