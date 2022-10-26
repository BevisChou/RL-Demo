#include <iostream>
#include <string>
#include <zmq.hpp>

#include <engine.h>
#include <msg.pb.h>

int main()
{
    GOOGLE_PROTOBUF_VERIFY_VERSION;

    zmq::context_t ctx;
    zmq::socket_t sock(ctx, zmq::socket_type::pair);
    sock.bind("tcp://127.0.0.1:5555");

    simulator::Engine engine;

    bool running = true;
    while (running) {
        zmq::message_t msg;
        auto res = sock.recv(msg, zmq::recv_flags::none);
        Request request;
        request.ParseFromString(msg.to_string());

        Response_State old_state;
        Response_State state;
        Response response;
        switch (request.type())
        {
        case Request_RequestType_RESET:
            std::cout << "RESET" << std::endl;
            state = engine.reset(request.config());
            break;
        case Request_RequestType_STEP:
            old_state = engine.state();
            std::cout << "a:" << old_state.angle() << " av:" << old_state.angular_velocity() << " f:" << request.action() << std::endl;
            state = engine.step(request.action());
            break;
        case Request_RequestType_CLOSE:
            std::cout << "CLOSE" << std::endl;
            running = false;
            break;
        }
        response.mutable_state()->CopyFrom(state);
        std::string str(response.SerializeAsString());
        msg.rebuild(str.c_str(), str.length());
        res = sock.send(msg, zmq::send_flags::none);
    }

    sock.close();
    return 0;
}