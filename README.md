**Acceptance Criteria:**

1. Given a user, when they access your application, then they should be presented with a search box prompting them for a topic
2. Given a user, when they enter a topic, results from Twitter should be returned
3. Given a user, when they enter a topic, results from Wikipedia should be returned
4. Given a user who's performed a search, when they hit the browser's refresh button, results should be refreshed under the same search criteria.

**Technical notes:**

[Heroku deployment of this app](http://topics-bcrom.herokuapp.com/)

This demonstrates the minimal app I would launch within an agile environment as
as a first draft.   The app makes two API calls: one to Wikipedia and one to
Twitter.  Each roundtrip takes about 300-700 ms depending on network latency.  

With input from users I would propose adding the follwing features:

1. Asyncrhonous fetching of additional detail, perhaps even iframes of messages
   upon hover (I prefer AngularJS for this).
2. Separate pagination for each table or perhaps paginating automatically
   from the REST endpoint when the user scrolls to the bottom of the page
3. A geo search to only return messages within a certain radius using a 
   great circle path function
