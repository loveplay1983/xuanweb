# Will add categorization later 

* # [flask tutorial](https://www.youtube.com/watch?v=KrRzZGcHjK8&list=PLXmMXHVSvS-BlLA5beNJojJLlpE0PJgCW&index=9)

* [jinja2 super()](https://jinja.palletsprojects.com/en/3.1.x/templates/?highlight=super)
    > It’s possible to render the contents of the parent 
    > block by calling super(). This gives back the results 
    > of the parent block

* [whitespace](https://python-web.teclado.com/section11/lectures/02_jinja_whitespace_control/)
  ```
  app.jinja_env.lstrip_blocks = True
  app.jinja_env.trim_blocks = True
  ```
  
* [sqlite3](https://linuxhint.com/install_sqlite_browser_ubuntu_1804/)
  > SQLite is a lightweight database software. It is a 
  > command line application. You must use the 
  > command line or SQLite API on other 
  > programming languages to use SQLite database. 
  > SQLite has a graphical front end SQLite Browser for working with SQLite databases graphically.
  
* [shell_context_processor](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database/page/0)

* [%r vs %s in python](https://stackoverflow.com/questions/6005159/when-to-use-r-instead-of-s-in-python)
  > The %s specifier converts the object using str(), and %r converts it using repr().
  
* [format r(repr) of print in python3](https://stackoverflow.com/questions/33337564/format-rrepr-of-print-in-python3)
  ```
  print('you say:{0!r}'.format("i love you"))
  you say:'i love you'
  ```
  
* [index vs primary key](https://sqlwithmanoj.com/2015/08/10/difference-between-index-and-primary-key-msdn-tsql-forum/#:~:text=The%20primary%20key%20are%20the,define%20rules%20for%20the%20table.)
  > An index is a physical concept and serves as a means to locate rows faster, but is not intended to define rules for the table.
  
* # [multiple db connection with raw sql](https://stackoverflow.com/questions/41290675/run-sql-in-several-different-databases-with-flask-sqlalchemy) 
  ```
  engine_db1 = db.get_engine(app, 'db1')
  engine_db2 = db.get_engine(app, 'db2')
  sql = text("SHOW TABLES")
  results_db1 = engine_db1.execute(sql)
  results_db2 = engine_db2.execute(sql)
  ```
  # [multi-db with bind - sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/binds/#binds)
  ```
  SQLALCHEMY_DATABASE_URI = 'postgres://localhost/main'
  SQLALCHEMY_BINDS = {
  'db1':        'mysqldb://localhost/users',
  'db2':      'sqlite:////path/to/appmeta.db'
  }
  ```
  

* [different sql join](https://www.w3schools.com/sql/sql_join.asp#:~:text=LEFT%20(OUTER)%20JOIN%20%3A%20Returns,either%20left%20or%20right%20table)
  * (INNER) JOIN: Returns records that have matching values in both tables
  * LEFT (OUTER) JOIN: Returns all records from the left table, and the matched records from the right table
  * RIGHT (OUTER) JOIN: Returns all records from the right table, and the matched records from the left table
  * FULL (OUTER) JOIN: Returns all records when there is a match in either left or right table

* [HTTP](https://www.tutorialspoint.com/http/http_quick_guide.htm)

* [HTML entities](https://www.w3schools.com/charsets/ref_html_entities_4.asp)

* [flask-bootstrap vs bootstrap-flask](https://www.reddit.com/r/flask/comments/mrjnnu/flaskbootstrap_or_bootstrapflask/)
  * [flask0bootstrap](https://pythonhosted.org/Flask-Bootstrap/basic-usage.html#)
  * [bootstrap-flask](https://bootstrap-flask.readthedocs.io/en/stable/basic/#starter-template)


# HTML
* [center legend of fieldset](https://stackoverflow.com/questions/4006824/how-to-center-the-legend-element-what-to-use-instead-of-aligncenter-attribu)
  ```
  legend {
    margin:0 auto;
  }
  ```
  
* [fieldset's top border not showing up](https://stackoverflow.com/questions/42413681/fieldsets-top-border-not-showing-up)
  ```
  width:auto;
  ```

*[center anything in html](https://www.freecodecamp.org/news/how-to-center-anything-with-css-align-a-div-text-and-more/)

