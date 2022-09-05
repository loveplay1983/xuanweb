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
* # [multi-db with bind - sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/binds/#binds)
  ```
  SQLALCHEMY_DATABASE_URI = 'postgres://localhost/main'
  SQLALCHEMY_BINDS = {
  'db1':        'mysqldb://localhost/users',
  'db2':      'sqlite:////path/to/appmeta.db'
  }
  ```
  
* # [raw sql via sqlalchemy](https://www.youtube.com/watch?v=FEtJgtmogSY)
  ```
  test = db.engine.execute("xxx")
  for each in test:
    print(each)  # each is a list that consist of  a set of tuples with which each tuple represents a record
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

* [flask app routing](https://www.geeksforgeeks.org/flask-app-routing/)

* [get_flashed_message](https://stackoverflow.com/questions/57660542/flask-closing-flash-message)




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

* [multiple forms in the same line](https://stackoverflow.com/questions/69601722/does-wtforms-integer-field-force-a-new-line-when-displayed-on-webpage)
  ```
  <!--<form method="get">-->
  <!--    <fieldset class="field-set-collect">-->
  <!--        <legend>病员信息</legend>-->
  <!--        {{ form.csrf_token }}-->
  <!--        <div class="container">-->
  <!--            <div class="row">-->
  <!--                <div class="col">-->
  <!--                    {{ form.patientNum.label }}-->
  <!--                    {{ form.patientNum }}-->
  <!--                </div>-->
  <!--                <div class="col">-->
  <!--                    {{ form.patientName.label }}-->
  <!--                    {{ form.patientName }}-->
  <!--                </div>-->
  <!--                <div class="col">-->
  <!--                    {{ form.patientSex.label }}-->
  <!--                    {{ form.patientSex }}-->
  <!--                </div>-->
  <!--                <div class="col">-->
  <!--                    {{ form.patientBorn.label }}-->
  <!--                    {{ form.patientBorn }}-->
  <!--                </div>-->
  <!--                <div class="w-100"></div>-->
  <!--                <div class="col">-->
  <!--                    {{ form.patientID.label }}-->
  <!--                    {{ form.patientID }}-->
  <!--                </div>-->
  <!--                <div class="col">-->
  <!--                    {{ form.patientPhone.label }}-->
  <!--                    {{ form.patientPhone }}-->
  <!--                </div>-->
  <!--                <div class="col">-->
  <!--                    {{ form.patientAddr.label }}-->
  <!--                    {{ form.patientAddr }}-->
  <!--                </div>-->
  <!--                <div id="submit-collect">-->
  <!--                    {{ form.patientSearch }}-->
  <!--                </div>-->
  <!--            </div>-->
  <!--        </div>-->
  <!--    </fieldset>-->
  <!--</form>-->
  ```
  
* [js, html code examples](https://codepen.io/)
* [js, html code playground](https://jsfiddle.net/)
* [js, html code demo](https://www.codeply.com/)

* [flex tutorial](https://www.quackit.com/css/flexbox/tutorial/)
* [grid tutorial](https://www.quackit.com/css/grid/)

* ### Different unit
  > PX: Pixels (px) are considered absolute units, although they 1
  > are relative to the DPI and resolution of the viewing device. 
  > But on the device itself, the PX unit is fixed and does not change 
  > based on any other element. Using PX can be problematic for responsive 
  > sites, but they are useful for maintaining consistent sizing for some 
  > elements. If you have elements that should not be resized, then using 
  > PX is a good choice.
  
  **Relative Units**
  * EM: Relative to the parent element
  * REM: Relative to the root element (HTML tag)
  * %: Relative to the parent element
  * VW: Relative to the viewport’s width
  * VH: Relative to the viewport’s height

* [what is viewport](https://developer.mozilla.org/en-US/docs/Web/HTML/Viewport_meta_tag)

* [center anything in html](https://www.freecodecamp.org/news/how-to-center-anything-with-css-align-a-div-text-and-more/)

* [what is flex: 1](https://stackoverflow.com/questions/37386244/what-does-flex-1-mean)

* [change image with range slider](https://codepen.io/salt/pen/vmBaNK)
* [change image with range slider2](https://stackoverflow.com/questions/59499604/how-to-change-the-images-based-on-the-range-slider)
* [change image with range slider3](https://stackoverflow.com/questions/25936001/html-javascript-change-image-with-slider-bar)
* [img placeholer](https://stackoverflow.com/questions/32909488/how-do-i-make-a-placeholder-image-in-html-if-the-original-image-hasnt-been-foun)


# flask wtforms
* [adding id or class name to wtforms](https://stackoverflow.com/questions/53896335/add-id-field-in-stringfield-object-in-wtforms)

# Forms
* [submit form with return key](https://www.techiedelight.com/submit-form-with-enter-key-javascript/)
* [submit form with return key2](https://www.geeksforgeeks.org/how-to-submit-a-form-on-enter-button-using-jquery/)
* [submit form with return key3](https://thewebdev.info/2022/02/02/how-to-submit-form-on-enter-key-press-with-javascript/)
* [submit form with return key4](https://stackoverflow.com/questions/29943/how-to-submit-a-form-when-the-return-key-is-pressed)

# Javascript
* [change input value](https://stackoverflow.com/questions/54203535/changing-input-value-inside-a-form-tags-when-enter-key-is-pressed)
* [manipulate database](https://stackoverflow.com/questions/857670/how-to-connect-to-sql-server-database-from-javascript-in-the-browser)
* [clear input](https://stackoverflow.com/questions/17237772/html-how-to-clear-input-using-javascript)
* [jinja and js](https://www.learn-codes.net/javascript/how-to-set-a-value-inside-jinja-template-and-pass-it-to-javascript-variable/)