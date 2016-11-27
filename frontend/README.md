
```
	> git clone git@github.com:StephenGrider/ReduxSimpleStarter.git
	> cd ReduxSimpleStarter
	> npm install
	> npm start
```

```
git clone
cd connyctDashboard
npm install
npm start or webpack -w (if webpack is not installed, install it globally using npm install webpack -g)
```

Reactjs

Reactjs is the most promising View library introduced by the minds of Facebook and Instagram engineers.Many people choose to think of React as the V in MVC. React solves one problem: building large applications with data that changes over time.

React.js is a component-based library created to build modular and fast UIs. React manages the DOM updates applying a concept called Virtual DOM, therefore you don't need to think about DOM manipulations anymore managing all the states in your UI with jQuey.
The React library includes a lightweight implementation of the DOM and events System with W3C Standards.

Simple
Simply express how your app should look at any given point in time, and React will automatically manage all UI updates when your underlying data changes.

Declarative
When the data changes, React conceptually hits the "refresh" button, and knows to only update the changed parts.

Build Composable Components
React is all about building reusable components. In fact, with React the only thing you do is build components. Since they're so encapsulated, components make code reuse, testing, and separation of concerns easy.


Some of Few Giant companies taking benefit from Reactjs

Airbnb
AirHelp
Asana
Atlassian
BBC
CloudFlare
Codecademy
Coursera
Clash of Clans
Dailymotion
Disqus
Docker
Dropbox
Facebook
Flipboard
Flipkart
GeekHub
Grammarly
HackerOne
Hashnode
HipChat
Housing.com
IMDb
Imgur
Instagram
Instacart
Khan Academy
Marvel App
Material 101
Netflix
Paypal
Pinterest
Postman
RedMart
Salesforce
The New York Times
Twitter - Fabric
Twitter Mobile
Tylio
Uber - Web App, Support, Clients, 15+ internal apps
Udacity - Classroom
WhatsApp
WordPress.com - source code
Yahoo



Now react-redux flow


Redux architecture revolves around a strict unidirectional data flow.

This means that all data in an application follows the same lifecycle pattern, making the logic of your app more predictable and easier to understand. It also encourages data normalization, so that you don't end up with multiple, independent copies of the same data that are unaware of one another.

Lifecycle of redux

Action - Dispatch (This two happens in actions) - reducer - your component
