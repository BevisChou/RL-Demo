#include <cstdio>
#include <string>

#include <boost/property_tree/json_parser.hpp>
#include <zmq.hpp>

#include <engine.h>

int main()
{
    zmq::context_t ctx;
    zmq::socket_t sock(ctx, zmq::socket_type::pair);
    sock.bind("tcp://127.0.0.1:5555");

    simulator::Engine engine;
    std::stringstream ss;

    bool running = true;
    while (running) {
        zmq::message_t msg;
        boost::property_tree::ptree request, response, state;

        auto res = sock.recv(msg, zmq::recv_flags::none);
        ss.str(msg.to_string());
        boost::property_tree::json_parser::read_json(ss, request);

        switch (static_cast<RequestType>(request.get<int>("type")))
        {
        case RESET:
            printf("RESET\n");
            state = engine.reset(request.get_child("config"));
            break;
        case STEP:
            state = engine.step(request.get_child("action"));
            printf("f:%.6f a:%.6f av:%.6f\n", 
                request.get_child("action").get<double>("f"),
                state.get<double>("angle"),
                state.get<double>("angular_velocity"));
            break;
        case CLOSE:
            running = false;
            break;
        }
        
        response.put_child("state", state);
        ss.str(std::string());
        boost::property_tree::json_parser::write_json(ss, response);
        std::string serialized(ss.str());
        msg.rebuild(serialized.c_str(), serialized.length());
        res = sock.send(msg, zmq::send_flags::none);
    }

    sock.close();
    return 0;
}