from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional, Protocol




class ProcessingStage(Protocol) :
    def process(data) -> Any:
        pass


class InputStage():

    def process(self, data) -> Dict:
        if isinstance(data, dict) and "value" in data:
            try:
                data["value"] = int(data["value"])
            except ValueError:
                raise ValueError("Error detected in Stage 1: value must be a valid number")
            return data

        elif isinstance(data, list):
            for item in data:
                try:
                    item = item.upper()
                except ValueError:
                    raise ValueError("Error detected in Stage 1: all items must be strings")
            processed_data = {f"key{i}": item for i, item in enumerate(data)}
            return processed_data

        elif isinstance(data, dict):
            for value in data.values():
                try:
                    value = int(value)
                except ValueError:
                    print("Error detected in Stage 1: all values must be valid numbers")
                    return
            data_processed = {key: value for key, value in data.items() if "temp" in key}
            return data_processed

        else:
            raise ValueError("Error detected in Stage 1: Indalid data format")


class TransfomStage():
    def process(self, data) -> Dict:
        if isinstance(data, dict) and "value" in data:
            new_data = {"range" :"", "status": "Enriched with metadata and validation", "data": data}
            if data["value"] <= 10:
                new_data["range"] = "Low range"
            elif data["value"] <= 30:
                new_data["range"] = "Normal range"
            else:
                new_data["range"] = "High range"

        elif isinstance(data, dict) and "temp" in list(data.keys())[0]:
            new_data = {"average" :0, "status": "Aggregated and filtered", "data": data}
            for value in data.values():
                new_data["average"] += int(value)
            new_data["average"] /= len(data)

        elif isinstance(data, dict):
            new_data = {"actions_count" :0, "status": "Parsed and structured data", "data": data}
            for item in data:
                if item == "action":
                    new_data["actions_count"] += 1

        else:
            raise ValueError("Error detected in Stage 2: Invalid data format")
        return new_data


class OutputStage():
    def process(self, data) -> str:
        if isinstance(data, dict) and "value" in data["data"]:
            data = f"""Transform: {data["status"]}
Output: Processed temperature reading: {data["data"]["value"]}°C ({data["range"]})"""

        elif isinstance(data, dict) and "average" in list(data.keys()):
            data = f"""Transform: {data["status"]}
Output: Stream summary: {len(data["data"])} readings, avg: {data["average"]}°C"""

        elif isinstance(data, dict):
            print(data)
            data = f"""Transform: {data["status"]}
Output: User activity logged: {data["actions_count"]} actions processed"""

        else:
            raise ValueError("Error detected in Stage 3: Invalid data format")
        return data


class ProcessingPipeline(ABC):
    def __init__(self):
        super().__init__()
        self.stages = [InputStage(), TransfomStage(), OutputStage()]

    def add_stage(self, stage):
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass

class JSONAdapter(ProcessingPipeline):
    def __init__(pipeline_id):
        super().__init__()

    def process(self, data: Any) -> Union[str, Any]:
        data_backup = data
        for stage in self.stages:
            data = stage.process(data)

        return f"""
Processing JSON data through pipeline...
Input: {data_backup}
{data}"""


class CSVAdapter(ProcessingPipeline):
    def __init__(pipeline_id):
        super().__init__()

    def process(self, data: Any) -> Union[str, Any]:
        data_backup = "\""
        for item in data:
            data_backup += f"{item}"
            if item != data[-1]:
                data_backup += ", "
        data_backup += "\""
        for stage in self.stages:
            data = stage.process(data)
        return f"""
Processing CSV data through same pipeline...
Input: {data_backup}
{data}"""


class StreamAdapter(ProcessingPipeline):
    def __init__(pipeline_id):
        super().__init__()

    def process(self, data: Any) -> Union[str, Any]:
        for stage in self.stages:
            data = stage.process(data)
        return f"""
Processing Stream data through same pipeline...
Input: Real-time sensor stream
{data}"""


class NexusManager():
    def __init__(self):
        self.pipelines = [JSONAdapter(), CSVAdapter(), StreamAdapter()]
    
    def add_pipeline(self, pipeline):
        self.pipelines.append(pipeline)

    def process_data(self, data):
        i = 0
        for pipeline in self.pipelines:
            print(pipeline.process(data[i]))
            i += 1

def test():
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")
    print("Initializing Nexus Manager...")
    print("Pipeline capacity: 1000 streams/second")
    print("\nCreating Data Processing Pipeline...")
    nexusmanager = NexusManager()
    jsonadapter = JSONAdapter()
    print("Stage 1: Input validation and parsing")
    jsonadapter.add_stage(InputStage())
    print("Stage 2: Data transformation and enrichment")
    jsonadapter.add_stage(TransfomStage())
    print("Stage 3: Output formatting and delivery")
    jsonadapter.add_stage(OutputStage())
    nexusmanager.process_data([{"sensor": "temp", "value": 25, "unit": "C"}, ["user", "action", "timestamp"], {"temp 1": "22", "humidity": "45", "temp 2": "18"}])


print(list({"__name__": "__main__"}.keys())[0])
test()





# class
# def
# super()
# isinstance()
# print()
# try/except
# list/dict comprehensions
# collections
# from abc import ABC abstractmethod,
# from typing import Any List Dict Union Optional Protocol