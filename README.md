# dbgap_study_participants

- The **dbgap_study_participants.py** script will pull specific information from each study listed in NIH’s dbGaP system like the **phs** and **num_participants** field from each of the files in the **xml folder** and store the results in a csv file.
- Note: Some files had empty strings for the num_participants field and others had no num_participants field name in which case "Not Found" was inserted into the csv.
