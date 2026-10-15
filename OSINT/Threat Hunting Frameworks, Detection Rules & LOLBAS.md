<h1 align="center">🛡️ Threat Hunting Frameworks, Detection Rules & LOLBAS</h1>

<h2>🧠 Purpose</h2>
<p>Curated repository of adversary tactic matrices, detection engineering rule repositories, Living-off-the-Land (LotL) execution catalogs, and forensic decoding tools for <b>SOC Engineers</b>, <b>Threat Hunters</b>, and <b>Adversary Emulation Teams</b>.</p>

---

<h2>📐 Adversary Frameworks & Detection Rulebases</h2>
<table>
  <thead>
    <tr>
      <th align="left">🌐 Framework / Repository</th>
      <th align="left">🔗 Clearnet URL</th>
      <th align="center">📡 Status</th>
      <th align="left">📌 Intelligence Scope & Description</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><b>MITRE ATT&CK</b></td><td><code>https://attack.mitre.org/</code></td><td align="center">200</td><td>Globally-accessible knowledge base of adversary tactics, techniques, and procedures (TTPs) based on real-world observations.</td></tr>
    <tr><td><b>Sigma HQ</b></td><td><code>https://github.com/SigmaHQ/sigma</code></td><td align="center">200</td><td>Generic and open signature format allowing security analysts to describe log events and convert detection rules into SIEM queries (Splunk, Elastic, Sentinel).</td></tr>
    <tr><td><b>Awesome-Yara</b></td><td><code>https://github.com/InQuest/awesome-yara</code></td><td align="center">200</td><td>Curated collection of YARA rules, tools, guides, and rule generators for classifying malware families and memory artifacts.</td></tr>
    <tr><td><b>Atomic Red Team</b></td><td><code>https://atomicredteam.io/</code></td><td align="center">200</td><td>Library of simple, open-source, automation-friendly tests mapped to the MITRE ATT&CK matrix for validating detection coverage.</td></tr>
    <tr><td><b>Unprotect Project</b></td><td><code>https://unprotect.it/</code></td><td align="center">200</td><td>Comprehensive database and evasion technique catalog tracking how malware bypasses EDRs, AVs, sandboxes, and debuggers.</td></tr>
  </tbody>
</table>

<br>

<h2>⚙️ Living-off-the-Land & Binary Execution Catalogs</h2>
<table>
  <thead>
    <tr>
      <th align="left">🌐 Project / Catalog</th>
      <th align="left">🔗 Clearnet URL</th>
      <th align="center">📡 Status</th>
      <th align="left">📌 Intelligence Scope & Description</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><b>LOLBAS Project</b></td><td><code>https://lolbas-project.github.io/</code></td><td align="center">200</td><td>Living Off The Land Binaries, Scripts, and Libraries: authoritative reference for Windows native binaries abused for execution, bypass, and persistence.</td></tr>
    <tr><td><b>GTFOBins</b></td><td><code>https://gtfobins.github.io/</code></td><td align="center">200</td><td>Curated list of Unix/Linux binaries that can be exploited by an attacker to bypass local security restrictions and escalate privileges.</td></tr>
    <tr><td><b>LOLDrivers</b></td><td><code>https://www.loldrivers.io/</code></td><td align="center">200</td><td>Catalog of vulnerable, legitimately signed Windows drivers used in Bring Your Own Vulnerable Driver (BYOVD) attacks to terminate EDRs.</td></tr>
    <tr><td><b>WADComs</b></td><td><code>https://wadcoms.github.io/</code></td><td align="center">200</td><td>Interactive cheat sheet and command generator for Windows and Active Directory privilege escalation and defense.</td></tr>
    <tr><td><b>CyberChef (GCHQ)</b></td><td><code>https://gchq.github.io/CyberChef/</code></td><td align="center">200</td><td>The Cyber Swiss Army Knife; browser application for decoding Base64/Hex, deobfuscating PowerShell, parsing XOR, and carving data.</td></tr>
  </tbody>
</table>
