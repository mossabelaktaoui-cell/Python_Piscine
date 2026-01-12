from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass
    
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        sum_ = 0
        for num in data:
            sum_ += num

        avg = sum_ / len(data)
        return f"Processed {len(data)} numeric values, sum={sum_}, avg={avg:.1f}"
    
    def validate(self, data: Any) -> bool:
        try:
            for number in data:
                number = float(number)
        except:
            return False
        if data == []:
            return False
        print("Numeric data verified")
        return True


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        characters_num = len(data)
        words_num = len(data.split(" "))
        return f"Processed text: {characters_num} characters, {words_num} words"
    
    def validate(self, data: Any) -> bool:
        try:
            data.upper()
        except:
            return False

        print("Text data verified")
        return True


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        levels = {"ERROR": "[ALERT] ERROR", "INFO": "[INFO] INFO", "WARNING": "[WARNING] WARNING"}
        for level, message in levels.items():
            if level in data.upper():
                return f"{message} level detected:{data.split(':')[1]}"
        return "Unknown level detected"
    
    def validate(self, data: Any) -> bool:
        try:
            data.upper()
        except:
            return False

        levels = ["ERROR", "WARNING", "INFO"]

        for level in levels:
            if level in data.upper():
                print("Log entry verified")
                return True
        return False


def initialize_numeric(number: NumericProcessor, data: Any) -> None:
    print("Initializing Numeric Processor...")
    print(f"Processing data: {data}")
    print(f"Validation: ", end='')
    if not number.validate(data):
        print("Data non valid")
        return
    print(number.format_output(number.process(data)))

def initialize_text(text: TextProcessor, data: Any) -> None:
    print("Initializing Text Processor...")
    print(f"Processing data: \"{data}\"")
    print(f"Validation: ", end='')
    if not text.validate(data):
        print("Data non valid")
        return
    print(text.format_output(text.process(data)))

def initialize_log(log: LogProcessor, data: Any) -> None:
    print("Initializing Log Processor...")
    print(f"Processing data: \"{data}\"")
    print(f"Validation: ", end='')
    if not log.validate(data):
        print("Data non valid")
        return
    print(log.format_output(log.process(data)))


def stream_processor() -> None:
    num = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    
    initialize_numeric(num, [1, 2, 3, 4, 5])
    print()
    initialize_text(text, "Hello Nexus World")
    print()
    initialize_log(log, "RROR: Connection timeout")
    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    i = 1
    for item, data in ((num, [1, 2, 3]), (text, "Nexus World!"), (log, "INFO: System ready")):
        print(f"Result {i}: {item.process(data)}")
        i += 1

stream_processor()
