# Replay receipt

Status: **PASS**  
Captured: `2026-09-01T11:10:56Z`
Role: **public-release payload replay**
Assurance class: **producer-side deterministic replay**

The DOI-bearing public-release manifest contains 55 files and has SHA-256
`d2500a9000574481a39ce036e0482eee19655ec3823f78595b69bbdb04ad9d52`.
The exact inventory plus the manifest and receipt surfaces was extracted in a
newly created host temporary directory; `bash run_all.sh` passed. The captured
replay output, after replacing only unittest's variable
`Ran 16 tests in [0-9.]+s` lines with `Ran 16 tests in <elapsed>s`, has
SHA-256 `fa63902f65b952735acca8c0ae8bb6a7628c07312b7dce6c7a6d91102b6a92bc`.

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
| `paper.tex` | `47930c1c525972b93c7704d901590b2fa1204fc0f8f63d3363f3f0f315391227` | canonical source |
| `paper.md` | `b409448ca63d4e0e0f5456e4e8bd5131c598ec191b72d4cbffb85a94adb75922` | accessible-text fallback |
| `MANIFEST.sha256` | `d2500a9000574481a39ce036e0482eee19655ec3823f78595b69bbdb04ad9d52` | 55 payload entries |

## Extraction convention

- executable: `/opt/homebrew/bin/pdftotext`;
- version: Poppler `pdftotext 26.01.0`;
- command: `pdftotext -layout paper.pdf raw.txt`;
- raw text: 31,375 bytes, SHA-256
  `d9354b9f01d654de16259f9c314661bd39e60987e276d7952f71d7a05d8b0dfe`;
- normalization: split on ASCII whitespace, join with one ASCII space, append
  one newline;
- normalized text: 25,905 bytes, SHA-256
  `38e72f8d56e40e922b32e3b417274270fc50213d36fb0d5e89b606f75f5b0bff`.

This supersedes the pre-editorial 43-file, 8-page, 14-test receipt.

## Claim boundary

The receipt establishes successful producer-side execution, PDF extraction,
and payload completeness only. It is not independent reconstruction,
specialist review, peer review, formal verification, or a novelty certificate.
