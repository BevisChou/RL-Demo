# RL Demo

## Dependency

```bash
apt update
apt install build-essential
apt install cmake
# zmq
apt install libzmq3-dev
# protobuf
apt install protobuf-compiler
apt install libprotobuf-dev
```

```bash
# zmq
pip install pyzmq
# protobuf
pip install protobuf==3.20.*
# stable-baselines3
pip install stable-baselines3[extra]
```

## 场景

![1](./docs/img/scene.png)

系统方程如下。
$$
L\frac{d^2\theta}{dt^2}=-kL\frac{d\theta}{dt}-G\sin(\theta)+F(t)
$$
初始条件如下。
$$
\left\{
\begin{aligned}
\theta(0)  &= \theta_0\\
\theta'(0) &= \omega_0
\end{aligned} \right.
$$
用数值方法。

令
$$
u_1(t) = \theta(t)
$$
有
$$
\left\{
\begin{aligned}
u_1' &= u_2\\
u_2' &= -k\cdot u_2 - \frac{G}{L}\cdot\sin(u_1)+\frac{F}{L}
\end{aligned} \right.
$$
初始条件如下。
$$
\left\{
\begin{aligned}
u_1(0) &= \theta_0\\
u_2(0) &= \omega_0
\end{aligned} \right.
$$
用四阶 Runge-Kutta 法解。

## 编译运行

在 `simulator`目录下执行。

```
mkdir build
cd build
cmake ..
make
./main
```

在`decision-maker`目录下执行。

```
python main.py
```

## 备注

### 关于 Protobuf

本来想使用 Boost 的 JSON 库，但是能 apt install 的最高版本是 1.74，不包含 JSON 库，所以用 protobuf。在`common`目录下编译生成相关文件请运行以下命令（已运行过）。

```
protoc msg.proto --cpp_out=../simulator --python_out=../decision-maker
```