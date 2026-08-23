---
name: rdptunnel
version: 4.7.4
description: Expose local RDP (Remote Desktop) servers to the public internet via aitun TCP tunnel with TLS-based routing. Perfect for AI agents that need to provide remote desktop access to Windows machines, GUI servers, or VDI instances behind NAT/firewall.
metadata:
  openclaw:
    requires:
      bins:
        - python3
    envVars:
      - name: AITUN_SERVER
        required: false
        description: "AiTun server address (default: aitun.cc:6639)"
    install:
      - kind: pip
        package: aitun
        bins: [aitun]
      - kind: uv
        package: aitun
        bins: [aitun]
    emoji: "💻"
    homepage: https://aitun.cc
    clawhub: https://clawhub.ai/ctz168/rdptunnel
---

# RDP Tunnel - Remote Desktop Access via Aitun TCP Forwarding

## When to Use

Use this skill when:
- You need to access a remote Windows desktop that is behind NAT, firewall, or a private network
- You want to expose a local RDP server so a colleague or client can connect remotely via Remote Desktop
- You are running a Windows VM or VDI instance with no public IP and need to make it reachable
- You want to provide temporary remote desktop access for support, training, or demonstration
- You need to connect to a home Windows PC or workstation from another location
- You want to access a Linux machine running xrdp or a VNC-to-RDP gateway
- You need to remotely manage a GUI application that cannot be accessed via SSH

Do NOT use this skill when:
- The RDP server already has a public IP and is directly reachable
- You only need command-line access (use sshtunnel instead)
- You want to expose an HTTP service (use aitun-tunnel instead)

## Instructions

### Step 1: Install aitun

```bash
pip install aitun
```

Or install via one-line script (Linux/macOS):
```bash
curl -fsSL https://aitun.cc/install.sh | bash
```

Windows (PowerShell):
```powershell
irm https://aitun.cc/install.ps1 | iex
```

Or verify it is already installed:

```bash
which aitun
```

### Step 2: Ensure RDP server is running locally

Verify the local RDP service is running and accessible:

**On Windows:**

```powershell
# Check if Remote Desktop is enabled
Get-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -Name fDenyTSConnections

# Enable Remote Desktop (0 = enabled, 1 = disabled)
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -Name fDenyTSConnections -Value 0

# Ensure the RDP service is running
Get-Service -Name TermService | Start-Service
```

**On Linux (xrdp):**

```bash
# Install xrdp
sudo apt install xrdp -y    # Debian/Ubuntu
sudo yum install xrdp -y    # CentOS/RHEL

# Start xrdp service
sudo systemctl start xrdp
sudo systemctl enable xrdp

# Verify it is listening on port 3389
ss -tlnp | grep :3389
```

### Step 3: Create a TCP tunnel for RDP

RDP uses TCP port 3389 by default. Use aitun's `--tcp-ports` flag to forward this port. TCP forwarding requires an auth token (register at https://aitun.cc):

```bash
aitun -k YOUR_TOKEN --tcp-ports 3389 &
AITUN_PID=$!
sleep 3
```

Or with HTTP tunnel alongside RDP:

```bash
aitun -k YOUR_TOKEN -p 8080 --tcp-ports 3389 &
AITUN_PID=$!
sleep 3
```

The output will show:

```
[TCP] rdp -> localhost:3389 (subdomain: yourname.t.aitun.cc:3389)
```

If port 3389 is occupied on the server, a port from the 7000-7999 range will be automatically assigned.

### Step 4: Connect remotely

From any machine on the internet:

**Windows (Remote Desktop Connection):**

1. Press `Win + R`, type `mstsc`, press Enter
2. Enter `yourname.t.aitun.cc:3389` as the computer name
3. Click Connect and enter credentials

**Linux (FreeRDP):**

```bash
xfreerdp /v:yourname.t.aitun.cc:3389 /u:username /cert:ignore
```

**macOS (Microsoft Remote Desktop):**

1. Open Microsoft Remote Desktop from the App Store
2. Click "+" → "New Remote Desktop"
3. Enter `yourname.t.aitun.cc:3389` as the PC name
4. Connect and enter credentials

### Step 5: Clean up

When done, stop the tunnel:

```bash
kill $AITUN_PID 2>/dev/null
```

## Advanced Usage

### Forward RDP + SSH Together

```bash
aitun -k YOUR_TOKEN --tcp-ports 3389,22 &
AITUN_PID=$!
sleep 3
```

### Custom RDP Port

If RDP is running on a non-standard port (e.g., 13389):

```bash
aitun -k YOUR_TOKEN --tcp-ports 13389 &
```

### Connect to RDP in a Docker Container

```bash
# Container running xrdp on port 3389, mapped to host port 13389
aitun -k YOUR_TOKEN --tcp-ports 13389 &
```

## How TCP Routing Works

aitun v4.7.0 uses TLS with SNI for all TCP tunnel routing:

1. **All TCP tunnels require TLS** — the server terminates TLS and extracts SNI for subdomain identification
2. **RDP connections** are routed by SNI just like SSH-over-TLS and HTTPS
3. **Each subdomain gets its own port 3389** — no conflicts with other users
4. If the requested port is occupied on the server, a port from the 7000-7999 range is assigned

Note: RDP clients connect directly without ProxyCommand (unlike SSH which needs `aitun ssh-proxy`), because RDP traffic is routed at the TCP level by the server based on SNI from the initial TLS handshake.

## Security Recommendations

- **Use strong passwords** on all RDP accounts
- **Enable Network Level Authentication (NLA)** on Windows RDP servers
- **Restrict RDP access** to specific users via group policy
- **Consider changing the default RDP port** (3389) to reduce automated attacks
- **Monitor RDP logs** for unauthorized access attempts
- **Disable RDP** when not actively needed

## CLI Reference

The `aitun` command (installed via `pip install aitun`, or alternatively `curl -fsSL https://aitun.cc/install.sh | bash` / `irm https://aitun.cc/install.ps1 | iex` on Windows) accepts these flags:

| Flag | Description |
|---|---|
| `-p PORT` | Local HTTP service port (optional; omit for TCP-only mode with `--tcp-ports`) |
| `-k TOKEN` | Auth token for registered subdomain (required for TCP forwarding) |
| `--host HOST` | Local service address (default: localhost) |
| `--tcp-ports PORTS` | TCP forwarding ports, comma-separated (e.g., `3389,22`; requires `-k`). Use without `-p` for TCP-only mode |
| `--p2p` | Enable P2P direct connection (default: enabled) |
| `--no-p2p` | Disable P2P, force server relay mode |
| `--daemon` | Run as background daemon |
| `--stop` | Stop running daemon |

**Subcommand:**

| Command | Description |
|---|---|
| `aitun ssh-proxy <host> [port]` | SSH ProxyCommand — wraps SSH in TLS for SNI routing |

## Notes

- TCP forwarding (required for RDP) requires a registered account and `-k` token — free tunnels do not support TCP
- Register at https://aitun.cc to get an auth token
- All traffic is encrypted through the aitun tunnel (TLS on the server side)
- If the requested port (e.g., 3389) is occupied on the server, a port from the 7000-7999 range will be automatically assigned
- RDP traffic itself is also encrypted, but the tunnel adds an additional security layer
- P2P mode reduces latency for remote desktop sessions; use `--no-p2p` only if P2P connection fails
- For best performance, ensure a stable internet connection on both ends
- The tunnel stays active as long as the aitun process runs; use `--daemon` for persistent background operation
- Subdomains remain active for 30 days of inactivity; use heartbeat to renew
