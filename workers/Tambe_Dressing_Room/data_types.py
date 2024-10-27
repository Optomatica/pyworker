import dataclasses
import random
import inspect
from typing import Dict, Any
from lib.data_types import ApiPayload, JsonDataException




@dataclasses.dataclass
class InputData(ApiPayload):
    person_img: str
    cloth_img: str
    category: str

    @classmethod
    def for_test(cls) -> "InputData":
        prompt = " ".join(random.choices(WORD_LIST, k=int(250)))
        return cls(person_img=person_img, cloth_img=cloth_img, category=category

    def generate_payload_json(self) -> Dict[str, Any]:
        return dataclasses.asdict(self)

    def count_workload(self) -> int:
        return 1
        # return len(tokenizer.tokenize(self.prompt))

    @classmethod
    def from_json_msg(cls, json_msg: Dict[str, Any]) -> "InputData":
        errors = {}
        for param in inspect.signature(cls).parameters:
            if param not in json_msg:
                errors[param] = "missing parameter"
        if errors:
            raise JsonDataException(errors)
        return cls(
            **{
                k: v
                for k, v in json_msg.items()
                if k in inspect.signature(cls).parameters
            }
        )
