import requests
import time
from datetime import datetime

class SentryConsole:
    def __init__(self, target_ip, target_port):
        self.url = f"http://{target_ip}:{target_port}/test_intrusion"
        self.target = target_ip

    def inject_traffic(self, scenario_name, params):
        print(f"\n[{datetime.now().strftime('%H:%M:%S')}] INJECTING: {scenario_name}")
        try:
            start = time.time()
            r = requests.get(self.url, params=params, timeout=5)
            latency = (time.time() - start) * 1000
            
            data = r.json()
            if "error" in data:
                print(f"| SERVER ERROR: {data['error']}")
            else:
                print(f"| SENTRY RESPONSE: {data['result']}")
                print(f"| LATENCY: {latency:.2f}ms")
        except Exception as e:
            print(f"| CONNECTION ERROR: Could not reach Pi at {self.target}")

def main():
    console = SentryConsole("192.168.0.105", 5000)
    
    while True:
        print("\n" + "="*40)
        print("  AI SENTRY INTERACTIVE TESTER")
        print("="*40)
        print("1. Inject SAFE Traffic")
        print("2. Inject MALICIOUS (Attack) Traffic")
        print("3. Inject BROKEN Data (Triggers Server Error)")
        print("4. Exit")
        
        choice = input("\nSelect Scenario [1-4]: ")

        if choice == '1':
            # Normal values
            data = {"duration": 0.5, "src_bytes": 150, "dst_bytes": 450, "important_feature_1": 1.0, 
                    "important_feature_2": 1.0, "protocol_type": "tcp", "service": "http"}
            console.inject_traffic("NORMAL_BEHAVIOR", data)

        elif choice == '2':
            # Use 'icmp' and 'eco_i' (standard KDD attack values) 
            # or 'tcp' and 'http' with very high byte counts
            data = {
                "duration": 0.1, 
                "src_bytes": 9000, 
                "dst_bytes": 0, 
                "important_feature_1": 5.0, 
                "important_feature_2": 5.0, 
                "protocol_type": "tcp", # Changed from udp
                "service": "http"        # Changed from private
            }
            console.inject_traffic("DOS_ATTACK_SIMULATION", data)

        elif choice == '3':
            # Missing keys or "None" values to force an error
            data = {"duration": "none", "src_bytes": "abc"} # This will crash the float() conversion
            console.inject_traffic("MALFORMED_PACKET_TEST", data)

        elif choice == '4':
            print("Shutting down tester...")
            break
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main()