from configparser import ConfigParser
from ClassSensor import Sensor

def get_sensor_properties():
    cfg = ConfigParser()
    cfg.read("ConfigFiles/sensorconfig.ini")  # Reading the config file

    sensors = cfg.sections()  # List of sensors present in the config file
    #sensors = ['CameraFront','CameraLeft','CameraRear','CameraRight','RadarFront']
    #print(sensors)

    # To create objects and create transformation matrices using the class 'Transformation'
    sensorlist = []
    sensordict = {}
    # transformationdict = {}
    # trustprobabilityexistance = {}
    # trustprobabilityclassification = {}
    for sensorname in sensors:
        # print(sensorname)
        # print(cfg.get(sensorname, 'x-distance'))
        # sensorname = Sensor(cfg.get(sensors[index], 'x-distance'), cfg.get(sensors[index], 'y-distance'), cfg.get(sensors[index], 'rotation'))   # Creating class object
        sensor = Sensor(cfg.get(sensorname, 'sensor_id'), cfg.get(sensorname, 'x-distance'),
                        cfg.get(sensorname, 'y-distance'), cfg.get(sensorname, 'rotation'),
                        cfg.get(sensorname, 'trustexistance'), cfg.get(sensorname, 'trustcar'),
                        cfg.get(sensorname, 'trusttruck'), cfg.get(sensorname, 'trustmotorcycle'),
                        cfg.get(sensorname, 'trustbicycle'), cfg.get(sensorname, 'trustpedestrian'),
                        cfg.get(sensorname, 'truststationary'),
                        cfg.get(sensorname, 'trustother'))  # Creating class object
        sensor.set_sensor_properties()

        sensorlist.append(sensor)
        sensordict[sensor.sensor_id] = sensor
        # transformationdict[sensor.sensor_id] = sensor.transformation
    #print(sensorlist)
    #print(sensordict)
    return (sensorlist, sensordict)