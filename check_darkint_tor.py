"""
CounterIntelCTI - Automated Tor .onion Link Verifier
Checks all .onion services in DARKINT/ and updates their live/dead status
Requires Tor SOCKS proxy running on 127.0.0.1:9050 or 127.0.0.1:9150 (Tor Browser)
"""

import os
import re
import socket
import urllib3
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/115.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

def detect_tor_proxy():
    for port in [9050, 9150]:
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=2):
                return f"socks5h://127.0.0.1:{port}"
        except (socket.timeout, ConnectionRefusedError, OSError):
            continue
    return None

def check_onion_url(session, url, proxy_url):
    url = url.strip()
    if not (url.startswith("http://") or url.startswith("https://")):
        url = "http://" + url
        
    try:
        resp = session.get(url, headers=HEADERS, timeout=25, verify=False, allow_redirects=True)
        code = resp.status_code
        if code in [200, 201, 202, 204, 301, 302, 303, 307, 308]:
            return "200"
        elif code in [401, 403, 503]:
            return f"{code} (Active/Protected)"
        elif code in [404, 410]:
            return f"Dead ({code})"
        else:
            return f"{code}"
    except requests.exceptions.ConnectTimeout:
        return "Dead (Timeout)"
    except requests.exceptions.ConnectionError:
        return "Dead (Offline)"
    except Exception:
        return "Dead"

def process_file(filepath, proxy_url):
    print(f"\nScanning: {os.path.basename(filepath)}")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.splitlines(keepends=True)
    tasks = []
    
    for idx, line in enumerate(lines):
        if "<tr>" in line and ("<code>" in line or "href=" in line):
            m = re.search(r'href=["\'](http[s]?://[^"\']+\.onion[^"\']*)["\']', line)
            if not m:
                m = re.search(r'<code>(http[s]?://[^\s<>]+\.onion[^\s<>]*)</code>', line)
            if not m:
                m = re.search(r'<code>([^<>]+\.onion[^<>]*)</code>', line)
            if not m:
                m = re.search(r'href=["\']([^"\']+\.onion[^"\']*)["\']', line)
            if m:
                tasks.append((idx, m.group(1).strip(), line))

    if not tasks:
        print("  No .onion links found.")
        return

    print(f"  Verifying {len(tasks)} onion links...")
    session = requests.Session()
    session.proxies = {"http": proxy_url, "https": proxy_url}

    results = {}
    with ThreadPoolExecutor(max_workers=5) as executor:
        future_map = {
            executor.submit(check_onion_url, session, t[1], proxy_url): t for t in tasks
        }
        for future in as_completed(future_map):
            idx, raw_url, original_line = future_map[future]
            try:
                status = future.result()
            except Exception:
                status = "Dead"
            results[idx] = status
            print(f"    [{status}] {raw_url[:55]}")

    new_lines = []
    for idx, line in enumerate(lines):
        if idx in results:
            status = results[idx]
            tds = list(re.finditer(r'<td\b[^>]*>(.*?)</td>', line, flags=re.DOTALL))
            if len(tds) >= 3:
                status_match = tds[2]
                before = line[:status_match.start()]
                after = line[status_match.end():]
                new_lines.append(f'{before}<td align="center">{status}</td>{after}')
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)

    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(new_lines)
    print(f"  Updated: {os.path.basename(filepath)}")

def main():
    proxy = detect_tor_proxy()
    if not proxy:
        print("[!] No active Tor SOCKS proxy found on 127.0.0.1:9050 or 127.0.0.1:9150.")
        print("[i] Please launch Tor Expert Bundle or Tor Browser first, then re-run this script.")
        return

    print(f"[+] Tor proxy active at {proxy}")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    darkint_dir = os.path.join(base_dir, "DARKINT")
    
    if not os.path.isdir(darkint_dir):
        print(f"[!] DARKINT directory not found at {darkint_dir}")
        return

    for fname in sorted(os.listdir(darkint_dir)):
        if fname.endswith(".md"):
            process_file(os.path.join(darkint_dir, fname), proxy)

    print("\n[+] All DARKINT files successfully updated with live/dead statuses!")

if __name__ == "__main__":
    main()
