# quiz

This is a Django project with a single app called answers.

It has 4 main components:

* A sign up page to register team names
* An answer submission page
* A live leaderboard to display who is currently in what place
* The Markertron 4000 marking engine which compares submitted answers against the correct answer in the DB

Markertron uses fuzzy logic to allow for spelling mistakes, errant spaces and various other things people would get wrong when submitting answers via smartphones or tablets. It also allows for partial answers so if people get it mostly right they still get the point.