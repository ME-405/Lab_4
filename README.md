# Cal Poly ME-405
## Lab 04
Jacob Bograd, Nick De Simone, Horacio Albarran

Documentation: https://me-405.github.io/Lab_4/

---

This lab conceptualize the way in which interrupts functions while using Queues with an Analog to Digital converter.
A time interrupt has been used in order to analyze the signal provided by such interruption while using a simple RC circuit.
Regarding the RC circuit display below, a capacitor of 4.75-uF was used as well as a 5.95-Kohms and 104-Kohms resistors; further,
the theoretical time constant for the RC circuit was calculated to be around 522-ms
![RC-Circuit](Images/rc_circuit.png) 

---
Graphs:  

![16-bits, Queue 1000, trial #1](Images/Figure_6.png)  
This graphs shows the signal for a 16-bits integers, with a 1000 size queue, and voltage signal of 3.3 Volts.
The experimental time constant for this trial was calculated to be 340-ms and yielded a numerical percent error of 34.87
  
![16-bits, Queue 1000, trial #2](Images/Figure_7.png)  
This graphs shows the signal for a 16-bits integers, with a 1000 size queue, and input voltage signal of 3.3 Volts.  
The experimental time constant for this trial was calculated to be 340-ms and yielded a numerical percent error of 34.87
  
![16-bits, Queue 2000](Images/Queue=2000.png)  
This graphs shows the signal for a 16-bits integers, with a 2000 size queue, and input voltage signal of 3.3 Volts.
The experimental time constant for this trial was calculated to be 375-ms and yielded a numerical percent error of 28.16  

**Note**
The horizontal red-line on each image represents the location of the voltage where the numerical value of the experimental time constant occurs.
The fact that the percent of error for each of our trials is not within the expected range for typical tolerences for electronic components 
can be due to the amount of electrostatic energy that was within the classroom. Since each of our team-mates, and people within the room, contributed
with some sort of energy to the environment. The more people within a room, the greater the bias produced, and the greater the percent of error. 
The percent of error could also be outside of the range since most of our cables were entangle with each other, therefore, producing the electric 
fields to have some constructive and destructive interference that would affect the electrical flow of the signal(s) within our system.
