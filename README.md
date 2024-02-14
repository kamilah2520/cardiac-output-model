# Machine Learning models for Cardiac Output Forecasting
This repository aims to model the prediction of cardiac output from acquired data from MIMIC-IV v.2 database. This mainly follows the Windkessel model developed and studied by several researchers who aimed to implement similar methods and variations of this thermodynamics theory for human blood flow. Cardiac output is crucial for determining the demands of tissue oxygen that meets human body’s heart demands, and it is often measured with Swan-Ganz catheters, which represents a risk in 10% of the cases for patients in clinical and ICU scenarios. The databases, contemplated in this research are compared in order to proceed with the most suitable implementation. These are as follows: The MIMIC II Clinical Database, MGH/MF Waveform Database and the Hemodynamics and Respiratory Pattern Dataset. The latter was selected for this work which contained 170 records with cardiac output values, which worked as ground truths for the prediction model. Therefore, algorithms such as XGBoost vector regression, decision trees, and random forest are implemented to forecast cardiac output based on the thermodilution theory in this research use case.

## System diagram
![image](https://github.com/kamilah2520/cardiac-output-model/assets/72052638/4fc16d72-290f-4889-9b30-b9e6d8ae8d27)

### Sample of Signals
![image](https://github.com/kamilah2520/cardiac-output-model/assets/72052638/020540ca-fda0-4649-acec-bb89f8988b90)
![image](https://github.com/kamilah2520/cardiac-output-model/assets/72052638/a0e14123-7c6c-4e69-bcfe-35417b25d3cc)



For the forecasting every parameter related to the heart rate from the datasets is considered for the analysis, which are HR_perc_pred and HR_peak, meaning the heart rate percentage and peak heart rate, respectively. Every value strictly related to both stroke volume and cardiac output, from which in Italian ‘basale’ means “main” and ‘picco’ is “peak”, hence SV picco, SV basale, delta SV (variation of stroke volume), CO basale, CO picco and CO peak%predetto (this is the percentage of CO variation), are implemented in the prediction models as well. 

The following figure provides an effective visualization through a scatter plot, aiding in the characterization of the remaining features.
![image](https://github.com/kamilah2520/cardiac-output-model/assets/72052638/e84bae58-6e31-4ba1-a5da-04a60b6a8168)
