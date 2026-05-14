road_segments = [
    {
        "id": "seg_001",
        "lat": 37.7749,
        "lon": -122.4194,
        "speed_limit": 35,
        "road_type": "residential",
    },
    {
        "id": "seg_002",
        "lat": 37.7750,
        "lon": -122.4180,
        "speed_limit": 25,
        "road_type": "residential",
    },
    {
        "id": "seg_003",
        "lat": 37.7755,
        "lon": -122.4170,
        "speed_limit": None,
        "road_type": "residential",
    },
    {
        "id": "seg_004",
        "lat": 37.7760,
        "lon": -122.4160,
        "speed_limit": 45,
        "road_type": "arterial",
    },
    {
        "id": "seg_005",
        "lat": 999.9,
        "lon": -122.4150,
        "speed_limit": 35,
        "road_type": None,
    },
]

print(f"Total segments: {len(road_segments)}")
print("---")

for segment in road_segments:
    print(segment)
print("---")
print("Running validations...")


# speed_limit validator
def check_missing_speed_limit(segments):
    for segment in segments:
        if segment["speed_limit"] is None:
            print(f" ISSUE: {segment['id']} has no speed limit")


# road_type validator
def check_missing_road_type(segments):
    for segment in segments:
        if segment["road_type"] is None:
            print(f" ISSUE: {segment['id']} has no road type")

# coordinate validator
def check_invalid_coordinates(segments):
    for segment in segments:
        lat = segment["lat"]
        lon = segment["lon"]

        if lat is None or lon is None:
            print(f" ISSUE: {segment['id']} has missing coordinates")
        elif lat < -90 or lat > 90:
            print(f" ISSUE:{segment['id']} has invalid latitude: {lat}")
        elif lon < -180 or lon > 180:
            print(f" ISSUE: {segment['id']} has invalid longitude: {lon}")

# duplicate coordinate validator
def check_duplicate_coordinates(segments):
    seen_coordinates = set()
    for segment in segments:
        coord = (segment["lat"], segment["lon"])
        if coord in seen_coordinates:
            print(f" ISSUE: {segment['id']} has duplicate coordinates: {coord}")
        else:
            seen_coordinates.add(coord)

check_missing_speed_limit(road_segments)
check_missing_road_type(road_segments)
check_invalid_coordinates(road_segments)
check_duplicate_coordinates(road_segments)
