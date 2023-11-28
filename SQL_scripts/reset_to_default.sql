CREATE DATABASE IF NOT EXISTS arduino_shop;
USE arduino_shop;

DROP TABLE IF EXISTS goods;

CREATE TABLE goods (
	id INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(150) NOT NULL,
    product_description TEXT NOT NULL,
    image VARCHAR(100) NOT NULL,
    price DECIMAL(7, 2) NOT NULL,
    category VARCHAR(50) NOT NULL,
    quantity INT NOT NULL,
    rating DECIMAL(2,1),
    PRIMARY KEY (id)
)ENGINE = INNODB;

INSERT INTO goods (`title`, `product_description`, `price`, `category`, `quantity`, `rating`, `image`) VALUES 
(
	'Arduino Mega 2560 R3 (CH340)',
    'A replica of the original Arduino Mega2560 board. The CH340 microcircuit is used as a USB-UART adapter, which has proven itself well and is characterized by good stability, high data transfer speed, but which requires additional installation of drivers. Also, the controller differs from its predecessors by additional SDA and SCL contacts (I2C interface) and AREF outputs - sources reference voltage for the ADC of the controller and IOREF - the output voltage of the input-output ports (for automatic switching of the peripheral voltage when using 5V and 3.3V controllers). In everything else, it is still the same Arduino Mega2560 controller based on the Atmega2560 microcontroller with a lot of example programs, libraries and a description of the construction of ready-made structures.
Arduino is an open platform with open source programs and freely available libraries that allows you to assemble a variety of electronic devices. The Arduino Mega2560 board will be of interest to designers, programmers, creative and curious people who want to assemble and program their own device or controllable structure.
A huge number of different application programs and libraries have been written for this platform. There are probably no sensors, displays, and actuators left for which an Arduino library or program that uses them is not written.
A simplified version of C++ is used for programming. Software development can be conducted both using the free Arduino IDE environment and using arbitrary C/C++ tools. A USB cable is required for programming and data transfer to a PC, and for autonomous operation you can use a power supply unit, batteries or a 7-12 V battery with a 5.5*2.1 mm connector.
#Characteristics:
*Microcontroller - ATmega2560 - 16AU
*USB connection method: CH340 converter
*Operating voltage of the controller:
**USB input: 5V
**VCC input: 5VVin input: 7.5V-12V
*Digital inputs/outputs - 54 (17 of which provide PWM/PWM output)
*Analog inputs - 16
*Interfaces:
**I2C
**SPI
**PWM
*Direct current of input/output lines: no more than 40 mA
*Constant output current of the stabilizer at 3.3V: no more than 50 mA
*Program flash memory: 256 KB, of which 8 KB are used by the bootloader
*RAM: 8 KB SRAM
*Non-volatile memory: 4 KB
*The clock frequency is 16 MHz
#Link:
*Driver for CH340->https://arduino.ua/docs/CH341SER.zip
*Datasheet for Atmega2560->http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-2549-8-bit-AVR-Microcontroller-ATmega640-1280-1281-2560-2561_datasheet.pdf',
	'15.85', 
	'microcontrollers', 
	'51', 
	'5',
    'arduino_mega.jpg'
),
(
'Arduino UNO R3 (CH340)',
'A replica of the original Arduino UNO board. The CH340 microcircuit is used as a USB-UART adapter, which has proven itself well and is characterized by good stability, high data transfer speed, but which requires additional installation of drivers. Also, the controller differs from its predecessors by additional SDA and SCL contacts (I2C interface) and AREF outputs - sources reference voltage for the ADC of the controller and IOREF - the output voltage of the input-output ports (for automatic switching of the peripheral voltage when using 5V and 3.3V controllers). In everything else, it is still the same Arduino UNO controller based on the Atmega328p microcontroller with a lot of example programs, libraries and a description of the construction of ready-made structures.
Arduino is an open platform with open source programs and freely available libraries that allows you to assemble a variety of electronic devices. The Arduino UNO board will be of interest to designers, programmers, creative and curious people who want to assemble and program their own device or controlled structure.
A huge number of different application programs and libraries have been written for this platform. There are probably no sensors, displays, and actuators left for which an Arduino library or program that uses them is not written.
A simplified version of C++ is used for programming. Software development can be conducted both using the free Arduino IDE environment and using arbitrary C/C++ tools. A USB cable is required for programming and data transfer to a PC, and for autonomous operation you can use a power supply unit, batteries or a 7-12 V battery with a 5.5*2.1 mm connector.
#Characteristics:
*Microcontroller: ATmega328
*Operating voltage of the controller:
**USB input: 5V
**VCC input: 5V
**Input Vin: 7.5V-12V
*Digital inputs/outputs: 14 (6 of them PWM)
*Analog inputs: 6
*Flash program memory: 32Kb
*RAM: 2KB
*Clock frequency: 16 MHz
*Size: 68 x 53 x 15 mm
#Link:
*Assignment of conclusions
*Development environment
*How does this board differ from the original',
'microcontrollers',
'6.55',
'42',
'5',
'arduino_uno_r3.jpg'
)
;