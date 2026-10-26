# CS-340 Client/Server Development

## Course Reflection

### How do you write programs that are maintainable, readable, and adaptable?

When writing programs, I try to keep my code organized and separate different functionalities so they are easier to understand and maintain. One example of this was the CRUD Python module I developed in Project One. Instead of writing the MongoDB connection and database operations directly into my dashboard, I created a separate module that handles creating, reading, updating, and deleting records.

This made Project Two easier because I could reuse the same module to connect my dashboard to MongoDB without having to rewrite the database operations. It also made the code easier to troubleshoot since the database functionality was separated from the dashboard components. In the future, I could reuse this module in other applications that need to interact with MongoDB, such as inventory management systems or other data-driven dashboards.

### How do you approach a problem as a computer scientist?

When approaching a problem, I usually start by understanding the requirements and breaking the project into smaller tasks. For the Grazioso Salvare dashboard, I first focused on establishing the MongoDB connection and making sure I could retrieve the animal records. Once that was working, I moved on to displaying the data in a table, implementing the rescue filters, and adding the visualizations.

This project was different from some of my previous assignments because I had to connect several technologies and make sure they worked together. It wasn’t just about writing individual functions. I also had to consider how the database, user interface, and callbacks would interact. In the future, I would continue using this approach by reviewing the client’s requirements, planning the database structure, and testing each component before combining everything into a complete application.

### What do computer scientists do, and why does it matter?

Computer scientists use technology and programming to solve problems, organize information, and develop systems that make tasks more efficient. Their work is important because software can help organizations manage large amounts of data and make better decisions.

For example, the dashboard I developed for Grazioso Salvare allows users to filter animal records based on specific rescue training requirements instead of manually searching through the dataset. The interactive table, breed distribution chart, and geolocation map also make the information easier to understand. This type of application can help an organization save time and focus more on its actual work.
