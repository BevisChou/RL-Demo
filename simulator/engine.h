#include <cmath>
#include <tuple>
#include <msg.pb.h>

namespace simulator{
    class Engine {
    public:
        Response_State reset(Request_Config);
        Response_State step(double);
        Response_State state() const;
    private:
        std::tuple<double, double> get_delta(double, std::tuple<double, double>);
        const double STEP_SIZE = 0.001;
        Request_Config _config;
        Response_State _state;
    };
}