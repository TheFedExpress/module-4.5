===========
Readme
===========

This simple API is mostly an excercise in passing parameters.

The base route is /tree_data.  From there, another path must be added to select a single column from the New York City tree census.  
A where clause can be added by passing the parameter "where" and a value.
Rows can be limited by passing the parameter "limit" and a value.

Ex: http://localhost:5000/tree_data/user_type?where=boroname=%22Bronx%22&limit=100
