from typing import Any
from bell.avr.mqtt.client import MQTTModule, mqtt


class MQTTModuleTest(MQTTModule):
    def test_handler(self, payload: Any) -> Any:
        pass

    def test_handler_empty(self) -> Any:
        pass

    def recieve_message(self, topic: str, payload: str) -> None:
        msg = mqtt.MQTTMessage(topic=topic.encode())
        msg.payload = payload.encode()
        self.on_message(None, None, msg)  # type: ignore
