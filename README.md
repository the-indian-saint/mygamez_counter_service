# Counting Service

Requires Python 3!

Start by creating virtualenv and install required packages (found in requirements.txt)

Launch server by executing run.sh in the projects' root directory

You can find interactive documentation by navigating to http://localhost:7777/docs


# IMPORTANT TODO LIST!!
* Add ability to delete counters
* Add ability to reset counters
* Add counters that can only be decremented, and instead of going to zero they go POW!
* Add tests -- OOPS!
* Add Prometheus metrics -- this seems to solve health checking and getting neat metrics, perhaps count total requests count
* Bake the API into a Docker image
* Make counters persistent. Use a real database and maybe ORM?
