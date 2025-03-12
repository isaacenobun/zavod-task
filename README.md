<h1>Test task for Fullstack Developer role at Zavod</h1>

<small>
Implement a news list with the ability to view news. Each news item must include tags.<br>
You need to be able to fill out news in the admin panel. Each news article consists of a
Title, Text, Pictures, and tags.<br>
You need to have pages: News, News, News by tag.<br>
There should also be a page for statistics on news views.<br>
Using Django/Python or Node.js + REST-API, add the ability to get/create/delete news.<br>
When deleting, a deletion confirmation window should pop up.<br>
Infinite scrolling on the page, which pulls out 3 news each time you scroll without
reloading the page. The idea of an infinite scroll is to show data from the backend piece
by piece. Imagine that there are 1000 news items in the database.<br>
You also need to like and dislike the news, in which when you like the news, the current
number of likes is displayed, even if at the time the news was viewed, another user of the
site liked it.<br>
The design is not important, you can use bootstrap.<br>
Publish the code on GitHub and send the link to us@zavod-it.com along with a video
recording of what happened. The letter also indicates the time spent on completing the
task. Also write a message that you have completed the task.<br>
Completion time is 2 days.</small>

<h2>My Approach</h2>

<p>So as I do with every project, I will initialize a github Repo for the project and then clone to my local machine.<br>
  From my terminal, i'd create and activate a virtual environment, install django and DRF (most important dependencies for now), then i'd go on to create the project.<br>
  <br>
  The project will contain two apps. One app for the News API and then one app that will contain the frontend.<br>
  I intend to start with the Api. I'll be using restframework's ModelViewsets to manage all the types of requests.<br>
  <br>
  Most parts of this app are pretty straight forward up until the implementation of the instant updating of likes and dislikes.To implement this smoothly, I will be using django's asynchronous server gateway service instead of the default. Since this task does not involve deployment on a production stage, I wil be sticking with a simple frontend-database connection to automatically update the frontend with data from the database without reloading the page. This is specifically for the like and dislikes to be updated asynchronously. The connection will be configured to check the database every 2 seconds. If I was optimizing for production, I would have implemented a web socket to run this more efficiently as the method i'm using breaks when connected with a hosted database.<br>
  As instructed, i will be using bootstrap for the frontend, so that's pretty straight forward.<br>
I made this writeup before i wrote any piece of code so it is possible that as I move on with the project, there might be some deviations in implementations based on what I face.<br>
  <br>
  This project was started on 11:00 WAT, 12th of March and is estimated to take about 12 hours to complete.
</p>
