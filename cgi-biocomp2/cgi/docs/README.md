## Documentation for the CGI script

The website usage is intended to be intuitive and straightforward. The user have two options:
* Search for a particular identifier (genbank accesion, gene id, gene product or chromosome location)
* Display a table containing all the entries in the database

The two options will redirect to a table with clickable elements that represent particular entries of a gene in the database. When clicking on a row, the user will get redirected to a webpage that displays all the required information in the project guidelines. The way this is done is using the ```get``` method, using the accession number as a unique identifier for each entry. This means every entry in the database can be theoretically accessed using URLs.
