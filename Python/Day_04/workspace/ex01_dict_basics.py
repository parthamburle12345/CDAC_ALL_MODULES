from vinutils import line
from pprint import pprint

def main():
    p1 = {}
    p2 = dict()

    print(f"{p1=}")
    print(f"{p2=}")

    p3 = {"name": "Vinod", "city": "Bangalore", "emails": ["vinod@vinod.co", "vinod@cyblore.com"]}

    p4 = dict(name="Shyam", emails=["shyam@xmpl.com"])

    print(f"{p3=}")
    print(f"{p4=}")

    geolocs = {
        (12.888352, 77.563314): "Forum mall, Kanakapura road, Bangalore",
        (12.991873, 77.571447): "Mantri mall, Malleshwaram, Bangalore",
    }

    pprint(geolocs)

line()
main()
