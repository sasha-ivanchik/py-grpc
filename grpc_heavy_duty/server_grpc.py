import random

from grpc import aio, StatusCode

from protos import heavy_duty_pb2
from protos import heavy_duty_pb2_grpc

compliments = ("good", "better than usual", "the best")


class HeavyDutyService(heavy_duty_pb2_grpc.HeavyDutyServiceServicer):

    def HeavyDuty(
            self,
            request: heavy_duty_pb2.HeavyDutyRequest,
            context: aio.ServicerContext
    ):
        compliment_message = f'{request.user.username} is {random.choice(compliments)}'
        try:
            return heavy_duty_pb2.HeavyDutyResponse(message=compliment_message)
        except Exception as e:
            context.abort(StatusCode.INTERNAL, details=str(e))
