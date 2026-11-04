import json
from pathlib import Path

INPUT_FILE = Path("/python/security_events.json")
OUTPUT_FILE = Path("/python/report.json")

def load_events():

    try:
        with INPUT_FILE.open("r",encoding="utf-8") as file:
            events = json.load(file)
        if not isinstance(events,list):
            raise ValueError("Json must contain a list of events.")
        return events
    except FileNotFoundError:
        print("Security event file not found")
        return []
    except json.JSONDecodeError:
        print("invalid json format")
        return []
    except ValueError as error:
        print(f"Error:{error}")
        return []

def detect_threats(event):
    threats= []

    #pattern 1:multiple login failure
    if event.get("event_type") =="login" and event.get("status")=="failed" and event.get("failed_attempts",0)>=5:
        threats.append("possible brute force login attack")

        #pattern 2:unauthorized file access

        if event.get("event_type")=="file_access" and event.get("status")=="denied":
            threats.append("unauthorized file access attempt")

        #pattern3: port scanning 

        if event.get("event_type")=="port_scan":
            threats.append("Possible network reconnaissance")
        return threats
def analyze_events(events):
    suspecious_events=[]

    for event in events:
        threats =detect_threats(event)
        if threats:
            suspecious_events.append({
                "event_id":event.get("event_id"),
                "ip":event.get("ip"),
                "username":event.get("username"),
                "threats":threats,
                "risk_level":("High" if len(threats)>=2 or"Possible brute-force login attack" in threats else "Medium")
            })
    return suspecious_events
def save_report(suspecious_events):
    report={
        "total_suspecious_events":len(suspecious_events),
        "events":suspecious_events
    }

    with OUTPUT_FILE.open("w",encoding="utf-8") as file:
        json.dump(report,file,indent=4)
    print("report saved in report.json")

def display_report(suspecious_events):
    print("\n=======Security Report========")
    if not suspecious_events:
        print("no suspecious event found")
    for event in suspecious_events:
        print(f"\nEvent ID:{event["event_id"]}")
        print(f"\nIP Address:{event["ip"]}")
        print(f"\nusername:{event["username"]}")
        print(f"\nRisk Level:{event["risk_level"]}")

        for threat in event["threats"]:
            print("threats:",threat)
    print("\n Total suspecious events :",len(suspecious_events))

def main():
    events=load_events()

    if not events:
        return
    suspecious_events=analyze_events(events)
    display_report(suspecious_events)
    save_report(suspecious_events)

if __name__=="__main__":
    main()
