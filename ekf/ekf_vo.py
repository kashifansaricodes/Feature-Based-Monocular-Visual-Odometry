import numpy as np
import matplotlib.pyplot as plt


class KalmanFilter:
    """
    Kalman Filter using a constant acceleration motion model
    """

    def __init__(self, dt, u, sigma_a, sigma_z):
        # Initialize the Kalman Filter parameters
        self.dt = dt  # time step
        self.u = u  # control input (acceleration)
        self.sigma_a = sigma_a  # process noise standard deviation
        self.sigma_z = sigma_z  # measurement noise standard deviation

        # State transition matrix
        self.A = np.array([[1, self.dt], [0, 1]])
        # Control input matrix
        self.B = np.array([[(self.dt**2)/2], [self.dt]])
        # Process noise covariance matrix
        self.R = np.array([
            [(self.dt**4)/4, (self.dt**3)/2],
            [(self.dt**3)/2, self.dt**2]
        ]) * self.sigma_a ** 2
        # Measurement noise covariance
        self.Q = sigma_z ** 2
        # Initial estimation error covariance
        self.P = np.eye(self.A.shape[1])
        # Measurement matrix
        self.C = np.array([[1, 0]])
        # Initial state estimate
        self.x = np.array([[0], [0]])
        # Identity matrix
        self.I = np.eye(self.C.shape[1])

    def predict(self):
        # Predict the next state
        self.x = np.dot(self.A, self.x) + np.dot(self.B, self.u)
        # Predict the next covariance
        self.P = np.dot(np.dot(self.A, self.P), self.A.T) + self.R
        return self.x

    def update(self, z):
        # Compute the Kalman Gain
        S = np.dot(self.C, np.dot(self.P, self.C.T)) + self.Q
        K = np.dot(self.P, np.dot(self.C.T, np.linalg.inv(S)))
        # Update the state estimate
        self.x = self.x + K * (z - np.dot(self.C, self.x))
        # Update the covariance estimate
        self.P = np.dot((self.I - (K * self.C)), self.P)


def main():
    dt = 0.1  # time step

    t = np.arange(0, 100, dt)  # time vector

    # Generate the real track (constant acceleration model)
    real_x = 0.1 * ((t**2) - t)

    u = 1  # control input (acceleration)
    sigma_a = 0.25  # process noise standard deviation
    sigma_z = 2.0  # measurement noise standard deviation
    kf = KalmanFilter(dt, u, sigma_a, sigma_z)  # initialize the Kalman Filter

    predictions = []  # list to store predictions
    measurements = []  # list to store measurements

    for x in real_x:
        # Simulate a noisy measurement
        z = kf.C.item(0) * x + np.random.normal(0, 50)

        measurements.append(z)  # store the measurement
        x_kf = kf.predict().item(0)  # predict the next state
        kf.update(z)  # update the state with the measurement

        predictions.append(x_kf)  # store the prediction

    # Plot the results
    plt.figure()
    plt.plot(t, measurements, label='Measurements', color='b', linewidth=0.5)
    plt.plot(t, real_x, label='Real Track', color='y', linewidth=1.5)
    plt.plot(t, predictions, label='Ext. Kalman Filter Prediction', color='r', linewidth=1.5)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()