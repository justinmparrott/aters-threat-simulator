import requests

def send_slack_alert(ip, reason, webhook_url):
    message = {
        "text": f"🚨 SOAR Alert: IP `{ip}` triggered response action.\nReason: {reason}"
    }
    try:
        response = requests.post(webhook_url, json=message)
        return response.status_code == 200
    except Exception as e:
        print(f"Slack alert failed: {e}")
        return False

def simulate_block_ip(ip):
    print(f"🧱 Simulated: Blocked IP {ip} on firewall (mock call)")

def simulate_isolate_host(ip):
    print(f"🖥️ Simulated: Isolated host with IP {ip} (mock EDR action)")

def simulate_create_ticket(ip, reason):
    print(f"📋 Simulated: Created ticket for IP {ip} → Reason: {reason}")
