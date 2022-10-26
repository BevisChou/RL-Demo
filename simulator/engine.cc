#include <engine.h>

Response_State simulator::Engine::reset(Request_Config _config)
{
    this->_config = _config;

    this->_state.set_angle(0);
    this->_state.set_angular_velocity(_config.w());

    return this->_state;
}

Response_State simulator::Engine::step(double f)
{
    std::tuple<double, double> s0{this->_state.angle(), this->_state.angular_velocity()};

    auto k1 = this->get_delta(f, s0);
    std::tuple<double, double> s1{
        this->_state.angle() + this->STEP_SIZE / 2 * std::get<0>(k1),
        this->_state.angular_velocity() + this->STEP_SIZE / 2 * std::get<1>(k1)};
    
    auto k2 = this->get_delta(f, s1);
    std::tuple<double, double> s2{
        this->_state.angle() + this->STEP_SIZE / 2 * std::get<0>(k2),
        this->_state.angular_velocity() + this->STEP_SIZE / 2 * std::get<1>(k2)};
    
    auto k3 = this->get_delta(f, s2);
    std::tuple<double, double> s3 = {
        this->_state.angle() + this->STEP_SIZE * std::get<0>(k3),
        this->_state.angular_velocity() + this->STEP_SIZE * std::get<1>(k3)};
    
    auto k4 = this->get_delta(f, s3);

    this->_state.set_angle(this->_state.angle() + this->STEP_SIZE * (std::get<0>(k1) +  2 * std::get<0>(k2) + 2 * std::get<0>(k3) + std::get<0>(k4)) / 6);
    this->_state.set_angular_velocity(this->_state.angular_velocity() + this->STEP_SIZE * (std::get<1>(k1) +  2 * std::get<1>(k2) + 2 * std::get<1>(k3) + std::get<1>(k4)) / 6);

    return this->_state;
}

Response_State simulator::Engine::state() const
{
    return this->_state;
}

std::tuple<double, double> simulator::Engine::get_delta(double f, std::tuple<double, double> s)
{
    return std::tuple<double, double>{
        _state.angular_velocity(),
        f / this->_config.l() - this->_config.k() * _state.angular_velocity() - this->_config.m() * this->_config.g() / this->_config.l() * sin(_state.angle())};
}