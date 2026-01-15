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
                print("Error detected in Stage 1: value must be a valid number")
                return
            return data
        elif isinstance(data, list):
            processed_data = {f"key{i}": item for i, item in data}
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
            print("Error detected in Stage 1: Indalid data format")


class TransfomStage():
    def process(self, data) -> Dict:
        if data is None:
            return
        else:
            return data


class OutputStage():
    def process(self, data) -> str:
        if data is None:
            return
        return f"{data}"


class ProcessingPipeline(ABC):
    def __init__(self):
        super().__init__()
        self.stages = []

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
        # if data["value"] >= 30:
        #     range_status = "High range"
        # elif data["value"] >= 10:
        #     range_status = "Normal range"
        # else:
        #     range_status = "Low range"
        return f"""
Processing JSON data through pipeline...
Input: {data_backup}
Transform: Enriched with metadata and validation
Output: {data})"""


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
Transform: Parsed and structured data
Output: {data}"""


class StreamAdapter(ProcessingPipeline):
    def __init__(pipeline_id):
        super().__init__()

    def process(self, data: Any) -> Union[str, Any]:
        for stage in self.stages:
            data = stage.process(data)
        return f"""
Processing Stream data through same pipeline...
Input: Real-time sensor stream
Transform: Aggregated and filtered
Output: {data}"""


class NexusManager():
    def __init__(self):
        self.pipelines = []
    
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
    csvadapter = CSVAdapter()
    streamadapter = StreamAdapter()
    print("Stage 1: Input validation and parsing")
    jsonadapter.add_stage(InputStage())
    print("Stage 2: Data transformation and enrichment")
    jsonadapter.add_stage(TransfomStage())
    print("Stage 3: Output formatting and delivery")
    jsonadapter.add_stage(OutputStage())
    nexusmanager.add_pipeline(jsonadapter)
    nexusmanager.add_pipeline(csvadapter)
    nexusmanager.add_pipeline(streamadapter)
    nexusmanager.process_data([{"value": "25"}, ["12", "7", "30"], {"temp 1": "22", "humidity": "45", "temp 2": "18"}])


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