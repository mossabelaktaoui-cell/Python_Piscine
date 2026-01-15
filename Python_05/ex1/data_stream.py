from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional

class DataStream(ABC):

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass
    
    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        pass

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        pass


class SensorStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__()
        self.stream_id = stream_id
        self.readings_processed = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        total = 0
        i = 0
        filtered_data = []
        for data in data_batch:
            unite, value = data.split(":")
            if unite == "temp":
                filtered_data.append(float(value))
        while i < len(filtered_data):
            total += filtered_data[i]
            i += 1
        average = total / len(filtered_data)
        self.readings_processed = len(data_batch)
        return(f"""
Initializing Sensor Stream...
Stream ID: {self.stream_id}, Type: Environmental Data
Processing sensor batch: {data_batch}
Sensor analysis: {self.readings_processed} readings processed, avg temp: {average:.2f}°C""")


    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        filtered_data = []
        for data in data_batch:
            unite, value = data.split(":")
            if unite == "temp":
                filtered_data.append(data)
        return filtered_data

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"- Sensor data" :f"{self.readings_processed} readings processed"}


class TransactionStream(DataStream):
    def __init__(self, trans_id: str):
        super().__init__()
        self.trans_id = trans_id
        self.operations = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        net_flow = 0
        for data in data_batch:
            trans, value = data.split(":")
            if trans == "sell":
                net_flow -= int(value)
            elif trans == "buy":
                net_flow += int(value)
        if net_flow > 0:
            net_flow = f"+{net_flow}"

        self.operations = len(data_batch)
        return(f"""
Initializing Transaction Stream...
Stream ID: {self.trans_id}, Type: Financial Data
Processing transaction batch: {data_batch}
Transaction analysis: {self.operations} operations, net flow: {net_flow} units""")        

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        filtered_data = []
        for data in data_batch:
            trans, value = data.split(":")
            if trans == criteria:
                filtered_data.append(data)
        return filtered_data

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"- Transaction data" :f"{self.operations} operations processed"}

class EventStream(DataStream):
    def __init__(self, event_id: str):
        super().__init__()
        self.event_id = event_id
        self.events = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        errors_detected = 0
        for event in data_batch:
            if "error" in event.lower():
                errors_detected += 1
        self.events = len(data_batch)
        return(f"""
Initializing Event Stream...
Stream ID: {self.event_id}, Type: System Events
Processing event batch: {data_batch}
Event analysis: {self.events} events, {errors_detected} error detected""")
    

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Andy]:
        filtered_data = []
        for data in data_batch:
            if data == criteria:
                filtered_data.append(data)
        return filtered_data

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"- Event data" :f"{self.events} events processed"}

class StreamProcessor():
    def __init__(self, streams: List[DataStream]):
        self.streams: List[DataStream] = streams
    
    def stream_info(self):
        print("\n=== Polymorphic Stream Processor ===")
        print("Processing mixed stream types through a unified interface...")
        print(f"\nBatch 1 Results")
        for stream in self.streams:
            stats = stream.get_stats()
            for key, value in stats.items():
                print(f"{key}: {value}")
        print("All streams processed successfully. Nexus throughput optimal.")



sensor = TransactionStream("S-1001")
print(sensor.process_batch(["buy:20", "sell:15", "buy:30", "sell:50"]))
print(sensor.filter_data(["buy:20", "sell:15", "buy:30", "sell:50"], "sell"))

transaction = SensorStream("S-1001")
print(transaction.process_batch(["temp:22.5", "humidity:65", "pressure:21.8", "temp:21.5"]))
print(transaction.filter_data(["temp:22.5", "humidity:65", "pressure:21.8", "temp:21.5"], "temp"))

event = EventStream("Event-1001")
print(event.process_batch(["login", "error:404", "logout", "error:500"]))
print(event.filter_data(["login", "error","logout", "error"], "error"))

processor = StreamProcessor([sensor, transaction, event])
processor.stream_info()