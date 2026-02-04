from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStaion(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str = Field(max_length=200, default=None)

def display_station_info(spacestation: SpaceStaion)

def main():
    print("Space Station Data Validation")
    print("========================================")
    try:
        space = SpaceStaion(station_id="ISS001",
                            name="Internatonal Space Station",
                            crew_size=60,
                            power_level=85.5,
                            oxygen_level=92.3,
                            is_operational=True)

        print("Valid station created:")
        print(
            f"ID: {space.station_id}\n"
            f"Name: {space.name}\n"
            f"Crew: {space.crew_size} peaple\n"
            f"Power: {space.power_level}%\n"
            f"Oxygen: {space.oxygen_level}:%\n"
            f"Status: {"Operational" if space.is_operational else "Not operational"}\n"
        )
    except ValidationError as e:
        print("Expected validation error:")
        print(e)

if __name__ == "__main__":
    main()
