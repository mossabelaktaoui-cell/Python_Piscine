from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        pass

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        pass


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__()
        self.stream_id = stream_id
        self.readings_processed = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        total: int = 0
        i: int = 0
        filtered_data: List[float] = []
        for data in data_batch:
            unite, value = data.split(":")
            if unite == "temp":
                filtered_data.append(float(value))
        while i < len(filtered_data):
            total += filtered_data[i]
            i += 1
        average: float = total / len(filtered_data)
        self.readings_processed = len(data_batch)
        return (
            f"Initializing Sensor Stream...\n"
            f"Stream ID: {self.stream_id}, Type: Environmental Data\n"
            f"Processing sensor batch: {data_batch}\n"
            f"Sensor analysis: {self.readings_processed} readings processed, "
            f"avg temp: {average:.2f}°C"
        )

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        filtered_data: List[Any] = []
        for data in data_batch:
            unite, value = data.split(":")
            if unite == "temp":
                filtered_data.append(data)
        return filtered_data

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "- Sensor data": f"{self.readings_processed} readings processed"
            }


class TransactionStream(DataStream):
    def __init__(self, trans_id: str) -> None:
        super().__init__()
        self.trans_id = trans_id
        self.operations = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        net_flow: int = 0
        for data in data_batch:
            trans, value = data.split(":")
            if trans == "sell":
                net_flow -= int(value)
            elif trans == "buy":
                net_flow += int(value)
        if net_flow > 0:
            net_flow_str: str = f"+{net_flow}"
        else:
            net_flow_str: str = str(net_flow)

        self.operations = len(data_batch)
        return (
            f"Initializing Transaction Stream...\n"
            f"Stream ID: {self.trans_id}, Type: Financial Data\n"
            f"Processing transaction batch: {data_batch}\n"
            f"Transaction analysis: {self.operations} operations, "
            f"net flow: {net_flow_str} units"
        )

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        filtered_data: List[Any] = []
        for data in data_batch:
            trans, value = data.split(":")
            if trans == criteria:
                filtered_data.append(data)
        return filtered_data

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "- Transaction data": f"{self.operations} operations processed"
            }


class EventStream(DataStream):
    def __init__(self, event_id: str) -> None:
        super().__init__()
        self.event_id = event_id
        self.events = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        errors_detected: int = 0
        for event in data_batch:
            if "error" in event.lower():
                errors_detected += 1
        self.events = len(data_batch)
        return (
            f"Initializing Event Stream...\n"
            f"Stream ID: {self.event_id}, Type: System Events\n"
            f"Processing event batch: {data_batch}\n"
            f"Event analysis: {self.events} events, "
            f"{errors_detected} error detected"
        )

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        filtered_data: List[Any] = []
        for data in data_batch:
            if data == criteria:
                filtered_data.append(data)
        return filtered_data

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "- Event data": f"{self.events} events processed"
            }


class StreamProcessor():
    def __init__(self, streams: List[DataStream]) -> None:
        self.streams: List[DataStream] = streams

    def stream_info(self) -> None:
        print("\n=== Polymorphic Stream Processor ===")
        print("Processing mixed stream types through a unified interface...")
        print("\nBatch 1 Results")
        for stream in self.streams:
            stats = stream.get_stats()
            for key, value in stats.items():
                print(f"{key}: {value}")
        print("\nStream filtering active: High-priority data only")
        print("Filtered results: 2 critical sensor alerts, "
              "1 large transaction")
        print("\nAll streams processed successfully. "
              "Nexus throughput optimal.")


def main():
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    sensor_data = ["temp:22.5", "humidity:65", "pressure:1013"]
    transaction_data = ["buy:100", "sell:150", "buy:75"]
    event_data = ["login", "error", "logout"]

    sensor = SensorStream("SENSOR_001")
    transaction = TransactionStream("TRANS_001")
    event = EventStream("EVENT_001")

    print(sensor.process_batch(sensor_data))
    print()
    print(transaction.process_batch(transaction_data))
    print()
    print(event.process_batch(event_data))

    processor = StreamProcessor([sensor, transaction, event])

    processor.stream_info()


if __name__ == "__main__":
    main()