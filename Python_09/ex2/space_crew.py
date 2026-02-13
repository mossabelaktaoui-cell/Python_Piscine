from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from typing import List


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5,  max_length=15)
    mission_name: str = Field(min_length=3,  max_length=100)
    destination: str = Field(min_length=3,  max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate(self):
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')

        leaders = [leader for leader in self.crew
                   if leader.rank == Rank.COMMANDER
                   or leader.rank == Rank.CAPTAIN]
        if len(leaders) < 1:
            raise ValueError('Must have at least one Commander or Captain')

        has_5_year_experience = [member for member in self.crew
                                 if member.years_experience >= 5]
        if self.duration_days > 365:
            if len(has_5_year_experience) < len(self.crew) / 2:
                raise ValueError('Long missions (> 365 days) '
                                 'need 50% experienced crew (5+ years)')

        inactive = [member for member in self.crew
                    if member.is_active is False]
        if len(inactive) > 0:
            raise ValueError('All crew members must be active')
        return self


def display_mission(mission: SpaceMission) -> None:
    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(
            f"- {member.name} ({member.rank.value}) "
            f"- {member.specialization}"
        )


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")

    try:
        mission1 = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            budget_millions=2500.0,
            crew=[
                CrewMember(
                    member_id="C001",
                    name="Sarah Connor",
                    rank=Rank.COMMANDER,
                    age=42,
                    specialization="Mission Command",
                    years_experience=15
                ),
                CrewMember(
                    member_id="C002",
                    name="John Smith",
                    rank=Rank.LIEUTENANT,
                    age=35,
                    specialization="Navigation",
                    years_experience=6
                ),
                CrewMember(
                    member_id="C003",
                    name="Alice Johnson",
                    rank=Rank.OFFICER,
                    age=30,
                    specialization="Engineering",
                    years_experience=5
                ),
            ]
        )
        display_mission(mission1)

    except ValidationError as e:
        print("Expected validation error:")
        for err in e.errors():
            if 'error' in err['ctx']:
                print(err['ctx']['error'])
            else:
                print(err['msg'])

    try:
        print("\n=========================================")
        mission2 = SpaceMission(
            mission_id="M2025_MOON",
            mission_name="Moon Research Mission",
            destination="Moon",
            launch_date=datetime.now(),
            duration_days=0,
            budget_millions=800.0,
            crew=[
                CrewMember(
                    member_id="C010",
                    name="Tom Hardy",
                    rank=Rank.COMMANDER,
                    age=38,
                    specialization="Science",
                    years_experience=10
                ),
                CrewMember(
                    member_id="C011",
                    name="Emma Stone",
                    rank=Rank.OFFICER,
                    age=32,
                    specialization="Communications",
                    years_experience=7
                ),
            ]
        )
        display_mission(mission2)

    except ValidationError as e:
        print("Expected validation error:")
        for err in e.errors():
            if 'error' in err['ctx']:
                print(err['ctx']['error'])
            else:
                print(err['msg'])


if __name__ == "__main__":
    main()
