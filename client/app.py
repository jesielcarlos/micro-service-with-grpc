from __future__ import print_function

import grpc
import users_pb2
import users_pb2_grpc


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = users_pb2_grpc.UserServiceStub(channel)
        response = stub.ListUsers(users_pb2.ListUsersRequest())
    print(response.users)


if __name__ == "__main__":
    run()