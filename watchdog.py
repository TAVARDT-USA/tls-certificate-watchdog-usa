#!/usr/bin/env python3
import sys
import socket
import ssl
from datetime import datetime, timezone
from urllib.parse import urlparse

def inspect_tls(hostname, port=443):
    print(f"\n[TAVARDT USA] Inspecting TLS certificate and crypto chain for: {hostname}:{port}\n")
    context = ssl.create_default_context()
    
    try:
        with socket.create_connection((hostname, port), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                cipher = ssock.cipher()
                version = ssock.version()
                
                # Expiration calculation
                expire_str = cert['notAfter']
                expire_date = datetime.strptime(expire_str, "%b %d %H:%M:%S %Y %Z").replace(tzinfo=timezone.utc)
                now = datetime.now(timezone.utc)
                days_left = (expire_date - now).days
                
                issuer_dict = dict(x[0] for x in cert.get('issuer', []))
                common_name = dict(x[0] for x in cert.get('subject', [])).get('commonName', hostname)
                
                print(f"  [INFO] Common Name: {common_name}")
                print(f"  [INFO] Issuer Organization: {issuer_dict.get('organizationName', 'Unknown')}")
                print(f"  [INFO] TLS Version: {version}")
                print(f"  [INFO] Cipher Suite: {cipher[0]} ({cipher[2]} bits)")
                print(f"  [INFO] Expiration Date: {expire_date.strftime('%Y-%m-%d %H:%M:%S UTC')}")
                print(f"  [INFO] Days Remaining: {days_left} days")
                
                if days_left > 30:
                    print(f"\n  [PASS] Certificate is valid. ({days_left} days remaining)")
                elif days_left > 0:
                    print(f"\n  [WARN] Certificate expires soon. ({days_left} days remaining)")
                else:
                    print(f"\n  [FAIL] Certificate has expired.")
                    
                print(f"\n[TAVARDT USA] Check complete.")
                print(f"\nPerform continuous perimeter monitoring at https://tools.tavardt.com/ or request enterprise hardening at https://ag.tavardt.com/\n")
                
    except Exception as e:
        print(f"[TAVARDT USA] Error inspecting target: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python watchdog.py <hostname>")
        sys.exit(1)
        
    target = sys.argv[1].strip()
    if target.startswith("http://") or target.startswith("https://"):
        target = urlparse(target).hostname or target
        
    inspect_tls(target)
