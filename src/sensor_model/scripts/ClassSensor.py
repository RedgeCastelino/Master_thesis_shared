import math
import numpy


class Sensor:
    """
    This class is used to generate the transformation matrix for the transformation from sensor coordinated to EGO coordinates.
    The source for the sensor position and orientation is configured in config file: '/SensorFusion/ConfigFiles/sensorconfig.ini'.

    The config file consists of sensor information which is read and transformation matrices are created in the class.

    Attributes:

    Mathods:
        '__init__()': class constructor
        'set_sensor_properties()': using sensor properties creates transformation matricies for all the sensors
    """


    def __init__(self, sensor_id, sensor_x_distance, sensor_y_distance, sensor_rotation, trust_existance, trust_car,
                 trust_truck, trust_motorcycle, trust_bicycle, trust_pedestrian, trust_stationary, trust_other):
        """
        This is a class constructor where it contains all the instance attributes.
        The objects are the different sensors whose parameters are read from the config file: '/SensorFusion/ConfigFiles/sensorconfig.ini'

        :param sensor_id:
        :param sensor_x_distance:
        :param sensor_y_distance:
        :param sensor_rotation:
        :param trust_existance:
        :param trust_car:
        :param trust_truck:
        :param trust_motorcycle:
        :param trust_bicycle:
        :param trust_pedestrian:
        :param trust_stationary:
        :param trust_other:
        """

        self.sensor_id = sensor_id
        self.sensor_x_distance = sensor_x_distance
        self.sensor_y_distance = sensor_y_distance
        self.sensor_rotation = sensor_rotation
        self.trust_existance = trust_existance
        self.trust_car = trust_car
        self.trust_truck = trust_truck
        self.trust_motorcycle = trust_motorcycle
        self.trust_bicycle = trust_bicycle
        self.trust_pedestrian = trust_pedestrian
        self.trust_stationary = trust_stationary
        self.trust_other = trust_other
        self.transformation_matrix = None


    def set_sensor_properties(self):
        """
        This function is used to create the transformation matrix for each sensor using the distance and rotation values.
        The distances and rotation are specified to instance attributes in class constructor
        The transformation matrices are appended to the class attribute 'transformation_matrices'.

        :return:
        """

        # Converting the string values to float to use with math library
        theta = float(self.sensor_rotation)
        delta_x = float(self.sensor_x_distance)
        delta_y = float(self.sensor_y_distance)

        # Calculating the mathematical values which are used to create the transformation matrix
        cosine_theta = math.cos(theta * math.pi / 180)
        sine_theta = math.sin(theta * math.pi / 180)
        minus_sine_theta = -(math.sin(theta * math.pi / 180))

        # The transformation matrix in the form of nested list
        transformation_matrix_list = [[cosine_theta, minus_sine_theta, 0, 0, 0, 0, delta_x],
                                      [sine_theta, cosine_theta, 0, 0, 0, 0, delta_y],
                                      [0, 0, cosine_theta, minus_sine_theta, 0, 0, 0],
                                      [0, 0, sine_theta, cosine_theta, 0, 0, 0],
                                      [0, 0, 0, 0, cosine_theta, minus_sine_theta, 0],
                                      [0, 0, 0, 0, sine_theta, cosine_theta, 0],
                                      [0, 0, 0, 0, 0, 0, 1]]

        # Transformation matrix list to numpy array (python matrix)
        transformation_matrix = numpy.array(transformation_matrix_list)

        # Set transformation matrix to the object instance variable
        self.transformation_matrix = transformation_matrix