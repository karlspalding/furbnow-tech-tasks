# Furbnow Technical Task

This repository contains the output of the django project creation command
```
django-admin startproject mysite
```
A few simple files have been added: `models.py`, `views.py` and `templates/measures.html`, and the `app` module has been registered in `settings.py` by adding its name to `INSTALLED_APPS`  

To run the project, navigate to the `app` directory and run `python manage.py runserver`. The only endpoint currently active is `/measures` 

## Task

Furbnow works with our customers to offer them various options for energy efficiency measures and low carbon technologies, like cavity wall insulation or solar panels.  

In this app, please create the following functionality:
- Show all the available measures on the `/measures` page (feel free to add a selection of measures in a sensible way)
- Add a `recommended` field to the `Measure` model and highlight recommended measures on the `/measures` page
- Allow users to select measures and display the total cost of all the selected measures

Suggest some further directions for this feature and note how you would implement them.

## Notes

Please only spend a maximum of 2-3 hours on this task. We are not looking for a finished product, but rather a demonstration of your approach to solving problems and your ability to learn new technologies.  
Feel free to include any other libraries, frameworks or scripts you feel are relevant to the task.  
Please document your process and any decisions you make in the README.md file.  
When you are finished, please send either a link to a public repository or a zip file of the project to your contact at Furbnow.
