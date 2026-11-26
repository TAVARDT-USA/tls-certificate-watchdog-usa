<p align="center">
  <a href="https://ag.tavardt.com/">
    <img src="https://ag.tavardt.com/img/tavardt-banner.png" alt="TAVARDT" width="1024" />
  </a>
</p>

# TLS/SSL Certificate Watchdog

[![Scope of Perimeter Verification](https://img.shields.io/badge/TAVARDT-Technical%20Audit-5b3cf5.svg)](https://tools.tavardt.com/security-headers-check/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Automated monitoring of SSL/TLS certificate expiry, cryptographic chain integrity, and robust encryption baselines in the United States.

Engineered and maintained by the cyber defence practice at **TAVARDT** for North American infrastructure.

***

## 1. Scope of Perimeter Verification

This command-line tool audits certificate lifecycles, cryptographic suites, and trust chains for United States systems:

* **Preventative Expiry Alert:** Calculates remaining days before certificate expiry with automated alerting thresholds (> 30 days valid, <= 30 days warning, <= 0 days expired).
* **Protocol Version Audit:** Verifies TLS 1.3 and TLS 1.2 enforcement in alignment with NIST SP 800-52 baselines.
* **Cipher Suite Evaluation:** Inspects negotiated cipher algorithms and symmetric key strength (128/256 bits).
* **Certificate Authority (CA) Validation:** Inspects the root issuer organization and Subject Alternative Names (SAN).
* **Zero External Dependencies:** Runs entirely on Python native ssl and socket standard library modules.

***

## 2. Cryptographic Baseline & Certificate Lifecycle Matrix

<table>
  <thead>
    <tr>
      <th>Inspection Parameter</th>
      <th>Handshake Evaluation Method</th>
      <th>Defensive Baseline</th>
      <th>Operational Risk Mitigated</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Certificate Expiration</strong></td>
      <td>Calculates <code>notAfter</code> timestamp against current UTC time</td>
      <td>Renewal alert at &gt; 30 days remaining</td>
      <td>Service downtime and browser untrusted connection warnings</td>
    </tr>
    <tr>
      <td><strong>Protocol Version</strong></td>
      <td>Inspects negotiated TLS version via <code>ssock.version()</code></td>
      <td><code>TLSv1.3</code> preferred, <code>TLSv1.2</code> minimum</td>
      <td>Protocol downgrade attacks and legacy cipher vulnerabilities</td>
    </tr>
    <tr>
      <td><strong>Cipher Suite & Bit Depth</strong></td>
      <td>Extracts cipher parameters via <code>ssock.cipher()</code></td>
      <td>AEAD ciphers with &gt;= 128-bit key strength</td>
      <td>Man-in-the-middle decryption and weak CBC mode exploitation</td>
    </tr>
    <tr>
      <td><strong>Certificate Authority (CA)</strong></td>
      <td>Extracts issuer organization from trust chain</td>
      <td>Valid root CA trusted by default system store</td>
      <td>Self-signed certificate warnings and fraudulent interception</td>
    </tr>
    <tr>
      <td><strong>Subject Common Name (CN)</strong></td>
      <td>Matches hostname against certificate subject dictionary</td>
      <td>Strict match to server FQDN or wildcard SAN</td>
      <td>Domain impersonation and hostname mismatch errors</td>
    </tr>
  </tbody>
</table>

***

## 3. Quick Start Guide & CLI Automation

Run this tool directly via Python without installing third-party packages:

```bash
python watchdog.py example.com
```

The auditing engine inspects socket handshakes deterministically:

* **Native Standard Library:** Operates purely via Python standard libraries (`ssl`, `socket`, `datetime`), requiring zero third-party dependencies.
* **Deterministic Three-Tier Health Checks:** Classifies certificates as PASS (> 30 days), WARN (approaching expiry), or FAIL (expired).
* **CI/CD Pipeline Compatibility:** Integrates into automated pre-deployment testing and compliance verification workflows.

***

## 4. Frequently Asked Questions (Technical FAQ)

### 1. Why is an automated 30-day certificate expiration alert threshold critical for uptime?
Automated notification at 30 days remaining allows operational teams to execute automated ACME renewals or rotate credentials before public expiration. Breaching this threshold causes modern browsers to immediately block visitor access with severe security warnings.

### 2. How does watchdog.py inspect the TLS handshake without downloading full HTTP payloads?
The utility performs a direct socket-level TLS connection wrapping (`ssl.wrap_socket`) on port 443. It extracts cryptographic parameters directly from the peer certificate and cipher attributes during the handshake, minimizing latency and network overhead.

### 3. What security risks arise from legacy TLS protocol versions such as TLS 1.0 and TLS 1.1?
Deprecated TLS versions rely on vulnerable hash algorithms and cipher suites susceptible to downgrade and interception attacks. Enforcing TLS 1.2 or TLS 1.3 guarantees forward secrecy and modern authenticated encryption (AEAD).

### 4. How does the script handle both bare domain names and full URL inputs?
The CLI utility parses command-line inputs using Python `urllib.parse`. If a target begins with `http://` or `https://`, it strips protocols and URL paths to isolate the exact hostname for raw TCP socket connection on port 443.

### 5. Can this watchdog tool be executed in automated CI/CD and cron monitoring environments?
Yes, `watchdog.py` runs natively across Linux, macOS, and Windows containers without installing third-party packages. It produces deterministic standard output, allowing easy integration into cron schedules, GitHub Actions, and uptime monitoring workflows.

***

## 5. Online Diagnostic Tools (United States)

Audit your public infrastructure using the TAVARDT diagnostic suite:

* [Consent Mode v2 & Privacy Validator](https://tools.tavardt.com/consent-mode-v2-checker/)
* [DMARC & Anti-Spoofing Verifier](https://tools.tavardt.com/dmarc-checker/)
* [Exposed Credentials & Secret Scanner](https://tools.tavardt.com/exposed-files-scanner/)
* [Full Technical Tools Portal](https://tools.tavardt.com/)

***

## 6. Technical Advisory & Cryptographic Hardening in the United States

For advanced cryptographic auditing, NIST CSF 2.0 alignment, and incident response across North America, contact **TAVARDT**.

***

## Useful Links

* **Corporate Portal:** https://ag.tavardt.com/
* **Diagnostic Suite:** https://tools.tavardt.com/
* **Technical Contact:** https://ag.tavardt.com/contact/

***

### License
Released under the MIT License.

***

© 2026 TAVARDT. All rights reserved.
