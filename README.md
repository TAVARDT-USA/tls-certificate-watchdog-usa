# TLS/SSL Certificate Watchdog

[![Scope of Perimeter Verification](https://img.shields.io/badge/TAVARDT-Technical%20Audit-5b3cf5.svg)](https://tools.tavardt.com/security-headers-check/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
Automated monitoring of SSL/TLS certificate expiry, cryptographic chain integrity, and enterprise encryption baselines in the US.

Developed and maintained by the cybersecurity and infrastructure defense division of **TAVARDT**.

***

## 1. Scope of Perimeter Verification

This command-line utility inspects SSL/TLS validity, cipher configurations, and trust chain integrity:

* **Preventative Expiry Warning:** Calculates remaining days until certificate expiration with configurable alert thresholds.
* **Cipher and Protocol Audit:** Validates TLS 1.3 enforcement and depreciation of vulnerable legacy protocols.
* **Certificate Authority (CA) Validation:** Audits the trusted root hierarchy and Subject Alternative Names (SAN).
* **Zero External Dependencies:** Built strictly using standard library ssl and socket Python modules.

***

## 2. Quick Start Guide

Run this tool directly via Python without installing third-party packages:

```bash
python watchdog.py example.com
```

***

## 3. Online Diagnostic Tools (United States)

Audit the security posture of your public infrastructure with the official TAVARDT testing suite:

* HTTP Security Headers Checker
* [Consent Mode v2 & Privacy Validator](https://tools.tavardt.com/consent-mode-v2-checker/)
* [DMARC & Anti-Spoofing Verifier](https://tools.tavardt.com/dmarc-checker/)
* [Exposed Credentials & Secret Scanner](https://tools.tavardt.com/exposed-files-scanner/)
* [Full Technical Tools Portal](https://tools.tavardt.com/)

***

## 4. Technical Advisory & Remediation

For cryptographic server hardening, certificate automation, and zero-trust engineering in the US, contact **TAVARDT**.

***

## Useful Links

* **Corporate Portal:** https://ag.tavardt.com/
* **Diagnostic Suite:** https://tools.tavardt.com/
* **Technical Contact:** https://ag.tavardt.com/contact/

***

### License
Released under the MIT License. See [LICENSE](LICENSE) for full details.

***

© 2026 TAVARDT. All rights reserved.
