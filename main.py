import os
from dotenv import load_dotenv
import requests
from utils.enrich_abuseipdb import enrich_abuseipdb
from utils.enrich_virustotal import enrich_virustotal
from utils.enrich_greynoise import enrich_greynoise
from utils.responders import send_slack_alert, simulate_block_ip, simulate_isolate_host, simulate_create_ticket

load_dotenv()  # Load environment variables from .env

ABUSEIPDB_KEY = os.getenv("ABUSEIPDB_KEY")
VT_KEY = os.getenv("VT_KEY")
GN_KEY = os.getenv("GN_KEY")
SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK")


def main():
    ip = input("Enter an IP address to enrich: ")

    print("\n Running multi-source enrichment...\n")

    abuse_data = enrich_abuseipdb(ip, ABUSEIPDB_KEY)
    vt_data = enrich_virustotal(ip, VT_KEY)
    gn_data = enrich_greynoise(ip, GN_KEY)

    #  Response Logic
    print("\n Response Logic Decision Tree:")

    #AbuseIPDB logic
    if abuse_data['abuseConfidenceScore'] > 70:
        print(f" AbuseIPDB score {abuse_data['abuseConfidenceScore']} > 70 → Block IP")
        simulate_block_ip(ip)
        send_slack_alert(ip, f"High AbuseIPDB score: {abuse_data['abuseConfidenceScore']}", SLACK_WEBHOOK)
    else:
        print(f" AbuseIPDB score {abuse_data['abuseConfidenceScore']} → No action")

    # VirusTotal logic
    if vt_data["reputation"] < 0:
        print(f" VirusTotal reputation {vt_data['reputation']} < 0 → Isolate host")
        simulate_isolate_host(ip)
        send_slack_alert(ip, f"VirusTotal reputation is {vt_data['reputation']}", SLACK_WEBHOOK)
    else:
        print(f" VirusTotal reputation {vt_data['reputation']} → No action")

    # GreyNoise logic
    if gn_data["classification"] in ["malicious", "unknown"] and gn_data["noise"]:
        print(f" GreyNoise: {gn_data['classification']}, noise={gn_data['noise']} → Create ticket")
        simulate_create_ticket(ip, "GreyNoise indicates scanning or attack activity")
        send_slack_alert(ip, f"GreyNoise flagged IP as {gn_data['classification']}", SLACK_WEBHOOK)
    else:
        print(f" GreyNoise: classification={gn_data['classification']}, noise={gn_data['noise']} → No action")

if __name__ == "__main__":
    main()

