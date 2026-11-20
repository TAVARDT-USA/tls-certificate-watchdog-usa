# TLS/SSL Certificate Watchdog | TAVARDT USA

[![TLS Watchdog](https://img.shields.io/badge/Security-TLS%20Watchdog-5b3cf5.svg)](https://tools.tavardt.com/)
[![Regulatory Compliance](https://img.shields.io/badge/Region-USD-00C853.svg)](https://ag.tavardt.com/)

Automated TLS/SSL certificate monitoring, modern cipher auditing, and NIST SP 800-52r2 compliance for US infrastructure.

Maintained by the infrastructure resilience and cybersecurity division at [TAVARDT USA](https://ag.tavardt.com/).

---

## 1. Capabilities

* **Expiration Watchdog:** Computes real-time days until SSL/TLS certificate expiry with configurable warning thresholds.
* **Cipher Suite Inspection:** Detects deprecated TLS versions (TLS 1.0/1.1) and verifies forward secrecy support.
* **Certificate Authority Validation:** Audits issuing CA identity and chain validity.
* **Zero External Dependencies:** Built with native Python `ssl` and `socket` modules for seamless integration into CI/CD pipelines, cron jobs, and server health checks.

---

## 2. Quick Start

Execute directly via Python without installing third-party packages:

```bash
python watchdog.py example.com
```

---

## 3. Online Diagnostic Suite

For comprehensive vulnerability scanning, DNS verification, and technical audits, visit our localized tools portal:

* [Online HTTP Security Headers Checker](https://tools.tavardt.com/security-headers-check/)
* [Exposed Secret & Credential Scanner](https://tools.tavardt.com/exposed-files-scanner/)
* [DMARC & Anti-Spoofing Verifier](https://tools.tavardt.com/dmarc-checker/)
* [Full Diagnostic Portal](https://tools.tavardt.com/)

For professional remediation and cybersecurity advisory, contact [TAVARDT USA](https://ag.tavardt.com/contact/).
