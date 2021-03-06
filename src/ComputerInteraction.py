"""!
@file    ComputerInteraction2.py
@details It contains a taksfile that collects data according to the readings from the
			enconder connected to the Nucleo-L476RG 
@author  Nick De Simone, Jacob-Bograd, Horacio Albarran
@date    February 08, 2022
"""

# Importing libraries and classes
import serial
import keyboard
import numpy as np
import matplotlib.pyplot as plt
import time


class UInterface:
    '''!
    @brief It defines a class for the User Interface interaction
    
    '''

    # constant defining state 0
    S0_CHECK = 0

    # constant defining state 1
    S1_Update_Position = 1

    def __init__(self):
        '''!
        @brief It creates an object for the User Interaction
        '''

        # It sets a local variable to use Numpy
        self.np = np

        # It sets a local variable to use the plot command
        self.plt = plt

        # It sets the variable to run the code once
        self.inv = 'G'

        # it initialized the serial port as well as defining it 
        self.ser = serial.Serial(port='COM3', baudrate=115273, timeout=1)

        # Initial state
        self.state = self.S0_CHECK

        # It defines a variable for the "Global" variables
        self.keyboard = keyboard

        ## The time-stamp for the first iteration
        self.start_time = time.time()

        ## The interval of time, in seconds, between runs of the task
        self.interval = 2e-3

        # It creates a list with the time position
        self.Time_list = []

        # It creates a list with the encoder position
        self.Position_list = []

        # It creates an array with the time and position in it 
        self.Data_list = []

    def SendChar(self):
        '''!
        @brief It creates an object which transforms the input to the ASCII corresponding value
        '''
        
        # Sending Control + C through the serial port
        self.ser.write(b'\x03')
        time.sleep(0.25)             # Sleeps for 0.5 seconds
        
        # Sending Control + D through the serial port
        self.ser.write(b'\x04')
        time.sleep(0.25)             # Sleeps for 0.5 seconds

    def transitionTo(self, newState):
        '''!
        @brief      Updates the variable defining the next state to run
        '''
        self.state = newState

    def Plot(self):
        '''!
        @brief It provides with the plot for the data provided
        '''
        # Getting a new figure
        self.plt.figure()
        
        # Plotting 63% of the value, 0.63 is the correction factor
		# to get the analog voltage signal at 63%
        self.voltage_at_tau = self.Position*0.63
        self.plt.axhline( y=self.voltage_at_tau ,color='r',linestyle='-')
        
        # Plotting the values
        self.plt.plot( self.Position_list, '.')
        self.plt.title('Volts vs Time')
        self.plt.ylabel('Voltage (mV)')
        self.plt.xlabel('Time (ms)')
        self.plt.grid()
        self.plt.show()
        
    def run(self):
        '''!
        @brief It will run the Computer Interaction code within Python
        '''
        while True:
            if self.state == self.S0_CHECK:
			
                self.SendChar()
                #self.curr_time = time.time()
                #self.fut_time = self.curr_time + 10  # It runs state_1 from 10 seconds
                #self.run = 0
                if self.inv == 'G':  # To keep collecting data
                    self.transitionTo(self.S1_Update_Position)

                elif self.inv == 'S':  # To start a new set of data
                    self.myval = self.ser.readline().decode('ascii')
                    self.Time_list.clear()
                    self.Position_list.clear()
                    print('\r\n')
                    print(self.myval)  # Prints the last value obtained
                    self.Plot()
                    self.transitionTo(self.S1_Update_Position)

                elif self.inv == 'P':  # To plot the data obtained
                    self.Plot()
                    self.transitionTo(self.S1_Update_Position)

                else:
                    print('Invalid input')    
                    self.transitionTo(self.S1_Update_Position)

            elif self.state == self.S1_Update_Position:
			
			    # Reading the lines provided through the serial interaction and stripping
				self.myval = self.ser.readline().decode('ascii')
				self.Data = self.myval.strip()

				if self.Data == '':
					#print('Empty array')                             # DEBUG
					pass
				elif self.Data == 'DONE':
					self.Plot()
					self.ser.close()
					break
				
				# elif len(self.Data) != 2:
				#     print('DEBUG ', self.Data, 'Incorrect length')  # DEBUG
				#     pass

				else:
					try:
						#print(self.Data)
						#self.Position = float(self.Data[1])
						#self.Time = float(self.Data[1])              # Time provided by PuTTY
						self.Position = float(self.Data)
						self.Position = self.Position*(3.3/4096)      # Units of mili-volts, analog voltage
						self.Position_list.append(self.Position)
						self.Data_list = [self.Position_list]
						self.Data_list2 = self.np.transpose(self.Data_list)
						#print('run # ' + str(self.run))
						# print(self.myval)
						# print(self.Data_list)
						np.savetxt('lab4Data.csv', self.Data_list2, delimiter=',')
						self.transitionTo(self.S1_Update_Position)
					except:
						print('DEBUG: Exception')

if __name__ == '__main__':
    ## Task object
    task1 = UInterface()  
    task1.run()
