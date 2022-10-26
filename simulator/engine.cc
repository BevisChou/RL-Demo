#include <engine.h>

boost::property_tree::ptree simulator::Engine::reset(boost::property_tree::ptree config)
{
    _config.g = config.get<double>("g");
    _config.k = config.get<double>("k");
    _config.l = config.get<double>("l");
    _config.m = config.get<double>("m");

    _state.put("angle", 0);
    _state.put("angular_velocity", config.get<double>("w"));

    return _state;
}

boost::property_tree::ptree simulator::Engine::step(boost::property_tree::ptree action)
{
    auto f = action.get<double>("f");
    std::tuple<double, double> s0{_state.get<double>("angle"), _state.get<double>("angular_velocity")};

    auto k1 = get_delta(f, s0);
    std::tuple<double, double> s1{
        _state.get<double>("angle") + STEP_SIZE / 2 * std::get<0>(k1),
        _state.get<double>("angular_velocity") + STEP_SIZE / 2 * std::get<1>(k1)};
    
    auto k2 = get_delta(f, s1);
    std::tuple<double, double> s2{
        _state.get<double>("angle") + STEP_SIZE / 2 * std::get<0>(k2),
        _state.get<double>("angular_velocity") + STEP_SIZE / 2 * std::get<1>(k2)};
    
    auto k3 = get_delta(f, s2);
    std::tuple<double, double> s3 = {
        _state.get<double>("angle") + STEP_SIZE * std::get<0>(k3),
        _state.get<double>("angular_velocity") + STEP_SIZE * std::get<1>(k3)};
    
    auto k4 = get_delta(f, s3);

    _state.put("angle", _state.get<double>("angle") + STEP_SIZE * (std::get<0>(k1) +  2 * std::get<0>(k2) + 2 * std::get<0>(k3) + std::get<0>(k4)) / 6);
    _state.put("angular_velocity", _state.get<double>("angular_velocity") + STEP_SIZE * (std::get<1>(k1) +  2 * std::get<1>(k2) + 2 * std::get<1>(k3) + std::get<1>(k4)) / 6);

    return _state;
}

boost::property_tree::ptree simulator::Engine::state() const
{
    return _state;
}

std::tuple<double, double> simulator::Engine::get_delta(double f, std::tuple<double, double> s)
{
    return std::tuple<double, double>{
        _state.get<double>("angular_velocity"),
        f / _config.l - _config.k * _state.get<double>("angular_velocity") - _config.m * _config.g / _config.l * sin(_state.get<double>("angle"))};
}