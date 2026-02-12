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

            if power is None and args:
                power = args[-1]

            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return _


def retry_spell(max_attempts: int) -> callable:
    def _(func: callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(max_attempts):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception:
                    print("Spell failed, retrying... "
                          f"({i + 1}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return _


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        for char in name:
            if not char.isalpha() and char != ' ':
                return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with power {power}!"


def main():
    @spell_timer
    def fire_spell(target):
        time.sleep(1)
        return f"Fire spell hits {target}!"

    @power_validator(10)
    def spell_attack(power):
        return f"Fire spell hits with {power}!"

    @retry_spell(5)
    def is_int(integer):
        return int(integer)

    print("\nTesting spell timer...")
    fire_spell("Goblin")

    print("\nTesting power validator...")
    print("Min power: 10")
    print("Curren power: 9")
    print(spell_attack(9))

    print("\nTesting retry spell...")
    print(is_int("hallo"))

    mage = MageGuild()
    print("\nTesting MageGuild...")
    print(mage.validate_mage_name("mossabe_lak"))
    print(mage.validate_mage_name("mossabe"))
    print(mage.cast_spell("Lightning", power=15))
    print(mage.cast_spell("Lightning", power=5))


if __name__ == "__main__":
    main()
