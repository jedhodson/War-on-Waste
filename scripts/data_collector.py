import serial

print("Starting data collector")

db = open("triad_materials.csv", "a")
port_name = raw_input("Enter serial port: ")
#port_name = '/dev/ttyUSB0'
serial_port = serial.Serial(port_name, 9600)

print("Openning " + port_name)

current_class = ""
running = True

while running:
    class_name = raw_input("Enter class name to record [" + current_class + "]: ")
    if class_name == "":
        class_name = current_class
    else:
        current_class = class_name

    if class_name == "exit":
        running = False
    else:
        serial_port.write(1)
        result = serial_port.readline()
        db.write(class_name + "," + result)

print("Closing...")
db.close()
