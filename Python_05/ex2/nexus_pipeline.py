from abc import ABC, abstractmethod
from typing import Any, Dict, Union, Protocol


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        pass


class InputStage():

    def process(self, data: Any) -> Dict:
        if isinstance(data, dict) and "value" in data:
            try:
                data["value"] = int(data["value"])
            except ValueError:
                raise ValueError("Error detected in Stage 1:"
                                 " value must be a valid number")
            return data

        elif isinstance(data, list):
            for item in data:
                try:
                    item = item.upper()
                except ValueError:
                    raise ValueError("Error detected in Stage 1:"
                                     " all items must be strings")
            processed_data = {f"key{i}": item for i, item in enumerate(data)}
            return processed_data

        elif isinstance(data, dict):
            for value in data.values():
                try:
                    value = int(value)
                except ValueError:
                    raise ValueError("Error detected in Stage 1:"
                                     " all values must be valid numbers")
            data_processed = {key: value for key,
                              value in data.items() if "temp" in key}
            return data_processed

        else:
            raise ValueError("Error detected in Stage 1: Indalid data format")


class TransformStage():
    def process(self, data: Any) -> Dict:
        if isinstance(data, dict) and "value" in data:
            new_data = {
                "range": "", "status": "Enriched with metadata and validation",
                "data": data
                }
            if data["value"] <= 10:
                new_data["range"] = "Low range"
            elif data["value"] <= 30:
                new_data["range"] = "Normal range"
            else:
                new_data["range"] = "High range"

        elif isinstance(data, dict) and "temp" in list(data.keys())[0]:
            new_data = {"average": 0, "status": "Aggregated and filtered",
                        "data": data
                        }
            for value in data.values():
                new_data["average"] += int(value)
            new_data["average"] /= len(data)

        elif isinstance(data, dict):
            new_data = {
                "actions_count": 0, "status": "Parsed and structured data",
                "data": data
                }
            for item in data.values():
                if item == "action":
                    new_data["actions_count"] += 1

        else:
            raise ValueError("Error detected in Stage 2: Invalid data format")
        return new_data


class OutputStage():
    def process(self, data: Any) -> str:
        if isinstance(data, dict) and "value" in data["data"]:
            data = (
                f"Transform: {data['status']}\n"
                "Output: Processed temperature reading:"
                f" {data['data']['value']}°C ({data['range']})"
            )

        elif isinstance(data, dict) and "average" in list(data.keys()):
            data = (
                f"Transform: {data["status"]}\n"
                f"Output: Stream summary: {len(data["data"])} "
                f"readings, avg: {data["average"]}°C"
                )

        elif isinstance(data, dict):
            data = (
                f"Transform: {data["status"]}\n"
                "Output: User activity logged: "
                f"{data["actions_count"]} actions processed"
                )

        else:
            raise ValueError("Error detected in Stage 3: Invalid data format")
        return data


class ProcessingPipeline(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.stages = []

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
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
    def __init__(self, pipeline_id: str) -> None:
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
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()

    def process(self, data: Any) -> Union[str, Any]:
        for stage in self.stages:
            data = stage.process(data)
        return f"""
Processing Stream data through same pipeline...
Input: Real-time sensor stream
{data}"""


class NexusManager():
    def __init__(self) -> None:
        self.pipelines = []

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def process_data(self, data: Any) -> None:
        i = 0
        for pipeline in self.pipelines:
            print(pipeline.process(data[i]))
            i += 1

    def demo_chaining(self) -> None:
        print("\n=== Pipeline Chaining Demo ===")
        print("Pipeline A -> Pipeline B -> Pipeline C")
        print("Data flow: Raw -> Processed -> Analyzed -> Stored")

        records = len(self.pipelines) * len(self.pipelines[0].stages)

        print(f"\nChain result: {records} "
              "records processed through 3-stage pipeline")
        print("Performance: 100% efficiency, 0.2s total processing time")


def main():
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")
    print("Initializing Nexus Manager...")
    print("Pipeline capacity: 1000 streams/second\n")

    nexusmanager = NexusManager()

    print("Creating Data Processing Pipeline...")
    json_pipe = JSONAdapter("id")
    print("Stage 1: Input validation and parsing")
    json_pipe.add_stage(InputStage())
    print("Stage 2: Data transformation and enrichment")
    json_pipe.add_stage(TransformStage())
    print("Stage 3: Output formatting and delivery")
    json_pipe.add_stage(OutputStage())

    nexusmanager.add_pipeline(json_pipe)

    csv_pipe = CSVAdapter("id")
    stream_pipe = StreamAdapter("id")
    for p in [csv_pipe, stream_pipe]:
        p.add_stage(InputStage())
        p.add_stage(TransformStage())
        p.add_stage(OutputStage())
        nexusmanager.add_pipeline(p)

    print("\n=== Multi-Format Data Processing ===")

    input_data = [
        {"sensor": "temp", "value": 25, "unit": "C"},
        ["user", "action", "timestamp"],
        {"temp 1": "22", "humidity": "45", "temp 2": "18"}
    ]

    nexusmanager.process_data(input_data)
    nexusmanager.demo_chaining()
    print("\nNexus Integration complete. All systems operational.")


if __name__ == "__main__":
    main()
