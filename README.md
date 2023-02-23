# Discussion

Hopefully the approach I took should be fairly clear from looking at the git log but let me elaborate
on some decisions:

* I added [Bulma](https://bulma.io/) to have a reasonable set of components to work with. It's pretty
  simple as it's class based and can be loaded directly from their CDN.

* Similarly I grabbed an SVG from [SVG Repo](https://www.svgrepo.com) to quickly get a reasonable icon for
  the recommendations.

* I decided to implement selection and total functionality client side as I assumed we may want to support
  multiple clients making different selections at the same time. The user experience is also arguably a bit
  nicer for this functionality if we avoid a round trip every selection. An alternative would be to use no JS
  and store the selections in the user's session.

* AlpineJS felt like a suitable choice here as it has fairly straightforward support for what we want to do
  and doesn't require setting up a JS build process. If we wanted to implement more complex front end behaviour
  we should revisit this and evaluate moving to e.g. React.

# Further Work

* There's not too much here that's amenable to automated testing but it's probably worth adding a test for
  the measures endpoint to catch any regressions and to have something to build on if we extend the feature.

* A fairly urgent task would be to move away from using a FloatField for the measure cost. For currencies we
  should use something with an underlying integer representation to avoid rounding errors.

* It's hard to speculate on future directions without a better understanding of the product vision and customer
  needs but perhaps users could create a quote from their selection. To implement this we could convert the list
  of recommendations to a form which gets posted to the back end to create a quote. Likely we'd want to also ask
  for some contact details at this point through a few more form fields. It might be nice to then e-mail the customer
  the quote for which Django has support (probably along with some transactional e-mail provider for actual delivery).

* Sorting of the measures might be a nice user experience improvement to make it easier to pick out recommendations or
  cheaper measures. I think the most straightforward implementation would be to add some links (e.g sort by cheapest)
  that append a GET parameter to the request (e.g ?sort=cost&direction=asc) and then to apply the appropriate sort
  in the database. It's important to remember to validate these parameters.

* Search is another possible extension but it's probably not worth it unless there is likely to be a very large
  number of measures. Nevertheless, if we happened to be using PostgreSQL then the full-text search feature it
  has would allow a fairly quick implementation.

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
- Show all the available measures on the `/measures` page (you will need to add some sample data)
- Add a `recommended` field to the `Measure` model and highlight recommended measures on the `/measures` page
- Allow users to select measures and display the total cost of all the selected measures

Suggest some further directions for this feature and note how you would implement them.

## Notes

Please only spend a maximum of 2-3 hours on this task. We are not looking for a finished product, but rather a demonstration of your approach to solving problems and your ability to learn new technologies.
Feel free to include any other libraries, frameworks or scripts you feel are relevant to the task.
Please document your process and any decisions you make in the README.md file.
When you are finished, please send either a link to a public repository or a zip file of the project to your contact at Furbnow.
