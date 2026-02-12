from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStaion(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(max_length=200, default=None)


def display_station_info(spacestation: SpaceStaion):
    print("Valid station created:")
    print(
        f"ID: {spacestation.station_id}\n"
        f"Name: {spacestation.name}\n"
        f"Crew: {spacestation.crew_size} peaple\n"
        f"Power: {spacestation.power_level}%\n"
        f"Oxygen: {spacestation.oxygen_level}:%\n"
        f"Status: {"Operational" if spacestation.is_operational
                   else "Not operational"}\n")


def main():
    print("Space Station Data Validation")
    print("========================================")
    try:
        space1 = SpaceStaion(station_id="ISS001",
                             name="Internatonal Space Station",
                             crew_size=6,
                             power_level=85.5,
                             oxygen_level=92.3,
                             last_maintenance=datetime.now(),
                             is_operational=True)
        display_station_info(space1)

    except ValidationError as e:
        print("Expected validation error:")
        print(e)

    print("========================================")
    try:
        space2 = SpaceStaion(station_id="ISS002",
                             name="Internatonal Space Station",
                             crew_size=60,
                             power_level=85.5,
                             oxygen_level=92.3,
                             last_maintenance=datetime.now(),
                             is_operational=True)
        display_station_info(space2)

    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]['msg'])


if __name__ == "__main__":
    main()
