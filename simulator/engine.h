#include <cmath>
#include <tuple>
#include <boost/property_tree/ptree.hpp>

#include <interface.h>

namespace simulator{
    struct Config {
        double g;
        double k;
        double l;
        double m;
    };

    class Engine {
    public:
        boost::property_tree::ptree reset(boost::property_tree::ptree);
        boost::property_tree::ptree step(boost::property_tree::ptree);
        boost::property_tree::ptree state() const;
    private:
        std::tuple<double, double> get_delta(double, std::tuple<double, double>);
        const double STEP_SIZE = 0.001;
        Config _config;
        boost::property_tree::ptree _state;
    };
}