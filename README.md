**Acceptance Criteria:**

1. Given a user, when they access your application, then they should be presented with a search box prompting them for a topic
2. Given a user, when they enter a topic, results from Twitter should be returned
3. Given a user, when they enter a topic, results from Wikipedia should be returned
4. Given a user who's performed a search, when they hit the browser's refresh button, results should be refreshed under the same search criteria.

**Technical notes:**

1. Perform your work in a git repo, and send a [git bundle](http://git-scm.com/docs/git-bundle) of the repo 
2. Use Python, Javascript or some mixture of the two -- play to your strengths :-)
3. Use the Wikipedia and Twitter APIs
4. Render the prompt and the results as a Web page
5. The application must gracefully handle one, the other, or both APIs being down
6. Include a README that describes the performance profile of your application, highlighting bottlenecks and how you’d tackle them in the future
7. Include unit tests
8. Make sure your submission accurately reflects your development style.
9. Commit early and often, with good messages.

**Bonus points:**

* Allow the user to check a box that says “limit result those near me” which restricts the results from Wikipedia and Twitter to a 100 mile radius around the user’s current location
* Deploy to Heroku
* Impress us :-)
