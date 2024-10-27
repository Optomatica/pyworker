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
        person_img = "https://firebasestorage.googleapis.com/v0/b/stylesphere-e8440.appspot.com/o/PersonImage%20(1).jpg?alt=media&token=7fa1242b-6c2d-4ef2-b4ba-84ecaa0f7aa7"
        cloth_img = "https://firebasestorage.googleapis.com/v0/b/stylesphere-e8440.appspot.com/o/clth_test.jpg?alt=media&token=e2478b35-7a68-42bd-b926-0b2eb76fa841"
        category = "upper_body"
        return cls(person_img=person_img, cloth_img=cloth_img, category=category)

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
