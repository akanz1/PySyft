from .syft_message import SyftMessage


class RunClassMethodMessage(SyftMessage):
    def __init__(self, path, _self, args, kwargs, id_at_location, route, msg_id=None):
        super().__init__(route=route, msg_id=msg_id)
        self.path = path
        self._self = _self
        self.args = args
        self.kwargs = kwargs
        self.id_at_location = id_at_location