# NAME Service User Documentation

## Overview of NAME Trajectory service

[**NAME**](https://www.metoffice.gov.uk/research/modelling-systems/dispersion-model) is the Met Office's *Numerical Atmospheric-dispersion Modelling Environment*.  
This site offers a Web Processing Service for users to be able to run [NAME on JASMIN](http://jasmin.ac.uk/jasmin-users/stories/processing/).  

## Quick start

To get started [login](#signing-in) with your ceda account.  
Once logged in go to [Processes](#the-processes) and select **NAME**.  
Select one of the three processes:  
* [Run NAME](#run-name)  
* [Run NAME with Presets](#run-name-with-presets)  
* [Plot NAME results](#plot-name-results)  

Enter your inputs and submit the job.
Go to the [Monitor](#monitoring-your-jobs) tab to view the progress of your job.  
Here you can see the Job Log and Outputs of your jobs. The outputs will vary depending on the job that was run.  

## Signing in

To sign in click "Sign in".  
[button]  
If you are not already signed into a CEDA account you will be asked to log in:  
[pic]  
Once logged in you will be asked to let NAME WPS read your CEDA profile. Click Allow:  
[pic]  
You should now be signed in with your ceda username. This lets you come back and see your completed jobs.  
[pic]  

## The Processes

To run a process, click on [Processes](https://name.ceda.ac.uk/processes).  
[pic]  
Select [**NAME**](https://name.ceda.ac.uk/processes/list?wps=name).  
[pic]  
Then select one of the following three processes:  

### Run NAME

[pic]  
[**Run NAME**](https://name.ceda.ac.uk/processes/execute?wps=name&process=run_name) runs NAME with the user providing all inputs, including location of release and bounding box.  
You must title the run something unique to refer to the job.  

#### Inputs

| Name | Description | Type | Default | Required | Example Value |
|------------|---------------------------|---------|-------------|----------|-----------------------|
|[Title](https://name.ceda.ac.uk/processes/execute?wps=name&process=run_name#item-deformField2)| Unique name that will identify your job later. Note that spaces will be converted to underscored. | String | None | Yes | [pic] |
|[Longitude](https://name.ceda.ac.uk/processes/execute?wps=name&process=run_name#item-deformField3)| The longitude of the location of release in decimal degrees. Longitude cannot exceed +/-180. | Float | -24.867222 | Yes | [pic] |
|[Latitude](https://name.ceda.ac.uk/processes/execute?wps=name&process=run_name#item-deformField4)| The latitude of the location of release in decimal degrees. Latitude cannot exceed +/-90. | Float | 16.863611 | Yes | [pic] |
|[Elevation](https://name.ceda.ac.uk/processes/execute?wps=name&process=run_name#item-deformField5)| Dictates the elevation of the release in metres above ground level. | Integer | 10 | Yes | [pic] |
|[Run Backwards](https://name.ceda.ac.uk/processes/execute?wps=name&process=run_name#item-deformField6)| Whether NAME will run backwards from the time selected or not. | Boolean | True | Yes | [pic] |
|[Time to run model over](https://name.ceda.ac.uk/processes/execute?wps=name&process=run_name#item-deformField7)| How long the model will be run over in selected units. Note that the maximum run length is 20 days. | Integer | 1 | Yes | [pic] |
|[Time to run model over (units)](https://name.ceda.ac.uk/processes/execute?wps=name&process=run_name#item-deformField8)| Units to use for *Time to run model over*. Either **days** or **hours**. | String | days | Yes | [pic] |
|[Computational Domain](https://name.ceda.ac.uk/processes/execute?wps=name&process=run_name#item-deformField9)| Bounding box in which NAME will calculate the dispersion within. Enter the minimum and maximum longitude (X) and latitude (Y) values. | BoundingBox | [180, -90, 180, 90] | Yes | [pic] |

#### Outputs

Explanation here

### Run NAME with Presets

#### Inputs

Walkthrough here

#### Outputs

Explanation here

### Plot NAME Results

#### Inputs

Walkthrough here

#### Outputs

Explanation here

## Monitoring your jobs

How to monitor job

Go to the [Monitor](https://name.ceda.ac.uk/monitor) tab to view the progress of your job.  
Click on Details to see the Job Log and Outputs of your job. The outputs will vary depending on the job that was run.  

## Further Information

Further info here
