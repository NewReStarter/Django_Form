# Generic Form App with Django

### Environment
Python 3.6.x  
Django 2.0.4 offical release  
MySQL 5.7.21  

----------------------
### Project Outcome
- **a bootstrap style dynamic input form**
- **an admin page to add new questions in the form**
- **a summary page**
- **a page for the details of every form input**

-----------------------
**Features all completed.**
-----------------------
### Installation

`pip install -r requirements.txt` to install dependencies.

### Urls
`/myadmin` to access data panel 
`/xadmin` to edit the database

### Introduction

This project uses django MVT design Pattern, whereas M stands for "Model" for the data access layer; T stands for "Template" the presentation layer and the 
V stands for "View" where business logic exists, similiar to the Controller in MVC models.

This project is supposed to be a template project for Form Input Task. Data are stored in JSON List and the elements of the List is JSON element, i.e. python dict.

**Example of data**

```
[{"id": 4, "text": "Radio Test", "questions": [{"answer": ["10-20"], "id": 6, "text": "age", "addtion_info": ""}, {"answer": ["female"], "id": 7, "text": "Gender", "addtion_info": ""}, {"answer": ["chinese"], "id": 8, "text": "language", "addtion_info": ""}]}, {"id": 5, "text": "Personal Info", "questions": [{"answer": ["Test"], "id": 9, "text": "Name", "addtion_info": "EN or CH"}, {"answer": ["2018-05-03"], "id": 10, "text": "DOB", "addtion_info": "Date of Birth"}, {"answer": ["ziliugao@gmail.com", "lawrence.ehrdesign@gmail.com"], "id": 11, "text": "Email", "addtion_info": ""}]}, {"id": 6, "text": "Select Test", "questions": [{"answer": ["JHO"], "id": 12, "text": "Company", "addtion_info": ""}, {"answer": ["CityU"], "id": 13, "text": "University", "addtion_info": ""}]}, {"id": 7, "text": "Textarea Test", "questions": [{"answer": ["No Statement so far"], "id": 14, "text": "Statement", "addtion_info": "Write your statement below"}]}]
```

### Project Features

- Dynamic Form Questions
    + Question Type:
        * select
        * text
        * textarea
        * date (select2 style)
        * checkbox
- Well-built Component
    + PDF / CSV Exporting
    + Generating Form
    + other python packages and Django apps
- JSON data storage
    + extensible to mongoDB
- Server side form validation
    + come with django framework
- Authentication Components
- Testing Components
    + Especially Useful to validate data input
- Stack Traceback of Bug Report
- PDF Generation comes with [ReportLab](https://www.reportlab.com/docs/reportlab-userguide.pdf)

-----------------------

### Future add-on

Features | Level of Difficulty | Time Comsuming | Implementation
-------- | ------------------- | -------------- | --------------
Presentaion | Difficult | Long | Currently each input field will generate a unique class name for styling. Adding colomns in database to add styles on the input fileds.
Scoring | Easy | Short | Iterate through the List and match each criteria.
Email | Easy | Short | Use [Django Email Component](https://docs.djangoproject.com/en/2.0/topics/email/) to do so.
Intereacting charts and table | Medium | Long | Query the data for each key input and group the data. Note that for each key input, the query function has to be rewritten.
CSV Exporting | Easy | Short | Iterate through the dict and print each elements to the csv files. It can be done with native python or [Django CSV component](https://docs.djangoproject.com/en/2.0/howto/outputting-csv/).
Generic chart | Difficult | Long | This require a extra database notation(new columns) for any key input to generate right data input for highchart API. [QuerySet](https://docs.djangoproject.com/zh-hans/2.0/ref/models/querysets/) May not be sufficient enough, noSQLDB may be needed. Meanwhile redesgin of current highchart data input port, the JSON List, is also required.
File uploading | Easy | Short | Use [Django FileUpload component](https://docs.djangoproject.com/en/2.0/topics/http/file-uploads/)
PDF Styling | Easy | Long | Static style of CSS should be added.

#### Time Scale
**Long:** Roughly 4 days or more 

**Medium:** Half a week should be sufficient 

**Short:** Within one day 



