from functools import wraps
import time


def spell_timer(func: callable) -> callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        print(f"Casting {func.__name__}...")
        result = func(*args, **kwargs)
        end = time.perf_counter()
        spent_time = end - start
        print(f"Spell completed in {spent_time:.4f} seconds")
        print(f"Result: {func.__name__} cast!")
        return result

    return wrapper


def power_validator(min_power: int) -> callable:
    def _(func: callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            power = kwargs.get("power")
            return f"This power ({power}) is enough"
        return wrapper
    return _
        


def retry_spell(max_attempts: int) -> callable:
    pass


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        pass

    def cast_spell(self, spell_name: str, power: int) -> str:
        pass


def main():
    print("Testing spell timer...")
    @spell_timer
    def fire_spell(target):
        time.sleep(1)
        return f"Fire spell hits {target}!"

    fire_spell("Goblin")

    @power_validator(10)
    def fire_spell(power):
        return f"Fire spell hits with {power}!"
